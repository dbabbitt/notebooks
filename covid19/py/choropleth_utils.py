#!/usr/bin/env python
# coding: utf-8

from matplotlib import cm
from shutil import copyfile
from sklearn.feature_extraction.text import TfidfVectorizer
from xml.etree.ElementTree import Element
import math
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import os
import pylab
import pyphen
import re
import textwrap
import xml
import xml.etree.ElementTree as et
import warnings
warnings.filterwarnings("ignore")

import storage
s = storage.Storage()

# Handy list of the different types of encodings
encoding_types_list = ['ascii', 'cp037', 'cp437', 'cp863', 'utf_32', 'utf_32_be', 'utf_32_le', 'utf_16', 'utf_16_be', 'utf_16_le', 'utf_7',
                       'utf_8', 'utf_8_sig', 'latin1', 'iso8859-1']
encoding_errors_list = ['ignore', 'replace', 'xmlcharrefreplace']
decoding_types_list = encoding_types_list.copy()
decoding_errors_list = encoding_errors_list.copy()
s.encoding_type = encoding_types_list[0]
s.encoding_error = encoding_errors_list[2]
s.decoding_type = decoding_types_list[11]
s.decoding_error = decoding_errors_list[0]

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
    
    >>> import choropleth_utils
    >>> 
    >>> afghanistan_provinces_df = s.load_object('afghanistan_provinces_df')
    >>> c = choropleth_utils.ChoroplethUtilities(iso_3166_2_code='af', one_country_df=afghanistan_provinces_df)
    """
    
    def __init__(self, iso_3166_2_code=None, one_country_df=None, all_countries_df=None):
        if iso_3166_2_code is None:
            self.iso_3166_2_code = 'us'
        else:
            self.iso_3166_2_code = iso_3166_2_code.lower()
        if one_country_df is None:
            self.one_country_df = s.load_object('us_stats_df')
        else:
            self.one_country_df = one_country_df
        if all_countries_df is None:
            self.all_countries_df = s.load_object('all_countries_df')
        else:
            self.all_countries_df = all_countries_df
        mask_series = (self.all_countries_df.index == self.iso_3166_2_code.upper())
        self.settings_dict = self.all_countries_df[mask_series].to_dict(orient='records')[0]
        
        # Define the SVG parts
        font_size = self.settings_dict.get('font_size', 12)
        if str(font_size) == 'nan':
            font_size = 12
        self.text_style_dict = {'font-style': 'normal', 'font-variant': 'normal', 'font-weight': 'normal',
                                'font-stretch': 'normal', 'font-size': '{}px'.format(font_size), 'line-height': '1.25',
                                'font-family': 'sans-serif', '-inkscape-font-specification': 'sans-serif, Normal',
                                'font-variant-ligatures': 'normal', 'font-variant-caps': 'normal',
                                'font-variant-numeric': 'normal', 'font-feature-settings': 'normal',
                                'text-align': 'center', 'letter-spacing': '0px', 'word-spacing': '0px',
                                'writing-mode': 'lr-tb', 'text-anchor': 'middle', 'fill': '#000000',
                                'fill-opacity': '1', 'stroke': 'none'}
        self.text_style_list = self.get_style_list(self.text_style_dict.copy())
        self.t_str = '''  <text
     x="{{}}"
     y="{{}}"
     id="text-{{}}"
     xml:space="preserve"
     style="{}"
     inkscape:label="{{}}">{{}}</text>'''.format(';'.join(self.text_style_list))
        self.ts_str = '''<tspan
       sodipodi:role="line"
       id="tspan-{}"
       x="{}"
       y="{}">{}</tspan>'''
        self.label_line_style_dict = {'fill': 'none', 'fill-rule': 'evenodd', 'stroke': '#e00000',
                                      'stroke-width': '2', 'stroke-linecap': 'butt', 'stroke-linejoin': 'miter',
                                      'stroke-opacity': '1', 'font-variant-east_asian': 'normal', 'opacity': '1',
                                      'vector-effect': 'none', 'fill-opacity': '1', 'stroke-miterlimit': '4',
                                      'stroke-dasharray': 'none', 'stroke-dashoffset': '0'}
        self.label_line_style_list = self.get_style_list(self.label_line_style_dict.copy())
        self.l_str = '''  <path
     style="{}"
     d="{{}}"
     id="path-{{}}"
     inkscape:connector-curvature="0"
     inkscape:label="{{}}" />'''.format(';'.join(self.label_line_style_list))
        self.label_line_file_path = os.path.join(s.saves_folder, 'xml', '{}_districts_label_line.xml'.format(self.iso_3166_2_code))
        self.svg_suffix = '''
</svg>'''
        self.regex_sub_str = self.svg_suffix.strip()
        self.svg_regex = re.compile(self.regex_sub_str)
        if self.iso_3166_2_code == 'us':
            self.copy_file_name = 'us - Copy.svg'
        elif self.iso_3166_2_code == 'af':
            self.copy_file_name = 'Afghanistan - Copy.svg'
        self.copy_file_path = os.path.join(s.data_folder, 'svg', self.copy_file_name)
        if ('svg_width' not in self.all_countries_df.columns) or ('svg_height' not in self.all_countries_df.columns):
            raise Exception('svg_width and svg_height must be in your all_countries_df')
        self.svg_width = self.settings_dict['svg_width']
        self.svg_height = self.settings_dict['svg_height']
        inkscape_cx = self.settings_dict.get('inkscape_cx', 519.35606)
        if str(inkscape_cx) == 'nan':
            inkscape_cx = 519.35606
        inkscape_cy = self.settings_dict.get('inkscape_cy', 287.55662)
        if str(inkscape_cy) == 'nan':
            inkscape_cy = 287.55662
        inkscape_zoom = self.settings_dict.get('inkscape_zoom', 1.2776908)
        if str(inkscape_zoom) == 'nan':
            inkscape_zoom = 1.2776908
        self.svg_attributes_list = ['xmlns:dc="http://purl.org/dc/elements/1.1/"',
                                    'xmlns:cc="http://creativecommons.org/ns#"',
                                    'xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"',
                                    'xmlns:svg="http://www.w3.org/2000/svg"', 'xmlns="http://www.w3.org/2000/svg"',
                                    'xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"',
                                    'xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"',
                                    'enable_background="new 0 0 {} {}"'.format(self.svg_width, self.svg_height),
                                    'height="{}px"'.format(self.svg_height),
                                    'id="svg"',
                                    'inkscape:version="0.92.4 (5da689c313, 2019-01-14)"',
                                    'style="fill:none;stroke:#000000;stroke-linejoin:round"',
                                    'version="1.0"',
                                    'viewBox="0 0 {} {}"'.format(self.svg_width, self.svg_height),
                                    'width="{}px"'.format(self.svg_width)]
        self.namedview_attributes_list = ['pagecolor="#ffffff"', 'bordercolor="#666666"', 'borderopacity="1"',
                                          'objecttolerance="10"', 'gridtolerance="10"', 'guidetolerance="10"',
                                          'inkscape:pageopacity="0"', 'inkscape:pageshadow="2"',
                                          'inkscape:window-width="1846"', 'inkscape:window-height="1057"',
                                          'id="named-view"', 'showgrid="false"', 'inkscape:zoom="{}"'.format(inkscape_zoom),
                                          'inkscape:cx="{}"'.format(inkscape_cx), 'inkscape:cy="{}"'.format(inkscape_cy),
                                          'inkscape:window-x="1432"', 'inkscape:window-y="112"',
                                          'inkscape:window-maximized="1"', 'inkscape:current-layer="svg"']
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
        <rdf:RDF><cc:Work rdf:about="">
            <dc:format>image/svg+xml</dc:format>
            <dc:type rdf:resource="http://purl.org/dc/dcmitype/StillImage" />
            <dc:title>File: {}</dc:title>
        </cc:Work></rdf:RDF>
  </metadata>
  <rect
     height="{}"
     id="adjacent-country-backgrounds"
     style="display:inline;fill:#e0e0e0"
     width="{}"
     x="0"
     y="0"
     inkscape:label="Adjacent Country Backgrounds" />'''
        self.html_style_str = '#{:02x}{:02x}{:02x}'
        self.fill_style_prefix = 'stroke-width:1.0;fill:{}'
        self.fill_style_str = self.fill_style_prefix.format(self.html_style_str)
        self.district_path_str = '<path id="{}" d="{}" data-id="{}" data-name="{}" style="{}" inkscape:connector-curvature="0" />'
        self.svg_dir = os.path.abspath(os.path.join(s.saves_folder, 'svg'))
        os.makedirs(name=self.svg_dir, exist_ok=True)
        
        # Unused XML bits for making your own colorbar
        self.figure_str = '''
  <g
     id="figure-main"
     style="stroke-linecap:butt;stroke-linejoin:round"
     inkscape:label="Column Name Colorbar">{}{}
  </g>'''
        self.label_text_style_list = ['font-style:normal', 'font-variant:normal', 'font-weight:normal',
                                      'font-stretch:normal', 'font-size:18px', 'line-height:1.25',
                                      'font-family:sans-serif',
                                      "-inkscape-font-specification:'sans-serif, Normal'",
                                      'font-variant-ligatures:normal', 'font-variant-caps:normal',
                                      'font-variant-numeric:normal', 'font-feature-settings:normal',
                                      'text-align:center', 'letter-spacing:0px', 'word-spacing:0px',
                                      'writing-mode:lr-tb', 'text-anchor:middle', 'fill:#000000', 'fill-opacity:1',
                                      'stroke:none', 'stroke-width:0.75', 'stroke-linecap:butt',
                                      'stroke-linejoin:round']
        self.label_tspan_style_list = ['font-style:normal', 'font-variant:normal', 'font-weight:normal',
                                       'font-stretch:normal', 'font-size:18px', 'font-family:sans-serif',
                                       "-inkscape-font-specification:'sans-serif, Normal'",
                                       'font-variant-ligatures:normal', 'font-variant-caps:normal',
                                       'font-variant-numeric:normal', 'font-feature-settings:normal',
                                       'text-align:center', 'writing-mode:lr-tb', 'text-anchor:middle',
                                       'stroke-width:0.75', 'stroke-linecap:butt', 'stroke-linejoin:round']
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
        self.gradient_file_path = os.path.join(s.data_folder, 'txt', 'gradient.txt')
        with open(self.gradient_file_path, 'r') as f:
            self.gradient_str = f.read()
        self.matplotlib_axis_str = '''
      <g
         id="matplotlib.axis-colorbar"
         style="stroke-linecap:butt;stroke-linejoin:round"
         inkscape:label="Axis Text">{}
      </g>'''
        self.tick_text_style_list = ['font-style:normal', 'font-variant:normal', 'font-weight:normal',
                                     'font-stretch:normal', 'font-size:10px', 'line-height:1.25',
                                     'font-family:sans-serif',
                                     "-inkscape-font-specification:'sans-serif, Normal'",
                                     'font-variant-ligatures:normal', 'font-variant-caps:normal',
                                     'font-variant-numeric:normal', 'font-feature-settings:normal',
                                     'text-align:center', 'letter-spacing:0px', 'word-spacing:0px',
                                     'writing-mode:lr-tb', 'text-anchor:middle', 'fill:#000000', 'fill-opacity:1',
                                     'stroke:none', 'stroke-width:0.75', 'stroke-linecap:butt',
                                     'stroke-linejoin:round']
        self.tick_tspan_style_list = ['font-style:normal', 'font-variant:normal', 'font-weight:normal',
                                      'font-stretch:normal', 'font-size:10px', 'font-family:sans-serif',
                                      "-inkscape-font-specification:'sans-serif, Normal'",
                                      'font-variant-ligatures:normal', 'font-variant-caps:normal',
                                      'font-variant-numeric:normal', 'font-feature-settings:normal',
                                      'text-align:center', 'writing-mode:lr-tb', 'text-anchor:middle',
                                      'stroke-width:0.75', 'stroke-linecap:butt', 'stroke-linejoin:round']
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
        self.line_height = 15
        self.intra_country_borders_str = '''
		<path
   id="intra-country-borders"
   d="{}"
   style="display:inline;fill:#fefee9"
   inkscape:connector-curvature="0"
   inkscape:label="{} Background" />'''
        self.width_ratio = -0.027663496798780152
        self.height_ratio = -0.0676069034160266
    
    
    ###########################
    # Methods used internally #
    ###########################
    
    
    
    def trim_d_path(self, file_path):
        with open(file_path, 'r', encoding=s.encoding_type, errors='ignore') as f:
            xml_str = f.read()
            d_regex = re.compile('d="([^"\r\n]+)[\r\n]+')
            while d_regex.search(xml_str):
                xml_str = d_regex.sub(r'd="\g<1>', xml_str)
            with open(file_path, 'w') as f:
                print(xml_str.strip().encode(s.encoding_type, errors=s.encoding_error).decode(encoding=s.decoding_type,
                                                                                              errors=s.decoding_error), file=f)
    
    
    
    def conjunctify_list(self, noun_list):
        if len(noun_list) > 2:
            list_str = ', and '.join([', '.join(noun_list[:-1])] + [noun_list[-1]])
        elif len(noun_list) == 2:
            list_str = ' and '.join(noun_list)
        elif len(noun_list) == 1:
            list_str = noun_list[0]
        else:
            list_str = ''
        
        return list_str
    
    
    
    def get_style_list(self, style_dict):
        style_list = []
        for key, value in style_dict.items():
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
        self.suggestion_list_dict = s.load_object('suggestion_list_dict')
        
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
    
    
    
    def get_legend_xml(self, labels_list):
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
            style_tuple = tuple(int(x*255) for x in PathCollection_obj.get_facecolor()[0][:-1])
            color = self.html_style_str.format(*style_tuple)
            colors_list.append(color)

        # Build and save legend for further manipulation
        legend_obj = pylab.legend(artists_list, labels_list, loc='upper left')
        file_path = os.path.join(self.svg_dir, 'legend.svg')
        plt.savefig(file_path)
        plt.close(fig)

        # Trim the legend xml
        self.trim_d_path(file_path)
        root = et.parse(file_path).getroot()
        for figure_1_xml in root.getchildren():
            if (figure_1_xml.tag.split('}')[-1] == 'g'):
                id = figure_1_xml.attrib['id']
                if id == 'figure_1':
                    key = 'transform'
                    value = '{}'.format(self.settings_dict.get('legend_transform', 'matrix(1,0,0,1,-35,-50)'))
                    if value == 'nan':
                        value = 'matrix(1,0,0,1,-35,-50)'
                    figure_1_xml.attrib[key] = value
                    break
        for axes_1_xml in figure_1_xml.getchildren():
            if (axes_1_xml.tag.split('}')[-1] == 'g'):
                id = axes_1_xml.attrib['id']
                if id == 'axes_1':
                    break
        path_collection_list = []
        path_strs_list = []
        for axes_element in axes_1_xml.getchildren():
            id = axes_element.attrib['id']
            if id.startswith('PathCollection_'):
                path_collection_list.append(id)
                for defs_element in axes_element.getchildren():
                    if (defs_element.tag.split('}')[-1].split(':')[-1] == 'defs'):
                        for path_element in defs_element.getchildren():
                            path_str = et.tostring(path_element, encoding='unicode')
                            path_str = '<{}'.format(':'.join(path_str.strip().split(':')[1:]))
                            path_strs_list.append(path_str)
        #print(path_strs_list)
        for legend_1_xml in axes_1_xml.getchildren():
            if (legend_1_xml.tag.split('}')[-1] == 'g'):
                id = legend_1_xml.attrib['id']
                if id == 'legend_1':
                    key = 'style'
                    value = 'fill:#000000;fill-opacity:1'
                    legend_1_xml.attrib[key] = value
                    defs_xml_str = '<defs>'
                    for path_str in path_strs_list:
                        defs_xml_str += path_str
                    defs_xml_str += '</defs>'
                    #print(defs_xml_str)
                    legend_1_xml.insert(0, et.fromstring(defs_xml_str))
                    break
        axes_id_list = ['patch_2', 'matplotlib.axis_1', 'matplotlib.axis_2', 'patch_3', 'patch_4', 'patch_5',
                        'patch_6']
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
        fig, ax = plt.subplots(figsize=(1, 6))
        fig.subplots_adjust(left=0.5)
        
        if min is None:
            min = self.one_country_df[column_name].min()
        if max is None:
            max = self.one_country_df[column_name].max()
        cmap = mpl.cm.get_cmap(cmap)
        norm = mpl.colors.Normalize(vmin=min, vmax=max)
        
        cb1 = mpl.colorbar.ColorbarBase(ax, cmap=cmap, norm=norm,
                                        orientation='vertical')
        cb1.set_label(self.get_column_description(column_name))
        file_path = os.path.join(self.svg_dir, 'colorbar.svg')
        plt.savefig(file_path)
        plt.close(fig)
        self.trim_d_path(file_path)
        root = et.parse(file_path).getroot()
        for colorbar_xml in root.getchildren():
            if (colorbar_xml.tag.split('}')[-1] == 'g'):
                id = colorbar_xml.attrib['id']
                if id == 'figure_1':
                    break
        for axes_element in colorbar_xml:
            id = axes_element.attrib['id']
            if id == 'axes_1':
                for matplotlib_element in axes_element:
                    id = matplotlib_element.attrib['id']
                    if id == 'matplotlib.axis_2':
                        key = 'style'
                        value = 'fill:#000000;fill-opacity:1'
                        matplotlib_element.attrib[key] = value
                        break
                break
        for patch_element in colorbar_xml:
            id = patch_element.attrib['id']
            if id == 'patch_1':
                colorbar_xml.remove(patch_element)
                break
        
        return et.tostring(colorbar_xml, encoding='unicode')
    
    
    
    def get_column_description(self, column_name):
        self.column_description_dict = s.load_object('column_description_dict')
        if column_name in self.column_description_dict:
            column_description = self.column_description_dict[column_name]
        else:
            column_description = re.sub('^pf_', 'Personal Freedom:_', str(column_name), 1)
            column_description = re.sub('^hf_', 'Human Freedom:_', str(column_description), 1)
            column_description = re.sub('^ef_', 'Economic Freedom:_', str(column_description), 1)
            column_list = column_description.split('_')
            descr_list = []
            for word in column_list:
                descr_list.append(word[0].upper()+word[1:])
            column_description = ' '.join(descr_list)
            self.column_description_dict[column_name] = column_description
            s.store_objects(column_description_dict=self.column_description_dict)
        
        return column_description
    
    
    ########################
    # Map Creation Methods #
    ########################
    
    
    
    def create_country_colored_labeled_map(self, numeric_column_name, string_column_name=None, one_country_df=None, cmap='viridis'):
        """
        one_country_df must have district names as an index, the district_abbreviation, outline_d, text_x and
        text_y columns, one (hopefully) numeric column labeled numeric_column_name, and one
        (not neccesarily) string column labeled string_column_name
        
        numeric_column_name = 'Total_Gun_Murder_Deaths_2010'
        string_column_name = 'Google_Suggest_Unique'
        svg_file_path = c.create_country_colored_labeled_map(numeric_column_name=numeric_column_name,
                                                             string_column_name=string_column_name,
                                                             one_country_df=c.one_country_df)
        
        numeric_column_name = 'Asian_Percent'
        string_column_name = 'Google_Suggest_Common'
        svg_file_path = c.create_country_colored_labeled_map(numeric_column_name=numeric_column_name,
                                                             string_column_name=string_column_name,
                                                             one_country_df=c.one_country_df)
        
        string_column_name = None
        for numeric_column_name in c.one_country_df.columns:
            svg_file_path = c.create_country_colored_labeled_map(numeric_column_name=numeric_column_name,
                                                                 string_column_name=string_column_name,
                                                                 one_country_df=c.one_country_df)
        """
        
        if one_country_df is None:
            one_country_df = self.one_country_df.copy()
        if not np.issubdtype(one_country_df[numeric_column_name].dtype, np.number):
            raise Exception('{} is not numeric'.format(numeric_column_name))
        if not os.path.exists(self.copy_file_path):
            raise Exception('{} does not exist'.format(self.copy_file_path))
        if not os.path.exists(self.label_line_file_path):
            raise Exception('{} does not exist'.format(self.label_line_file_path))
        if 'district_abbreviation' not in one_country_df.columns:
            raise Exception('one_country_df needs to have the district_abbreviation column')
        if 'outline_d' not in one_country_df.columns:
            raise Exception('one_country_df needs to have the outline_d column')
        if 'text_x' not in one_country_df.columns:
            raise Exception('one_country_df needs to have the text_x column')
        if 'text_y' not in one_country_df.columns:
            raise Exception('one_country_df needs to have the text_y column')
        
        # Create the text tag xml
        if string_column_name is None:
            file_name = 'index_districts_text.xml'
        else:
            file_name = '{}_districts_text.xml'.format(string_column_name)
        text_file_path = os.path.join(s.saves_folder, 'xml', file_name)
        with open(text_file_path, 'w') as f:
            print('', file=f)
        if string_column_name is None:
            mask_series = one_country_df['text_x'].isnull() | one_country_df['text_y'].isnull()
        else:
            mask_series = one_country_df[string_column_name].isnull()
        for district_name, row_series in one_country_df[~mask_series].sort_index(axis='index', ascending=False).iterrows():
            id = '{}'.format('-'.join(district_name.lower().split(' ')))
            if string_column_name is None:
                label = '{} Index'.format(district_name)
            else:
                label = '{} {}'.format(district_name, ' '.join(string_column_name.split('_')))
            x = row_series['text_x']
            if str(x) == 'nan':
                x = 900.94183
            y = row_series['text_y']
            if str(y) == 'nan':
                y = 546.21332
            if string_column_name is None:
                column_value = district_name.strip()
            else:
                column_value = row_series[string_column_name].strip()
            tspan_list = self.get_tspan_list(column_value)
            tspan_str = ''
            for i, column_value_str in enumerate(tspan_list):
                tspan_str += self.ts_str.format(id+str(i), x, y+self.line_height*i, column_value_str)
            text_str = self.t_str.format(x, y, id, label, tspan_str)
            with open(text_file_path, 'a') as f:
                print(text_str.encode(s.encoding_type, errors=s.encoding_error).decode(encoding=s.decoding_type,
                                                                                       errors=s.decoding_error), file=f)
        
        # Build the SVG file from scratch
        if string_column_name is None:
            svg_file_name = '{}_Index_{}.svg'.format(self.iso_3166_2_code.upper(), numeric_column_name)
        else:
            svg_file_name = '{}_{}_{}.svg'.format(self.iso_3166_2_code.upper(), numeric_column_name, string_column_name)
        svg_file_path = os.path.join(s.saves_folder, 'svg', svg_file_name)
        if not os.path.exists(svg_file_path):
            copyfile(self.copy_file_path, svg_file_path)
        with open(svg_file_path, 'w') as f:
            attributes_list = self.svg_attributes_list.copy()
            attributes_list.append('sodipodi:docname="{}"'.format(svg_file_name))
            svg_prefix = self.svg_prefix_str.format(' '.join(attributes_list),
                                                    ' '.join(self.namedview_attributes_list),
                                                    self.copy_file_name, self.svg_height,
                                                    self.svg_width)
            print(svg_prefix, file=f)
        
        # Create the outline paths
        ListedColormap_obj = cm.get_cmap(cmap, len(one_country_df[numeric_column_name].unique()))
        min = one_country_df[numeric_column_name].min()
        max = one_country_df[numeric_column_name].max()
        mask_series = one_country_df[numeric_column_name].isnull()
        for district_name, row_series in one_country_df[~mask_series].sort_index(axis='index', ascending=False).iterrows():
            column_value = row_series[numeric_column_name]
            district_abbreviation = row_series.district_abbreviation
            outline_d = row_series.outline_d
            normed_value = (column_value - min) / (max - min)
            style_tuple = tuple(int(x*255) for x in ListedColormap_obj(normed_value)[:-1])
            style_value = self.fill_style_str.format(*style_tuple)
            id_value = 'district-{}'.format('-'.join(district_name.lower().split(' ')))
            path_tag = self.district_path_str.format(id_value, outline_d, district_abbreviation,
                                                  district_name, style_value)
            with open(svg_file_path, 'a') as f:
                print(path_tag, file=f)
        
        # Paste it all together
        with open(text_file_path, 'r') as f:
            text_str = f.read()
            with open(self.label_line_file_path, 'r') as f:
                label_line_str = f.read()
                with open(svg_file_path, 'a') as f:
                
                    # Add the text labels
                    print(text_str, file=f)
                
                    # Add the label lines
                    print(label_line_str, file=f)
                    
                    # Add the colorbar
                    colorbar_xml = self.get_colorbar_xml(numeric_column_name, cmap=cmap)
                    print(colorbar_xml, file=f)
                    
                    print(self.regex_sub_str, file=f)
        
        return svg_file_path
    
    
    
    def create_country_colored_map(self, numeric_column_name, one_country_df=None, cmap='viridis', min=None, max=None):
        '''
        one_country_df must have district names as an index, the district_abbreviation and outline_d columns,
        and one (hopefully) numeric column labeled whatever you're putting in numeric_column_name
        
        numeric_column_name = 'Total_Gun_Murder_Deaths_2010'
        svg_file_path = c.create_country_colored_map(numeric_column_name, one_country_df=c.one_country_df)
        
        numeric_column_name = 'Asian_Percent'
        svg_file_path = c.create_country_colored_map(numeric_column_name, one_country_df=c.one_country_df)
        
        for numeric_column_name in c.one_country_df.columns:
            svg_file_path = c.create_country_colored_map(numeric_column_name=numeric_column_name,
                                                         one_country_df=c.one_country_df)
        '''
        if one_country_df is None:
            one_country_df = self.one_country_df.copy()
        if np.issubdtype(one_country_df[numeric_column_name].dtype, np.number):
            ListedColormap_obj = cm.get_cmap(cmap, len(one_country_df[numeric_column_name].unique()))
            if min is None:
                min = one_country_df[numeric_column_name].min()
            if max is None:
                max = one_country_df[numeric_column_name].max()
            svg_file_path = os.path.join(s.saves_folder, 'svg', '{}_{}.svg'.format(self.iso_3166_2_code.upper(), numeric_column_name))
            with open(svg_file_path, 'w') as f:
                attributes_list = self.svg_attributes_list.copy()
                attributes_list.append('sodipodi:docname="{}.svg"'.format(numeric_column_name))
                svg_prefix = self.svg_prefix_str.format(' '.join(attributes_list),
                                                        ' '.join(self.namedview_attributes_list),
                                                        self.copy_file_name, self.svg_height,
                                                        self.svg_width)
                print(svg_prefix, file=f)
            for district_name, row_series in one_country_df.sort_index(axis='index', ascending=False).iterrows():
                column_value = row_series[numeric_column_name]
                district_abbreviation = row_series.district_abbreviation
                outline_d = row_series.outline_d
                if str(column_value) != 'nan':
                    normed_value = (column_value - min) / (max - min)
                    style_tuple = tuple(int(x*255) for x in ListedColormap_obj(normed_value)[:-1])
                else:
                    style_tuple = (128, 128, 128)
                style_value = self.fill_style_str.format(*style_tuple)
                id_value = 'district-{}'.format('-'.join(district_name.lower().split(' ')))
                path_tag = self.district_path_str.format(id_value, outline_d, district_abbreviation,
                                                         district_name, style_value)
                with open(svg_file_path, 'a') as f:
                    print(path_tag, file=f)
            
            # Create the colorbar
            colorbar_xml = self.get_colorbar_xml(numeric_column_name, cmap=cmap, min=min, max=max)
            with open(svg_file_path, 'a') as f:
                print(colorbar_xml, file=f)
                print(self.svg_suffix, file=f)
            
            return svg_file_path
    
    
    
    def create_country_labeled_map(self, string_column_name, one_country_df=None):
        """
        one_country_df must have district names as an index, the district_abbreviation, outline_d, text_x and
        text_y columns, and one (not neccesarily) string column labeled string_column_name
        
        string_column_name = 'Google_Suggest_Unique'
        svg_file_path = c.create_country_labeled_map(string_column_name=string_column_name,
                                                     one_country_df=c.one_country_df)
        
        string_column_name = 'Google_Suggest_Common'
        svg_file_path = c.create_country_labeled_map(string_column_name=string_column_name,
                                                     one_country_df=c.one_country_df)
        
        string_column_name = 'Google_Suggest_First'
        svg_file_path = c.create_country_labeled_map(string_column_name=string_column_name,
                                                     one_country_df=c.one_country_df)
        """
        
        if one_country_df is None:
            one_country_df = self.one_country_df.copy()
        if not os.path.exists(self.copy_file_path):
            raise Exception('{} does not exist'.format(self.copy_file_path))
        if not os.path.exists(self.label_line_file_path):
            raise Exception('{} does not exist'.format(self.label_line_file_path))
        
        # Create the text tag xml
        file_name = '{}_districts_text.xml'.format(string_column_name)
        text_file_path = os.path.join(s.saves_folder, 'xml', file_name)
        with open(text_file_path, 'w') as f:
            print('', file=f)
        mask_series = one_country_df[string_column_name].isnull()
        for district_name, row_series in one_country_df[~mask_series].sort_index(axis='index', ascending=False).iterrows():
            id = '{}'.format('-'.join(district_name.lower().split(' ')))
            label = '{} {}'.format(district_name, ' '.join(string_column_name.split('_')))
            x = row_series['text_x']
            if str(x) == 'nan':
                x = 900.94183
            y = row_series['text_y']
            if str(y) == 'nan':
                y = 546.21332
            column_value = row_series[string_column_name].strip()
            tspan_list = self.get_tspan_list(column_value)
            tspan_str = ''
            for i, column_value_str in enumerate(tspan_list):
                tspan_str += self.ts_str.format(id+str(i), x, y+self.line_height*i, column_value_str)
            text_str = self.t_str.format(x, y, id, label, tspan_str)
            with open(text_file_path, 'a') as f:
                #print(text_str.encode(s.encoding_type, errors=s.encoding_error).decode(), file=f)
                print(text_str.encode(s.encoding_type, errors=s.encoding_error).decode(encoding=s.decoding_type,
                                                                                       errors=s.decoding_error), file=f)
        
        # Build the SVG file from scratch
        svg_file_name = '{}_{}.svg'.format(self.iso_3166_2_code.upper(), re.sub(r'[:]+', '_', string_column_name))
        svg_file_path = os.path.join(s.saves_folder, 'svg', svg_file_name)
        if not os.path.exists(svg_file_path):
            copyfile(self.copy_file_path, svg_file_path)
        with open(svg_file_path, 'w') as f:
            attributes_list = self.svg_attributes_list.copy()
            attributes_list.append('sodipodi:docname="{}"'.format(svg_file_name))
            svg_prefix = self.svg_prefix_str.format(' '.join(attributes_list),
                                                    ' '.join(self.namedview_attributes_list),
                                                    self.copy_file_name, self.svg_height,
                                                    self.svg_width)
            print(svg_prefix, file=f)
        
        # Create the outline paths
        mask_series = one_country_df[string_column_name].isnull()
        labels_list = self.one_country_df[~mask_series][string_column_name].unique().tolist()
        legend_xml, colors_dict = self.get_legend_xml(labels_list)
        for district_name, row_series in one_country_df.sort_index(axis='index', ascending=False).iterrows():
            column_value = str(row_series[string_column_name]).strip()
            if column_value in colors_dict:
                color = colors_dict[column_value]
            else:
                color = '#f9f9f9'
            district_abbreviation = row_series.district_abbreviation
            outline_d = row_series.outline_d
            style_value = self.fill_style_prefix.format(color)
            id_value = 'district-{}'.format('-'.join(district_name.lower().split(' ')))
            path_tag = self.district_path_str.format(id_value, outline_d, district_abbreviation,
                                                  district_name, style_value)
            with open(svg_file_path, 'a') as f:
                print(path_tag, file=f)
        
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
                    if len(colors_dict.keys()) < 11:
                        print(legend_xml, file=f)
                    
                    print(self.regex_sub_str, file=f)
        
        return svg_file_path
    
    
    
    def create_us_google_suggest_labeled_map(self, cu_str='unique'):
        """
        districts_file_path = c.create_us_google_suggest_labeled_map(cu_str='unique')
        districts_file_path = c.create_us_google_suggest_labeled_map(cu_str='common')
        districts_file_path = c.create_us_google_suggest_labeled_map(cu_str='first')
        """
        if os.path.exists(self.copy_file_path) and os.path.exists(self.label_line_file_path):
            districts_file_path = os.path.join(s.saves_folder, 'svg', '{}_{}.svg'.format(self.iso_3166_2_code.upper(), cu_str.upper()))
            if os.path.exists(districts_file_path):
                os.remove(districts_file_path)
            copyfile(self.copy_file_path, districts_file_path)
            with open(districts_file_path, 'r') as f:
                xml_str = f.read()
            if self.svg_regex.search(xml_str):
                text_file_path = os.path.join(s.saves_folder, 'xml', '{}_districts_text.xml'.format(cu_str))
                with open(text_file_path, 'w') as f:
                    print('', file=f)
                cap_str = cu_str[:1].upper()+cu_str[1:]
                column_name = 'Google_Suggest_{}'.format(cap_str)
                mask_series = self.one_country_df[column_name].isnull()
                for district_name, row_series in self.one_country_df[~mask_series].sort_index(axis='index', ascending=False).iterrows():
                    id = '{}'.format('-'.join(district_name.lower().split(' ')))
                    label = '{} Google {} Suggestion'.format(district_name, cap_str)
                    suggestion = row_series[column_name]
                    x = row_series['text_x']
                    if str(x) == 'nan':
                        x = 900.94183
                    y = row_series['text_y']
                    if str(y) == 'nan':
                        y = 546.21332
                    tspan_list = self.get_tspan_list(suggestion)
                    tspan_str = ''
                    for i, suggestion_str in enumerate(tspan_list):
                        tspan_str += self.ts_str.format(id+str(i), x, y+self.line_height*i, suggestion_str)
                    text_str = self.t_str.format(x, y, id, label, tspan_str)
                    with open(text_file_path, 'a') as f:
                        print(text_str.encode(s.encoding_type, errors=s.encoding_error).decode(encoding=s.decoding_type,
                                                                                               errors=s.decoding_error), file=f)
                with open(text_file_path, 'r') as f:
                    text_str = f.read()
                    with open(self.label_line_file_path, 'r') as f:
                        label_line_str = f.read()
                        xml_str = self.svg_regex.sub(text_str.rstrip()+label_line_str+self.regex_sub_str, xml_str, 1)
                        with open(districts_file_path, 'w') as f:
                            print(xml_str.strip(), file=f)
            
            return districts_file_path
    
    
    ###############################
    # Methods not internally used #
    ###############################
    
    
    
    def get_google_suggestion_list(self, district_name):
        f_str = 'The whole list for {} is: {}.'
        suggestion_list = self.suggestion_list_dict[district_name]
        conjunctified_str = self.conjunctify_list(suggestion_list)
        
        return(f_str.format(district_name, conjunctified_str))
    
    
    
    def create_label_line_file(self):
        with open(self.label_line_file_path, 'w') as f:
            print('', file=f)
        for district_name, row_series in self.one_country_df.sort_index(axis='index', ascending=False).iterrows():
            id = '{}'.format('-'.join(district_name.lower().split(' ')))
            label = '{} Label Line'.format(district_name)
            d = row_series['label_line_d']
            if str(d) != 'nan':
                label_line_str = self.l_str.format(d, id, label)
                with open(self.label_line_file_path, 'a') as f:
                    print(label_line_str.encode(s.encoding_type, errors=s.encoding_error).decode(encoding=s.decoding_type,
                                                                                                 errors=s.decoding_error), file=f)
    
    
    
    # Do some ft-idf calculations
    def scrape_suggestion_list_dictionary(self, refresh=True):
        
        # Retrieve the page with tag results and set it up to be scraped
        driver = u.get_driver()
        site_url = 'https://www.google.com'
        u.driver_get_url(driver, url_str=site_url, verbose=True)
        
        input_css = '.gLFyf'
        dropdown_css = '#tsf > div:nth-child(2) > div > div > div > ul'
        if refresh:
            suggestion_list_dict = {}
        else:
            suggestion_list_dict = self.suggestion_list_dict.copy()
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
                        if (dropdown is not None) and (dropdown != ''):
                            dropdown_list.append(dropdown.strip())
                    suggestion_list_dict[district] = dropdown_list

                except Exception as e:
                    message = str(e).strip()
                    print('Wait for {} dropdown to show up: {}'.format(district, message))
        driver.quit()
        
        return suggestion_list_dict
    
    
    
    def clean_up_district_unique_dict(self):
        sorted_d, reverse_sorted_d = self.get_tfidf_lists()
        self.district_unique_dict = s.load_object('district_unique_dict')
        while len(self.district_unique_dict.keys()) < len(self.suggestion_list_dict):
            for (key_word, idf) in reverse_sorted_d:
                if len(self.district_unique_dict.keys()) == len(self.suggestion_list_dict):
                    break
                for district, dropdown_list in self.suggestion_list_dict.items():
                    if len(self.district_unique_dict.keys()) == len(self.suggestion_list_dict):
                        break
                    if district not in self.district_unique_dict.keys():
                        for ngram in dropdown_list:
                            if key_word in ngram:
                                self.district_unique_dict[district] = ngram
                                break
        s.store_objects(district_unique_dict=self.district_unique_dict)
    
    
    
    def clean_up_district_common_dict(self):
        sorted_d, reverse_sorted_d = self.get_tfidf_lists()
        self.district_common_dict = s.load_object('district_common_dict')
        while len(self.district_common_dict.keys()) < len(self.suggestion_list_dict):
            for (key_word, idf) in sorted_d:
                if len(self.district_common_dict.keys()) == len(self.suggestion_list_dict):
                    break
                for district, dropdown_list in self.suggestion_list_dict.items():
                    if len(self.district_common_dict.keys()) == len(self.suggestion_list_dict):
                        break
                    if district not in self.district_common_dict.keys():
                        for ngram in dropdown_list:
                            if key_word in ngram:
                                self.district_common_dict[district] = ngram
                                break
        s.store_objects(district_common_dict=self.district_common_dict)
    
    
    
    def create_district_first_dict(self):
        district_first_dict = {}
        for district, dropdown_list in self.suggestion_list_dict.items():
            district_first_dict[district] = dropdown_list[0]
        s.store_objects(district_first_dict=district_first_dict)
        
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
            s.store_objects(suggestion_list_dict=self.suggestion_list_dict)
        for old_key in self.suggestion_list_dict.keys():
            new_key = re.sub(r'\xa0', r'', old_key)
            self.suggestion_list_dict[new_key] = self.suggestion_list_dict.pop(old_key)
    
    
    
    def show_colorbar(self, column_name, cmap='viridis'):
        '''
        column_name = 'Total_Gun_Murder_Deaths_2010'
        cb1 = show_colorbar(column_name)
        print(['cb1.ax.{}'.format(fn) for fn in dir(cb1.ax) if 'get_y' in fn.lower()])
        '''
        fig, ax = plt.subplots(figsize=(1, 6))
        fig.subplots_adjust(left=0.5)
        
        min = self.one_country_df[column_name].min()
        max = self.one_country_df[column_name].max()
        cmap = mpl.cm.get_cmap(cmap)
        norm = mpl.colors.Normalize(vmin=min, vmax=max)
        
        cb1 = mpl.colorbar.ColorbarBase(ax, cmap=cmap,
                                        norm=norm,
                                        orientation='vertical')
        cb1.set_label(self.get_column_description(column_name))
        file_path = os.path.join(self.svg_dir, 'colorbar.svg')
        plt.savefig(file_path)
        self.trim_d_path(file_path)
        
        return cb1
    
    
    
    def clean_up_district_merge_dataframe(self):
        for column_name in self.one_country_df.columns:
            try:
                self.one_country_df[column_name] = pd.to_numeric(self.one_country_df[column_name], errors='raise', downcast='float')
            except Exception as e:
                print('The {} column get this error: {}'.format(column_name, str(e).strip()))
        s.store_objects(one_country_df=self.one_country_df)