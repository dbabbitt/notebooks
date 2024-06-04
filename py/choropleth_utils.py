#!/usr/bin/env python
# coding: utf-8



# Soli Deo gloria



from html import escape
from math import sqrt
from matplotlib import cm
from os import path as osp
from shutil import copyfile
from sklearn.feature_extraction.text import TfidfVectorizer
from xml.etree.ElementTree import Element
import math
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import pylab
import pyphen
import re
import textwrap
import warnings
import webcolors
import xml
import xml.etree.ElementTree as et

warnings.filterwarnings("ignore")
class ChoroplethUtilities(object):
    """This class implements the core of the utility functions
    needed to create SVG choropleths or labels of the United States.
    
    A choropleth map is a type of thematic map in which areas are
    shaded or patterned in proportion to a statistical variable that
    represents an aggregate summary of a geographic characteristic
    within each area.
    
    A labeled map just contains a few words of text located at the
    center of or with a line to the center of each district.
    
    Examples
    --------
    
    import sys
    sys.path.insert(1, '../py')
    from storage import Storage
    from choropleth_utils import ChoroplethUtilities
    
    s = Storage()
    afghanistan_provinces_df = s.load_object('afghanistan_provinces_df')
    cu = ChoroplethUtilities(iso_3166_2_code='af', one_country_df=afghanistan_provinces_df,
                             s=s)
    """
    def __init__(self, iso_3166_2_code=None, one_country_df=None, all_countries_df=None,
                 s=None, verbose=False):
        if iso_3166_2_code is None: self.iso_3166_2_code = 'us'
        else: self.iso_3166_2_code = iso_3166_2_code.lower()
        if s is None:
            from storage import Storage
            self.s = Storage()
        else: self.s = s
        if not hasattr(self.s, 'encoding_types_list'): self.s.encoding_types_list = [
            'ascii', 'cp037', 'cp437', 'cp863', 'utf_32', 'utf_32_be', 'utf_32_le', 'utf_16',
            'utf_16_be', 'utf_16_le', 'utf_7', 'utf_8', 'utf_8_sig', 'latin1', 'iso8859-1'
        ]
        if not hasattr(self.s, 'encoding_errors_list'): self.s.encoding_errors_list = [
            'ignore', 'replace', 'xmlcharrefreplace'
        ]
        self.s.encoding_type = self.s.encoding_types_list[0]
        self.s.encoding_error = self.s.encoding_errors_list[2]
        self.s.decoding_type = self.s.decoding_types_list[11]
        self.s.decoding_error = self.s.decoding_errors_list[0]
        if one_country_df is None: self.one_country_df = self.s.load_object('us_stats_df')
        else: self.one_country_df = one_country_df
        if all_countries_df is None: self.all_countries_df = self.s.load_object('all_countries_df')
        else: self.all_countries_df = all_countries_df
        
        # Create preferences dictionary
        self.settings_dict = {}
        mask_series = (self.all_countries_df.index == self.iso_3166_2_code.upper())
        rows_list = self.all_countries_df[mask_series].to_dict(orient='records')
        if rows_list: self.settings_dict = rows_list[0]
        elif self.s.pickle_exists('choropleth_settings_dict'):
            self.settings_dict = self.s.load_object('choropleth_settings_dict')
        
        # Define the SVG parts
        font_size = self.settings_dict.get('font_size', 12)
        if str(font_size) == 'nan': font_size = 12
        self.text_style_dict = {
            'font-style': 'normal', 'font-variant': 'normal', 'font-weight': 'normal',
            'font-stretch': 'normal', 'font-size': f'{font_size}px', 'line-height': '1.25',
            'font-family': 'sans-serif', '-inkscape-font-specification': 'sans-serif, Normal',
            'font-variant-ligatures': 'normal', 'font-variant-caps': 'normal',
            'font-variant-numeric': 'normal', 'font-feature-settings': 'normal',
            'text-align': 'center', 'letter-spacing': '0px', 'word-spacing': '0px',
            'writing-mode': 'lr-tb', 'text-anchor': 'middle', 'fill': self.get_fill_color(fill_color='#000000'),
            'fill-opacity': '1', 'stroke': 'none'
        }
        self.text_style_list = self.get_style_list(self.text_style_dict.copy())
        self.ts_str = '<tspan sodipodi:role="line" id="tspan-{}" x="{}" dy="{}">{}</tspan>'
        self.label_line_style_list = self.get_style_list({
            'fill': 'none', 'fill-rule': 'evenodd', 'stroke': '#e00000',
            'stroke-width': '2', 'stroke-linecap': 'butt', 'stroke-linejoin': 'miter',
            'stroke-opacity': '1', 'font-variant-east_asian': 'normal', 'opacity': '1',
            'vector-effect': 'none', 'fill-opacity': '1', 'stroke-miterlimit': '4',
            'stroke-dasharray': 'none', 'stroke-dashoffset': '0'
        })
        self.l_str = '<path style="{}" d="{{}}" id="path-{{}}" inkscape:connector-curvature="0" inkscape:label="{{}}" />'.format(';'.join(self.label_line_style_list))
        self.label_line_file_path = osp.join(
            self.s.saves_folder, 'xml', '{}_districts_label_line.xml'.format(self.iso_3166_2_code)
        )
        self.svg_suffix = '\n</svg>'
        self.regex_sub_str = self.svg_suffix.strip()
        self.svg_regex = re.compile(self.regex_sub_str)
        if self.iso_3166_2_code == 'us': self.copy_file_name = 'us - Copy.svg'
        elif self.iso_3166_2_code == 'af': self.copy_file_name = 'Afghanistan - Copy.svg'
        self.copy_file_path = osp.join(self.s.data_folder, 'svg', self.copy_file_name)
        if ('svg_width' not in self.all_countries_df.columns) or ('svg_height' not in self.all_countries_df.columns):
            raise Exception('svg_width and svg_height must be in your all_countries_df')
        self.svg_width = self.settings_dict['svg_width']
        self.svg_height = self.settings_dict['svg_height']
        inkscape_cx = self.settings_dict.get('inkscape_cx', 341.81217)
        if str(inkscape_cx) == 'nan': inkscape_cx = 341.81217
        inkscape_cy = self.settings_dict.get('inkscape_cy', 167.65197)
        if str(inkscape_cy) == 'nan': inkscape_cy = 167.65197
        inkscape_zoom = self.settings_dict.get('inkscape_zoom', 1.9206455)
        if str(inkscape_zoom) == 'nan': inkscape_zoom = 1.9206455
        self.svg_attributes_list = [
            f'height="{self.svg_height}"',
            'id="svg"',
            'inkscape:version="1.1.2 (b8e25be833, 2022-02-05)"',
            'version="1.0"',
            f'viewBox="0 0 {self.svg_width} {self.svg_height}"',
            f'width="{self.svg_width}"',
            'xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"',
            'xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"',
            'xmlns:svg="http://www.w3.org/2000/svg"',
            'xmlns="http://www.w3.org/2000/svg"'
        ]
        self.namedview_attributes_list = [
            f'bordercolor="#666666"',
            f'borderopacity="1.0"',
            f'id="named-view"',
            f'inkscape:current-layer="svg"',
            f'inkscape:cx="{inkscape_cx}"',
            f'inkscape:cy="{inkscape_cy}"',
            f'inkscape:pagecheckerboard="0"',
            f'inkscape:pageopacity="0.0"',
            f'inkscape:pageshadow="2"',
            f'inkscape:window-height="991"',
            f'inkscape:window-maximized="1"',
            f'inkscape:window-width="1920"',
            f'inkscape:window-x="-9"',
            f'inkscape:window-y="-9"',
            f'inkscape:zoom="{inkscape_zoom}"',
            f'pagecolor="#ffffff"',
            f'showgrid="false"',
        ]
        self.svg_prefix_str = '''<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg {}>
  <sodipodi:namedview {} />
  <defs id="defs-main">
        <style type="text/css" id="style-main">
            path {{fill-rule: evenodd;}};
            *{{stroke-linecap:butt;stroke-linejoin:round;}}
        </style>
        <path
            d="M 0,0 H 3.5"
            id="m-ticks"
            style="stroke:#000000;stroke-width:0.80000001;stroke-linecap:butt;stroke-linejoin:round"
            inkscape:connector-curvature="0" />
  </defs>
  <metadata id="metadata-main">
  </metadata>
  <rect
     height="{}"
     id="ocean-background"
     style="display:inline;fill:{};"
     width="{}"
     x="0"
     y="0"
     inkscape:label="Ocean Background" />'''
        self.html_style_str = '#{:02x}{:02x}{:02x}'
        self.fill_style_prefix = 'stroke-width:1.0;fill:{};'
        self.fill_style_str = self.fill_style_prefix.format(self.get_fill_color(self.html_style_str))
        self.district_path_str = '<path id="{}" d="{}" data-id="{}" data-name="{}" style="{}" inkscape:connector-curvature="0" />'
        self.svg_dir = osp.abspath(osp.join(self.s.saves_folder, 'svg'))
        os.makedirs(name=self.svg_dir, exist_ok=True)
        
        # Unused XML bits for making your own colorbar
        self.figure_str = '''
  <g
     id="figure-main"
     style="stroke-linecap:butt;stroke-linejoin:round"
     inkscape:label="Column Name Colorbar">{}{}
  </g>'''
        self.label_text_style_list = [
            'font-style:normal', 'font-variant:normal', 'font-weight:normal',
            'font-stretch:normal', 'font-size:18px', 'line-height:1.25',
            'font-family:sans-serif',
            "-inkscape-font-specification:'sans-serif, Normal'",
            'font-variant-ligatures:normal', 'font-variant-caps:normal',
            'font-variant-numeric:normal', 'font-feature-settings:normal',
            'text-align:center', 'letter-spacing:0px', 'word-spacing:0px',
            'writing-mode:lr-tb', 'text-anchor:middle', 'fill:' + self.get_fill_color('#000000'), 'fill-opacity:1',
            'stroke:none', 'stroke-width:0.75', 'stroke-linecap:butt',
            'stroke-linejoin:round'
        ]
        self.label_tspan_style_list = [
            'font-style:normal', 'font-variant:normal', 'font-weight:normal',
            'font-stretch:normal', 'font-size:18px', 'font-family:sans-serif',
            "-inkscape-font-specification:'sans-serif, Normal'",
            'font-variant-ligatures:normal', 'font-variant-caps:normal',
            'font-variant-numeric:normal', 'font-feature-settings:normal',
            'text-align:center', 'writing-mode:lr-tb', 'text-anchor:middle',
            'stroke-width:0.75', 'stroke-linecap:butt', 'stroke-linejoin:round'
        ]
        self.legend_label_str = '''
    <text
       xml:space="preserve"
       style="{}"
       x="-215.13533"
       y="110.72276"
       id="text-{{}}"
       transform="rotate(-90)"
       inkscape:label="{{}} Text"><tspan
         sodipodi:role="line"
         id="tspan-{{}}"
         style="{}"
         x="-215.13533"
         y="110.72276">{{}}</tspan></text>'''.format(';'.join(self.label_text_style_list),
                                                     ';'.join(self.label_tspan_style_list))
        self.axes_str = '''
    <g
       id="axes-colorbar"
       style="stroke-linecap:butt;stroke-linejoin:round"
       inkscape:label="Colorbar">{}{}
    </g>'''
        self.gradient_file_path = osp.join(self.s.data_folder, 'txt', 'gradient.txt')
        with open(self.gradient_file_path, 'r') as f:
            self.gradient_str = f.read()
        self.matplotlib_axis_str = '''
      <g
         id="matplotlib.axis-colorbar"
         style="stroke-linecap:butt;stroke-linejoin:round"
         inkscape:label="Axis Text">{}
      </g>'''
        self.tick_text_style_list = [
            'font-style:normal', 'font-variant:normal', 'font-weight:normal',
            'font-stretch:normal', 'font-size:10px', 'line-height:1.25',
            'font-family:sans-serif',
            "-inkscape-font-specification:'sans-serif, Normal'",
            'font-variant-ligatures:normal', 'font-variant-caps:normal',
            'font-variant-numeric:normal', 'font-feature-settings:normal',
            'text-align:center', 'letter-spacing:0px', 'word-spacing:0px',
            'writing-mode:lr-tb', 'text-anchor:middle', 'fill:' + self.get_fill_color('#000000'), 'fill-opacity:1',
            'stroke:none', 'stroke-width:0.75', 'stroke-linecap:butt',
            'stroke-linejoin:round'
        ]
        self.tick_tspan_style_list = [
            'font-style:normal', 'font-variant:normal', 'font-weight:normal',
            'font-stretch:normal', 'font-size:10px', 'font-family:sans-serif',
            "-inkscape-font-specification:'sans-serif, Normal'",
            'font-variant-ligatures:normal', 'font-variant-caps:normal',
            'font-variant-numeric:normal', 'font-feature-settings:normal',
            'text-align:center', 'writing-mode:lr-tb', 'text-anchor:middle',
            'stroke-width:0.75', 'stroke-linecap:butt', 'stroke-linejoin:round'
        ]
        self.tick_text_str = '''
          <text
             xml:space="preserve"
             style="{}"
             x="79.746887"
             y="{{}}"
             id="text-{{}}"
             inkscape:label="{{}} Text"><tspan
               sodipodi:role="line"
               id="tspan-{{}}"
               style="{}"
               x="79.746887"
               y="{{}}">{{}}</tspan></text>'''.format(';'.join(self.tick_text_style_list),
                                                      ';'.join(self.tick_tspan_style_list))
        self.ytick_str = '''
        <g
           id="ytick-{}"
           style="stroke-linecap:butt;stroke-linejoin:round"
           inkscape:label="{} Tick">
          <g
             id="line2d-{}"
             style="stroke-linecap:butt;stroke-linejoin:round"
             inkscape:label="{} Tick Line">
            <g
               id="g-{}"
               style="stroke-linecap:butt;stroke-linejoin:round">
              <use
                 style="stroke:#000000;stroke-width:0.80000001;stroke-linecap:butt;stroke-linejoin:round"
                 x="64.800003"
                 xlink:href="#m-ticks"
                 y="{}"
                 id="use-{}"
                 width="100%"
                 height="100%" />
            </g>
          </g>{}
        </g>'''
        self.hyphen_dict = pyphen.Pyphen(lang='en_US')
        self.line_height = 9
        self.width_ratio = -0.027663496798780152
        self.height_ratio = -0.0676069034160266
        self.nonword_regex = re.compile(r'\W+')
        self.light_grey_hex_str = '#e0e0e0'
        self.ocean_blue_hex_str = '#c8eafb'
        self.us_states_list = [
            'Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado',
            'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia',
            'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky',
            'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota',
            'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire',
            'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota',
            'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina',
            'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia',
            'Washington', 'West Virginia', 'Wisconsin', 'Wyoming'
        ]
    
    
    ###############################
    # Methods not used externally #
    ###############################
    
    
    
    def indexize_string(self, indexable_str):
        """
        Indexizes a string by performing the following steps:
        
        1. Converts the string to lowercase.
        2. Removes all non-word characters using a regular expression.
        3. Strips leading and trailing whitespace.
        4. Replaces all remaining whitespace characters with hyphens.
        
        Parameters:
            indexable_str (str): The string to be indexed.
        
        Returns:
            str: The indexed string.
        """
        
        # Lowercase the string
        lowercased_str = indexable_str.lower()
        
        # Remove non-word characters using the pre-defined nonword_regex attribute
        cleaned_str = self.nonword_regex.sub(' ', lowercased_str)
        
        # Strip leading and trailing whitespace
        stripped_str = cleaned_str.strip()
        
        # Replace remaining whitespace with hyphens
        indexed_str = stripped_str.replace(' ', '-')
        
        return indexed_str
    
    
    
    def trim_d_path(self, file_path):
        """
        Trims the leading and trailing quotation marks from all `d` attributes
        within an XML file. This function assumes the file encoding and error handling
        settings are defined in the `self.s` attribute (assumed to be an object with 
        `encoding_type`, `encoding_error`, `decoding_type`, and `decoding_error` attributes).
        
        Parameters:
            file_path (str): The path to the XML file.
        
        Raises:
            FileNotFoundError: If the specified file is not found.
        """
        
        # Open the file for reading in the specified encoding and error handling mode
        try:
            with open(file_path, 'r', encoding=self.s.encoding_type, errors='ignore') as f:
                xml_str = f.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {file_path}")
        
        # Compile the regular expression to match `d` attributes
        d_regex = re.compile('d="([^"\r\n]+)[\r\n]+')
        
        # Replace all occurrences of `d="..."` with `d="\g"` to trim quotes
        while d_regex.search(xml_str):
            xml_str = d_regex.sub(r'd="\g<1>', xml_str)
        
        # Open the file again for writing in the specified encoding and error handling mode
        with open(file_path, 'w') as f:
            
            # Encode the trimmed string, decode it back to the desired encoding, and then write to the file
            print(
                xml_str.strip().encode(self.s.encoding_type, errors=self.s.encoding_error).decode(
                    encoding=self.s.decoding_type, errors=self.s.decoding_error
                ), file=f
            )
    
    
    
    @staticmethod
    def get_style_list(style_dict):
        style_list = []
        for key, value in style_dict.items():
            value = str(value)
            if ' ' in value:
                style_list.append("{}:'{}'".format(key, value))
            else:
                style_list.append('{}:{}'.format(key, value))
        
        return style_list
    
    
    
    def hyphenate_words(self, suggestion):
        hyphenated_list = []
        for word in suggestion.split(' '):
            width = len(word)
            if width > 12:
                hyphen_tuple = self.hyphen_dict.wrap(word, int(width/2))
                if hyphen_tuple is None:
                    hyphenated_list.append(word)
                else:
                    hyphenated_list.append(''.join(hyphen_tuple))
            else:
                hyphenated_list.append(word)
        
        return(' '.join(hyphenated_list))
    
    
    
    def get_tspan_list(self, suggestion):
        suggestion = self.hyphenate_words(suggestion)
        tspan_list = [suggestion]
        #if (' ' in suggestion) or ('-' in suggestion):
        if ' ' in suggestion:
            split_point = math.ceil(len(suggestion)/2)
            if ' ' in suggestion[split_point:]:
                split_point += suggestion[split_point:].index(' ')
            tspan_list = textwrap.wrap(suggestion, split_point,
                                       break_long_words=False, break_on_hyphens=True)
        elif '-' in suggestion:
            split_point = max(len(x) for x in suggestion.split('-'))
            tspan_list = textwrap.wrap(suggestion, split_point,
                                       break_long_words=True, break_on_hyphens=True)
        
        return tspan_list
    
    
    
    def get_tfidf_lists(self):
        self.suggestion_list_dict = self.s.load_object('suggestion_list_dict')
        
        # Get your list of lists of strings
        corpus = list(self.suggestion_list_dict.values())
        
        # Good trick for flattening 2D lists to 1D
        corpus = sum(corpus, [])
        
        vectorizer = TfidfVectorizer(min_df=1, stop_words='english')
        X = vectorizer.fit_transform(corpus)
        idf = vectorizer.idf_
        d = dict(zip(vectorizer.get_feature_names(), idf))
        sorted_d = sorted(d.items(), key=lambda x: x[1], reverse=False)
        reverse_sorted_d = sorted(d.items(), key=lambda x: x[1], reverse=True)
        
        return sorted_d, reverse_sorted_d
    
    
    
    def strip_namespaces(self, el):
        '''Recursively search this element tree, removing namespaces.'''
        if el.tag.startswith("{"):
            el.tag = el.tag.split('}', 1)[1]  # strip namespace
        keys = list(el.attrib.keys())
        for k in keys:
            if k.startswith("{"):
                k2 = k.split('}', 1)[1]
                el.attrib[k2] = el.attrib[k]
                del el.attrib[k]
        for child in el:
            self.strip_namespaces(child)
    
    
    
    def get_legend_xml(self, labels_list, verbose=False):
        labels_list = [lbl for lbl in labels_list if str(lbl) != 'nan']

        # Build chart as a side-effect
        fig, ax = plt.subplots(figsize=(1, 6))
        fig.subplots_adjust(left=0.5)
        x = y = list(range(10))

        # Get artists and colors lists
        artists_list = []
        colors_list = []
        for i in range(len(labels_list)):
            PathCollection_obj = plt.scatter(x, y)
            artists_list.append(PathCollection_obj)
            rgb_tuple = tuple(int(x*255) for x in PathCollection_obj.get_facecolor()[0][:-1])
            color = self.html_style_str.format(*rgb_tuple)
            colors_list.append(color)

        # Build and save legend for further manipulation
        legend_obj = pylab.legend(artists_list, labels_list, loc='upper left')
        file_path = osp.join(self.svg_dir, 'legend.svg')
        plt.savefig(file_path)
        plt.close(fig)

        # Trim the legend xml
        self.trim_d_path(file_path)
        root = et.parse(file_path).getroot()
        self.strip_namespaces(root)
        for figure_1_xml in root.iter():
            if (figure_1_xml.tag == 'g'):
                id = figure_1_xml.attrib['id']
                if id == 'figure_1':
                    key = 'transform'
                    value = self.settings_dict.get('legend_transform', 'translate(-12.768599,191.52893)')
                    if value == 'nan':
                        value = 'translate(-12.768599,191.52893)'
                    figure_1_xml.attrib[key] = value
                    break
        for axes_1_xml in figure_1_xml.iter():
            if (axes_1_xml.tag == 'g'):
                id = axes_1_xml.attrib['id']
                if id == 'axes_1':
                    break
        path_collection_list = []
        path_strs_list = []
        for axes_element in axes_1_xml.iter():
            if 'id' in axes_element.attrib:
                id = axes_element.attrib['id']
                if id.startswith('PathCollection_'):
                    path_collection_list.append(id)
                    for defs_element in axes_element.iter():
                        if (defs_element.tag == 'defs'):
                            for path_element in defs_element.iter():
                                path_str = et.tostring(path_element, encoding='unicode')
                                if verbose: print(path_str)
                                path_strs_list.append(re.sub(r'>\s+<', '><', path_str))
        if verbose:
            for path_str in path_strs_list:
                print()
                print(path_str)
        for legend_1_xml in axes_1_xml.iter():
            if (legend_1_xml.tag == 'g'):
                if 'id' in legend_1_xml.attrib:
                    id = legend_1_xml.attrib['id']
                    if id == 'legend_1':
                        key = 'style'
                        value = 'fill:' + self.get_fill_color('#000000') + ';fill-opacity:1'
                        legend_1_xml.attrib[key] = value
                        defs_xml_str = '<defs>'
                        for path_str in path_strs_list:
                            defs_xml_str += path_str
                        defs_xml_str += '</defs>'
                        try: defs_xml = et.fromstring(defs_xml_str)
                        except Exception as e:
                            print(f'{e.__class__.__name__} error in defs_xml = et.fromstring(defs_xml_str): {str(e).strip()}')
                            print()
                            print('defs_xml_str')
                            print(defs_xml_str)
                            raise
                        try: legend_1_xml.insert(0, defs_xml)
                        except Exception as e:
                            print(f'{e.__class__.__name__} error in legend_1_xml.insert(0, defs_xml): {str(e).strip()}')
                            print()
                            print('defs_xml_str')
                            print(defs_xml_str)
                            print()
                            print('legend_1_xml')
                            print(et.tostring(legend_1_xml, encoding='unicode'))
                            raise
                        break
        axes_id_list = [
            'patch_2', 'matplotlib.axis_1', 'matplotlib.axis_2', 'patch_3', 'patch_4', 'patch_5', 'patch_6'
        ]
        for axes_id in path_collection_list+axes_id_list:
            for axes_element in axes_1_xml:
                id = axes_element.attrib['id']
                if id == axes_id:
                    axes_1_xml.remove(axes_element)
                    break
        for patch_element in figure_1_xml:
            id = patch_element.attrib['id']
            if id == 'patch_1':
                figure_1_xml.remove(patch_element)
                break
        legend_xml = et.tostring(figure_1_xml, encoding='unicode')
        colors_dict = {label: color for label, color in zip(labels_list, colors_list)}

        return legend_xml, colors_dict
    
    
    def get_colorbar_xml(self, column_name, cmap='viridis', min=None, max=None):
        cb1 = self.show_colorbar(column_name, cmap=cmap, min=min, max=max)
        file_path = osp.join(self.svg_dir, 'colorbar.svg')
        
        # Trim the colorbar xml
        self.trim_d_path(file_path)
        root = et.parse(file_path).getroot()
        for colorbar_xml in root.iter():
            if (colorbar_xml.tag.split('}')[-1] == 'g'):
                id = colorbar_xml.attrib['id']
                if id == 'figure_1':
                    key = 'transform'
                    value = self.settings_dict.get('colorbar_transform', 'translate(-12.768599,191.52893)')
                    if value == 'nan': value = 'translate(-12.768599,191.52893)'
                    colorbar_xml.attrib[key] = value
                    break
        for axes_element in colorbar_xml:
            id = axes_element.attrib['id']
            if id == 'axes_1':
                for matplotlib_element in axes_element:
                    id = matplotlib_element.attrib['id']
                    if id == 'matplotlib.axis_2':
                        key = 'style'
                        value = 'fill:' + self.get_fill_color('#000000') + ';fill-opacity:1;'
                        matplotlib_element.attrib[key] = value
                        break
                break
        for patch_element in colorbar_xml:
            id = patch_element.attrib['id']
            if id == 'patch_1':
                colorbar_xml.remove(patch_element)
                break
        colorbar_xml = et.tostring(colorbar_xml, encoding='unicode')
        
        return colorbar_xml
    
    
    
    def get_column_description(self, column_name):
        self.column_description_dict = self.s.load_object('column_description_dict')
        if column_name in self.column_description_dict: column_description = self.column_description_dict[column_name]
        else:
            column_description = re.sub('^pf_', 'Personal Freedom:_', str(column_name), 1)
            column_description = re.sub('^hf_', 'Human Freedom:_', str(column_description), 1)
            column_description = re.sub('^ef_', 'Economic Freedom:_', str(column_description), 1)
            column_list = column_description.split('_')
            descr_list = []
            for word in column_list: descr_list.append(word[0].upper()+word[1:])
            column_description = ' '.join(descr_list)
            self.column_description_dict[column_name] = column_description
            self.s.store_objects(column_description_dict=self.column_description_dict)
        
        return column_description
    
    
    ########################
    # Map Creation Methods #
    ########################
    
    @staticmethod
    def color_distance_from(from_color, to_rgb_tuple):
        if from_color == 'white':
            green_diff = 255 - to_rgb_tuple[0]
            blue_diff = 255 - to_rgb_tuple[1]
            red_diff = 255 - to_rgb_tuple[2]
            color_distance = sqrt(green_diff**2 + blue_diff**2 + red_diff**2)
        elif from_color == 'black':
            color_distance = sqrt(to_rgb_tuple[0]**2 + to_rgb_tuple[1]**2 + to_rgb_tuple[2]**2)
        
        return color_distance

    def get_fill_color(self, fill_color='#000000', backround_hex_str='#ffffff'):
        if backround_hex_str != '#ffffff':
            rbg_tuple = tuple(webcolors.hex_to_rgb(backround_hex_str))
            text_colors_list = []
            for color in ['white', 'black']:
                color_tuple = (self.color_distance_from(color, rbg_tuple), color)
                text_colors_list.append(color_tuple)
            text_color = sorted(text_colors_list, key=lambda x: x[0])[-1][1]
            fill_color = webcolors.name_to_hex(text_color)
        
        return fill_color

    def get_fill_color_rgb(self, fill_color_rgb=(0, 0, 0), backround_rgb=(255, 255, 255)):
        if backround_rgb != (255, 255, 255):
            text_colors_list = []
            for color in ['white', 'black']:
                color_tuple = (self.color_distance_from(color, backround_rgb), color)
                text_colors_list.append(color_tuple)
            text_color = sorted(text_colors_list, key=lambda x: x[0])[-1][1]
            fill_color_rgb = webcolors.name_to_rgb(text_color)

        return fill_color_rgb

    @staticmethod
    def add_docname(attributes_set, docname_str):
        attributes_set.add(f'sodipodi:docname="{docname_str}"')
        
        return attributes_set

    def possibly_raise_exceptions(self, one_country_df):
        if not osp.exists(self.copy_file_path):
            raise Exception('{} does not exist'.format(self.copy_file_path))
        if not osp.exists(self.label_line_file_path):
            raise Exception('{} does not exist'.format(self.label_line_file_path))
        if 'district_abbreviation' not in one_country_df.columns:
            raise Exception('one_country_df needs to have the district_abbreviation column')
        if 'outline_d' not in one_country_df.columns:
            raise Exception('one_country_df needs to have the outline_d column')
        if 'text_x' not in one_country_df.columns:
            raise Exception('one_country_df needs to have the text_x column')
        if 'text_y' not in one_country_df.columns:
            raise Exception('one_country_df needs to have the text_y column')
    
    def create_text_tag_xml(self, string_column_name, one_country_df, text_file_path=None, district_rgb_dict=None):
        if text_file_path is None:
            if string_column_name is None: file_name = 'index_districts_text.xml'
            else: file_name = '{}_districts_text.xml'.format(string_column_name)
            text_file_path = osp.join(self.s.saves_folder, 'xml', file_name)
        
        # Wipe out any preruns
        with open(text_file_path, 'w') as f: print('', file=f)
        
        mask_series = one_country_df['centroid_id'].isnull()
        if string_column_name is not None: mask_series = mask_series | one_country_df[string_column_name].isnull()
        for district_name, row_series in one_country_df[~mask_series].sort_index(
            axis='index', ascending=False
        ).iterrows():
            text_id = self.indexize_string(district_name)
            centroid_id = row_series.centroid_id
            if str(centroid_id) == 'nan': centroid_id = f'path-{text_id}'
            group_id = row_series.get('svg_id', text_id)
            if str(group_id) == 'nan': group_id = text_id
            if string_column_name is None: label = '{} Index'.format(district_name)
            else: label = '{} {}'.format(district_name, ' '.join(string_column_name.split('_')))
            x = row_series['text_x']
            if str(x) == 'nan': x = 900.94183
            y = row_series['text_y']
            if str(y) == 'nan': y = 546.21332
            if string_column_name is None: column_value = district_name.strip()
            else: column_value = row_series[string_column_name].strip()
            tspan_list = self.get_tspan_list(column_value)
            tspan_str = ''
            for i, column_value_str in enumerate(tspan_list):
                if str(row_series.dy) == 'nan': dy_num = self.line_height*i
                else: dy_num = row_series.dy*i
                tspan_str += self.ts_str.format(text_id+str(i), x, dy_num, escape(column_value_str))
            
            # Update the background color and font size
            # fill: rgb(0, 0, 0); font-size: 380%;
            if str(row_series.label_line_d) != 'nan':
                backround_hex_str = self.ocean_blue_hex_str
                backround_rgb = webcolors.hex_to_rgb(self.ocean_blue_hex_str)
            else:
                backround_hex_str = webcolors.rgb_to_hex(district_rgb_dict.get(district_name, (128, 128, 128)))
                backround_rgb = district_rgb_dict.get(district_name, (128, 128, 128))
            text_style_dict = {}
            text_style_dict['fill'] = self.get_fill_color(backround_hex_str=backround_hex_str)
            # text_style_dict['fill'] = f'rgb{self.get_fill_color_rgb(backround_rgb=backround_rgb)}'
            if str(row_series.font_size) != 'nan': text_style_dict['font-size'] = row_series.font_size
            elif str(row_series.dy) == 'nan': text_style_dict['font-size'] = '1em'
            
            style_str = ';'.join(self.get_style_list(text_style_dict)) + ';'
            text_str = f'''
  <style id="style-{group_id}">.{group_id}{{fill:rgb{backround_rgb};}}</style>
  <text x="{x}" y="{y}" id="text-{text_id}" style="{style_str}" inkscape:label="{label}" dominant-baseline="text-after-edge" text-anchor="middle">{tspan_str}</text>'''
            if str(row_series.dy) == 'nan': text_str += f'''
  <script type="application/ecmascript" id="script-{text_id}">
        
        // Get path size
        var groupNode = document.getElementById(&quot;{centroid_id}&quot;);
        var pathBB = groupNode.getBBox();
        
        // Scale the font size and line height of the text
        scaleTextNode(pathBB, &quot;text-{text_id}&quot;);
        
  </script>'''
            with open(text_file_path, 'a') as f:
                print(
                    text_str.encode(self.s.encoding_type, errors=self.s.encoding_error).decode(
                        encoding=self.s.decoding_type, errors=self.s.decoding_error
                    ), file=f
                )

        return text_file_path

    def create_svg_file_beginning(self, svg_file_name):
        svg_file_path = osp.join(self.s.saves_folder, 'svg', svg_file_name)
        if not osp.exists(svg_file_path): copyfile(self.copy_file_path, svg_file_path)
        with open(svg_file_path, 'w') as f:
            attributes_set = self.add_docname(set(self.svg_attributes_list), svg_file_name)
            svg_prefix = self.svg_prefix_str.format(
                ' '.join(list(attributes_set)),
                ' '.join(self.namedview_attributes_list),
                self.svg_height, self.get_fill_color(self.ocean_blue_hex_str),
                self.svg_width
            )
            print(svg_prefix, file=f)
        
        return svg_file_path

    
    
    def create_country_colored_labeled_map(
        self, numeric_column_name, string_column_name=None, one_country_df=None, cmap='viridis'
    ):
        """
        one_country_df must have district names as an index, the district_abbreviation, outline_d, text_x and
        text_y columns, one (hopefully) numeric column labeled numeric_column_name, and one
        (not neccesarily) string column labeled string_column_name
        
        numeric_column_name = 'Total_Gun_Murder_Deaths_2010'
        string_column_name = 'Google_Suggest_Unique'
        svg_file_path = cu.create_country_colored_labeled_map(
            numeric_column_name=numeric_column_name, string_column_name=string_column_name,
            one_country_df=cu.one_country_df
        )
        
        numeric_column_name = 'Asian_Percent'
        string_column_name = 'Google_Suggest_Common'
        svg_file_path = cu.create_country_colored_labeled_map(
            numeric_column_name=numeric_column_name, string_column_name=string_column_name,
            one_country_df=cu.one_country_df
        )
        
        string_column_name = None
        for numeric_column_name in cu.one_country_df.columns:
            svg_file_path = cu.create_country_colored_labeled_map(
                numeric_column_name=numeric_column_name, string_column_name=string_column_name,
                one_country_df=cu.one_country_df
            )
        """
        if one_country_df is None: one_country_df = self.one_country_df.copy()
        if not np.issubdtype(one_country_df[numeric_column_name].dtype, np.number):
            one_country_df['categorical_'+numeric_column_name] = pd.Categorical(one_country_df[numeric_column_name])
            one_country_df['codes_'+numeric_column_name] = one_country_df['categorical_'+numeric_column_name].cat.codes
            numeric_column_name = 'codes_' + numeric_column_name
        self.possibly_raise_exceptions(one_country_df)
        
        # Build the SVG file from scratch
        if string_column_name is None:
            svg_file_name = f'{self.iso_3166_2_code.upper()}_Index_{numeric_column_name}.svg'
        else:
            svg_file_name = '{}_{}_{}.svg'.format(
                self.iso_3166_2_code.upper(), numeric_column_name, re.sub(r'[:]+', '_', string_column_name)
            )
        svg_file_path = self.create_svg_file_beginning(svg_file_name)
        
        # Create the outline paths
        ListedColormap_obj = cm.get_cmap(cmap, one_country_df[numeric_column_name].nunique())
        min = one_country_df[numeric_column_name].min()
        max = one_country_df[numeric_column_name].max()
        mask_series = one_country_df[numeric_column_name].isnull()
        district_rgb_dict = {}
        for district_name, row_series in one_country_df[~mask_series].sort_index(axis='index', ascending=False).iterrows():
            column_value = row_series[numeric_column_name]
            district_abbreviation = row_series.district_abbreviation
            outline_d = row_series.outline_d
            if str(column_value) != 'nan':
                normed_value = (column_value - min) / (max - min)
                rgb_tuple = tuple(int(x*255) for x in ListedColormap_obj(normed_value)[:-1])
            else: rgb_tuple = (128, 128, 128)
            district_rgb_dict[district_name] = rgb_tuple
            style_value = self.fill_style_str.format(*rgb_tuple)
            indexized_str = self.indexize_string(district_name)
            id_value = 'district-{}'.format(indexized_str)
            path_tag = self.district_path_str.format(
                id_value, outline_d, district_abbreviation, district_name, style_value
            )
            with open(svg_file_path, 'a') as f: print(path_tag, file=f)
        
        # Create the text tag xml
        text_file_path = self.create_text_tag_xml(string_column_name, one_country_df, text_file_path=None, district_rgb_dict=district_rgb_dict)

        # Paste the rest together
        with open(text_file_path, 'r') as f:
            text_str = f.read()
            with open(self.label_line_file_path, 'r') as f:
                label_line_str = f.read()
                with open(svg_file_path, 'a') as f:
                
                    # Add the label lines
                    print(label_line_str, file=f)

                    # Add the text labels
                    print(text_str, file=f)
                    
                    # Add the colorbar
                    colorbar_xml = self.get_colorbar_xml(numeric_column_name, cmap=cmap)
                    print(colorbar_xml, file=f)
                    
                    print(self.regex_sub_str, file=f)
        
        return svg_file_path
    
    
    
    def create_country_colored_map(self, numeric_column_name, one_country_df=None, cmap='viridis', min=None, max=None):
        """
        one_country_df must have district names as an index, the district_abbreviation and outline_d columns,
        and one (hopefully) numeric column labeled whatever you're putting in numeric_column_name
        
        numeric_column_name = 'Total_Gun_Murder_Deaths_2010'
        svg_file_path = cu.create_country_colored_map(numeric_column_name, one_country_df=cu.one_country_df)
        
        numeric_column_name = 'Asian_Percent'
        svg_file_path = cu.create_country_colored_map(numeric_column_name, one_country_df=cu.one_country_df)
        
        for numeric_column_name in cu.one_country_df.columns:
            svg_file_path = cu.create_country_colored_map(
                numeric_column_name=numeric_column_name, one_country_df=cu.one_country_df
            )
        """
        if one_country_df is None: one_country_df = self.one_country_df.copy()
        if not np.issubdtype(one_country_df[numeric_column_name].dtype, np.number):
            one_country_df['categorical_'+numeric_column_name] = pd.Categorical(one_country_df[numeric_column_name])
            one_country_df['codes_'+numeric_column_name] = one_country_df['categorical_'+numeric_column_name].cat.codes
            numeric_column_name = 'codes_' + numeric_column_name
        
        # Build the SVG file from scratch
        svg_file_name = '{}_{}.svg'.format(self.iso_3166_2_code.upper(), numeric_column_name)
        svg_file_path = self.create_svg_file_beginning(svg_file_name)
        
        # Create the outline paths
        ListedColormap_obj = cm.get_cmap(cmap, one_country_df[numeric_column_name].nunique())
        if min is None:
            min = one_country_df[numeric_column_name].min()
        if max is None:
            max = one_country_df[numeric_column_name].max()
        for district_name, row_series in one_country_df.sort_index(axis='index', ascending=False).iterrows():
            column_value = row_series[numeric_column_name]
            district_abbreviation = row_series.district_abbreviation
            outline_d = row_series.outline_d
            if str(column_value) != 'nan':
                normed_value = (column_value - min) / (max - min)
                rgb_tuple = tuple(int(x*255) for x in ListedColormap_obj(normed_value)[:-1])
            else: rgb_tuple = (128, 128, 128)
            style_value = self.fill_style_str.format(*rgb_tuple)
            id_value = f'district-{self.indexize_string(district_name)}'
            path_tag = self.district_path_str.format(
                id_value, outline_d, district_abbreviation, district_name, style_value
            )
            with open(svg_file_path, 'a') as f: print(path_tag, file=f)
        
        # Create the colorbar
        colorbar_xml = self.get_colorbar_xml(numeric_column_name, cmap=cmap, min=min, max=max)
        with open(svg_file_path, 'a') as f:
            print(colorbar_xml, file=f)
            print(self.svg_suffix, file=f)
        
        return svg_file_path
    
    
    
    def edit_and_display_svg(self, numeric_column_name, string_column_name=None, verbose=False):
        text_editor_path = r'C:\Program Files\Notepad++\notepad++.exe'
        if string_column_name is None:
            svg_file_path = osp.abspath(self.create_country_colored_map(
                numeric_column_name,
                one_country_df=self.one_country_df,
                cmap='viridis',
                min=None,
                max=None,
            ))
        else:
            svg_file_path = osp.abspath(self.create_country_colored_labeled_map(
                numeric_column_name,
                string_column_name=string_column_name,
                one_country_df=self.one_country_df,
                cmap='viridis',
            ))
        if verbose: print(f'Opening {svg_file_path} in Notepad++')
        import subprocess
        Popen_obj = subprocess.Popen(
            [text_editor_path, svg_file_path], creationflags=subprocess.CREATE_NEW_PROCESS_GROUP
        )
        inkscape_path = r'C:\Program Files\Inkscape\bin\inkscape.exe'
        png_file_path = svg_file_path.replace('svg', 'png')
        os.makedirs(osp.dirname(png_file_path), exist_ok=True)
        if verbose: print(f'Creating {png_file_path}')
        return_value = subprocess.call([inkscape_path, svg_file_path, f'--export-filename={png_file_path}'])
        common_prefix = osp.commonprefix([png_file_path, os.getcwd()])
        relative_path = osp.join(*png_file_path.split(common_prefix)[1:])
        from IPython.display import HTML
        display(HTML('<img src="../' + relative_path.replace(os.sep, '/') + '" style="width:50%"/>'))
    
    
    
    def create_country_labeled_map(
        self, string_column_name=None, one_country_df=None, cmap='viridis', colors_dict=None,
        colors_keyed_to_district_abbreviation=False
    ):
        """
        one_country_df must have district names as an index, the district_abbreviation, outline_d, text_x and
        text_y columns, and one (not neccesarily) string column labeled string_column_name
        
        string_column_name = 'Google_Suggest_Unique'
        svg_file_path = cu.create_country_labeled_map(
            string_column_name=string_column_name, one_country_df=cu.one_country_df
        )
        
        string_column_name = 'Google_Suggest_Common'
        svg_file_path = cu.create_country_labeled_map(
            string_column_name=string_column_name, one_country_df=cu.one_country_df
        )
        
        string_column_name = 'Google_Suggest_First'
        svg_file_path = cu.create_country_labeled_map(
            string_column_name=string_column_name, one_country_df=cu.one_country_df
        )
        """
        
        if one_country_df is None: one_country_df = self.one_country_df.copy()
        self.possibly_raise_exceptions(one_country_df)
        
        # Build the SVG file from scratch
        if string_column_name is None:
            svg_file_name = '{}_Index_{}.svg'.format(self.iso_3166_2_code.upper(), numeric_column_name)
        else:
            svg_file_name = '{}_{}.svg'.format(self.iso_3166_2_code.upper(), re.sub(r'[:]+', '_', string_column_name))
        svg_file_path = self.create_svg_file_beginning(svg_file_name)
        
        # Create the outline paths
        if colors_dict is None:
            mask_series = one_country_df[string_column_name].isnull()
            labels_list = one_country_df[~mask_series][string_column_name].unique().tolist()
            legend_xml, colors_dict = self.get_legend_xml(labels_list)
            show_legend = (len(colors_dict.keys()) < 11)
        else: show_legend = False
        district_rgb_dict = {}
        for district_name, row_series in one_country_df.sort_index(axis='index', ascending=False).iterrows():
            column_value = str(row_series[string_column_name]).strip()
            district_abbreviation = row_series.district_abbreviation
            outline_d = row_series.outline_d
            if colors_keyed_to_district_abbreviation: color = colors_dict.get(district_abbreviation, '#f9f9f9')
            else: color = colors_dict.get(column_value, '#f9f9f9')
            district_rgb_dict[district_name] = tuple(webcolors.hex_to_rgb(color))
            style_value = self.fill_style_prefix.format(self.get_fill_color(color))
            id_value = f'district-{self.indexize_string(district_name)}'
            path_tag = self.district_path_str.format(
                id_value, outline_d, district_abbreviation, district_name, style_value
            )
            with open(svg_file_path, 'a') as f: print(path_tag, file=f)

        # Create the text tag xml
        text_file_path = self.create_text_tag_xml(string_column_name, one_country_df, text_file_path=None, district_rgb_dict=district_rgb_dict)
        
        # Paste the rest together
        with open(text_file_path, 'r') as f:
            text_str = f.read()
            with open(self.label_line_file_path, 'r') as f:
                label_line_str = f.read()
                with open(svg_file_path, 'a') as f:
                
                    # Add the text labels
                    print(text_str, file=f)
                
                    # Add the label lines
                    print(label_line_str, file=f)
                    
                    # Add the legend
                    if show_legend: print(legend_xml, file=f)
                    
                    print(self.regex_sub_str, file=f)
        
        return svg_file_path
    
    
    
    def create_us_google_suggest_labeled_map(self, cu_str='unique'):
        """
        districts_file_path = cu.create_us_google_suggest_labeled_map(cu_str='unique')
        districts_file_path = cu.create_us_google_suggest_labeled_map(cu_str='common')
        districts_file_path = cu.create_us_google_suggest_labeled_map(cu_str='first')
        """
        if osp.exists(self.copy_file_path) and osp.exists(self.label_line_file_path):
            districts_file_path = osp.join(
                self.s.saves_folder, 'svg', '{}_{}.svg'.format(self.iso_3166_2_code.upper(), cu_str.upper())
            )
            if osp.exists(districts_file_path): os.remove(districts_file_path)
            copyfile(self.copy_file_path, districts_file_path)
            with open(districts_file_path, 'r') as f: xml_str = f.read()
            if self.svg_regex.search(xml_str):
                text_file_path = osp.join(self.s.saves_folder, 'xml', '{}_districts_text.xml'.format(cu_str))
                with open(text_file_path, 'w') as f: print('', file=f)
                cap_str = cu_str[:1].upper()+cu_str[1:]
                column_name = 'Google_Suggest_{}'.format(cap_str)
                mask_series = self.one_country_df[column_name].isnull()
                for district_name, row_series in self.one_country_df[~mask_series].sort_index(axis='index', ascending=False).iterrows():
                    text_id = self.indexize_string(district_name)
                    label = '{} Google {} Suggestion'.format(district_name, cap_str)
                    suggestion = row_series[column_name]
                    x = row_series['text_x']
                    if str(x) == 'nan': x = 900.94183
                    y = row_series['text_y']
                    if str(y) == 'nan': y = 546.21332
                    tspan_list = self.get_tspan_list(suggestion)
                    tspan_str = ''
                    for i, suggestion_str in enumerate(tspan_list):
                        tspan_str += self.ts_str.format(text_id+str(i), x, self.line_height*i, escape(suggestion_str))
                    style_str = ';'.join(self.text_style_list)
                    text_str = f'<text x="{x}" y="{y}" id="text-{text_id}" style="{style_str}" inkscape:label="{label}">{tspan_str}</text>'
                    with open(text_file_path, 'a') as f:
                        print(
                            text_str.encode(self.s.encoding_type, errors=self.s.encoding_error).decode(
                                encoding=self.s.decoding_type, errors=self.s.decoding_error
                            ), file=f
                        )
                with open(text_file_path, 'r') as f:
                    text_str = f.read()
                    with open(self.label_line_file_path, 'r') as f:
                        label_line_str = f.read()
                        xml_str = self.svg_regex.sub(text_str.rstrip()+label_line_str+self.regex_sub_str, xml_str, 1)
                        with open(districts_file_path, 'w') as f: print(xml_str.strip(), file=f)
            
            return districts_file_path
    
    
    ###############################
    # Methods not internally used #
    ###############################
    
    
    
    def get_google_suggestion_list(self, district_name):
        f_str = 'The whole list for {} is: {}.'
        suggestion_list = self.suggestion_list_dict[district_name]
        conjunctified_str = self.conjunctify_nouns(suggestion_list)
        
        return(f_str.format(district_name, conjunctified_str))
    
    
    
    def create_label_line_file(self):
        with open(self.label_line_file_path, 'w') as f: print('', file=f)
        mask_series = self.one_country_df.label_line_d.isnull()
        for district_name, row_series in self.one_country_df[~mask_series].sort_index(axis='index', ascending=False).iterrows():
            label_id = self.indexize_string(district_name)
            label = '{} Label Line'.format(district_name)
            label_line_str = self.l_str.format(row_series['label_line_d'], label_id, label)
            with open(self.label_line_file_path, 'a') as f:
                print(
                    label_line_str.encode(self.s.encoding_type, errors=self.s.encoding_error).decode(
                        encoding=self.s.decoding_type, errors=self.s.decoding_error
                    ), file=f
                )
    
    
    
    # Do some tf-idf calculations
    def create_suggestion_list_dictionary(self, refresh=True, prompt='why is {} so '):
        import suggests
        import logging

        logging.getLogger().setLevel(logging.CRITICAL)
        if refresh: suggestion_list_dict = {}
        else: suggestion_list_dict = self.suggestion_list_dict.copy()
        for district in self.one_country_df.index.tolist():
            if district not in suggestion_list_dict:
                response_dict = suggests.get_suggests(prompt.format(district), source='google')
                dropdown_list = [sg[0].split('>')[1].split('<')[0].strip() for sg in response_dict['data'][1]]
                suggestion_list_dict[district] = dropdown_list
        
        return suggestion_list_dict
    
    
    
    def scrape_suggestion_list_dictionary(self, refresh=True):
        
        # Retrieve the page with tag results and set it up to be scraped
        driver = u.get_driver()
        site_url = 'https://www.google.com'
        u.driver_get_url(driver, url_str=site_url, verbose=True)
        
        input_css = '.gLFyf'
        dropdown_css = '#tsf > div:nth-child(2) > div > div > div > ul'
        if refresh: suggestion_list_dict = {}
        else: suggestion_list_dict = self.suggestion_list_dict.copy()
        for district in self.one_country_df.index.tolist():
            if district not in suggestion_list_dict:
                try:

                    # Wait for input field to show up
                    input_tag = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, input_css))
                    )
                    input_tag.click()
                    ActionChains(driver).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
                    field_value = 'why is {} so '.format(district.lower())
                    input_tag.send_keys(field_value)

                except Exception as e:
                    message = str(e).strip()
                    raise Exception('Waiting for input field to show up: {}'.format(message))
                time.sleep(5)
                try:

                    # Wait for dropdown to show up
                    dropdown_tag = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, dropdown_css))
                    )
                    dropdown_list = []
                    regex_str = '(why is {} )?so '.format(district.lower())
                    dd_regex = re.compile(regex_str)
                    for dropdown in dd_regex.split(dropdown_tag.text):
                        if (dropdown is not None) and (dropdown != ''): dropdown_list.append(dropdown.strip())
                    suggestion_list_dict[district] = dropdown_list

                except Exception as e:
                    message = str(e).strip()
                    print('Wait for {} dropdown to show up: {}'.format(district, message))
        driver.quit()
        
        return suggestion_list_dict
    
    
    
    def clean_up_district_unique_dict(self):
        sorted_d, reverse_sorted_d = self.get_tfidf_lists()
        self.district_unique_dict = self.s.load_object('district_unique_dict')
        while len(self.district_unique_dict.keys()) < len(self.suggestion_list_dict):
            for (key_word, idf) in reverse_sorted_d:
                if len(self.district_unique_dict.keys()) == len(self.suggestion_list_dict): break
                for district, dropdown_list in self.suggestion_list_dict.items():
                    if len(self.district_unique_dict.keys()) == len(self.suggestion_list_dict): break
                    if district not in self.district_unique_dict.keys():
                        for ngram in dropdown_list:
                            if key_word in ngram:
                                self.district_unique_dict[district] = ngram
                                break
        self.s.store_objects(district_unique_dict=self.district_unique_dict)
    
    
    
    def clean_up_district_common_dict(self):
        sorted_d, reverse_sorted_d = self.get_tfidf_lists()
        self.district_common_dict = self.s.load_object('district_common_dict')
        while len(self.district_common_dict.keys()) < len(self.suggestion_list_dict):
            for (key_word, idf) in sorted_d:
                if len(self.district_common_dict.keys()) == len(self.suggestion_list_dict): break
                for district, dropdown_list in self.suggestion_list_dict.items():
                    if len(self.district_common_dict.keys()) == len(self.suggestion_list_dict): break
                    if district not in self.district_common_dict.keys():
                        for ngram in dropdown_list:
                            if key_word in ngram:
                                self.district_common_dict[district] = ngram
                                break
        self.s.store_objects(district_common_dict=self.district_common_dict)
    
    
    
    def create_district_first_dict(self):
        district_first_dict = {}
        for district, dropdown_list in self.suggestion_list_dict.items():
            district_first_dict[district] = dropdown_list[0]
        self.s.store_objects(district_first_dict=district_first_dict)
        
        return district_first_dict
    
    
    
    def clean_up_suggestion_list_dict(self):
        for district in self.suggestion_list_dict.keys():
            field_value = 'why is {} so '.format(district.lower())
            value_length = len(field_value)
            dropdown_list = self.suggestion_list_dict[district]
            if dropdown_list[0][:value_length] == field_value:
                dropdown_list = [st[value_length:] for st in dropdown_list]
                self.suggestion_list_dict[district] = dropdown_list
        if(set(self.one_country_df.index.tolist()) - set(self.suggestion_list_dict) == set()):
            self.s.store_objects(suggestion_list_dict=self.suggestion_list_dict)
        for old_key in self.suggestion_list_dict.keys():
            new_key = re.sub(r'\xa0', r'', old_key)
            self.suggestion_list_dict[new_key] = self.suggestion_list_dict.pop(old_key)
    
    
    def show_colorbar(self, column_name, cmap='viridis', min=None, max=None):
        '''
        column_name = 'Total_Gun_Murder_Deaths_2010'
        cb1 = cu.show_colorbar(column_name)
        print(['cb1.ax.{}'.format(fn) for fn in dir(cb1.ax) if 'get_y' in fn.lower()])
        '''
        fig, ax = plt.subplots(figsize=(1, 6))
        fig.subplots_adjust(left=0.5)
        
        if min is None: min = self.one_country_df[column_name].min()
        if max is None: max = self.one_country_df[column_name].max()
        cmap = mpl.cm.get_cmap(cmap)
        norm = mpl.colors.Normalize(vmin=min, vmax=max)
        
        cb1 = mpl.colorbar.ColorbarBase(ax, cmap=cmap, norm=norm, orientation='vertical')
        cb1.set_label(self.get_column_description(column_name))
        file_path = osp.join(self.svg_dir, 'colorbar.svg')
        plt.savefig(file_path)
        plt.close(fig)
        
        return cb1
    
    
    
    def clean_up_district_merge_dataframe(self):
        for column_name in self.one_country_df.columns:
            try:
                self.one_country_df[column_name] = pd.to_numeric(
                    self.one_country_df[column_name], errors='raise', downcast='float'
                )
            except Exception as e: print('The {} column get this error: {}'.format(column_name, str(e).strip()))
        self.s.store_objects(one_country_df=self.one_country_df)
    
    
    
    @staticmethod
    def convert_svg_to_dataframe(file_path):
        root = et.parse(file_path).getroot()
        rows_list = []
        for el in root.iter(): rows_list.append(el.attrib)
        df = pd.DataFrame(rows_list).rename(columns={'style': 'element_style', 'd': 'outline_d'})
        
        return df
    
    
    
    def get_greatest_area(self, g_soup):
        path_id = path_obj = None
        path_tuples_list = [(path_soup['id'], path_soup['d']) for path_soup in g_soup.find_all(self.has_no_limitxx)]
        
        # Find the path object with the greatest area
        import svgpathtools
        if len(path_tuples_list) > 1:
            path_objs_list = [(path_id, svgpathtools.parse_path(pathdef=d_path, current_pos=0j)) for (path_id, d_path) in path_tuples_list]
            closed_path_objs_list = []
            for (path_id, path_obj) in path_objs_list:
                if (not path_obj.iscontinuous()) or (not path_obj.isclosed()):
                    (xmin, xmax, ymin, ymax) = path_obj.bbox()
                    d_path = f'M {xmin},{ymin} H {xmax} V {ymax} H {xmin} V {ymin} Z'
                    path_obj = svgpathtools.parse_path(pathdef=d_path, current_pos=0j)
                path_tuple = (path_id, path_obj)
                closed_path_objs_list.append(path_tuple)
            (path_id, path_obj) = sorted(closed_path_objs_list, key=lambda x: x[1].area())[-1]
        else:
            for (path_id, d_path) in path_tuples_list:
                path_obj = svgpathtools.parse_path(pathdef=d_path, current_pos=0j)
        
        return path_id, path_obj
    
    
    
    @staticmethod
    def has_no_limitxx(tag_obj):
        result_bool = False
        if (tag_obj.name == 'path') and ('d' in tag_obj.attrs):
            if ('class' not in tag_obj.attrs) or ('limitxx' not in tag_obj['class']): result_bool = True
        
        return result_bool
    
    
    
    @staticmethod
    def path_to_poly(inpath):
        '''Convert paths to polygons'''
        points = []
        from svgpathtools import Line
        for path in inpath:
            if isinstance(path, Line): points.append([path.end.real, path.end.imag])
            else:
                num_segments = math.ceil(path.length() / 1.0)
                for seg_i in range(int(num_segments + 1)):
                    xy_list = [
                        path.point(seg_i / num_segments).real,
                        path.point(seg_i / num_segments).imag
                        ]
                    points.append(xy_list)
        from shapely.geometry import Polygon

        return Polygon(points)
