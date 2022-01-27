#!/usr/bin/env python
# coding: utf-8

# From Anaconda Prompt (anaconda3), type:
# D:
# cd D:\Documents\GitHub\notebooks\py
# cls
# python Wordle.py


import storage as s
import csv
from pathlib import Path
import re

s = s.Storage()



print('Getting words from the Wordle JavaScript')
if s.pickle_exists('wordle_words_list'):
	words_list = s.load_object('wordle_words_list')
else:
	words_list = []
	az_regex = re.compile('[^a-z]')
	file_path = r'D:\Documents\GitHub\notebooks\data\txt\wordle_words_short_list.txt'
	with open(file_path, encoding='utf8') as infile:
		for line in infile:
			word_str = line.strip()
			if (len(word_str) == 5) and not az_regex.search(word_str):
				words_list.append(word_str)
	file_path = r'D:\Documents\GitHub\notebooks\data\txt\wordle_words_long_list.txt'
	with open(file_path, encoding='utf8') as infile:
		for line in infile:
			word_str = line.strip()
			if (len(word_str) == 5) and not az_regex.search(word_str):
				words_list.append(word_str)
	words_list = list(set(words_list))
	s.store_objects(wordle_words_list=words_list)


# 
# ----
# # Create a Dataset of All Responses



def measure_word(test_word, target_word):
	colors_list = []
	for i in range(5):
		if test_word[i] == target_word[i]:
			colors_list.append('G')
		elif test_word[i] in target_word:
			colors_list.append('Y')
		else:
			colors_list.append('x')
	
	return ''.join(colors_list)

file_path = '../saves/csv/response_patterns_df.csv'
Path(file_path).touch()
with open(file_path, 'w') as f:
	writer = csv.writer(f, delimiter=',', lineterminator='\n')
	writer.writerow(['test_word', 'target_word', 'response_pattern'])
	for test_word in words_list:
		for target_word in words_list:
			word_measure = measure_word(test_word, target_word)
			print(test_word, target_word, word_measure)
			writer.writerow([test_word, target_word, word_measure])