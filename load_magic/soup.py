
#!/usr/bin/env python
# Utility Functions to scrape web pages using bs4.
# Use it something like this:
#
# %run ../load_magic/soup.py
#
# Dave Babbitt <dave.babbitt@gmail.com>
# Author: Dave Babbitt, Data Scientist
# coding: utf-8

# Soli Deo gloria

"""
A set of utility functions specific to web scraping using BeautifulSoup
"""
from bs4 import BeautifulSoup as bs
from pathlib import Path
from urllib.request import urlretrieve
import io
import os
import pandas as pd
import random
import re
import urllib
import numpy as np

URL_REGEX = re.compile(r'\b(https?|file)://[-A-Z0-9+&@#/%?=~_|$!:,.;]*[A-Z0-9+&@#/%=~_|$]', re.IGNORECASE)
FILEPATH_REGEX = re.compile(r'\b[c-d]:\\(?:[^\\/:*?"<>|\x00-\x1F]{0,254}[^.\\/:*?"<>|\x00-\x1F]\\)*(?:[^\\/:*?"<>|\x00-\x1F]{0,254}[^.\\/:*?"<>|\x00-\x1F])', re.IGNORECASE)

def get_page_soup(page_url_or_filepath, verbose=True):
    match_obj = URL_REGEX.search(page_url_or_filepath)
    if match_obj:
        with urllib.request.urlopen(page_url_or_filepath) as response:
            page_html = response.read()
    else:
        with open(page_url_or_filepath, 'r', encoding='utf-8') as f:
            page_html = f.read()
    page_soup = bs(page_html, 'html.parser')
    
    return page_soup

def get_wiki_tables(tables_url_or_filepath, verbose=True):
    table_dfs_list = []
    try:
        table_dfs_list = get_page_tables(tables_url_or_filepath, verbose=verbose)
    except ValueError as e:
        if verbose:
            print(str(e).strip())
        page_soup = get_page_soup(tables_url_or_filepath, verbose=verbose)
        table_soups_list = page_soup.find_all('table', attrs={'class': 'wikitable'})
        table_dfs_list = []
        for table_soup in table_soups_list:
            table_dfs_list += get_page_tables(str(table_soup))
    
    return table_dfs_list

def get_page_tables(tables_url_or_filepath, verbose=True):
    '''
    %run ../../load_magic/dataframes.py
    tables_url = 'https://en.wikipedia.org/wiki/Provinces_of_Afghanistan'
    page_tables_list = get_page_tables(tables_url)
    '''
    if URL_REGEX.fullmatch(tables_url_or_filepath) or FILEPATH_REGEX.fullmatch(tables_url_or_filepath):
        tables_df_list = pd.read_html(tables_url_or_filepath)
    else:
        f = io.StringIO(tables_url_or_filepath)
        tables_df_list = pd.read_html(f)
    if verbose:
        print(sorted([(i, df.shape) for (i, df) in enumerate(tables_df_list)],
                     key=lambda x: x[1][0]*x[1][1], reverse=True))
    
    return tables_df_list