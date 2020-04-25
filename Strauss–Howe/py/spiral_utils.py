
#!/usr/bin/env python
# Utility Functions to initialize Strauss-Howe shapes.
# Dave Babbitt <dave.babbitt@gmail.com>
# Author: Dave Babbitt, Data Scientist
# coding: utf-8
"""
isc: A set of utility functions common to spiral audio web scraping
"""
from PIL import Image, ImageDraw, ImageFont
from cycler import cycler
from datetime import date, datetime, timedelta
from io import BytesIO
from itertools import combinations
from math import cos, sin, pi, sqrt, atan
from matplotlib.pyplot import imshow
from pathlib import Path
import imageio
import logging
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import pandas as pd
np = pd.np
import os
import random
import re
import requests
import storage as s
import webcolors
import warnings
warnings.filterwarnings('ignore')

class StraussHoweUtilities(object):
    """This class implements the core of the utility functions
    needed to create patriline spirals.
    
    Examples
    --------
    
    >>> import spiral_utils
    >>> u = spiral_utils.StraussHoweUtilities()
    """
    
    def __init__(self):
        self.s = s.Storage()
        
        # Get datasets
        self.archetypes_df = self.s.load_object('archetypes_df')
        self.dresses_file_dict = self.s.load_object('dresses_file_dict')
        self.eras_df = self.s.load_object('eras_df')
        self.generations_df = self.s.load_object('generations_df')
        self.history_radius_dict = self.s.load_object('history_radius_dict')
        self.history_year_dict = self.s.load_object('history_year_dict')
        self.patriline_df = self.s.load_object('patriline_df')
        self.saecula_df = self.s.load_object('saecula_df')
        self.saeculum_cmap_dict = self.s.load_object('saeculum_cmap_dict')
        self.turnings_df = self.s.load_object('turnings_df')
        self.turning_numbers_df = self.s.load_object('turning_numbers_df')
        self.us_presidents_df = self.s.load_object('us_presidents_df')
        self.min_year = self.patriline_df['year_of_birth'].min()
        
        # Create movie folders
        self.jpg_dir = os.path.join(self.s.saves_folder, 'jpg')
        self.png_folder = os.path.join(self.s.saves_folder, 'png')
        self.movie_folder = os.path.join(self.s.saves_folder, 'movies')
        os.makedirs(name=self.movie_folder, exist_ok=True)
        self.bare_movie_folder = os.path.join(self.movie_folder, 'bare')
        os.makedirs(name=self.bare_movie_folder, exist_ok=True)
        self.diagonal_movie_folder = os.path.join(self.movie_folder, 'diagonal')
        os.makedirs(name=self.diagonal_movie_folder, exist_ok=True)
        self.saeculum_dir = os.path.join(self.s.data_folder, 'saeculum')
        os.makedirs(name=self.saeculum_dir, exist_ok=True)
        self.saeculum_movie_folder = os.path.join(self.movie_folder, 'saeculum')
        os.makedirs(name=self.saeculum_movie_folder, exist_ok=True)
        self.saeculum_fashionable_movie_folder = os.path.join(self.movie_folder, 'saeculum_fashionable')
        os.makedirs(name=self.saeculum_fashionable_movie_folder, exist_ok=True)
        
        # Color values
        self.full_corner_list = ['white', 'black', 'red', 'green', 'blue',
                                 'magenta', 'yellow', 'cyan']
        self.white_tuple = (255, 255, 255, 0)
        self.black_tuple = (0, 0, 0, 255)
        
        # Diagonal diagram values
        self.cycles_image = Image.open(fp=os.path.join(self.s.data_folder, 'png',
                                                       'cycle_rectangles_boxes.png'),
                                       mode='r')
        self.babbitt_years_tuple = (1435, 2029)
        self.babbitt_min_year = min(self.patriline_df.year_of_birth.min(),
                                    self.patriline_df.year_of_death.min())
        self.zoom_image = self.get_zoom_in(self.cycles_image, self.babbitt_min_year)
        self.babbitt_random_year = random.randrange(self.babbitt_years_tuple[0],
                                                    self.babbitt_years_tuple[1]+1)
        self.now_year = datetime.now().year
    
    def show_generation_blurb(self, generation_name):
        if str(generation_name) != 'nan':
            print('{}'.format(generation_name))
            mask_series = (self.generations_df.index == generation_name[:-1])
            turnings_archetype_list = self.generations_df[mask_series]['turnings_archetype'].tolist()
            if not len(turnings_archetype_list):
                mask_series = (self.generations_df.index == generation_name)
                turnings_archetype_list = self.generations_df[mask_series]['turnings_archetype'].tolist()
            if len(turnings_archetype_list):
                turnings_archetype = turnings_archetype_list[0].lower()
                print('({})'.format(turnings_archetype))
            generations_archetype_list = self.generations_df[mask_series]['generations_archetype'].tolist()
            if len(generations_archetype_list):
                generations_archetype = generations_archetype_list[0].lower()
                print('{}'.format(generations_archetype))
    
    def print_turnings(self):
        for turning_name, row_series in self.turnings_df.iterrows():
            turning_begin_year = row_series['turning_begin_year']
            turning_end_year = row_series['turning_end_year']
            turning_notes = row_series['turning_notes']
            entering_elderhood = row_series['entering_elderhood']
            entering_midlife = row_series['entering_midlife']
            entering_young_adulthood = row_series['entering_young_adulthood']
            entering_childhood = row_series['entering_childhood']
            print()
            print('{}-{}'.format(turning_begin_year, turning_end_year))
            print('{}'.format('\n'.join(turning_notes.split('. '))))
            print('-------------------------')
            self.show_generation_blurb(entering_elderhood)
            print('-------------------------')
            self.show_generation_blurb(entering_midlife)
            print('-------------------------')
            self.show_generation_blurb(entering_young_adulthood)
            print('-------------------------')
            self.show_generation_blurb(entering_childhood)
            print('-------------------------')
    
    def add_guide(self, zoom_image):
        file_path = os.path.join(self.diagonal_movie_folder, 'guide.png')
        guide_image = Image.open(fp=file_path, mode='r')
        guide_size_tuple = guide_image.size
        zoom_size_tuple = zoom_image.size
        guide_x = 4
        guide_y = int((zoom_size_tuple[1]-guide_size_tuple[1])/2) + 1
        zoom_x = 4 + guide_size_tuple[0] + 4
        zoom_y = 0
        frame_width = zoom_x + zoom_size_tuple[0]
        frame_height = zoom_size_tuple[1]
        frame_image = Image.new(mode=zoom_image.mode,
                                size=(frame_width, frame_height),
                                color=(255, 255, 255, 255))
        frame_image.paste(im=zoom_image, box=(zoom_x, zoom_y),
                          mask=zoom_image)
        frame_image.paste(im=guide_image, box=(guide_x, guide_y),
                          mask=guide_image)
        
        return frame_image
    
    def get_image_array(self, stop_year, png_suffix, movie_folder):
        zoom_image = self.get_zoom_in(self.cycles_image, stop_year)
        # png_name = 'plot_{}{}.png'.format(stop_year, png_suffix)
        # png_path = os.path.join(movie_folder, png_name)
        # zoom_image.save(png_path)
        # image_array = imageio.imread(png_path)
        image_io = BytesIO()
        zoom_image.save(fp=image_io, format='png')
        image_array = imageio.imread(image_io.getvalue(), format='png')
        
        return image_array
        
    def make_a_movie(self, min_year, stop_year, movie_folder,
                     png_suffix='', movie_name=None):
        images_list = []
        for stopped_year in range(min_year, stop_year):
            image_array = self.get_image_array(stopped_year, png_suffix, movie_folder)
            for i in range(2):
                images_list.append(image_array)
        image_array = self.get_image_array(stop_year, png_suffix, movie_folder)
        for i in range(100):
            images_list.append(image_array)
        if movie_name is None:
            movie_name = '_'.join(png_suffix.split('_')[1:] + ['movie']) + '.gif'
        gif_path = os.path.join(movie_folder, movie_name)
        imageio.mimsave(uri=gif_path, ims=images_list, format='gif')
        
        return os.path.abspath(gif_path)
    
    def label_life_line(self, img, label_text, xy_tuple, rgb_tuple):
        font_obj = ImageFont.truetype(r'C:\Windows\Fonts\Arial.ttf', size=12)
        width, height = font_obj.getsize(label_text)
        
        text_img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(text_img)
        draw.text((0, 0), text=label_text, font=font_obj, fill=rgb_tuple)
        
        text_img = text_img.rotate(41, expand=1)
        
        sx, sy = text_img.size
        px = int(xy_tuple[0] + (xy_tuple[2]-xy_tuple[0])/2 - sx/2)
        py = int(xy_tuple[1] + (xy_tuple[3]-xy_tuple[1])/2 - sy/2)
        img.paste(text_img, (px, py, px + sx, py + sy), text_img)
    
    def convert_years_to_x(self, year, y_tuple=(0, 2220), years_tuple=(1435, 2029)):
        a = (y_tuple[1]-y_tuple[0])/(years_tuple[1]-years_tuple[0])
        b = y_tuple[0] - (years_tuple[0]*a)
        x = a*year + b
        
        return x
    
    def draw_life_line(self, center_year, year_of_death, img=None, year_of_birth=1961,
                       age_of_birth=0, rgb_tuple=(0, 255, 0)):
        if img is None:
            img = self.get_zoom_in(self.cycles_image, center_year)
        draw = ImageDraw.Draw(img)
        right_year = center_year + 80
        y_tuple = (0, img.size[0])
        if year_of_birth < center_year - 80:
            left_year = center_year - 80
        else:
            left_year = year_of_birth
        years_tuple = (center_year - 80, right_year)
        xy_tuple = (self.convert_years_to_x(left_year, y_tuple=y_tuple, years_tuple=years_tuple),
                    self.convert_age_to_y(age_of_birth),
                    self.convert_years_to_x(year_of_death, y_tuple=y_tuple, years_tuple=years_tuple),
                    self.convert_age_to_y(year_of_death-year_of_birth))
        #print('xy_tuple: {}'.format(xy_tuple))
        draw.line(xy=xy_tuple, fill=rgb_tuple, width=12)
        
        return xy_tuple
    
    def get_zoom_in(self, img, center_year):
        size_tuple = img.size
        y_tuple = (0, size_tuple[0])
        left_year = center_year - 80
        right_year = center_year + 80
        left = self.convert_years_to_x(left_year, y_tuple=y_tuple)
        upper = 0
        right = self.convert_years_to_x(right_year, y_tuple=y_tuple)
        lower = size_tuple[1]
        
        # (Upper left x coordinate, upper left y coordinate, lower right x coordinate, lower right y coordinate)
        crop_tuple = (left, upper, right, lower)
        img = img.crop(box=crop_tuple)
        
        birth_match_series = (self.patriline_df.year_of_birth >= left_year) & (self.patriline_df.year_of_birth <= center_year)
        death_match_series = (self.patriline_df.year_of_death >= left_year) & (self.patriline_df.year_of_death <= right_year)
        mask_series = birth_match_series | death_match_series
        for patriarch_name, row_series in self.patriline_df[mask_series].iterrows():
            year_of_birth = row_series.year_of_birth
            year_of_death = row_series.year_of_death
            if (str(year_of_death) == 'nan') or (year_of_death > center_year):
                year_of_death = center_year
            age_of_birth = 0
            if year_of_birth < left_year:
                age_of_birth = left_year - year_of_birth
            css4_color = row_series.css4_color
            rgb_obj = webcolors.name_to_rgb(css4_color, spec='css3')
            rgb_tuple = (rgb_obj.red, rgb_obj.green, rgb_obj.blue, 255)
            xy_tuple = self.draw_life_line(center_year=center_year, year_of_death=year_of_death,
                                      img=img, year_of_birth=year_of_birth, age_of_birth=age_of_birth,
                                      rgb_tuple=rgb_tuple)
            #print(xy_tuple)
            css4_text_color = row_series.css4_text_color
            rgb_obj = webcolors.name_to_rgb(css4_text_color, spec='css3')
            rgb_tuple = (rgb_obj.red, rgb_obj.green, rgb_obj.blue, 255)
            if patriarch_name.strip() == 'Stephen Elkanah Babbitt':
                patriarch_name = 'Baby Boy Babbitt'
            self.label_life_line(img=img, label_text=patriarch_name, xy_tuple=xy_tuple, rgb_tuple=rgb_tuple)
        size_tuple = img.size
        frame_img = Image.new(mode=img.mode, size=(size_tuple[0]+8, size_tuple[1]+8), color=(255, 255, 255, 255))
        #frame_img.paste(img, (4, 4, 4 + size_tuple[0], 4 + size_tuple[1]), img)
        frame_img.paste(im=img, box=(4, 4), mask=img)
        frame_img = self.add_guide(frame_img)
        
        return frame_img
    
    def convert_age_to_y(self, age, size_tuple=(333, 133), age_tuple=(20, 80)):
        a = (size_tuple[0] - size_tuple[1])/(age_tuple[0] - age_tuple[1])
        b = size_tuple[0] - (age_tuple[0]*a)
        y = a*age + b
        
        return y
    
    def draw_hl(self, draw, y, image_width):
        draw.line(xy=(0, y, image_width, y), fill=(255, 0, 0), width=1, joint=None)
    
    def add_fashion_image(self, year):
        
        # Get old image data
        old_path = os.path.join(self.png_folder, 'plot_{}.png'.format(year))
        foreground = Image.open(old_path)
        foreground = foreground.convert('RGBA')
        old_data_list = foreground.getdata()
        
        # Get new image data
        new_data_list = []
        for old_tuple in old_data_list:
            if (old_tuple[0] == 255) and (old_tuple[1] == 255) and (old_tuple[2] == 255):
                new_data_list.append(self.white_tuple)
            else:
                new_data_list.append(old_tuple)
        
        # Replace old with new
        foreground.putdata(new_data_list)
        
        # Get dresses image
        dresses_file = self.dresses_file_dict[year]
        if dresses_file is None:
            file_path = os.path.join(self.png_folder, 'plot_{}_fashionable.png'.format(year))
            foreground.save(file_path, 'PNG')
        else:
            file_path = os.path.join(self.png_folder, dresses_file)
            dresses_img = Image.open(file_path)
            dresses_img = dresses_img.convert('RGBA')
            
            dresses_img.paste(foreground, (0, 0), foreground)
            
            file_path = os.path.join(self.png_folder, 'plot_{}_fashionable.png'.format(year))
            dresses_img.save(file_path, 'PNG')
    
    def add_fashion_saeculum_image(self, year):
        
        # Get old image data
        old_path = os.path.join(self.bare_movie_folder, 'plot_{}.png'.format(year))
        foreground = Image.open(old_path)
        foreground = foreground.convert('RGBA')
        foreground = self.make_transparent(foreground, threshold=6)
        
        # Get dresses image
        dresses_file = self.dresses_file_dict[year]
        if dresses_file is None:
            dresses_img = foreground
        else:
            file_path = os.path.join(self.png_folder, dresses_file)
            dresses_img = Image.open(file_path)
            dresses_img = dresses_img.convert('RGBA')
            dresses_img = self.make_transparent(dresses_img, threshold=5)
            dresses_img.paste(foreground, (0, 0), foreground)
        
        # Get saeculum image
        mask_series = (self.turnings_df['turning_begin_year'] <= year) & (self.turnings_df['turning_end_year'] >= year)
        saeculum_list = self.turnings_df[mask_series].index.tolist()
        if len(saeculum_list):
            saeculum_name = saeculum_list[0]
            saeculum_file = '{}.png'.format(saeculum_name)
            saeculum_path = Path(os.path.join(self.saeculum_dir, saeculum_file))
            if saeculum_path.is_file():
                saeculum_img = Image.open(saeculum_path, mode='r')
                saeculum_img = saeculum_img.convert('RGBA')
                saeculum_img.paste(dresses_img, (0, 0), dresses_img)
            else:
                saeculum_img = dresses_img
            file_path = os.path.join(self.saeculum_fashionable_movie_folder, 'plot_{}_saeculum_fashionable.png'.format(year))
            saeculum_img.save(file_path, 'PNG')
    
    def add_saeculum_image(self, year):
        
        # Get old image data
        old_path = os.path.join(self.bare_movie_folder, 'plot_{}.png'.format(year))
        foreground = Image.open(old_path)
        foreground = foreground.convert('RGBA')
        old_data_list = foreground.getdata()
        
        # Get new image data
        new_data_list = []
        for old_tuple in old_data_list:
            if (old_tuple[0] == 255) and (old_tuple[1] == 255) and (old_tuple[2] == 255):
                new_data_list.append(self.white_tuple)
            else:
                new_data_list.append(old_tuple)
        
        # Replace old with new
        foreground.putdata(new_data_list)
        
        # Get saeculum image
        mask_series = (self.turnings_df['turning_begin_year'] <= year) & (self.turnings_df['turning_end_year'] >= year)
        saeculum_list = self.turnings_df[mask_series].index.tolist()
        if len(saeculum_list):
            saeculum_name = saeculum_list[0]
            saeculum_file = '{}.png'.format(saeculum_name)
            saeculum_path = Path(os.path.join(self.saeculum_dir, saeculum_file))
            new_path = os.path.join(self.saeculum_movie_folder, 'plot_{}_saeculum.png'.format(year))
            if saeculum_path.is_file():
                saeculum_img = Image.open(saeculum_path, mode='r')
                saeculum_img = saeculum_img.convert('RGBA')
                saeculum_img.paste(foreground, (0, 0), foreground)
                saeculum_img.save(new_path, 'PNG')
            else:
                foreground.save(new_path, 'PNG')
    
    def polar_to_cartesian(self, r, theta):
        radians = theta*(pi/180)
        
        return int(r*cos(radians)), int(r*sin(radians))
    
    def add_spiral_labels(self, years_list, history_year_dict, i=0):
        i = i % 4
        for year in years_list:
            radius, theta = history_year_dict[year]
            radius += 25*i
            radius -= 25/2
            x, y = self.polar_to_cartesian(radius, theta)
            text_obj = plt.text(x, y, year, fontsize=10, color='gray',
                                rotation=theta-90, rotation_mode='anchor')
    
    def archimedes_spiral(self, theta, theta_offset=0.0):
        """
        Return Archimedes spiral
        
        Args:
            theta: array-like, angles from polar coordinates to be converted
            theta_offset: float, angle offset in radians (2*pi = 0)
        """
        
        (x, y) = (theta * np.cos(theta + theta_offset), theta
                  * np.sin(theta + theta_offset))
        x_norm = np.max(np.abs(x))
        y_norm = np.max(np.abs(y))
        (x, y) = (x / x_norm, y / y_norm)
        
        return (x, y)
    
    def bernoulli_spiral(self, theta, theta_offset=0.0, *args, **kwargs):
        """
        Return Equiangular (Bernoulli's) spiral
        
        Args:
        theta: array-like, angles from polar coordinates to be converted
        theta_offset: float, angle offset in radians (2*pi = 0)
        
        Kwargs:
        exp_scale: growth rate of the exponential
        """
        
        exp_scale = kwargs.pop('exp_scale', 0.1)
        
        (x, y) = (np.exp(exp_scale * theta) * np.cos(theta + theta_offset),
                  np.exp(exp_scale * theta) * np.sin(theta + theta_offset))
        x_norm = np.max(np.abs(x))
        y_norm = np.max(np.abs(y))
        (x, y) = (x / x_norm, y / y_norm)
        
        return (x, y)
    
    def colors_dict_to_dataframe(self, colors_dict):
        columns_list = ['Red', 'Green', 'Blue']
        rows_list = []
        index_list = []
        for base_name, color_tuple in colors_dict.items():
            row_dict = {}
            index_list.append(base_name)
            for i, color_value in enumerate(columns_list):
                row_dict[color_value] = color_tuple[i]
            rows_list.append(row_dict)
        df = pd.DataFrame(rows_list, columns=columns_list, index=index_list)
        
        return df
    
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
    
    def create_xy_list(self, history_radius_dict):
        xy_list = []
        for radius in sorted(history_radius_dict.keys()):
            year, theta = history_radius_dict[radius]
            cartesian_tuple = self.polar_to_cartesian(radius, theta)
            if len(xy_list):
                if (cartesian_tuple != xy_list[-1]):
                    xy_list.append(cartesian_tuple)
            else:
                xy_list.append(cartesian_tuple)
        
        return xy_list
    
    def display_test_colors(self, test_list, saeculum_title, face_title, nearness_str='far from',
                            color_dict=mcolors.XKCD_COLORS, color_title='XKCD', face_point='Face'):
        print(test_list)
        name_list = [name for distance, name in test_list]
        colors_dict = {name: color for name, color in color_dict.items() if name in name_list}
        title_str = '{} {} Colors, {} the {} {}'.format(color_title, saeculum_title, nearness_str,
                                                        face_title, face_point)
        self.plot_colortable(colors_dict=colors_dict, title=title_str, sort_colors=True, emptycols=0)
    
    def distance_between(self, new_tuple, old_tuple):
        green_diff = new_tuple[0] - old_tuple[0]
        blue_diff = new_tuple[1] - old_tuple[1]
        red_diff = new_tuple[2] - old_tuple[2]
        
        return sqrt(green_diff**2 + blue_diff**2 + red_diff**2)
    
    def distance_from_black(self, old_tuple):
        
        return sqrt(old_tuple[0]**2 + old_tuple[1]**2 + old_tuple[2]**2)
    
    def distance_from_blue(self, old_tuple):
        blue_diff = 1.0 - old_tuple[1]
        
        return sqrt(old_tuple[0]**2 + blue_diff**2 + old_tuple[2]**2)
    
    def distance_from_cyan(self, old_tuple):
        green_diff = 1.0 - old_tuple[0]
        blue_diff = 1.0 - old_tuple[1]
        
        return sqrt(green_diff**2 + blue_diff**2 + old_tuple[2]**2)
    
    def distance_from_green(self, old_tuple):
        green_diff = 1.0 - old_tuple[0]
        
        return sqrt(green_diff**2 + old_tuple[1]**2 + old_tuple[2]**2)
    
    def distance_from_kbcg_face(self, old_tuple):
        green_diff = 0.5 - old_tuple[0]
        blue_diff = 0.5 - old_tuple[1]
        
        return sqrt(green_diff**2 + blue_diff**2 + old_tuple[2]**2)
    
    def distance_from_krmb_face(self, old_tuple):
        blue_diff = 0.5 - old_tuple[1]
        red_diff = 0.5 - old_tuple[2]
        
        return sqrt(old_tuple[0]**2 + blue_diff**2 + red_diff**2)
    
    def distance_from_kryg_face(self, old_tuple):
        green_diff = 0.5 - old_tuple[0]
        red_diff = 0.5 - old_tuple[2]
        
        return sqrt(green_diff**2 + old_tuple[1]**2 + red_diff**2)
    
    def distance_from_magenta(self, old_tuple):
        blue_diff = 1.0 - old_tuple[1]
        red_diff = 1.0 - old_tuple[2]
        
        return sqrt(old_tuple[0]**2 + blue_diff**2 + red_diff**2)
    
    def distance_from_red(self, old_tuple):
        red_diff = 1.0 - old_tuple[2]
        
        return sqrt(old_tuple[0]**2 + old_tuple[1]**2 + red_diff**2)
    
    def distance_from_wcbm_face(self, old_tuple):
        green_diff = 0.5 - old_tuple[0]
        blue_diff = 1.0 - old_tuple[1]
        red_diff = 0.5 - old_tuple[2]
        
        return sqrt(green_diff**2 + blue_diff**2 + red_diff**2)
    
    def distance_from_wcgy_face(self, old_tuple):
        green_diff = 1.0 - old_tuple[0]
        blue_diff = 0.5 - old_tuple[1]
        red_diff = 0.5 - old_tuple[2]
        
        return sqrt(green_diff**2 + blue_diff**2 + red_diff**2)
    
    def distance_from_white(self, old_tuple):
        green_diff = 1.0 - old_tuple[0]
        blue_diff = 1.0 - old_tuple[1]
        red_diff = 1.0 - old_tuple[2]
        
        return sqrt(green_diff**2 + blue_diff**2 + red_diff**2)
    
    def distance_from_wyrm_face(self, old_tuple):
        green_diff = 0.5 - old_tuple[0]
        blue_diff = 0.5 - old_tuple[1]
        red_diff = 1.0 - old_tuple[2]
        
        return sqrt(green_diff**2 + blue_diff**2 + red_diff**2)
    
    def distance_from_yellow(self, old_tuple):
        green_diff = 1.0 - old_tuple[0]
        red_diff = 1.0 - old_tuple[2]
        
        return sqrt(green_diff**2 + old_tuple[1]**2 + red_diff**2)
    
    def translate_upper_left_to_center(self, point, screen_size):
        """
        Takes a point and converts it to the appropriate coordinate system.
        Note that PIL uses upper left as 0, we want the center.
        Args:
            point (real, real): A point in space.
            screen_size (int): Size of an N x N screen.
        Returns:
            (real, real): Translated point for Pillow coordinate system.
        """
        
        return point[0] + screen_size / 2, point[1] + screen_size / 2
    
    def draw_spiral(self, a, b, img, step=0.1, loops=10):
        """
        Draw the Archimedean spiral defined by:
        r = a + b*theta
        Args:
            a (real): First parameter
            b (real): Second parameter
            img (Image): Image to write spiral to.
            step (real): How much theta should increment by. (default: 0.1)
            loops (int): How many times theta should loop around. (default: 10)
        """
        draw = ImageDraw.Draw(img)
        theta = 0.0
        r = a
        prev_pos = self.polar_to_cartesian(r, theta)
        while theta < 2 * loops * pi:
            theta += step / r
            r = a + b*theta
            # Draw pixels, but remember to convert to Cartesian:
            pos = self.polar_to_cartesian(r, theta)
            draw.line(self.translate_upper_left_to_center(prev_pos, img.size[0]) +
                      self.translate_upper_left_to_center(pos, img.size[0]), fill=1)
            prev_pos = pos
    
    def exists(self, path):
        r = requests.head(path)
        
        return r.status_code == requests.codes.ok
    
    def fermat_spiral(self, theta, theta_offset=0.0):
        """
        Return Parabolic (Fermat's) spiral
        
        Args:
            theta: array-like, angles from polar coordinates to be converted
            theta_offset: float, angle offset in radians (2*pi = 0)
        """
        
        (x, y) = (np.sqrt(theta) * np.cos(theta + theta_offset),
                  np.sqrt(theta) * np.sin(theta + theta_offset))
        x_norm = np.max(np.abs(x))
        y_norm = np.max(np.abs(y))
        (x, y) = (x / x_norm, y / y_norm)
        
        return (x, y)
    
    def get_distance_dataframe(self, colors_df, color_title='XKCD'):
        rows_list = []
        columns_list = ['color_title', 'distance_from_white', 'distance_from_black',
                        'distance_from_red', 'distance_from_green', 'distance_from_blue',
                        'distance_from_magenta', 'distance_from_yellow', 'distance_from_cyan',
                        'distance_from_kryg_face', 'distance_from_krmb_face', 'distance_from_kbcg_face',
                        'distance_from_wcgy_face', 'distance_from_wcbm_face', 'distance_from_wyrm_face']
        index_list = []
        for row_index, row_series in colors_df.iterrows():
            green_value = row_series['Green']
            blue_value = row_series['Blue']
            red_value = row_series['Red']
            row_tuple = (green_value, blue_value, red_value)
            row_dict = {}
            row_dict['color_title'] = color_title
            row_dict['distance_from_white'] = self.distance_from_white(row_tuple)
            row_dict['distance_from_black'] = self.distance_from_black(row_tuple)
            row_dict['distance_from_red'] = self.distance_from_red(row_tuple)
            row_dict['distance_from_green'] = self.distance_from_green(row_tuple)
            row_dict['distance_from_blue'] = self.distance_from_blue(row_tuple)
            row_dict['distance_from_magenta'] = self.distance_from_magenta(row_tuple)
            row_dict['distance_from_yellow'] = self.distance_from_yellow(row_tuple)
            row_dict['distance_from_cyan'] = self.distance_from_cyan(row_tuple)
            row_dict['distance_from_kryg_face'] = self.distance_from_kryg_face(row_tuple)
            row_dict['distance_from_krmb_face'] = self.distance_from_krmb_face(row_tuple)
            row_dict['distance_from_kbcg_face'] = self.distance_from_kbcg_face(row_tuple)
            row_dict['distance_from_wcgy_face'] = self.distance_from_wcgy_face(row_tuple)
            row_dict['distance_from_wcbm_face'] = self.distance_from_wcbm_face(row_tuple)
            row_dict['distance_from_wyrm_face'] = self.distance_from_wyrm_face(row_tuple)
            rows_list.append(row_dict)
            index_list.append(row_index)
        distance_df = pd.DataFrame(rows_list, columns=columns_list, index=index_list)
        
        return distance_df
    
    def get_face_dictionary(self, distance_df):
        face_dictionary = {}
        for row_index, row_series in distance_df.iterrows():
            tuple_list = sorted(row_series.to_dict().items(), key=lambda x: x[1])
            if tuple_list[0][1] == 0.0:
                face_dictionary[row_index] = tuple_list[0][0].split('_')[2]
            else:
                corners_list = tuple_list[:3]
                face_set = set([corners_list[0][0].split('_')[2],
                                corners_list[1][0].split('_')[2],
                                corners_list[2][0].split('_')[2]])
                if face_set in kryg_face_set_list:
                    face_dictionary[row_index] = 'black-red-yellow-green'
                elif face_set in krmb_face_set_list:
                    face_dictionary[row_index] = 'black-red-magenta-blue'
                elif face_set in kbcg_face_set_list:
                    face_dictionary[row_index] = 'black-blue-cyan-green'
                elif face_set in wcgy_face_set_list:
                    face_dictionary[row_index] = 'white-cyan-green-yellow'
                elif face_set in wcbm_face_set_list:
                    face_dictionary[row_index] = 'white-cyan-blue-magenta'
                elif face_set in wyrm_face_set_list:
                    face_dictionary[row_index] = 'white-yellow-red-magenta'
                else:
                    face_dictionary[row_index] = '-'.join(list(face_set))
        
        return face_dictionary
    
    def get_face_set_list(self, combinations_list):
        combs_obj = combinations(combinations_list, 3)
        face_set_list = []
        for color_tuple in combs_obj:
            face_set_list.append(set(color_tuple))
        
        return face_set_list
    
    def get_hsv_dict(self, colors_dict):
        """
        Hue, Saturation, Value
        """
        
        return {name: tuple(mcolors.rgb_to_hsv(mcolors.to_rgb(color))) for name,
                color in colors_dict.items()}
    
    def get_one_arc(self, start_year, stop_year, history_year_dict, i=0):
        xy_list = []
        i = i % 4
        start_radius = history_year_dict[start_year][0]
        start_radius += 25*i
        stop_radius = history_year_dict[stop_year][0]
        stop_radius += 25*i
        increment_count = int(2*pi*start_radius)
        radius_array = np.linspace(start=start_radius, stop=stop_radius,
                                   num=increment_count)
        start_theta = history_year_dict[start_year][1]
        stop_theta = history_year_dict[stop_year][1]
        theta_array = np.linspace(start=start_theta, stop=stop_theta,
                                  num=increment_count)
        for radius, theta in zip(radius_array, theta_array):
            cartesian_tuple = self.polar_to_cartesian(radius, theta)
            if len(xy_list):
                if (cartesian_tuple != xy_list[-1]):
                    xy_list.append(cartesian_tuple)
            else:
                xy_list.append(cartesian_tuple)
        
        return xy_list
    
    def get_one_stopped_arc(self, start_year, stop_year, stopped_year,
                            history_year_dict, i=0):
        xy_list = []
        i = i % 4
        if stop_year > stopped_year:
            stop_year = stopped_year
        start_radius = history_year_dict[start_year][0]
        start_radius += 25*i
        stop_radius = history_year_dict[stop_year][0]
        stop_radius += 25*i
        increment_count = int(2*pi*start_radius)
        radius_array = np.linspace(start=start_radius, stop=stop_radius,
                                   num=increment_count)
        start_theta = history_year_dict[start_year][1]
        stop_theta = history_year_dict[stop_year][1]
        theta_array = np.linspace(start=start_theta, stop=stop_theta,
                                  num=increment_count)
        for radius, theta in zip(radius_array, theta_array):
            cartesian_tuple = self.polar_to_cartesian(radius, theta)
            if len(xy_list):
                if (cartesian_tuple != xy_list[-1]):
                    xy_list.append(cartesian_tuple)
            else:
                xy_list.append(cartesian_tuple)
        
        return xy_list
    
    def get_page_tables(self, tables_url):
        tables_df_list = pd.read_html(tables_url)
        print(sorted([(i, df.shape) for (i, df) in enumerate(tables_df_list)],
                     key=lambda x: x[1][0], reverse=True))
        
        return tables_df_list
    
    def get_row_label(self, present_year, patriarch_name, row_series):
        patriarch_age = present_year - int(row_series['year_of_birth'])
        year_of_death = row_series['year_of_death']
        generation_name = row_series['generation_name']
        try:
            year_of_death = int(year_of_death)
        except:
            year_of_death = present_year + 1
        age_str = ''
        if (year_of_death > present_year):
            if patriarch_age > 80:
                age_str = ' in Late Elderhood'
            elif patriarch_age > 60:
                age_str = ' in Elderhood'
            elif patriarch_age > 40:
                age_str = ' in Midlife'
            elif patriarch_age > 20:
                age_str = ' as a Young Adult'
            else:
                age_str = ' in Childhood'
        label_str = '{} ({} Generation{})'.format(patriarch_name, generation_name, age_str)
        
        return label_str
    
    def get_shortest_distance(self, row_series):
        for column_name in ['xkcd_color', 'css4_color']:
            new_column_name = '{}_text_color'.format(column_name.split('_')[0])
            color = mcolors.to_rgb(row_series[column_name])
            white_distance = self.distance_from_white(color)
            black_distance = self.distance_from_black(color)
            if min(white_distance, black_distance) == white_distance:
                row_series[new_column_name] = 'black'
            else:
                row_series[new_column_name] = 'white'
        
        return row_series
    
    def label_arc(self, start_year, stopped_year,
                  history_theta_dict, arc_label, history_year_dict, ideal_distance=13,
                  i=0, label_color='black'):
        i = i % 4
        starting_year = int(((start_year + stopped_year) / 2) - (len(arc_label) / 2))
        starting_radius, starting_theta = history_year_dict[starting_year]
        next_radius, next_theta = history_year_dict[starting_year+1]
        
        # Tan(A) = Opposite/Adjacent
        radians = atan(ideal_distance/starting_radius)
        theta_sign = np.sign(next_theta-starting_theta)
        
        # Increment the theta so that it spaces the letters the same regardless of the radius
        theta_increment = theta_sign*(radians*180/pi)
        
        # Figure out if you have to flip the characters upside-down and place them backwards
        if (starting_theta%360) < 200:
            #logging.info('')
            #logging.info('Right-side up thetas:')
            theta = starting_theta
            radius = starting_radius + 25*i
            radius -= 25/2
            for c in arc_label[::int(-theta_sign)]:
                #logging.info('c: "{}", radius: "{}", theta: "{}"'.format(c, radius, theta % 360))
                x, y = self.polar_to_cartesian(radius, theta)
                text_obj = plt.text(x, y, c, fontsize=12, color=label_color,
                                    rotation=theta-90, rotation_mode='anchor')
                theta += theta_increment
                if int(theta) in history_theta_dict:
                    radius = history_theta_dict[int(theta)][1]
                    radius += 25*i
                    radius -= 25/2
        else:
            logging.info('')
            logging.info('Upside-down thetas:')
            theta = starting_theta + theta_increment*len(arc_label)
            if int(theta) in history_theta_dict:
                radius = history_theta_dict[int(theta)][1]
                radius += 25*i
            else:
                radius = starting_radius + 25*i
            radius += 25/2
            for c in arc_label[::int(-theta_sign)]:
                logging.info('c: "{}", radius: "{}", theta: "{}"'.format(c, radius, theta % 360))
                x, y = self.polar_to_cartesian(radius, theta)
                text_obj = plt.text(x, y, c, fontsize=12, color=label_color,
                                    rotation=theta+90, rotation_mode='anchor')
                theta -= theta_increment
                if int(theta) in history_theta_dict:
                    radius = history_theta_dict[int(theta)][1]
                    radius += 25*i
                    radius += 25/2
    
    def make_transparent(self, img, threshold=38):
        margin = 255/self.distance_from_white(self.black_tuple)
        old_data_list = img.getdata()
        
        # Get new image data
        new_data_list = []
        for old_tuple in old_data_list:
            transparency = int(margin * self.distance_from_white(old_tuple))
            if transparency > threshold:
                transparency = 255
            elif transparency < 0:
                transparency = 0
            old_tuple = (old_tuple[0], old_tuple[1], old_tuple[2], transparency)
            new_data_list.append(old_tuple)
        
        # Replace old with new
        img.putdata(new_data_list)
        
        return img
    
    def plot_colortable(self, colors_dict, title, sort_colors=True, emptycols=0):
        if len(colors_dict):
            cell_width = 212
            cell_height = 22
            swatch_width = 48
            margin = 12
            topmargin = 40
            
            # Sort colors_dict by hue, saturation, value and name.
            if sort_colors is True:
                by_hsv = sorted((tuple(mcolors.rgb_to_hsv(mcolors.to_rgb(color))),
                                 name)
                                for name, color in colors_dict.items())
                names = [name for hsv, name in by_hsv]
            else:
                names = list(colors_dict)
            
            n = len(names)
            ncols = 4 - emptycols
            nrows = n // ncols + int(n % ncols > 0)
            
            width = cell_width * 4 + 2 * margin
            height = cell_height * nrows + margin + topmargin
            dpi = 72
            
            fig, ax = plt.subplots(figsize=(width / dpi, height / dpi), dpi=dpi)
            fig.subplots_adjust(margin/width, margin/height,
                                (width-margin)/width, (height-topmargin)/height)
            ax.set_xlim(0, cell_width * 4)
            ax.set_ylim(cell_height * (nrows-0.5), -cell_height/2.)
            ax.yaxis.set_visible(False)
            ax.xaxis.set_visible(False)
            ax.set_axis_off()
            ax.set_title(title, fontsize=24, loc="left", pad=10)
            
            for i, name in enumerate(names):
                row = i % nrows
                col = i // nrows
                y = row * cell_height
                
                swatch_start_x = cell_width * col
                swatch_end_x = cell_width * col + swatch_width
                text_pos_x = cell_width * col + swatch_width + 7
                
                ax.text(text_pos_x, y, name, fontsize=14,
                        horizontalalignment='left',
                        verticalalignment='center')
                
                ax.hlines(y, swatch_start_x, swatch_end_x,
                          color=colors_dict[name], linewidth=18)
    
    def plot_patriarch(self, patriarch_name, history_year_dict):
        mask_series = (self.patriline_df.index == patriarch_name)
        start_year = int(self.patriline_df[mask_series]['Year of Birth'].tolist()[0])
        stop_year = self.patriline_df[mask_series]['Year of Death'].tolist()[0]
        try:
            stop_year = int(stop_year)
        except:
            stop_year = max(history_year_dict.keys())
        xy_list = self.get_one_arc(start_year=start_year, stop_year=stop_year,
                                   history_year_dict=history_year_dict, i=0)
        PathCollection_obj = plt.plot([x[0] for x in xy_list], [y[1] for y in xy_list], alpha=0.5)
        self.add_spiral_labels([start_year, stop_year], history_year_dict)
    
    def save_stopped_babbitt_plot(self, stopped_year, out_file_path, footer_str,
                                  history_year_dict):
        mask_series = (self.patriline_df['Year of Birth'] <= stopped_year)
        i = self.patriline_df[mask_series].shape[0]-1
        with open(out_file_path, 'w') as output:
            size = output.write(py_file_header_str)
            for patriarch_name, row_series in self.patriline_df[mask_series].iterrows():
                start_year = int(row_series['Year of Birth'])
                stop_year = row_series['Year of Death']
                try:
                    stop_year = int(stop_year)
                except:
                    stop_year = start_year + 80
                    if stop_year > max(history_year_dict.keys()):
                        stop_year = max(history_year_dict.keys())
                xy_list = self.get_one_stopped_arc(start_year=start_year, stop_year=stop_year,
                                                   stopped_year=stopped_year,
                                                   history_year_dict=history_year_dict, i=i)
                size = output.write("patriarch_coords_dict['{}'] = {}\n".format(patriarch_name,
                                                                                str([(x,y,1) for (x, y) in xy_list])))
                i -= 1
            size = output.write(footer_str)
    
    def show_babbitt_plot(self, history_theta_dict, history_year_dict):
        fig = plt.figure(figsize=(13, 13))
        ax = fig.add_subplot(111, autoscale_on=False)
        ax.set_xlim(-1000, 1000)
        ax.set_ylim(-1000, 1000)
        i = self.patriline_df.shape[0]-1
        d = 5
        previous_saeculum = self.patriline_df.head(1)['Saeculum Name'].tolist()[0]
        for patriarch_name, row_series in self.patriline_df.iterrows():
            start_year = int(row_series['Year of Birth'])
            stop_year = row_series['Year of Death']
            try:
                stop_year = int(stop_year)
            except:
                stop_year = start_year + 80
                if stop_year > max(history_year_dict.keys()):
                    stop_year = max(history_year_dict.keys())
            xy_list = self.get_one_arc(start_year=start_year, stop_year=stop_year,
                                       history_year_dict=history_year_dict, i=i)
            self.add_spiral_labels([start_year, stop_year], history_year_dict, i)
            self.label_arc(start_year=start_year, stopped_year=stop_year,
                           history_theta_dict=history_theta_dict, arc_label=patriarch_name,
                           history_year_dict=history_year_dict, ideal_distance=13, i=i,
                           label_color='black')
            saeculum = row_series['Saeculum Name']
            if saeculum != previous_saeculum:
                previous_saeculum = saeculum
                d = 5
            #print(patriarch_name, i, d, saeculum)
            cmap = self.saeculum_cmap_dict[saeculum]
            c = plt.get_cmap(cmap)(np.linspace(0, 1, 6))[d]
            PathCollection_obj = plt.plot([x[0] for x in xy_list], [y[1] for y in xy_list],
                                          alpha=0.75, label=patriarch_name, c=c)
            i -= 1
            d -= 1
        Legend_obj = ax.legend()
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
    
    def show_color_proximity(self, distance_df, color_dict=mcolors.XKCD_COLORS,
                             color_title='XKCD', color_str='Red', saeculum_title='Reformation',
                             nearness_str='close to'):
        distance_dict = {}
        for name, color in color_dict.items():
            mask_series = (distance_df.index == name)
            distance_list = distance_df[mask_series]['distance_from_{}'.format(color_str.lower())].tolist()
            if len(distance_list) == 1:
                distance_dict[name] = distance_list[0]
        color_tuple_list = sorted((distance, name) for name, distance in distance_dict.items())
        test_list = color_tuple_list[:32]
        self.display_test_colors(test_list=test_list, saeculum_title=saeculum_title,
                            face_title=color_str, nearness_str=nearness_str,
                            color_dict=color_dict, color_title=color_title,
                            face_point='Corner')
    
    def show_face_proximity(self, distance_df):
        for row_index, row_series in distance_df.iterrows():
            tuple_list = sorted(row_series.to_dict().items(), key=lambda x: x[1])
            if tuple_list[0][1] == 0.0:
                print('{} is in the {} corner'.format(row_index, tuple_list[0][0].split('_')[2]))
            else:
                corners_list = tuple_list[:3]
                face_set = set([corners_list[0][0].split('_')[2], corners_list[1][0].split('_')[2],
                                corners_list[2][0].split('_')[2]])
                if face_set in kryg_face_set_list:
                    print('{} is nearest the black-red-yellow-green face'.format(row_index))
                elif face_set in krmb_face_set_list:
                    print('{} is nearest the black-red-magenta-blue face'.format(row_index))
                elif face_set in kbcg_face_set_list:
                    print('{} is nearest the black-blue-cyan-green face'.format(row_index))
                elif face_set in wcgy_face_set_list:
                    print('{} is nearest the white-cyan-green-yellow face'.format(row_index))
                elif face_set in wcbm_face_set_list:
                    print('{} is nearest the white-cyan-blue-magenta face'.format(row_index))
                elif face_set in wyrm_face_set_list:
                    print('{} is nearest the white-yellow-red-magenta face'.format(row_index))
                else:
                    print('{} is nearest the {} face'.format(row_index, '-'.join(list(face_set))))
    
    def show_saeculum_image(self, saeculum_name):
        file_name = '{}.jpg'.format(saeculum_name)
        file_path = os.path.join(self.jpg_dir, file_name)
        jpg_image = Image.open(fp=file_path, mode='r')
        jpg_image = jpg_image.rotate(angle=180)
        width, height = jpg_image.size
        if (width > MAX_WIDTH) or (height > MAX_HEIGHT):
            if (width > MAX_WIDTH):
                multiple = MAX_WIDTH / width
                width *= multiple
                height *= multiple
            if (height > MAX_HEIGHT):
                multiple = MAX_HEIGHT / height
                width *= multiple
                height *= multiple
            jpg_image = jpg_image.resize(size=(int(width), int(height)), resample=0, box=None)
            width, height = jpg_image.size
        left = 0 - int(width/2)
        right = int(width/2)
        top = 0 - int(height/2)
        bottom = int(height/2)
        AxesImage_obj = imshow(X=np.asarray(jpg_image), origin='upper', extent=(left, right, bottom, top))
        
        return jpg_image
    
    def show_turning_image(self, year):
        mask_series = (self.turnings_df['turning_begin_year'] <= year) & (self.turnings_df['turning_end_year'] >= year)
        turning_name_list = self.turnings_df[mask_series].index.tolist()
        if len(turning_name_list):
            turning_name = turning_name_list[0]
            file_name = '{}.jpg'.format(turning_name)
            file_path = os.path.join(self.jpg_dir, file_name)
            jpg_image = Image.open(fp=file_path, mode='r')
            jpg_image = jpg_image.rotate(angle=180)
            width, height = jpg_image.size
            if (width > MAX_WIDTH) or (height > MAX_HEIGHT):
                if (width > MAX_WIDTH):
                    multiple = MAX_WIDTH / width
                    width *= multiple
                    height *= multiple
                if (height > MAX_HEIGHT):
                    multiple = MAX_HEIGHT / height
                    width *= multiple
                    height *= multiple
                jpg_image = jpg_image.resize(size=(int(width), int(height)), resample=0, box=None)
            width, height = jpg_image.size
        left = 0 - int(width/2)
        right = int(width/2)
        top = 0 - int(height/2)
        bottom = int(height/2)
        AxesImage_obj = imshow(X=np.asarray(jpg_image), origin='upper', extent=(left, right, bottom, top))
        
        return jpg_image
    
    def show_stopped_babbitt_plot(self, history_theta_dict, stopped_year, history_year_dict):
        
        # Turn interactive plotting off
        plt.ioff()
        
        # Create a new figure, plot into it, then close it so it never gets displayed
        fig = plt.figure(figsize=(13, 13))
        ax = fig.add_subplot(111, autoscale_on=False)
        ax.set_xlim(-1000, 1000)
        ax.set_ylim(-1000, 1000)
        mask_series = (self.patriline_df['year_of_birth'] <= stopped_year)
        i = self.patriline_df[mask_series].shape[0]-1
        d = 5
        previous_saeculum = self.patriline_df[mask_series].head(1)['saeculum_name'].tolist()[0]
        for patriarch_name, row_series in self.patriline_df[mask_series].iterrows():
            start_year = int(row_series['year_of_birth'])
            stop_year = row_series['year_of_death']
            try:
                stop_year = int(stop_year)
            except:
                stop_year = start_year + 80
                if stop_year > max(history_year_dict.keys()):
                    stop_year = max(history_year_dict.keys())
            xy_list = self.get_one_stopped_arc(start_year=start_year, stop_year=stop_year,
                                               stopped_year=stopped_year,
                                               history_year_dict=history_year_dict, i=i)
            years_list = [year for year in [start_year,
                                            stop_year] if year <= stopped_year]
            self.add_spiral_labels(years_list, history_year_dict, i)
            if stop_year > stopped_year:
                stop_year = stopped_year
            text_color = row_series['xkcd_text_color']
            self.label_arc(start_year=start_year, stopped_year=stop_year,
                           history_theta_dict=history_theta_dict, arc_label=patriarch_name,
                           history_year_dict=history_year_dict, ideal_distance=13, i=i,
                           label_color=text_color)
            saeculum = row_series['saeculum_name']
            if saeculum != previous_saeculum:
                previous_saeculum = saeculum
                d = 5
            #print(patriarch_name, i, d, saeculum)
            cmap = self.saeculum_cmap_dict[saeculum]
            #c = plt.get_cmap(cmap)(np.linspace(0, 1, 6))[d]
            c = row_series['xkcd_color']
            label_str = self.get_row_label(stopped_year, patriarch_name, row_series)
            PathCollection_obj = plt.plot([xy[0] for xy in xy_list],
                                          [xy[1] for xy in xy_list],
                                          alpha=0.75, label=label_str,
                                          c=c, linewidth=9)
            i -= 1
            d -= 1
        
        #self.show_turning_image(stopped_year)
        legend_obj = ax.legend(ncol=2, loc='upper left')
        frame_obj = legend_obj.get_frame()
        frame_obj.set_facecolor('whitesmoke')
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        
        # Close it so it never gets displayed
        file_name = 'plot_{}.png'.format(stopped_year)
        file_path = os.path.join(self.bare_movie_folder, file_name)
        plt.savefig(file_path, format='png')
        plt.close(fig)
    
    def show_year_image(self, year):
        file_name = '{}.jpg'.format(year)
        file_path = os.path.join(self.jpg_dir, file_name)
        jpg_image = Image.open(fp=file_path, mode='r')
        jpg_image = jpg_image.rotate(angle=180)
        width, height = jpg_image.size
        if (width > MAX_WIDTH) or (height > MAX_HEIGHT):
            if (width > MAX_WIDTH):
                multiple = MAX_WIDTH / width
                width *= multiple
                height *= multiple
            if (height > MAX_HEIGHT):
                multiple = MAX_HEIGHT / height
                width *= multiple
                height *= multiple
            jpg_image = jpg_image.resize(size=(int(width), int(height)), resample=0, box=None)
            width, height = jpg_image.size
        left = 0 - int(width/2)
        right = int(width/2)
        top = 0 - int(height/2)
        bottom = int(height/2)
        AxesImage_obj = imshow(X=np.asarray(jpg_image), origin='upper', extent=(left, right, bottom, top))
        
        return jpg_image
    
    def spirals(n_samples=100, noise=None, seed=None, mode='archimedes', n_loops=2, *args, **kwargs):
        """
        Create spirals
        
        Currently only binary classification is supported for spiral generation
        
        Args:
            n_samples: int, number of datapoints to generate
            noise: float or None, standard deviation of the Gaussian noise added
            seed: int or None, seed for the noise
            n_loops: int, number of spiral loops, doesn't play well with 'bernoulli'
            mode: str, how the spiral should be generated. Current implementations:
                'archimedes': a spiral with equal distances between branches
                'bernoulli': logarithmic spiral with branch distances increasing
                'fermat': a spiral with branch distances decreasing (sqrt)
        
        Returns:
            Shuffled features and labels for 'spirals' synthetic dataset of type
            `base.Dataset`
        
        Raises:
            ValueError: If the generation `mode` is not valid
        
        TODO:
            - Generation of unbalanced data
        """
        
        n_classes = 2  # I am not sure how to make it multiclass
        
        _modes = {'archimedes': self.archimedes_spiral,
                  'bernoulli': self.bernoulli_spiral,
                  'fermat': self.fermat_spiral}
        
        if mode is None or mode not in _modes:
            raise ValueError('Cannot generate spiral with mode %s' % mode)
        
        if seed is not None:
            np.random.seed(seed)
        linspace = np.linspace(0, 2 * n_loops * np.pi,
                               n_samples // n_classes)
        spir_x = np.empty(0, dtype=np.int32)
        spir_y = np.empty(0, dtype=np.int32)
        
        y = np.empty(0, dtype=np.int32)
        for label in range(n_classes):
            (base_cos, base_sin) = _modes[mode](linspace, label * np.pi,
                    *args, **kwargs)
            spir_x = np.append(spir_x, base_cos)
            spir_y = np.append(spir_y, base_sin)
            y = np.append(y, label * np.ones(n_samples // n_classes,
                          dtype=np.int32))
        
        # Add more points if n_samples is not divisible by n_classes (unbalanced!)
        extras = n_samples % n_classes
        if extras > 0:
            (x_extra, y_extra) = _modes[mode](np.random.rand(extras) * 2 * np.pi,
                                              *args, **kwargs)
            spir_x = np.append(spir_x, x_extra)
            spir_y = np.append(spir_y, y_extra)
            y = np.append(y, np.zeros(extras, dtype=np.int32))
        
        # Reshape the features/labels
        X = np.vstack((spir_x, spir_y)).T
        y = np.hstack(y)
        
        # Shuffle the data
        indices = np.random.permutation(range(n_samples))
        if noise is not None:
            X += np.random.normal(scale=noise, size=X.shape)
        
        return Dataset(data=X[indices], target=y[indices])