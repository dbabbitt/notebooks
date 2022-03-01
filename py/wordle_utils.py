
#!/usr/bin/env python
# Utility Functions to play Wordle (https://www.nytimes.com/games/wordle/index.html) and Quordle (https://www.quordle.com/#/)
# Dave Babbitt <dave.babbitt@gmail.com>
# Author: Dave Babbitt, Data Scientist
# coding: utf-8
"""
WordleUtilities: A set of utility functions common to playing Wordle and Quordle
"""
from IPython.display import HTML, display
from num2words import num2words
import collections
import pandas as pd
import storage as s
import webbrowser

import warnings
warnings.filterwarnings("ignore")

class WordleUtilities(object):
    """This class implements the core of the utility functions
    needed to play wordle.

    Examples
    --------

    >>> import sys
    >>> sys.path.insert(1, '../py')
    >>> import wordle_utils
    >>> w = wordle_utils.WordleUtilities()
    """

    def __init__(self):
        self.s = s.Storage()

        # Get words list
        if self.s.pickle_exists('wordle_words_list'):
            self.words_list = self.s.load_object('wordle_words_list')
        else:

            # Get words from the Wordle JavaScript
            import re

            self.words_list = []
            az_regex = re.compile('[^a-z]')
            file_path = r'D:\Documents\GitHub\notebooks\data\txt\wordle_words_short_list.txt'
            with open(file_path, encoding='utf8') as infile:
                for line in infile:
                    word_str = line.strip()
                    if (len(word_str) == 5) and not az_regex.search(word_str):
                        self.words_list.append(word_str)
            file_path = r'D:\Documents\GitHub\notebooks\data\txt\wordle_words_long_list.txt'
            with open(file_path, encoding='utf8') as infile:
                for line in infile:
                    word_str = line.strip()
                    if (len(word_str) == 5) and not az_regex.search(word_str):
                        self.words_list.append(word_str)
            self.words_list = list(set(self.words_list))
            if not self.words_list:
                import requests

                link = 'https://www.powerlanguage.co.uk/wordle/main.814b2d17.js'
                f = requests.get(link)
                commands_list = f.text.split(';')
                list_str = commands_list[331].split(']')[0].split('[')[1]
                self.words_list = eval(f'[{list_str}]')
            self.s.store_objects(wordle_words_list=self.words_list)

        # Get the response patterns
        if self.s.pickle_exists('wordle_response_patterns_df'):
            self.response_patterns_df = self.s.load_object('wordle_response_patterns_df')
        else:
            self.response_patterns_df = self.s.load_csv('response_patterns_df', folder_path=self.s.saves_folder)
            if not self.response_patterns_df.shape[0]:
                rows_list = []
                for test_word in self.words_list:
                    for target_word in self.words_list:
                        row_dict = {}
                        row_dict['test_word'] = test_word
                        row_dict['target_word'] = target_word
                        row_dict['response_pattern'] = self.measure_word(test_word, target_word)
                        rows_list.append(row_dict)
                self.response_patterns_df = pd.DataFrame(rows_list)
            self.s.store_objects(wordle_response_patterns_df=self.response_patterns_df)
            
        self.wordle_url = 'https://www.nytimes.com/games/wordle/index.html'
        self.quordle_url = 'https://www.quordle.com/#/'



    def surf_to_wordle_website(self):
        webbrowser.open(self.wordle_url, new=2)



    def surf_to_quordle_website(self):
        webbrowser.open(self.quordle_url, new=2)



    def conjunctify_nouns(self, noun_list):
        if len(noun_list) > 2:
            last_noun_str = noun_list[-1]
            but_last_nouns_str = ', '.join(noun_list[:-1])
            list_str = ', and '.join([but_last_nouns_str, last_noun_str])
        elif len(noun_list) == 2:
            list_str = ' and '.join(noun_list)
        elif len(noun_list) == 1:
            list_str = noun_list[0]
        else:
            list_str = ''

        return list_str



    def minimize_branches_to_solve_a_wordle(self, testwords_list=[], response_patterns_list=[], verbose=True):
        if (not testwords_list):
            if verbose:
                print(f'list of possible solutions: {len(self.words_list):,}')
            self.tree_first_guess = self.get_word_guess(self.response_patterns_df, self.words_list)
            if verbose:
                print(f'FIRST MOVE: {self.tree_first_guess}')
        
        if len(response_patterns_list) == 1:
            self.tree_first_candidates_list = self.get_candidates_list(testwords_list, response_patterns_list)
            if verbose:
                print(f'list of possible solutions ({len(self.tree_first_candidates_list):,}): {self.conjunctify_nouns(self.tree_first_candidates_list)}')
            self.tree_second_guess = self.get_word_guess(self.response_patterns_df, self.tree_first_candidates_list, guesses_list=testwords_list)
            if verbose:
                print(f'SECOND MOVE: {self.tree_second_guess}')
        
        if len(response_patterns_list) == 2:
            self.tree_second_candidates_list = self.get_candidates_list(testwords_list, response_patterns_list, self.tree_first_candidates_list)
            if verbose:
                print(f'list of possible solutions ({len(self.tree_second_candidates_list):,}): {self.conjunctify_nouns(self.tree_second_candidates_list)}')
            self.tree_third_guess = self.get_word_guess(self.response_patterns_df, self.tree_second_candidates_list, guesses_list=testwords_list)
            if verbose:
                print(f'THIRD MOVE: {self.tree_third_guess}')
        
        if len(response_patterns_list) == 3:
            self.tree_third_candidates_list = self.get_candidates_list(testwords_list, response_patterns_list, self.tree_second_candidates_list)
            if verbose:
                print(f'list of possible solutions ({len(self.tree_third_candidates_list):,}): {self.conjunctify_nouns(self.tree_third_candidates_list)}')
            self.tree_fourth_guess = self.get_word_guess(self.response_patterns_df, self.tree_third_candidates_list, guesses_list=testwords_list)
            if verbose:
                print(f'FOURTH MOVE: {self.tree_fourth_guess}')
        
        if len(response_patterns_list) == 4:
            self.tree_fourth_candidates_list = self.get_candidates_list(testwords_list, response_patterns_list, self.tree_third_candidates_list)
            if verbose:
                print(f'list of possible solutions ({len(self.tree_fourth_candidates_list):,}): {self.conjunctify_nouns(self.tree_fourth_candidates_list)}')
            self.tree_fifth_guess = self.get_word_guess(self.response_patterns_df, self.tree_fourth_candidates_list, guesses_list=testwords_list)
            if verbose:
                print(f'FIFTH MOVE: {self.tree_fifth_guess}')
        
        if len(response_patterns_list) == 5:
            self.tree_fifth_candidates_list = self.get_candidates_list(testwords_list, response_patterns_list, self.tree_fourth_candidates_list)
            if verbose:
                print(f'list of possible solutions: ({len(self.tree_fifth_candidates_list)}): {self.conjunctify_nouns(sorted(self.tree_fifth_candidates_list))}')
            self.tree_sixth_guess, max_score = self.get_best_word(self.tree_fifth_candidates_list)
            if verbose:
                print(f'SIXTH MOVE: {self.tree_sixth_guess}')
        
        if len(response_patterns_list) == 6:
            self.tree_sixth_candidates_list = self.get_candidates_list(testwords_list, response_patterns_list, self.tree_fifth_candidates_list)
            if verbose:
                print(f'list of possible solutions: ({len(self.tree_sixth_candidates_list)}): {self.conjunctify_nouns(sorted(self.tree_sixth_candidates_list))}')
            self.tree_seventh_guess, max_score = self.get_best_word(self.tree_sixth_candidates_list)
            if verbose:
                print(f'SEVENTH MOVE: {self.tree_seventh_guess}')
        
        if len(response_patterns_list) == 7:
            self.tree_seventh_candidates_list = self.get_candidates_list(testwords_list, response_patterns_list, self.tree_sixth_candidates_list)
            if verbose:
                print(f'list of possible solutions: ({len(self.tree_seventh_candidates_list)}): {self.conjunctify_nouns(sorted(self.tree_seventh_candidates_list))}')
            self.tree_eighth_guess, max_score = self.get_best_word(self.tree_seventh_candidates_list)
            if verbose:
                print(f'EIGHTH MOVE: {self.tree_eighth_guess}')



    def maximize_green_responses_to_solve_a_wordle(self, leaf_first_guess=None, leaf_first_response_pattern=None, leaf_second_guess=None, leaf_second_response_pattern=None,
                                                   leaf_third_guess=None, leaf_third_response_pattern=None, leaf_fourth_guess=None, leaf_fourth_response_pattern=None,
                                                   leaf_fifth_guess=None, leaf_fifth_response_pattern=None, leaf_sixth_guess=None, leaf_sixth_response_pattern=None,
                                                   leaf_seventh_guess=None, leaf_seventh_response_pattern=None, verbose=True):
        if leaf_first_guess is None:
            if verbose:
                print(f'list of possible solutions: ({len(self.words_list):,})')
            leaf_first_guess, max_score = self.get_best_word(self.words_list)
            if verbose:
                print(f'FIRST MOVE: {leaf_first_guess}')

        if leaf_first_response_pattern is not None:
            self.testwords_list = [leaf_first_guess]
            self.response_patterns_list = [leaf_first_response_pattern]
            yellows_list = self.get_yellows_list(self.testwords_list, self.response_patterns_list)
            greys_list = self.get_greys_list(self.testwords_list, self.response_patterns_list)
            self.leaf_first_candidates_list = []
            for word_str in self.words_list:
                if all(map(lambda x: x in word_str, yellows_list)):
                    if all(map(lambda x: x not in word_str, greys_list)):
                        if self.is_greened(word_str, self.testwords_list, self.response_patterns_list):
                            self.leaf_first_candidates_list.append(word_str)
            if verbose:
                print(f'list of possible solutions: ({len(self.leaf_first_candidates_list)}): {self.conjunctify_nouns(sorted(self.leaf_first_candidates_list))}')
            leaf_second_guess, max_score = self.get_best_word(self.leaf_first_candidates_list)
            if verbose:
                print(f'SECOND MOVE: {leaf_second_guess}')

        if leaf_second_response_pattern is not None:
            self.testwords_list = [leaf_first_guess, leaf_second_guess]
            self.response_patterns_list = [leaf_first_response_pattern, leaf_second_response_pattern]
            yellows_list = self.get_yellows_list(self.testwords_list, self.response_patterns_list)
            greys_list = self.get_greys_list(self.testwords_list, self.response_patterns_list)
            self.leaf_second_candidates_list = []
            for word_str in self.words_list:
                if all(map(lambda x: x in word_str, yellows_list)):
                    if all(map(lambda x: x not in word_str, greys_list)):
                        if self.is_greened(word_str, self.testwords_list, self.response_patterns_list):
                            self.leaf_second_candidates_list.append(word_str)
            if verbose:
                print(f'list of possible solutions: ({len(self.leaf_second_candidates_list)}): {self.conjunctify_nouns(sorted(self.leaf_second_candidates_list))}')
            leaf_third_guess, max_score = self.get_best_word(self.leaf_second_candidates_list)
            if verbose:
                print(f'THIRD MOVE: {leaf_third_guess}')

        if leaf_third_response_pattern is not None:
            self.testwords_list = [leaf_first_guess, leaf_second_guess, leaf_third_guess]
            self.response_patterns_list = [leaf_first_response_pattern, leaf_second_response_pattern, leaf_third_response_pattern]
            yellows_list = self.get_yellows_list(self.testwords_list, self.response_patterns_list)
            greys_list = self.get_greys_list(self.testwords_list, self.response_patterns_list)
            self.leaf_third_candidates_list = []
            for word_str in self.words_list:
                if all(map(lambda x: x in word_str, yellows_list)):
                    if all(map(lambda x: x not in word_str, greys_list)):
                        if self.is_greened(word_str, self.testwords_list, self.response_patterns_list):
                            self.leaf_third_candidates_list.append(word_str)
            if verbose:
                print(f'list of possible solutions: ({len(self.leaf_third_candidates_list)}): {self.conjunctify_nouns(sorted(self.leaf_third_candidates_list))}')
            leaf_fourth_guess, max_score = self.get_best_word(self.leaf_third_candidates_list)
            if verbose:
                print(f'FOURTH MOVE: {leaf_fourth_guess}')

        if leaf_fourth_response_pattern is not None:
            self.testwords_list = [leaf_first_guess, leaf_second_guess, leaf_third_guess, leaf_fourth_guess]
            self.response_patterns_list = [leaf_first_response_pattern, leaf_second_response_pattern, leaf_third_response_pattern, leaf_fourth_response_pattern]
            yellows_list = self.get_yellows_list(self.testwords_list, self.response_patterns_list)
            greys_list = self.get_greys_list(self.testwords_list, self.response_patterns_list)
            self.leaf_fourth_candidates_list = []
            for word_str in self.words_list:
                if all(map(lambda x: x in word_str, yellows_list)):
                    if all(map(lambda x: x not in word_str, greys_list)):
                        if self.is_greened(word_str, self.testwords_list, self.response_patterns_list):
                            self.leaf_fourth_candidates_list.append(word_str)
            if verbose:
                print(f'list of possible solutions: ({len(self.leaf_fourth_candidates_list)}): {self.conjunctify_nouns(sorted(self.leaf_fourth_candidates_list))}')
            leaf_fifth_guess, max_score = self.get_best_word(self.leaf_fourth_candidates_list)
            if verbose:
                print(f'FIFTH MOVE: {leaf_fifth_guess}')

        if leaf_fifth_response_pattern is not None:
            self.testwords_list = [leaf_first_guess, leaf_second_guess, leaf_third_guess, leaf_fourth_guess, leaf_fifth_guess]
            self.response_patterns_list = [leaf_first_response_pattern, leaf_second_response_pattern, leaf_third_response_pattern, leaf_fourth_response_pattern,
                                      leaf_fifth_response_pattern]
            yellows_list = self.get_yellows_list(self.testwords_list, self.response_patterns_list)
            greys_list = self.get_greys_list(self.testwords_list, self.response_patterns_list)
            self.leaf_fifth_candidates_list = []
            for word_str in self.words_list:
                if all(map(lambda x: x in word_str, yellows_list)):
                    if all(map(lambda x: x not in word_str, greys_list)):
                        if self.is_greened(word_str, self.testwords_list, self.response_patterns_list):
                            self.leaf_fifth_candidates_list.append(word_str)
            if verbose:
                print(f'list of possible solutions: ({len(self.leaf_fifth_candidates_list)}): {self.conjunctify_nouns(sorted(self.leaf_fifth_candidates_list))}')
            leaf_sixth_guess, max_score = self.get_best_word(self.leaf_fifth_candidates_list)
            if verbose:
                print(f'SIXTH MOVE: {leaf_sixth_guess}')

        if leaf_sixth_response_pattern is not None:
            self.testwords_list = [leaf_first_guess, leaf_second_guess, leaf_third_guess, leaf_fourth_guess, leaf_fifth_guess, leaf_sixth_guess]
            self.response_patterns_list = [leaf_first_response_pattern, leaf_second_response_pattern, leaf_third_response_pattern, leaf_fourth_response_pattern,
                                      leaf_fifth_response_pattern, leaf_sixth_response_pattern]
            yellows_list = self.get_yellows_list(self.testwords_list, self.response_patterns_list)
            greys_list = self.get_greys_list(self.testwords_list, self.response_patterns_list)
            self.leaf_sixth_candidates_list = []
            for word_str in self.words_list:
                if all(map(lambda x: x in word_str, yellows_list)):
                    if all(map(lambda x: x not in word_str, greys_list)):
                        if self.is_greened(word_str, self.testwords_list, self.response_patterns_list):
                            self.leaf_sixth_candidates_list.append(word_str)
            if verbose:
                print(f'list of possible solutions: ({len(self.leaf_sixth_candidates_list)}): {self.conjunctify_nouns(sorted(self.leaf_sixth_candidates_list))}')
            leaf_seventh_guess, max_score = self.get_best_word(self.leaf_sixth_candidates_list)
            if verbose:
                print(f'SEVENTH MOVE: {leaf_seventh_guess}')

        if leaf_seventh_response_pattern is not None:
            self.testwords_list = [leaf_first_guess, leaf_second_guess, leaf_third_guess, leaf_fourth_guess, leaf_fifth_guess, leaf_sixth_guess, leaf_seventh_guess]
            self.response_patterns_list = [leaf_first_response_pattern, leaf_second_response_pattern, leaf_third_response_pattern, leaf_fourth_response_pattern,
                                      leaf_fifth_response_pattern, leaf_sixth_response_pattern, leaf_seventh_response_pattern]
            yellows_list = self.get_yellows_list(self.testwords_list, self.response_patterns_list)
            greys_list = self.get_greys_list(self.testwords_list, self.response_patterns_list)
            self.leaf_seventh_candidates_list = []
            for word_str in self.words_list:
                if all(map(lambda x: x in word_str, yellows_list)):
                    if all(map(lambda x: x not in word_str, greys_list)):
                        if self.is_greened(word_str, self.testwords_list, self.response_patterns_list):
                            self.leaf_seventh_candidates_list.append(word_str)
            if verbose:
                print(f'list of possible solutions: ({len(self.leaf_seventh_candidates_list)}): {self.conjunctify_nouns(sorted(self.leaf_seventh_candidates_list))}')
            leaf_eighth_guess, max_score = self.get_best_word(self.leaf_seventh_candidates_list)
            if verbose:
                print(f'EIGHTH MOVE: {leaf_eighth_guess}')

        if leaf_eighth_response_pattern is not None:
            self.testwords_list = [leaf_first_guess, leaf_second_guess, leaf_third_guess, leaf_fourth_guess, leaf_fifth_guess, leaf_sixth_guess, leaf_seventh_guess, leaf_eighth_guess]
            self.response_patterns_list = [leaf_first_response_pattern, leaf_second_response_pattern, leaf_third_response_pattern, leaf_fourth_response_pattern,
                                      leaf_fifth_response_pattern, leaf_sixth_response_pattern, leaf_seventh_response_pattern, leaf_eighth_response_pattern]
            yellows_list = self.get_yellows_list(self.testwords_list, self.response_patterns_list)
            greys_list = self.get_greys_list(self.testwords_list, self.response_patterns_list)
            self.leaf_eighth_candidates_list = []
            for word_str in self.words_list:
                if all(map(lambda x: x in word_str, yellows_list)):
                    if all(map(lambda x: x not in word_str, greys_list)):
                        if self.is_greened(word_str, self.testwords_list, self.response_patterns_list):
                            self.leaf_eighth_candidates_list.append(word_str)
            if verbose:
                print(f'list of possible solutions: ({len(self.leaf_eighth_candidates_list)}): {self.conjunctify_nouns(sorted(self.leaf_eighth_candidates_list))}')
            leaf_ninth_guess, max_score = self.get_best_word(self.leaf_eighth_candidates_list)
            if verbose:
                print(f'NINTH MOVE: {leaf_ninth_guess}')



    def display_the_difference(self):

        return (f'''<table>
            <tr>
                <th rowspan="2">Move</th>
                <th colspan="2" style="text-align:center">Green Maximizer</th>
                <th colspan="2" style="text-align:center">Branch Minimizer</th>
            </tr>
            <tr>
                <th style="text-align:center">Solutions</th>
                <th style="text-align:center">Guess</th>
                <th style="text-align:center">Solutions</th>
                <th style="text-align:center">Guess</th>
            </tr>
            {self.get_tr(1, leaf_count=len(self.words_list), tree_count=len(self.words_list))}
            {self.get_tr(2)}
            {self.get_tr(3)}
            {self.get_tr(4)}
            {self.get_tr(5)}
            {self.get_tr(6)}
        </table>''')



    def get_proportion_score(self, word_str, letter_proportions_df):
        word_score = 0
        for row_index, row_series in letter_proportions_df.iterrows():
            letter = row_series.letter_char
            if letter in word_str:
                proportion = row_series.proportion
                word_score += proportion

        return word_score



    def get_best_word(self, candidates_list):

        # Get proportions from candidate list
        import collections

        letters_list = []
        for word_str in candidates_list:
            letters_list += list(word_str)
        counter = collections.Counter(letters_list)
        letter_proportions_df = pd.DataFrame([{'letter_char': x, 'letter_count': y} for x, y in dict(counter).items()])
        min_count = letter_proportions_df.letter_count.min()
        letter_proportions_df['proportion'] = letter_proportions_df.letter_count.map(lambda x: x/min_count)

        # Minimize words to pick through after you get the next word colors back

        # Calculate maximum proportionality
        max_score = 0
        max_word = ''
        for word_str in candidates_list:
            word_score = self.get_proportion_score(word_str, letter_proportions_df)
            if word_score > max_score:
                max_score = word_score
                max_word = word_str

        return max_word, max_score



    def measure_word(self, test_word, target_word):
        colors_list = []
        for i in range(5):
            if test_word[i] == target_word[i]:
                colors_list.append('G')
            elif test_word[i] in target_word:
                colors_list.append('Y')
            else:
                colors_list.append('x')

        return ''.join(colors_list)



    def get_word_guess(self, response_patterns_df, candidates_list, guesses_list=[]):
        if len(candidates_list) == 1:

            return candidates_list[0]
        mask_series = response_patterns_df.target_word.isin(candidates_list) & ~response_patterns_df.test_word.isin(guesses_list)
        columns_list = ['test_word', 'response_pattern']
        guess_df = response_patterns_df[mask_series].groupby(columns_list).count()
        guess_df = guess_df.reset_index().groupby('test_word').max().sort_values(by='target_word').head(20)

        # Get proportions from candidate list
        if guess_df.shape[0] > 1:
            letters_list = []
            for word_str in guess_df.index:
                letters_list += list(word_str)
            counter = collections.Counter(letters_list)
            letter_proportions_df = pd.DataFrame([{'letter_char': x, 'letter_count': y} for x, y in dict(counter).items()])
            min_count = letter_proportions_df.letter_count.min()
            letter_proportions_df['proportion'] = letter_proportions_df.letter_count.map(lambda x: x/min_count)

            guess_df['word_score'] = guess_df.index.map(lambda x: self.get_proportion_score(x, letter_proportions_df))
            max_word_score = guess_df.word_score.max()
            mask_series = (guess_df.word_score == max_word_score)
            guess_df = guess_df[mask_series]

        guesses_list = guess_df.sort_values(by='target_word', ascending=False).index.tolist()
        guess = None
        if guesses_list:
            guess = guesses_list[0]

        return guess



    def get_greens_set(self, testwords_list, response_patterns_list):
        greens_set = set()
        for test_word, response_pattern in zip(testwords_list, response_patterns_list):
            for i in range(5):
                if response_pattern[i] == 'G':
                    greens_set.add(test_word[i])

        return greens_set



    def get_yellows_set(self, testwords_list, response_patterns_list):
        yellows_set = set()
        for test_word, response_pattern in zip(testwords_list, response_patterns_list):
            for i in range(5):
                if response_pattern[i] == 'Y':
                    yellows_set.add(test_word[i])

        return yellows_set



    def get_greys_list(self, testwords_list, response_patterns_list):
        greens_set = self.get_greens_set(testwords_list, response_patterns_list)    
        yellows_set = self.get_yellows_set(testwords_list, response_patterns_list)
        greys_set = set()
        for test_word, response_pattern in zip(testwords_list, response_patterns_list):
            for i in range(5):
                if (response_pattern[i] == 'x') and (test_word[i] not in greens_set) and (test_word[i] not in yellows_set):
                    greys_set.add(test_word[i])
        greys_list = sorted(greys_set)

        return greys_list



    def get_yellows_list(self, testwords_list, response_patterns_list):
        yellows_set = set()
        for test_word, response_pattern in zip(testwords_list, response_patterns_list):
            for i in range(5):
                if (response_pattern[i] == 'Y'):
                    yellows_set.add(test_word[i])
        yellows_list = sorted(yellows_set)

        return yellows_list



    def is_greened(self, word_str, testwords_list, response_patterns_list):
        transposed_tests_list = list(map(list, zip(*testwords_list)))
        transposed_responses_list = list(map(list, zip(*response_patterns_list)))
        is_greened = True
        for i in range(5):
            test_chars_list = transposed_tests_list[i]
            response_chars_list = transposed_responses_list[i]
            if 'G' in response_chars_list:
                idx = response_chars_list.index('G')
                is_greened = is_greened and (word_str[i] == test_chars_list[idx])
            else:
                is_greened = is_greened and (word_str[i] not in test_chars_list)

        return is_greened



    def get_candidates_list(self, testwords_list, response_patterns_list, previous_candidates_list=[]):
        mask_series = False
        for test_word, response_pattern in zip(testwords_list, response_patterns_list):
            mask_series = mask_series | ((self.response_patterns_df.test_word == test_word) & (self.response_patterns_df.response_pattern == response_pattern))
        candidates_df = self.response_patterns_df[mask_series].groupby('target_word').count()
        mask_series = (candidates_df.response_pattern == len(response_patterns_list))
        candidates_list = sorted(set(candidates_df[mask_series].index.tolist()))
        if previous_candidates_list and not candidates_list:
            greys_list = self.get_greys_list(testwords_list, response_patterns_list)
            yellows_list = self.get_yellows_list(testwords_list, response_patterns_list)
            for word_str in previous_candidates_list:
                if all(map(lambda x: x in word_str, yellows_list)):
                    if all(map(lambda x: x not in word_str, greys_list)):
                        if self.is_greened(word_str, testwords_list, response_patterns_list):
                            candidates_list.append(word_str)

        return candidates_list



    def patternize_guess(self, word_str, pattern_str):
        pre_str = '<span style="font-family:Courier;font-size:3em;text-transform:uppercase;font-variant-numeric:tabular-nums lining-nums;background-color:'
        in_str = ';">'
        post_str = '</span>'
        patternized_str = ''
        for letter_str, letter_pattern in zip(word_str, pattern_str):
            patternized_str += pre_str
            if letter_pattern == 'G':
                patternized_str += 'green'
            elif letter_pattern == 'Y':
                patternized_str += 'yellow'
            else:
                patternized_str += 'grey'
            patternized_str += in_str + letter_str + post_str

        return patternized_str



    def get_tr(self, ordinal, leaf_count=None, tree_count=None):
        ordinal_str = num2words(ordinal, lang='en', to='ordinal')
        previous_ordinal_str = num2words(ordinal-1, lang='en', to='ordinal')
        if leaf_count is None:
            leaf_count = eval(f'len(leaf_{previous_ordinal_str}_candidates_list)')
        leaf_guess = eval(f'leaf_{ordinal_str}_guess')
        leaf_pattern = eval(f'leaf_{ordinal_str}_response_pattern')
        if tree_count is None:
            tree_count = eval(f'len(tree_{previous_ordinal_str}_candidates_list)')
        tree_guess = eval(f'tree_{ordinal_str}_guess')
        tree_pattern = eval(f'tree_{ordinal_str}_response_pattern')
        html_str = f'''<tr>
            <td>{ordinal_str.title()}</td>
            <td>{leaf_count:,}</td>
            <td>{self.patternize_guess(leaf_guess, leaf_pattern)}</td>
            <td>{tree_count:,}</td>
            <td>{self.patternize_guess(tree_guess, tree_pattern)}</td>
        </tr>'''

        return html_str