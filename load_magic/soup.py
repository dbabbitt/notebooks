
#!/usr/bin/env python
# Utility Functions to scrape web pages using bs4.
# Dave Babbitt <dave.babbitt@gmail.com>
# Author: Dave Babbitt, Data Scientist
# coding: utf-8
"""
A set of utility functions specific to web scraping using BeautifulSoup
"""
from bs4 import BeautifulSoup as bs
from pathlib import Path
from urllib.request import urlretrieve
import os
import random
import re
import urllib

url_regex = re.compile(r'\b(https?|file)://[-A-Z0-9+&@#/%?=~_|$!:,.;]*[A-Z0-9+&@#/%=~_|$]', re.IGNORECASE)


def get_page_soup(page_url_or_filepath):
    match_obj = url_regex.search(page_url_or_filepath)
    if match_obj:
        with urllib.request.urlopen(page_url_or_filepath) as response:
            page_html = response.read()
    else:
        with open(page_url_or_filepath, 'r', encoding='utf-8') as f:
            page_html = f.read()
    page_soup = bs(page_html, 'html.parser')
    
    return page_soup