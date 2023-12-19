
#!/usr/bin/env python
# Utility Functions to run Jupyter notebooks.
# Dave Babbitt <dave.babbitt@gmail.com>
# Author: Dave Babbitt, Data Scientist
# coding: utf-8

# Soli Deo gloria

from datetime import timedelta
from os import listdir as listdir, makedirs as makedirs, path as osp
from pandas import DataFrame, Series, concat, read_csv, read_html
from typing import List, Optional
import humanize
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import re
import subprocess
import sys
import urllib
try: import dill as pickle
except:
    try: import pickle5 as pickle
    except: import pickle

import warnings
warnings.filterwarnings('ignore')

class NotebookUtilities(object):
    """
    This class implements the core of the utility
    functions needed to install and run GPTs and 
    also what is common to running Jupyter notebooks.
    
    Example:
        import sys
        import os.path as osp
        sys.path.insert(1, osp.abspath('../py'))
        from notebook_utils import NotebookUtilities
        
        nu = NotebookUtilities(
            data_folder_path=osp.abspath('../data'),
            saves_folder_path=osp.abspath('../saves')
        )
    """
    
    def __init__(self, data_folder_path=None, saves_folder_path=None, verbose=False):
        self.verbose = verbose
        self.pip_command_str = f'{sys.executable} -m pip'
        # self.update_modules_list(verbose=verbose)
        
        # Assume this is instantiated in a subfolder one below the main
        self.github_folder = osp.dirname(osp.abspath(osp.curdir))
        
        # Create the data folder if it doesn't exist
        if data_folder_path is None:
            self.data_folder = '../data'
        else:
            self.data_folder = data_folder_path
        makedirs(self.data_folder, exist_ok=True)
        if verbose: print('data_folder: {}'.format(osp.abspath(self.data_folder)), flush=True)
        
        # Create the saves folder if it doesn't exist
        if saves_folder_path is None:
            self.saves_folder = '../saves'
        else:
            self.saves_folder = saves_folder_path
        makedirs(self.saves_folder, exist_ok=True)
        if verbose: print('saves_folder: {}'.format(osp.abspath(self.saves_folder)), flush=True)
        
        # Create the assumed directories
        self.data_csv_folder = osp.join(self.data_folder, 'csv'); makedirs(name=self.data_csv_folder, exist_ok=True)
        self.saves_csv_folder = osp.join(self.saves_folder, 'csv'); makedirs(name=self.saves_csv_folder, exist_ok=True)
        self.saves_mp3_folder = osp.join(self.saves_folder, 'mp3'); makedirs(name=self.saves_mp3_folder, exist_ok=True)
        self.saves_pickle_folder = osp.join(self.saves_folder, 'pkl'); makedirs(name=self.saves_pickle_folder, exist_ok=True)
        self.saves_text_folder = osp.join(self.saves_folder, 'txt'); makedirs(name=self.saves_text_folder, exist_ok=True)
        self.saves_wav_folder = osp.join(self.saves_folder, 'wav'); makedirs(name=self.saves_wav_folder, exist_ok=True)
        self.txt_folder = osp.join(self.data_folder, 'txt'); makedirs(self.txt_folder, exist_ok=True)
        
        # Create the model directories
        self.bin_folder = osp.join(self.data_folder, 'bin'); makedirs(self.bin_folder, exist_ok=True)
        self.cache_folder = osp.join(self.data_folder, 'cache'); makedirs(self.cache_folder, exist_ok=True)
        self.data_models_folder = osp.join(self.data_folder, 'models'); makedirs(name=self.data_models_folder, exist_ok=True)
        self.db_folder = osp.join(self.data_folder, 'db'); makedirs(self.db_folder, exist_ok=True)
        self.graphs_folder = osp.join(self.saves_folder, 'graphs'); makedirs(self.graphs_folder, exist_ok=True)
        self.indices_folder = osp.join(self.saves_folder, 'indices'); makedirs(self.indices_folder, exist_ok=True)
        
        # Ensure the Scripts folder is in PATH
        self.anaconda_folder = osp.dirname(sys.executable)
        self.scripts_folder = osp.join(self.anaconda_folder, 'Scripts')
        if self.scripts_folder not in sys.path:
            sys.path.insert(1, self.scripts_folder)

        # Handy list of the different types of encodings
        self.encoding_type = ['latin1', 'iso8859-1', 'utf-8'][2]
        
        # Determine URL from file path
        self.url_regex = re.compile(r'\b(https?|file)://[-A-Z0-9+&@#/%?=~_|$!:,.;]*[A-Z0-9+&@#/%=~_|$]', re.IGNORECASE)
        self.filepath_regex = re.compile(
            r'\b[c-d]:\\(?:[^\\/:*?"<>|\x00-\x1F]{0,254}[^.\\/:*?"<>|\x00-\x1F]\\)*(?:[^\\/:*?"<>|\x00-\x1F]{0,254}[^.\\/:*?"<>|\x00-\x1F])', re.IGNORECASE
        )
        
        # Various aspect ratios
        self.facebook_aspect_ratio = 1.91
        self.twitter_aspect_ratio = 16/9
        
        try:
            from pysan.elements import get_alphabet
            self.get_alphabet = get_alphabet
        except: self.get_alphabet = lambda sequence: set(sequence)

    
    ### String Functions ###
    
    
    @staticmethod
    def compute_similarity(a: str, b: str) -> float:
        """
        Calculates the similarity between two strings.
        
        Parameters:
            a (str): The first string.
            b (str): The second string.
        
        Returns:
            float: The similarity between the two strings, as a float between 0 and 1.
        """
        from difflib import SequenceMatcher
        
        return SequenceMatcher(None, str(a), str(b)).ratio()
    
    
    @staticmethod
    def get_first_year_element(x):
        """
        Extracts the first year element from a given string, potentially containing multiple date or year formats.
        
        Parameters:
            x (str): The input string containing potential year information.
        
        Returns:
            int or float: The extracted first year element, or NaN if no valid year element is found.
        """
        
        # Split the input string using various separators
        stripped_list = re.split(r'( |/|–|\\u2009|-|\[)', str(x), 0)
        
        # Remove non-numeric characters from each element in the stripped list
        stripped_list = [re.sub(r'\D+', '', x) for x in stripped_list]
        
        # Filter elements with lengths between 3 and 4, as likely to be years
        stripped_list = [x for x in stripped_list if (len(x) >= 3) and (len(x) <= 4)]
        
        try:
            
            # Identify the index of the first numeric element in the stripped list
            numeric_list = [x.isnumeric() for x in stripped_list]
            
            # If a numeric substring is found, extract the first numeric value
            if True in numeric_list:
                idx = numeric_list.index(True, 0)
                first_numeric = int(stripped_list[idx])
            
            # If no numeric substring is found, raise an exception
            else: raise Exception('No numeric year element found')
        
        # Handle exceptions and return the first substring if no numeric substring is found
        except Exception as e:
            
            # If there are any substrings, return the first one as the year element
            if stripped_list: first_numeric = int(stripped_list[0])
            
            # If there are no substrings, return NaN
            else: first_numeric = np.nan

        return first_numeric

    
    @staticmethod
    def format_timedelta(time_delta):
        """
        Formats a time delta object to a string in the
        format '0 sec', '30 sec', '1 min', '1:30', '2 min', etc.
        
        Parameters:
          time_delta: A time delta object.
        
        Returns:
          A string in the format '0 sec', '30 sec', '1 min',
          '1:30', '2 min', etc.
        """
        seconds = time_delta.total_seconds()
        minutes = int(seconds // 60)
        seconds = int(seconds % 60)
        
        if minutes == 0: return f'{seconds} sec'
        elif seconds > 0: return f'{minutes}:{seconds:02}'
        else: return f'{minutes} min'
    
    
    ### List Functions ###
    
    
    @staticmethod
    def conjunctify_nouns(noun_list=None, and_or='and', verbose=False):
        """
        Concatenates a list of nouns into a grammatically correct string with specified conjunctions.
        
        Parameters:
            noun_list (list or str): A list of nouns to be concatenated.
            and_or (str, optional): The conjunction used to join the nouns. Default is 'and'.
            verbose (bool, optional): If True, prints verbose output. Default is False.
        
        Returns:
            str: A string containing the concatenated nouns with appropriate conjunctions.
        
        Example:
            noun_list = ['apples', 'oranges', 'bananas']
            conjunction = 'and'
            result = conjunctify_nouns(noun_list, and_or=conjunction)
            print(result)
            Output: 'apples, oranges, and bananas'
        """
        
        # Handle special cases where noun_list is None or not a list
        if (noun_list is None): return ''
        if not isinstance(noun_list, list): noun_list = list(noun_list)
        
        # If there are more than two nouns in the list, join the last two nouns with `and_or`
        # Otherwise, join all of the nouns with `and_or`
        if (len(noun_list) > 2):
            last_noun_str = noun_list[-1]
            but_last_nouns_str = ', '.join(noun_list[:-1])
            list_str = f', {and_or} '.join([but_last_nouns_str, last_noun_str])
        elif (len(noun_list) == 2): list_str = f' {and_or} '.join(noun_list)
        elif (len(noun_list) == 1): list_str = noun_list[0]
        else: list_str = ''
        
        # Print debug output if requested
        if verbose: print(f'noun_list="{noun_list}", and_or="{and_or}", list_str="{list_str}"')
        
        # Return the conjuncted noun list
        return list_str

    
    @staticmethod
    def get_jitter_list(ages_list):
        """
        Generates a list of jitter values for plotting age data points with a scattered plot.
        
        Parameters:
            ages_list (list): A list of ages for which jitter values are generated.
        
        Returns:
            list of float: A list of jitter values corresponding to the input ages.
        """
        
        # Initialize an empty list to store jitter values
        jitter_list = []
        
        # Iterate over the list of age groups
        for splits_list in get_splits_list(ages_list):
            
            # If there are multiple ages in a group, calculate jitter values for each age in the group
            if (len(splits_list) > 1):
                
                # Generate jitter values using the cut method and extend the jitter_list
                jitter_list.extend(
                    pd.cut(
                        np.array([min(splits_list) - 0.99, max(splits_list) + 0.99]),
                        len(splits_list) - 1,
                        retbins=True
                    )[1]
                )
            
            # If there is only one age in a group, add that age as the jitter value
            else: jitter_list.extend(splits_list)
        
        # Return the list of jitter values
        return jitter_list

    
    @staticmethod
    def get_splits_list(ages_list):
        """
        Divides a list of ages into sublists based on gaps in the age sequence.
        
        Parameters:
            ages_list (list of int or float): A list of ages to be split into sublists.
    
        Returns:
            list of lists of int or float: A list of sublists, each containing consecutive ages.
        """
        splits_list = []  # List to store sublists of consecutive ages
        current_list = []  # Temporary list to store the current consecutive ages
        previous_age = ages_list[0] - 1  # Initialize with a value lower than the first age
        
        # Iterate over the list of ages
        for age in ages_list:
            
            # Check if there is a gap larger than 1 between the current age and the previous age
            if age - previous_age > 1:
                splits_list.append(current_list)  # Append the current_list to splits_list
                current_list = []  # Reset the current_list
            current_list.append(age)  # Add the current age to the current_list
            previous_age = age  # Update the previous_age
        
        splits_list.append(current_list)  # Append the last current_list to splits_list
        
        # Return the list of sublists of ages
        return splits_list
    
    
    @staticmethod
    def count_ngrams(actions_list, highlighted_ngrams):
        """
        Counts how many times a given sequence of elements occurs in a list.
        
        Parameters:
            actions_list: A list of elements.
            highlighted_ngrams: A sequence of elements to count.
        
        Returns:
            The number of times the given sequence of elements occurs in the list.
        """
        count = 0
        for i in range(len(actions_list) - len(highlighted_ngrams) + 1):
            if (actions_list[i:i + len(highlighted_ngrams)] == highlighted_ngrams): count += 1
            
        return count
    
    
    @staticmethod
    def get_sequences_by_count(tg_dict, count=4):
        """
        Get sequences from the input dictionary based on a specific sequence length.

        Parameters:
            tg_dict (dict): Dictionary containing sequences.
            count (int, optional): Desired length of sequences to filter. Default is 4.

        Returns:
            list: List of sequences with the specified length.
        
        Raises:
            AssertionError: If no sequences of the specified length are found in the dictionary.
        """
        
        # Count the lengths of sequences in the dictionary to convert the sequence lengths list
        # into a pandas series to get the value counts of unique sequence lengths
        value_counts = Series([len(actions_list) for actions_list in tg_dict.values()]).value_counts()
        
        # Filter value counts to show only counts of count to get the desired sequence length of exactly count sequences from the dictionary
        value_counts_list = value_counts[value_counts == count].index.tolist()
        assert value_counts_list, f"You don't have exactly {count} sequences of the same length in the dictionary"
        sequences = [
            actions_list for actions_list in tg_dict.values() if (len(actions_list) == value_counts_list[0])
        ]
    
        return sequences
    
    
    @staticmethod
    def get_shape(list_of_lists):
        """
        Returns the shape of a list of lists, assuming the sublists are all of the same length.
        
        Parameters:
            list_of_lists: A list of lists.
        
        Returns:
            A tuple representing the shape of the list of lists.
        """
        
        # Check if the list of lists is empty.
        if not list_of_lists: return ()
        
        # Get the length of the first sublist.
        num_cols = len(list_of_lists[0])
        
        # Check if all of the sublists are the same length.
        for sublist in list_of_lists:
            if len(sublist) != num_cols: raise ValueError('All of the sublists must be the same length.')
        
        # Return a tuple representing the shape of the list of lists.
        return (len(list_of_lists), num_cols)
    
    
    @staticmethod
    def split_row_indices_list(splitting_indices_list, excluded_indices_list=[]):
        """
        Splits a list of row indices into a list of lists, where each inner list
        contains a contiguous sequence of indices that are not in the excluded indices list.
        
        Parameters:
            splitting_indices_list: A list of row indices to split.
            excluded_indices_list: A list of row indices that should be considered excluded.
                                   Empty by default.
        
        Returns:
            A list of lists, where each inner list contains a contiguous sequence of indices that are not in the excluded indices.
        """
        
        # Initialize the output list
        split_list = []
        
        # Initialize the current list
        current_list = []
        
        # Iterate over the splitting indices list
        for current_idx in range(int(min(splitting_indices_list)), int(max(splitting_indices_list)) + 1):
            
            # Check that the current index is in the splitting indices list and not in the excluded indices list
            if (current_idx in splitting_indices_list) and (current_idx not in excluded_indices_list):
                
                # Add it to the current list
                current_list.append(current_idx)
            
            # Otherwise, if the current list is not empty, add it to the split list and start a new current list
            else:
                if current_list: split_list.append(current_list)
                current_list = []
            
        # If the current list is not empty, add it to the split list
        if current_list: split_list.append(current_list)
        
        # Return the split list
        return split_list
    
    
    def check_4_doubles(self, item_list, verbose=False):
        """
        Check for similar items in the given list.

        Parameters:
            item_list (list): List of items to be compared.
            verbose (bool, optional): If True, print the execution time. Default is False.

        Returns:
            pandas.DataFrame: DataFrame containing similar item pairs and their similarities.
        """
        if verbose: t0 = time.time()
        rows_list = []
        n = len(item_list)
        for i in range(n-1):
            first_item = item_list[i]
            max_similarity = 0.0
            max_item = first_item
            for j in range(i+1, n):
                second_item = item_list[j]

                # Assume the first item is never identical to the second item
                this_similarity = self.compute_similarity(str(first_item), str(second_item))

                if this_similarity > max_similarity:
                    max_similarity = this_similarity
                    max_item = second_item

            # Get input row in dictionary format; key = col_name
            row_dict = {}
            row_dict['first_item'] = first_item
            row_dict['second_item'] = max_item
            row_dict['first_bytes'] = '-'.join(str(x) for x in bytearray(str(first_item),
                                                                         encoding=self.encoding_type, errors='replace'))
            row_dict['second_bytes'] = '-'.join(str(x) for x in bytearray(str(max_item),
                                                                          encoding=self.encoding_type, errors='replace'))
            row_dict['max_similarity'] = max_similarity

            rows_list.append(row_dict)

        column_list = ['first_item', 'second_item', 'first_bytes', 'second_bytes', 'max_similarity']
        item_similarities_df = DataFrame(rows_list, columns=column_list)
        if verbose:
            t1 = time.time()
            print(t1 - t0, time.ctime(t1))

        return item_similarities_df

    
    def check_for_typos(
        self, left_list, right_list, rename_dict={'left_item': 'left_item', 'right_item': 'right_item'},
        verbose=False
    ):
        """
        Check the closest names for typos by comparing items from left_list with
        items from right_list and computing their similarities.
        
        Parameters:
            left_list (list): List containing items to be compared (left side).
            right_list (list): List containing items to be compared (right side).
            rename_dict (dict, optional): Dictionary specifying custom column names in the output DataFrame.
                Default is {'left_item': 'left_item', 'right_item': 'right_item'}.
            verbose (bool, optional): If True, print the time taken for the computation. Default is False.
        
        Returns:
            pandas.DataFrame: DataFrame containing columns: 'left_item', 'right_item', and 'max_similarity'.
        
        Example:
            sd_set = set(some_dict.keys()).symmetric_difference(set(df.similar_key))
            typos_df = check_for_typos(list(set(df.similar_key).intersection(sd_set)),
                                       list(set(some_dict.keys()).intersection(sd_set)), verbose=False)
            for i, r in typos_df.sort_values(['max_similarity', 'left_item', 'right_item'], ascending=[False, True, True]).iterrows():
                print(f'some_dict[{r.left_item}] = some_dict.pop({r.right_item})')
        """
        
        # Initialize the time taken for the computation if verbose is True
        if verbose: t0 = time.time()
        
        # Initialize an empty list to store rows of the output data frame
        rows_list = []
        
        # Iterate through items in the left list
        for left_item in left_list:
            max_similarity = 0.0
            max_item = left_item
            
            # Iterate through items in the right list and find the most similar item
            for right_item in right_list:
                this_similarity = self.compute_similarity(left_item, right_item)
                if this_similarity > max_similarity:
                    max_similarity = this_similarity
                    max_item = right_item
            
            # Create a dictionary representing a row in the output data frame
            row_dict = {
                'left_item': left_item,
                'right_item': max_item,
                'max_similarity': max_similarity
            }
            
            # Add the row dictionary to the list of rows
            rows_list.append(row_dict)
        
        # Define the column names for the output data frame
        column_list = ['left_item', 'right_item', 'max_similarity']
        
        # Create a data frame from the list of rows, rename columns if necessary
        name_similarities_df = pd.DataFrame(rows_list, columns=column_list).rename(columns=rename_dict)
        
        # Print the time taken for the computation if verbose is True
        if verbose:
            t1 = time.time()
            print(t1-t0, time.ctime(t1))
        
        # Return the resulting data frame
        return name_similarities_df
    
    
    def convert_strings_to_integers(self, sequence, alphabet_list=None):
        """
        Converts a sequence of strings to a sequence of integers.
        
        Parameters:
            sequence: A sequence of strings.
            alphabet_list: A list of the unique elements of sequence,
                           passed in to stabilize the order.
        
        Returns:
            A sequence of integers.
            A string to integer map as dictionary.
        """
        if alphabet_list is None: alphabet_list = list(self.get_alphabet(sequence))
        
        # Create a dictionary to map strings to integers
        string_to_integer_map = {}
    
        # Create a new integer array with the same length as sequence but with no elements in it
        new_sequence = np.zeros_like(sequence, dtype=int)
        
        for i, string in enumerate(sequence):
            if string not in string_to_integer_map:
                if string not in alphabet_list: string_to_integer_map[string] = -1
                else: string_to_integer_map[string] = alphabet_list.index(string)
            new_sequence[i] = string_to_integer_map[string]
        new_sequence = new_sequence.astype(int)
        
        return new_sequence, string_to_integer_map
    
    
    def get_ndistinct_subsequences(self, sequence, verbose=False):
        """
        Note:
            This replaces from pysan import get_ndistinct_subsequences
        """

        # This implementation works on strings, so parse non-strings to strings
        if (type(sequence) is not str) or (not all([(len(str(e)) == 1) for e in sequence])):
            new_sequence, string_to_integer_map = self.convert_strings_to_integers(sequence, alphabet_list=None)
            sequence = []
            for e in new_sequence: sequence.append(e)
        if verbose: print('sequence', sequence)

        # Create an array to store index of last
        last = [-1 for i in range(256 + 1)] # hard-coded value needs explaining -ojs

        # Length of input string
        sequence_length = len(sequence)

        # dp[i] is going to store count of discount subsequence of length of i
        dp = [-2 for i in range(sequence_length + 1)]

        # Empty substring has only one subseqence
        dp[0] = 1

        # Traverse through all lengths from 1 to n 
        for i in range(1, sequence_length + 1):

            # Number of subseqence with substring str[0...i-1]
            dp[i] = 2 * dp[i - 1]

            # If current character has appeared before, then remove all subseqences ending with previous occurrence
            if last[sequence[i - 1]] != -1: dp[i] = dp[i] - dp[last[sequence[i - 1]]]

            last[sequence[i - 1]] = i - 1

        return dp[sequence_length]
    
    
    def get_turbulence(self, sequence, verbose=False):
        """
        Computes turbulence for a given sequence, based on
        [Elzinga & Liefbroer's 2007 definition](https://www.researchgate.net/publication/225402919_De-standardization_of_Family-Life_Trajectories_of_Young_Adults_A_Cross-National_Comparison_Using_Sequence_Analysis)
        which is also implemented in the [TraMineR](http://traminer.unige.ch/doc/seqST.html) sequence analysis library.

        Note:
            This replaces from pysan import get_turbulence
        """
        import statistics
        phi = self.get_ndistinct_subsequences(sequence, verbose=verbose)
        if verbose: print('phi', phi)
        
        from pysan.statistics import get_spells
        state_durations = [value for key, value in get_spells(sequence)]
        if verbose: print('durations', state_durations)
        if verbose: print('mean duration', statistics.mean(state_durations))
        
        try: variance_of_state_durations = statistics.variance(state_durations)
        except: variance_of_state_durations = 0.0
        if verbose: print('variance', variance_of_state_durations)
        
        tbar = statistics.mean(state_durations)
        
        maximum_state_duration_variance = (len(sequence) - 1) * (1 - tbar) ** 2
        if verbose: print('smax', maximum_state_duration_variance)
        
        top_right = maximum_state_duration_variance + 1
        bot_right = variance_of_state_durations + 1
        turbulence = math.log2(phi * (top_right / bot_right))
        if verbose: print('turbulence', turbulence)
        
        return turbulence
    
    
    def replace_consecutive_elements(self, actions_list, element):
        """
        Replaces consecutive elements in a list with a count of how many there are in a row.
        
        Parameters:
            list1: A list of elements.
            element: The element to replace consecutive occurrences of.
        
        Returns:
            A list with the consecutive elements replaced with a count of how many there are in a row.
        """
        result = []
        count = 0
        for i in range(len(actions_list)):
            if (actions_list[i] == element): count += 1
            else:
                if (count > 0): result.append(f'{element} x{str(count)}')
                result.append(actions_list[i])
                count = 0
        
        # Handle the last element
        if (count > 0): result.append(f'{element} x{str(count)}')
        
        return(result)
    
    
    ### File Functions ###
    
    
    @staticmethod
    def get_function_file_path(func):
        """
        Returns the relative or absolute file path where the function is stored.

        Parameters:
            func: A Python function.

        Returns:
            A string representing the relative or absolute file path where the function is stored.

        Example:
            def my_function(): pass
            file_path = nu.get_function_file_path(my_function)
            print(osp.abspath(file_path))
        """
        import inspect
        file_path = inspect.getfile(func)

        # If the function is defined in a Jupyter notebook, return the absolute file path
        if file_path.startswith('<stdin>'): return osp.abspath(file_path)

        # Otherwise, return the relative file path
        else: return osp.relpath(file_path)
    
    
    @staticmethod
    def get_utility_file_functions(util_path=None):
        """
        Extracts a set of function names already defined in the utility file.
        
        Parameters:
            util_path (str, optional): The path to the utility file. Default is '../py/notebook_utils.py'.
        
        Returns:
            set of str: A set containing the names of functions already defined in the utility file.
        """
        
        # Set the utility path if not provided
        if util_path is None: util_path = '../py/notebook_utils.py'
        
        # Compile the regular expression pattern for identifying function definitions
        utils_regex = re.compile(r'def ([a-z0-9_]+)\(')
        
        # Read the utility file and extract function names
        with open(util_path, 'r', encoding='utf-8') as f:
            
            # Read the file contents line by line
            lines_list = f.readlines()
            
            # Initialize an empty set to store function names
            utils_set = set()
            
            # Iterate over each line in the file
            for line in lines_list:
                
                # Search for function definitions using the regular expression
                match_obj = utils_regex.search(line)
                
                # If a function definition is found, extract the function name and add it to the set
                if match_obj:
                    
                    # Extract the function name from the match
                    scraping_util = match_obj.group(1)
                    utils_set.add(scraping_util)
        
        return utils_set
    
    
    @staticmethod
    def open_path_in_notepad(path_str, home_key='USERPROFILE', text_editor_path=r'C:\Program Files\Notepad++\notepad++.exe', verbose=True):
        """
        Open a file in Notepad or a specified text editor.
        
        Parameters:
            path_str (str): The path to the file to be opened.
            home_key (str, optional): The environment variable key for the home directory. Default is 'USERPROFILE'.
            text_editor_path (str, optional): The path to the text editor executable. Default is Notepad++.
            verbose (bool, optional): If True, prints debug output. Default is False.
        
        Returns:
            None
        
        Notes:
            The function uses subprocess to run the specified text editor with the provided file path.
        
        Example:
            nu.open_path_in_notepad('C:/example.txt')
        """
        
        # Expand '~' to the home directory in the file path
        environ_dict = dict(os.environ)
        if ('~' in path_str):
            if home_key in environ_dict: path_str = path_str.replace('~', environ_dict[home_key])
            else: path_str = osp.expanduser(path_str)
        
        # Get the absolute path to the file
        absolute_path = osp.abspath(path_str)
        if verbose: print(f'Attempting to open {absolute_path}')

        # Open the absolute path to the file in Notepad or the specified text editor
        # !"{text_editor_path}" "{absolute_path}"
        import subprocess
        try: subprocess.run([text_editor_path, absolute_path])
        except FileNotFoundError as e: subprocess.run(['explorer.exe', osp.dirname(absolute_path)])

    
    @staticmethod
    def get_top_level_folder_paths(folder_path, verbose=False):
        """
        Gets all top-level folder paths within a given directory.
        
        Parameters:
            folder_path (str): The path to the directory to scan for top-level folders.
            verbose (bool, optional): Whether to print debug information about the process. Defaults to False.
        
        Returns:
            list[str]: A list of absolute paths to all top-level folders within the provided directory.
        
        Raises:
            FileNotFoundError: If the provided folder path does not exist.
            NotADirectoryError: If the provided folder path points to a file or non-existing directory.
        
        Notes:
            This function does not recursively scan for subfolders within the top-level folders.
            If `verbose` is True, it will print the number of discovered top-level folders.
        """
        
        # Make sure the provided folder exists and is a directory
        if not os.path.exists(folder_path): raise FileNotFoundError(f'Directory {folder_path} does not exist.')
        if not os.path.isdir(folder_path): raise NotADirectoryError(f'Path {folder_path} is not a directory.')
        
        # Initialize an empty list to store top-level folder paths
        top_level_folders = []
        
        # Iterate through items in the specified folder
        for item in os.listdir(folder_path):
            
            # Construct the full path for each item
            full_item_path = os.path.join(folder_path, item)
            
            # Check if the item is a directory, and if so, add its path to the list
            if os.path.isdir(full_item_path): top_level_folders.append(full_item_path)
        
        # Optionally print information based on the `verbose` flag
        if verbose: print(f'Found {len(top_level_folders)} top-level folders in {folder_path}.')
        
        # Return the list of top-level folder paths
        return top_level_folders
    
    
    def get_notebook_functions_dictionary(self, github_folder=None):
        """
        Gets a dictionary of all functions defined within notebooks in the github folder,
        with the key being the function name,
        and the value being the count of how many times the function has been defined.

        Parameters:
            github_folder (str, optional): The path of the root folder of the GitHub repository containing the notebooks.
                                           Defaults to the parent directory of the current working directory.

        Returns:
            dict: The dictionary of function definitions with the count of their occurances.
        """
        fn_regex = re.compile(r'\s+"def ([a-z0-9_]+)\(')
        black_list = ['.ipynb_checkpoints', '$Recycle.Bin']
        if github_folder is None: github_folder = self.github_folder
        rogue_fns_dict = {}
        for sub_directory, directories_list, files_list in os.walk(github_folder):
            if all(map(lambda x: x not in sub_directory, black_list)):
                for file_name in files_list:
                    if file_name.endswith('.ipynb') and not ('Attic' in file_name):
                        file_path = osp.join(sub_directory, file_name)
                        with open(file_path, 'r', encoding=self.encoding_type) as f:
                            lines_list = f.readlines()
                            for line in lines_list:
                                match_obj = fn_regex.search(line)
                                if match_obj:
                                    fn = match_obj.group(1)
                                    rogue_fns_dict[fn] = rogue_fns_dict.get(fn, 0) + 1
        
        return rogue_fns_dict
    
    
    def get_notebook_functions_set(self, github_folder=None):
        """
        Gets a set of all functions defined within notebooks in the github folder.

        Parameters:
            github_folder (str, optional): The path of the root folder of the GitHub repository containing the notebooks.
                                           Defaults to the parent directory of the current working directory.

        Returns:
            set: The set of function definitions.
        """
        if github_folder is None: github_folder = self.github_folder
        rogue_fns_set = set([k for k in self.get_notebook_functions_dictionary(github_folder=github_folder).keys()])
        
        return rogue_fns_set
    
    
    def show_duplicated_util_fns_search_string(self, util_path=None, github_folder=None):
        """
        Search for duplicate utility function definitions in Jupyter notebooks within a specified GitHub repository folder.
        The function identifies rogue utility function definitions in Jupyter notebooks and prints a regular expression
        pattern to search for instances of these definitions. The intention is to replace these calls with the
        corresponding `nu.` equivalent and remove the duplicates.

        Parameters:
            util_path (str, optional): The path to the utilities file to check for existing utility function definitions.
                                       Defaults to `../py/notebook_utils.py`.
            github_folder (str, optional): The path of the root folder of the GitHub repository containing the notebooks.
                                           Defaults to the parent directory of the current working directory.

        Returns:
            None: The function prints the regular expression pattern to identify rogue utility function definitions.
        """

        # Get a list of rogue functions already in utilities file
        utils_set = self.get_utility_file_functions(util_path=util_path)

        # Make a set of rogue util functions
        if github_folder is None: github_folder = self.github_folder
        rogue_fns_list = [fn for fn in self.get_notebook_functions_dictionary(github_folder=github_folder).keys() if fn in utils_set]
        
        if rogue_fns_list:
            print(f'Search for *.ipynb; file masks in the {github_folder} folder for this pattern:')
            print('\\s+"def (' + '|'.join(rogue_fns_list) + ')\(')
            print('Replace each of the calls to these definitions with calls the the nu. equivalent (and delete the definitions).')

    
    def list_dfs_in_folder(self, pickle_folder=None):
        """
        List DataFrame names stored as pickles in a specified folder.
        
        Parameters:
            pickle_folder (str, optional): The folder path where pickle files are stored.
                If None, uses the default saves_pickle_folder. Default is None.
        
        Returns:
            list of str: A list of DataFrame pickle file names.
        """
        
        # Set the pickle folder if not provided
        if pickle_folder is None: pickle_folder = self.saves_pickle_folder
        
        # Filter the file names to include only pickle files (.pkl or .pickle extensions)
        pickles_list = [file_name.split('.')[0] for file_name in listdir(pickle_folder) if (file_name.split('.')[1] in ['pkl', 'pickle'])]
        
        # Filter the list to include only DataFrame names (ending with '_df')
        dfs_list = [pickle_name for pickle_name in pickles_list if pickle_name.endswith('_df')]
        
        # Return the list of DataFrame pickle file names
        return dfs_list
    
    
    def show_dupl_fn_defs_search_string(self, util_path=None, github_folder=None):
        """
        Identifies and reports duplicate function definitions in Jupyter notebooks and suggests how to consolidate them.
        
        Parameters:
            util_path (str, optional): The path to the utility file where refactored functions will be added.
                Defaults to '../py/notebook_utils.py'.
            github_folder (str, optional): The path to the GitHub repository containing the Jupyter notebooks.
                Default is the parent folder of the current directory.
        
        Returns:
            None
        
        Notes:
        The function prints a search string pattern that can be used to identify duplicate function definitions in Jupyter notebooks.
        The pattern is based on the function names extracted from the notebook using `get_notebook_functions_dictionary()`.
        
        Example:
            nu.show_dupl_fn_defs_search_string()
        """
        
        # Set the utility path if not provided
        if util_path is None: util_path = '../py/notebook_utils.py'
        
        # Set the GitHub folder path if not provided
        if github_folder is None: github_folder = self.github_folder
        
        # Get the function definitions dictionary
        function_definitions_dict = self.get_notebook_functions_dictionary()
        
        # Convert the dictionary to a DataFrame
        df = DataFrame([{'function_name': k, 'definition_count': v} for k, v in function_definitions_dict.items()])
        
        # Create a mask to filter functions with more than one definition
        mask_series = (df.definition_count > 1)
        duplicate_fns_list = df[mask_series].function_name.tolist()

        # If there are duplicate function definitions, print a message and search string
        if duplicate_fns_list:
            print(f'Search for *.ipynb; file masks in the {github_folder} folder for this pattern:')
            print('\\s+"def (' + '|'.join(duplicate_fns_list) + ')\(')
            print(f'Consolidate these duplicate definitions and add the refactored one to {util_path} (and delete the definitions).')
    
    
    def delete_ipynb_checkpoint_folders(self, github_folder=None):
        """
        Deletes all '.ipynb_checkpoints' folders within the specified GitHub folder and its subdirectories.
        
        Parameters:
            github_folder (str, optional): The path to the GitHub folder containing the '.ipynb_checkpoints' folders.
                If not provided, the current working directory is used.
        
        Returns:
            None
        """
        
        # Set the GitHub folder path if not provided
        if github_folder is None: github_folder = self.github_folder
        
        # Import required libraries
        import shutil
        
        # Iterate over all subdirectories within the github_folder
        for sub_directory, directories_list, files_list in os.walk(github_folder):
            
            # Check if the directory 'ipynb_checkpoints' exists in the current subdirectory
            if '.ipynb_checkpoints' in directories_list:
                
                # Construct the full path to the '.ipynb_checkpoints' folder
                folder_path = os.path.join(sub_directory, '.ipynb_checkpoints')
                
                # Remove the folder and its contents
                shutil.rmtree(folder_path)
    
    
    ### Storage Functions ###
    
    
    @staticmethod
    def attempt_to_pickle(
        df: DataFrame, pickle_path: str, raise_exception: bool = False,
        verbose: bool = True
    ) -> None:
        """
        Attempts to pickle a DataFrame to a file.
        
        Parameters:
            df (DataFrame): The DataFrame to pickle.
            pickle_path (str): The path to the pickle file.
            raise_exception (bool, optional): Whether to raise an exception if the pickle fails. Defaults to False.
            verbose (bool, optional): Whether to print status messages. Defaults to True.
        
        Returns:
            None
        """
        try:
            if verbose: print('Pickling to {}'.format(osp.abspath(pickle_path)), flush=True)

            # Protocol 4 is not handled in python 2
            if sys.version_info.major == 2: df.to_pickle(pickle_path, protocol=2)

            # Pickle protocol must be <= 4
            elif sys.version_info.major == 3: df.to_pickle(pickle_path, protocol=min(4, pickle.HIGHEST_PROTOCOL))

        except Exception as e:
            os.remove(pickle_path)
            if verbose: print(e, ": Couldn't save {:,} cells as a pickle.".format(df.shape[0]*df.shape[1]), flush=True)
            if raise_exception: raise

    
    def csv_exists(self, csv_name, folder_path=None, verbose=False):
        """
        Checks if a CSV file exists in the specified folder or the default CSV folder.
        
        Parameters:
            csv_name (str): The name of the CSV file (with or without the '.csv' extension).
            folder_path (str, optional): The path to the folder containing the CSV file.
                If None, uses the default saves_csv_folder specified in the class.
            verbose (bool, optional): If True, print the absolute path of the CSV file. Default is False.
        
        Returns:
            bool: True if the CSV file exists, False otherwise.
        """
        
        # Set folder path if not provided
        if folder_path is None: folder_path = self.saves_csv_folder
        
        # Construct the full path to the CSV file, including the .csv extension if it's not already included
        if csv_name.endswith('.csv'): csv_path = osp.join(folder_path, csv_name)
        else: csv_path = osp.join(folder_path, f'{csv_name}.csv')
        
        # Optionally print the absolute path to the CSV file
        if verbose: print(osp.abspath(csv_path), flush=True)
        
        # Check if the CSV file exists
        return osp.isfile(csv_path)

    
    def load_csv(self, csv_name=None, folder_path=None):
        """
        Loads a CSV file from the specified folder or the default CSV folder,
        returning the data as a pandas DataFrame.
        
        Parameters:
            csv_name (str, optional): The name of the CSV file (with or without the '.csv' extension).
                If None, loads the most recently modified CSV file in the specified or default folder.
            folder_path (str, optional): The path to the folder containing the CSV file.
                If None, uses the default data_csv_folder specified in the class.
        
        Returns:
            pandas.DataFrame: The data from the CSV file as a pandas DataFrame.
        """
        
        # Set folder path if not provided
        if folder_path is None: csv_folder = self.data_csv_folder
        else: csv_folder = osp.join(folder_path, 'csv')
        
        # Determine the CSV file path based on the provided name or the most recently modified file in the folder
        if csv_name is None:
            
            # If no specific CSV file is named, load the most recently modified CSV file
            csv_path = max([osp.join(csv_folder, f) for f in listdir(csv_folder)], key=osp.getmtime)
        else:
            
            # If a specific CSV file is named, construct the full path to the CSV file
            if csv_name.endswith('.csv'): csv_path = osp.join(csv_folder, csv_name)
            else: csv_path = osp.join(csv_folder, f'{csv_name}.csv')
        
        # Load the CSV file as a pandas DataFrame using the class-specific encoding
        data_frame = read_csv(osp.abspath(csv_path), encoding=self.encoding_type)
        
        return data_frame

    
    def pickle_exists(self, pickle_name: str) -> bool:
        """
        Checks if a pickle file exists.

        Parameters:
            pickle_name (str): The name of the pickle file.

        Returns:
            bool: True if the pickle file exists, False otherwise.
        """
        pickle_path = osp.join(self.saves_pickle_folder, '{}.pkl'.format(pickle_name))

        return osp.isfile(pickle_path)
    
    
    def load_object(
        self, obj_name: str, pickle_path: str = None, download_url: str = None,
        verbose: bool = False
    ) -> object:
        """
        Load an object from a pickle file.

        Parameters:
            obj_name (str): The name of the object to load.
            pickle_path (str, optional): The path to the pickle file. Defaults to None.
            download_url (str, optional): The URL to download the pickle file from. Defaults to None.
            verbose (bool, optional): Whether to print status messages. Defaults to False.

        Returns:
            object: The loaded object.
        """
        if pickle_path is None:
            pickle_path = osp.join(self.saves_pickle_folder, '{}.pkl'.format(obj_name))
        if not osp.isfile(pickle_path):
            if verbose: print('No pickle exists at {} - attempting to load as csv.'.format(osp.abspath(pickle_path)), flush=True)
            csv_path = osp.join(self.saves_csv_folder, '{}.csv'.format(obj_name))
            if not osp.isfile(csv_path):
                if verbose: print('No csv exists at {} - attempting to download from URL.'.format(osp.abspath(csv_path)), flush=True)
                object = read_csv(download_url, low_memory=False,
                                     encoding=self.encoding_type)
            else:
                object = read_csv(csv_path, low_memory=False,
                                     encoding=self.encoding_type)
            if isinstance(object, DataFrame):
                self.attempt_to_pickle(object, pickle_path, raise_exception=False)
            else:
                with open(pickle_path, 'wb') as handle:

                    # Protocol 4 is not handled in python 2
                    if sys.version_info.major == 2:
                        pickle.dump(object, handle, 2)
                    elif sys.version_info.major == 3:
                        pickle.dump(object, handle, pickle.HIGHEST_PROTOCOL)

        else:
            try:
                object = pd.read_pickle(pickle_path)
            except:
                with open(pickle_path, 'rb') as handle:
                    object = pickle.load(handle)

        if verbose: print('Loaded object {} from {}'.format(obj_name, pickle_path), flush=True)

        return(object)
    
    
    def load_data_frames(self, **kwargs):
        """
        Loads Pandas DataFrames from pickle or CSV files, potentially switching between folders if necessary.
        
        Parameters:
            **kwargs (dict): Keyword arguments specifying the names of the data frames to load.
                The frame_name is used to construct file paths for loading DataFrames.
        
        Returns:
            dict: A dictionary where keys are frame_names and values are Pandas DataFrames.
        """
        frame_dict = {}  # Dictionary to store loaded DataFrames
        
        # Iterate over each frame_name provided in kwargs
        for frame_name in kwargs:
            was_successful = False
            
            # Attempt to load the data frame from a pickle file
            if not was_successful:
                pickle_path = osp.abspath(osp.join(self.saves_pickle_folder, f'{frame_name}.pkl'))
                
                # If the pickle file exists, load it using the load_object function
                if osp.isfile(pickle_path):
                    print(f'Attempting to load {pickle_path}.', flush=True)
                    try:
                        frame_dict[frame_name] = self.load_object(frame_name)
                        was_successful = True
                    except Exception as e:
                        print(str(e).strip())
                        was_successful = False
            
            # If the pickle file doesn't exist, check for a CSV file with the same name
            if not was_successful:
                csv_name = f'{frame_name}.csv'
                csv_path = osp.abspath(osp.join(self.saves_csv_folder, csv_name))
                
                # If the CSV file exists in the saves folder, load it from there
                if osp.isfile(csv_path):
                    print(f'No pickle exists for {frame_name} - attempting to load {csv_path}.', flush=True)
                    try:
                        frame_dict[frame_name] = self.load_csv(csv_name=frame_name, folder_path=self.saves_folder)
                        was_successful = True
                    except Exception as e:
                        print(str(e).strip())
                        was_successful = False
            
            # If the CSV file doesn't exist in the saves folder, check for it in the data folder
            if not was_successful:
                csv_path = osp.abspath(osp.join(self.data_csv_folder, csv_name))
                
                # If the CSV file exists in the data folder, load it from there
                if osp.isfile(csv_path):
                    print(f'No csv exists for {frame_name} - trying {csv_path}.', flush=True)
                    try:
                        frame_dict[frame_name] = self.load_csv(csv_name=frame_name)
                        was_successful = True
                    except Exception as e:
                        print(str(e).strip())
                        was_successful = False
            
            # If the CSV file doesn't exist anywhere, skip loading this data frame
            if not was_successful:
                print(f'No csv exists for {frame_name} - just forget it.', flush=True)
                frame_dict[frame_name] = None
        
        return frame_dict
    
    
    def save_data_frames(self, include_index=False, verbose=True, **kwargs):
        """
        Saves data frames to CSV files.

        Parameters:
            include_index: Whether to include the index in the CSV files.
            verbose: Whether to print information about the saved files.
            **kwargs: A dictionary of data frames to save. The keys of the dictionary
                      are the names of the CSV files to save the data frames to.

        Returns:
            None
        """

        # Iterate over the data frames in the kwargs dictionary and save them to CSV files
        for frame_name in kwargs:
            if isinstance(kwargs[frame_name], DataFrame):
                
                # Generate the path to the CSV file
                csv_path = osp.join(self.saves_csv_folder, '{}.csv'.format(frame_name))

                # Print a message about the saved file if verbose is True
                if verbose: print('Saving to {}'.format(osp.abspath(csv_path)), flush=True)

                # Save the data frame to a CSV file
                kwargs[frame_name].to_csv(csv_path, sep=',', encoding=self.encoding_type,
                                          index=include_index)
    
    
    def store_objects(self, verbose: bool = True, **kwargs: dict) -> None:
        """
        Store objects to pickle files.

        Parameters:
            verbose (bool, optional): Whether to print status messages. Defaults to True.
            **kwargs (dict): The objects to store. The keys of the dictionary are the names of the objects,
                and the values are the objects themselves.

        Returns:
            None

        """
        for obj_name in kwargs:
            # if hasattr(kwargs[obj_name], '__call__'):
            #     raise RuntimeError('Functions cannot be pickled.')
            pickle_path = osp.join(self.saves_pickle_folder, '{}.pkl'.format(obj_name))
            if isinstance(kwargs[obj_name], DataFrame):
                self.attempt_to_pickle(kwargs[obj_name], pickle_path, raise_exception=False, verbose=verbose)
            else:
                if verbose: print('Pickling to {}'.format(osp.abspath(pickle_path)), flush=True)
                with open(pickle_path, 'wb') as handle:

                    # Protocol 4 is not handled in python 2
                    if sys.version_info.major == 2:
                        pickle.dump(kwargs[obj_name], handle, 2)

                    # Pickle protocol must be <= 4
                    elif sys.version_info.major == 3:
                        pickle.dump(kwargs[obj_name], handle, min(4, pickle.HIGHEST_PROTOCOL))
    
    
    ### Module Functions ###
    
    
    @staticmethod
    def get_dir_tree(module_name, contains_str=None, not_contains_str=None, verbose=False):
        """
        Gets a list of all attributes in a given module.
        
        Parameters::
            module_name (str): The name of the module to get the directory list for.
            contains_str (str, optional): If provided, only print attributes containing this substring (case-insensitive).
            not_contains_str (str, optional): If provided, exclude printing attributes containing this
                substring (case-insensitive).
            verbose (bool, optional): If True, print additional information during processing.
        
        Returns:
            list[str]: A list of attributes in the module that match the filtering criteria.
        """
        
        # Initialize sets for processed attributes and their suffixes
        dirred_set = set([module_name])
        suffix_set = set([module_name])
        
        # Initialize an unprocessed set of all attributes in the module_name module that don't start with an underscore
        import importlib
        module_obj = importlib.import_module(module_name)
        undirred_set = set([f'module_obj.{fn}' for fn in dir(module_obj) if not fn.startswith('_')])
        
        # Continue processing until the unprocessed set is empty
        while undirred_set:
    
            # Pop the next function or submodule
            fn = undirred_set.pop()
    
            # Extract the suffix of the function or submodule
            fn_suffix = fn.split('.')[-1]
    
            # Check if the suffix has not been processed yet
            if fn_suffix not in suffix_set:
                
                # Add it to processed and suffix sets
                dirred_set.add(fn)
                suffix_set.add(fn_suffix)
                
                try:
                    
                    # Evaluate the 'dir()' function for the attribute and update the unprocessed set with its function or submodule
                    dir_list = eval(f'dir({fn})')
                    
                    # Add all of the submodules of the function or submodule to undirred_set if they haven't been processed yet
                    undirred_set.update([f'{fn}.{fn1}' for fn1 in dir_list if not fn1.startswith('_')])
                
                # If there is an error getting the dir() of the function or submodule, just continue to the next iteration
                except: continue
                
        # Apply filtering criteria if provided
        if (not bool(contains_str)) and bool(not_contains_str):
            dirred_set = [fn for fn in dirred_set if (not_contains_str not in fn.lower())]
        elif bool(contains_str) and (not bool(not_contains_str)):
            dirred_set = [fn for fn in dirred_set if (contains_str in fn.lower())]
        elif bool(contains_str) and bool(not_contains_str):
            dirred_set = [fn for fn in dirred_set if (contains_str in fn.lower()) and (not_contains_str not in fn.lower())]
        
        # Remove the importlib object variable name
        dirred_set = set([fn.replace('module_obj', module_name) for fn in dirred_set])
        
        return sorted(dirred_set)
    
    
    def update_modules_list(
        self, modules_list: Optional[List[str]] = None, verbose: bool = False
    ) -> None:
        """
        Updates the list of modules that are installed.

        Parameters:
            modules_list (Optional[List[str]], optional): The list of modules to update. If None,
                the list of installed modules will be used. Defaults to None.
            verbose (bool, optional): Whether to print status messages. Defaults to False.

        Returns:
            None
        """

        if modules_list is None: self.modules_list = [
            o.decode().split(' ')[0] for o in subprocess.check_output(f'{self.pip_command_str} list'.split(' ')).splitlines()[2:]
            ]
        else: self.modules_list = modules_list

        if verbose: print('Updated modules list to {}'.format(self.modules_list), flush=True)
    
    
    def ensure_module_installed(self, module_name: str, upgrade: bool = False, verbose: bool = True) -> None:
        """
        Checks if a module is installed and installs it if it is not.
        
        Parameters:
            module_name (str): The name of the module to check for.
            upgrade (bool, optional): Whether to upgrade the module if it is already installed.
                Defaults to False.
            verbose (bool, optional): Whether to print status messages. Defaults to True.
        
        Returns:
            None
        """

        if module_name not in self.modules_list:
            command_str = f'{self.pip_command_str} install {module_name}'
            if upgrade: command_str += ' --upgrade'
            if verbose: print(command_str, flush=True)
            else: command_str += ' --quiet'
            output_str = subprocess.check_output(command_str.split(' '))
            if verbose:
                for line_str in output_str.splitlines(): print(line_str.decode(), flush=True)
            self.update_modules_list(verbose=verbose)
    
    
    ### URL and Soup Functions ###
    
    
    @staticmethod
    def get_filename_from_url(url, verbose=False):
        """
        Extracts the filename from a given URL.
        
        Parameters:
            url (str): The URL from which to extract the filename.
            verbose (bool, optional): If True, print additional information (default is False).
        
        Returns:
            str: The extracted filename from the URL.
        """

        # Parse the URL and extract the filename from the path
        file_name = urllib.parse.urlparse(url).path.split('/')[-1]
        
        # Print verbose information if verbose flag is True
        if verbose: print(f"Extracted filename from '{url}': '{file_name}'")

        return file_name
    
    
    @staticmethod
    def get_style_column(tag_obj, verbose=False):
        """
        Extracts the style column from a given BeautifulSoup tag object and returns
        the style column tag object.
    
        Parameters:
            tag_obj (bs4.element.Tag): The BeautifulSoup tag object to extract the style column from.
            verbose (bool, optional): If True, display intermediate steps for debugging. Default is False.
    
        Returns:
            bs4.element.Tag: The modified BeautifulSoup tag object representing the style column.
        """
        
        # Display the initial tag object if verbose is True
        if verbose: display(tag_obj)
    
        # Get the parent td tag object
        tag_obj = get_td_parent(tag_obj, verbose=verbose)
        if verbose: display(tag_obj)
    
        # Traverse the siblings of the table tag object backward until a style column is found
        from bs4.element import NavigableString
        while isinstance(tag_obj, NavigableString) or not tag_obj.has_attr('style'):
            tag_obj = tag_obj.previous_sibling
            if verbose: display(tag_obj)
    
        # Display the text content of the found style column if verbose is True
        if verbose: display(tag_obj.text.strip())
        
        # Return the style column tag object
        return tag_obj

    
    @staticmethod
    def get_td_parent(tag_obj, verbose=False):
        """
        Finds and returns the closest ancestor of the given BeautifulSoup tag object that is a 'td' tag.
    
        Parameters:
            tag_obj (bs4.element.Tag): The BeautifulSoup tag object whose 'td' ancestor needs to be found.
            verbose (bool, optional): If True, display intermediate steps for debugging. Default is False.
    
        Returns:
            bs4.element.Tag: The closest 'td' ancestor tag object.
        """
        if verbose: display(tag_obj)
        
        # Traverse the parent tags upward until a table cell (<td>) is found
        while (tag_obj.name != 'td'):
            tag_obj = tag_obj.parent
            if verbose: display(tag_obj)
        
        # Return the closest 'td' ancestor tag object
        return tag_obj
    
    
    def download_file(self, url, download_dir=None, exist_ok=False, verbose=False):
        """
        Downloads a file from the internet.

        Parameters:
            url: The URL of the file to download.
            download_dir: The directory to download the file to. If None, the file
                          will be downloaded to the `downloads` subdirectory of the data folder.
            exist_ok: If True, the function will not raise an error if the file
                      already exists.
            verbose: If True, the function will print progress information to the
                     console.

        Returns:
            The path to the downloaded file.
        """

        # Get the file name from the URL
        file_name = self.get_filename_from_url(url, verbose=verbose)

        # If the download directory is not specified, use the downloads subdirectory
        if download_dir is None: download_dir = osp.join(self.data_folder, 'downloads')

        # Create the download directory if it does not exist
        makedirs(download_dir, exist_ok=True)

        # Compute the path to the downloaded file
        file_path = osp.join(download_dir, file_name)

        # If the file does not exist or if exist_ok is True, download the file
        if exist_ok or (not osp.isfile(file_path)):
            from urllib.request import urlretrieve
            urlretrieve(url, file_path)
    
        return file_path

    
    def get_page_soup(self, page_url_or_filepath, verbose=False):
        """
        Gets the BeautifulSoup soup object for a given page URL or filepath.

        Parameters:
            page_url_or_filepath (str): The URL or filepath of the page to get the soup object for.
            verbose (bool, optional): Whether to print verbose output. Defaults to True.

        Returns:
            BeautifulSoup: The BeautifulSoup soup object for the given page.
        """
            
        # Check if the page URL or filepath is a URL
        if self.url_regex.fullmatch(page_url_or_filepath):

            # If the page URL or filepath is a URL, open it using urllib.request.urlopen()
            with urllib.request.urlopen(page_url_or_filepath) as response: page_html = response.read()
        
        # If the page URL or filepath is not a URL, ensure it exists and open it using open()
        elif self.filepath_regex.fullmatch(page_url_or_filepath):
            assert osp.isfile(page_url_or_filepath), f"{page_url_or_filepath} doesn't exist"
            with open(page_url_or_filepath, 'r', encoding=self.encoding_type) as f: page_html = f.read()

        # The string is already in the format we want
        else: page_html = page_url_or_filepath

        # Parse the page HTML using BeautifulSoup
        from bs4 import BeautifulSoup as bs
        page_soup = bs(page_html, 'html.parser')

        # If verbose output is enabled, print the page URL or filepath
        if verbose: print(f'Getting soup object for: {page_url_or_filepath}')

        # Return the page soup object
        return page_soup
    
    
    def get_page_tables(self, tables_url_or_filepath, verbose=True):
        """
        Retrieves tables from a given URL or file path and returns a list of DataFrames.
    
        Parameters:
            tables_url_or_filepath (str): The URL or file path of the page containing tables.
            verbose (bool, optional): If True, print summary information about the retrieved tables, sorted by size. Default is True.
    
        Returns:
            List[pandas.DataFrame]: A list of DataFrames containing tables from the specified source.
        
        Example:
            
            # Import necessary libraries and modules
            import sys
            sys.path.insert(1, '../py')  # Add the '../py' directory to the system path
            from notebook_utils import NotebookUtilities
            import os.path as osp
            
            # Create a NotebookUtilities instance with a specified data folder path
            nu = NotebookUtilities(
                data_folder_path=osp.abspath('../data'),
                saves_folder_path=osp.abspath('../saves')
            )
            
            # Example usage of the function
            tables_url = 'https://en.wikipedia.org/wiki/Provinces_of_Afghanistan'
            page_tables_list = nu.get_page_tables(tables_url)
            
        """
    
        # Check if the input is a URL or a filepath
        if self.url_regex.fullmatch(tables_url_or_filepath) or self.filepath_regex.fullmatch(tables_url_or_filepath):
            
            # If it's a filepath, check if the file exists
            if self.filepath_regex.fullmatch(tables_url_or_filepath): assert osp.isfile(tables_url_or_filepath), f"{tables_url_or_filepath} doesn't exist"
    
            # Read tables from the URL or file path
            tables_df_list = read_html(tables_url_or_filepath)
        else:
            
            # If it's not a URL or a filepath, assume it's a string representation of the tables
            from io import StringIO
    
            # Create a StringIO object from the string
            f = StringIO(tables_url_or_filepath)
    
            # Read the tables from the StringIO object using pandas.read_html()
            tables_df_list = read_html(f)
    
        # Print a summary of the tables if verbose is True
        if verbose:
            print(sorted([(i, df.shape) for (i, df) in enumerate(tables_df_list)],
                          key=lambda x: x[1][0]*x[1][1], reverse=True))

        # Return the list of pandas DataFrames containing the tables
        return tables_df_list
    
    
    def get_wiki_tables(self, tables_url_or_filepath, verbose=True):
        """
        Gets a list of DataFrames from Wikipedia tables.

        Parameters:
            tables_url_or_filepath: The URL or filepath to the Wikipedia page containing the tables.
            verbose: Whether to print verbose output.

        Returns:
            A list of DataFrames containing the data from the Wikipedia tables.

        Raises:
            Exception: If there is an error getting the Wikipedia page or the tables from the page.
        """
        table_dfs_list = []
        try:
            
            # Get the BeautifulSoup object for the Wikipedia page
            page_soup = self.get_page_soup(tables_url_or_filepath, verbose=verbose)
            
            # Find all the tables on the Wikipedia page
            table_soups_list = page_soup.find_all('table', attrs={'class': 'wikitable'})
            
            # Recursively get the DataFrames for all the tables on the Wikipedia page
            table_dfs_list = []
            for table_soup in table_soups_list: table_dfs_list += self.get_page_tables(str(table_soup), verbose=False)

            # If verbose is True, print a sorted list of the tables by their number of rows and columns
            if verbose: print(sorted([(i, df.shape) for (i, df) in enumerate(table_dfs_list)], key=lambda x: x[1][0]*x[1][1], reverse=True))

        except Exception as e:

            # If there is an error, print the error message
            if verbose: print(str(e).strip())

            # Recursively get the DataFrames for the tables on the Wikipedia page again, but with verbose=False
            table_dfs_list = self.get_page_tables(tables_url_or_filepath, verbose=False)

        # Return the list of DataFrames
        return table_dfs_list
    
    
    ### Pandas Functions ###
    
    
    @staticmethod
    def get_inf_nan_mask(x_list, y_list):
        """
        Returns a mask indicating which elements of x_list and y_list are not inf or nan.
        
        Parameters:
        x_list: A list of numbers.
        y_list: A list of numbers.
        
        Returns:
        A numpy array of booleans, where True indicates that the corresponding element
        of x_list and y_list is not inf or nan.
        """
        
        # Check if the input lists are empty.
        if not x_list or not y_list: return np.array([], dtype=bool)
        
        # Create masks indicating which elements of x_list and y_list are not inf or nan.
        x_mask = np.logical_and(np.logical_not(np.isinf(x_list)), np.logical_not(np.isnan(x_list)))
        y_mask = np.logical_and(np.logical_not(np.isinf(y_list)), np.logical_not(np.isnan(y_list)))
        
        # Return a mask indicating which elements of both x_list and y_list are not inf or nan.
        return np.logical_and(x_mask, y_mask)
    
    
    @staticmethod
    def get_column_descriptions(df, column_list=None, verbose=False):
        """
        Generate a DataFrame containing descriptive statistics for specified columns in a given DataFrame.
        
        Parameters:
            df (pandas.DataFrame): The DataFrame to analyze.
            column_list (list of str, optional): A list of specific columns to analyze.
                If None, all columns will be analyzed. Defaults to None.
            verbose (bool, optional): If True, display intermediate steps for debugging. Default is False.
        
        Returns:
            pandas.DataFrame: A DataFrame containing the descriptive statistics of the analyzed columns.
        """
        
        # If column_list is not provided, use all columns in the DataFrame
        if column_list is None: column_list = df.columns
        
        # Convert the CategoricalDtype instances to their string representations, and then group by those strings
        grouped_columns = df.columns.to_series().groupby(df.dtypes.astype(str)).groups
        
        # Initialize an empty list to store the descriptive statistics rows
        rows_list = []
        
        # Iterate over each data type and its corresponding column list
        for dtype, dtype_column_list in grouped_columns.items():
            for column_name in dtype_column_list:
                
                # Check if the column is in the specified column list
                if column_name in column_list:
                    
                    # Create a boolean mask for null values in the column
                    null_mask_series = df[column_name].isnull()
                    
                    # Dictionary to store column description
                    row_dict = {
                        'column_name': column_name,
                        'dtype': str(dtype),
                        'count_blanks': df[column_name].isnull().sum()
                    }
                    
                    # Count unique values in the column
                    try: row_dict['count_uniques'] = len(df[column_name].unique())
                        
                    # Set count of unique values to NaN if an error occurs
                    except Exception: row_dict['count_uniques'] = np.nan
                    
                    # Count the number of zeros
                    try: row_dict['count_zeroes'] = int((df[column_name] == 0).sum())
                    
                    # Set count of zeros to NaN if an error occurs
                    except Exception: row_dict['count_zeroes'] = np.nan
                    
                    # Check if the column contains any dates
                    date_series = pd.to_datetime(df[column_name], errors='coerce')
                    null_series = date_series[~date_series.notnull()]
                    row_dict['has_dates'] = (null_series.shape[0] < date_series.shape[0])
                    
                    # Find the minimum value
                    try: row_dict['min_value'] = df[~null_mask_series][column_name].min()
                    
                    # Set minimum value to NaN if an error occurs
                    except Exception: row_dict['min_value'] = np.nan
                    
                    # Find the maximum value
                    try: row_dict['max_value'] = df[~null_mask_series][column_name].max()
                    
                    # Set maximum value to NaN if an error occurs
                    except Exception: row_dict['max_value'] = np.nan
                    
                    # Check if the column contains only integers
                    try: row_dict['only_integers'] = (df[column_name].apply(lambda x: float(x).is_integer())).all()
                    
                    # Set only_integers to NaN if an error occurs
                    except Exception: row_dict['only_integers'] = float('nan')
    
                    # Append the row dictionary to the rows list
                    rows_list.append(row_dict)
    
        # Define column order for the resulting DataFrame
        columns_list = [
            'column_name', 'dtype', 'count_blanks', 'count_uniques', 'count_zeroes', 'has_dates', 'min_value', 'max_value', 'only_integers'
        ]

        # Create a data frame from the list of dictionaries
        blank_ranking_df = DataFrame(rows_list, columns=columns_list)
        
        # Return the data frame containing the descriptive statistics
        return blank_ranking_df
    
    
    @staticmethod
    def get_statistics(describable_df, columns_list):
        """
        Calculates and presents descriptive statistics for a given DataFrame's columns.
    
        Parameters:
            describable_df (pandas.DataFrame): The DataFrame to calculate descriptive statistics for.
            columns_list (list of str): A list of specific columns to calculate statistics for.
    
        Returns:
            pandas.DataFrame: A DataFrame containing the descriptive statistics for the analyzed columns.
        """
    
        # Compute basic descriptive statistics for the specified columns
        df = describable_df[columns_list].describe().rename(index={'std': 'SD'})
        
        # If the mode is not already included in the statistics, calculate it
        if ('mode' not in df.index):
            
            # Create the mode row dictionary
            row_dict = {cn: describable_df[cn].mode().tolist()[0] for cn in columns_list}
            
            # Convert the row dictionary to a data frame to match the df structure
            row_df = DataFrame([row_dict], index=['mode'])
            
            # Append the row data frame to the df data frame
            df = concat([df, row_df], axis='index', ignore_index=False)
        
        # If the median is not already included in the statistics, calculate it
        if ('median' not in df.index):
            
            # Create the median row dictionary
            row_dict = {cn: describable_df[cn].median() for cn in columns_list}
            
            # Convert the row dictionary to a data frame to match the df structure
            row_df = DataFrame([row_dict], index=['median'])
            
            # Append the row data frame to the df data frame
            df = concat([df, row_df], axis='index', ignore_index=False)
        
        # Define the desired index order for the resulting DataFrame
        index_list = ['mean', 'mode', 'median', 'SD', 'min', '25%', '50%', '75%', 'max']
    
        # Create a boolean mask to select rows with desired index values
        mask_series = df.index.isin(index_list)
        df = df[mask_series].reindex(index_list)
        
        # Return the filtered DataFrame containing the selected statistics
        return df
    
    
    @staticmethod
    def modalize_columns(df, columns_list, new_column):
        """
        Create a new column in a DataFrame representing the modal value of specified columns.
        
        Parameters:
            df (pandas.DataFrame): The input DataFrame.
            columns_list (list): The list of column names from which to calculate the modal value.
            new_column (str): The name of the new column to create.
        
        Returns:
            pandas.DataFrame: The modified DataFrame with the new column representing the modal value.
        """
        
        # Ensure that all columns are in the data frame
        columns_list = list(set(df.columns).intersection(set(columns_list)))
        
        # Create a mask series indicating rows with unique values across the specified columns
        mask_series = (df[columns_list].apply(Series.nunique, axis='columns') == 1)
        
        # Replace non-unique or missing values with NaN
        df.loc[~mask_series, new_column] = np.nan
        
        # Define a function to extract the first valid value in each row
        f = lambda srs: srs[srs.first_valid_index()]
        
        # For rows with identical values in specified columns, set the new column to the modal value
        df.loc[mask_series, new_column] = df[mask_series][columns_list].apply(f, axis='columns')
    
        return df
    
    
    @staticmethod
    def get_regexed_columns(df, search_regex=None, verbose=False):
        """
        Identify columns in a DataFrame that contain references based on a specified regex pattern.
        
        Parameters:
            df (pd.DataFrame): The input DataFrame.
            search_regex (re.Pattern, optional): The compiled regular expression pattern for identifying references.
                If None, a default regex pattern is used to match names followed by '_Root'.
            verbose (bool, optional): If True, print additional information during processing. Default is False.
        
        Returns:
            list: A list of column names that contain references based on the specified regex pattern.
        """
        
        # Ensure that the search_regex is a compiled regular expression object
        assert (
            isinstance(search_regex, re.Pattern)
        ), "search_regex must be a compiled regular expression."
        
        # If no search_regex is provided, use the default pattern for detecting references
        if search_regex is None:
            search_regex = re.compile(
                '(Mike|Gary|Helga|Bob|Gloria|Lily)(_(0|1|2|3|4|5|6|7|8|9|10))? Root'
            )
        
        # Print the type of the search_regex if verbose mode is enabled
        if verbose: print(type(search_regex))
        
        # Apply the search_regex to each element in the DataFrame and count occurrences for each column
        srs = df.applymap(
            lambda x: bool(search_regex.search(str(x))), na_action='ignore'
        ).sum()
        
        # Extract column names where the count of occurrences is not zero
        columns_list = srs[srs != 0].index.tolist()
        
        return columns_list
    
    
    @staticmethod
    def get_regexed_dataframe(filterable_df, columns_list, search_regex=None, verbose=False):
        """
        Create a DataFrame that displays an example of what search_regex is finding for each column in columns_list.
        
        Parameters:
            filterable_df (pandas.DataFrame): The input DataFrame to filter.
            columns_list (list of str): The list of column names to investigate for matches.
            search_regex (re.Pattern, optional): The compiled regular expression pattern for identifying matches.
                If None, the default pattern for detecting references will be used.
            verbose (bool, optional): If True, print additional information during processing. Default is False.
        
        Returns:
            pandas.DataFrame: A DataFrame containing an example row for each column in columns_list that matches the regex pattern.
        """
        
        # Ensure that all column names in columns_list are in the filterable_df.columns
        assert all(
            map(lambda cn: cn in filterable_df.columns, columns_list)
        ), "Column names in columns_list must be in filterable_df.columns"
        
        # Set default pattern for detecting references if not provided
        if search_regex is None:
            search_regex = re.compile(
                '(Mike|Gary|Helga|Bob|Gloria|Lily)(_(0|1|2|3|4|5|6|7|8|9|10))? Root'
            )
        
        # Print the debug info if verbose is True
        if verbose: print(type(search_regex))
        
        # Create an empty DataFrame to store the filtered rows
        filtered_df = DataFrame([])
        
        # For each column in columns_list, filter the filterable df and extract the first row that matches the search_regex
        for cn in columns_list:
            
            # Create a mask to filter rows where the column matches the regex pattern
            mask_series = filterable_df[cn].map(
                lambda x: bool(search_regex.search(str(x)))
            )
            
            # Concatenate the first matching row not already in the result data frame
            df = filterable_df[mask_series]
            mask_series = ~df.index.isin(filtered_df.index)
            if mask_series.any(): filtered_df = concat([filtered_df, df[mask_series].iloc[0:1]], axis='index')
        
        return filtered_df
    
    
    @staticmethod
    def convert_to_df(row_index, row_series, verbose=True):
        """
        Convert a row represented as a Pandas Series into a single-row DataFrame.
        
        Parameters:
            row_index (int): The index to be assigned to the new DataFrame row.
            row_series (pandas.Series): The Pandas Series representing the row's data.
            verbose (bool, optional): Whether to print debug info. Default is True.
        
        Returns:
            pandas.DataFrame: A single-row DataFrame containing the data from the input Pandas Series.
        """
        
        # Print the type of row_index if verbose is True and it is not an integer
        if verbose and (type(row_index) != int): print(type(row_index))
        
        # Create a new DataFrame with the data from the input Pandas Series and the specified index
        df = DataFrame(data=row_series.to_dict(), index=[row_index])
        
        return df
    
    
    def get_row_dictionary(self, value_obj, row_dict={}, key_prefix=''):
        """
        This function takes a value_obj (either a dictionary, list or scalar value) and creates a flattened
        dictionary from it, where keys are made up of the keys/indices of nested dictionaries and lists. The
        keys are constructed with a key_prefix (which is updated as the function traverses the value_obj) to
        ensure uniqueness. The flattened dictionary is stored in the row_dict argument, which is updated at
        each step of the function.
        
        Parameters:
            value_obj (dict, list, scalar value): The object to be flattened into a dictionary.
            row_dict (dict, optional): The dictionary to store the flattened object.
            key_prefix (str, optional): The prefix for constructing the keys in the row_dict.
        
        Returns:
            row_dict (dict): The flattened dictionary representation of the value_obj.
        """
        
        # Check if the value is a dictionary
        if isinstance(value_obj, dict):
            
            # Iterate through the dictionary 
            for k, v, in value_obj.items():
                
                # Recursively call get row dictionary with the dictionary key as part of the prefix
                row_dict = self.get_row_dictionary(
                    v, row_dict=row_dict, key_prefix=f'{key_prefix}_{k}'
                )
                
        # Check if the value is a list
        elif isinstance(value_obj, list):
            
            # Get the minimum number of digits in the list length
            list_length = len(value_obj)
            digits_count = min(len(str(list_length)), 2)
            
            # Iterate through the list
            for i, v in enumerate(value_obj):
                
                # Add leading zeros to the index
                if (i == 0) and (list_length == 1):
                    i = ''
                else:
                    i = str(i).zfill(digits_count)
                
                # Recursively call get row dictionary with the list index as part of the prefix
                row_dict = self.get_row_dictionary(
                    v, row_dict=row_dict, key_prefix=f'{key_prefix}{i}'
                )
                
        # If value is neither a dictionary nor a list
        else:
            
            # Add the value to the row dictionary
            if key_prefix.startswith('_') and (key_prefix[1:] not in row_dict):
                key_prefix = key_prefix[1:]
            row_dict[key_prefix] = value_obj
        
        return row_dict
    
    
    def show_time_statistics(self, describable_df, columns_list):
        """
        Display time-related statistics for specified columns in a DataFrame.
        
        Parameters:
            describable_df (pandas.DataFrame): The DataFrame to calculate descriptive statistics for.
            columns_list (list of str): A list of specific time-related columns to calculate statistics for.
    
        Returns:
            pandas.DataFrame: A DataFrame containing the descriptive statistics for the analyzed time-related columns.
        """
        
        # Get time-related statistics using the get_statistics method
        df = self.get_statistics(describable_df, columns_list)

        # Apply a formatting function to convert milliseconds to a formatted timedelta for all elements in the DataFrame
        df = df.applymap(lambda x: self.format_timedelta(timedelta(milliseconds=int(x))), na_action='ignore').T

        # Format the standard deviation (SD) column to include the '±' symbol
        df.SD = df.SD.map(lambda x: '±' + str(x))
        
        # Display the resulting DataFrame
        display(df)
    
    
    ### 3D Point Functions ###
    
    
    @staticmethod
    def get_coordinates(second_point, first_point=None):
        """
        Get the coordinates of two 3D points.
        
        Parameters:
            second_point (str): The coordinates of the second point as a string.
            first_point (str, optional): The coordinates of the first point as a string. If not provided, the
                default values (0, 0, 0) will be used.
        
        Returns:
            tuple of float: The coordinates of the two points.
        
        """
        if first_point is None:
            x1 = 0.0  # The x-coordinate of the first point
            y1 = 0.0  # The y-coordinate of the first point
            z1 = 0.0  # The z-coordinate of the first point
        else:
            location_tuple = eval(first_point)
            x1 = location_tuple[0]  # The x-coordinate of the first point
            y1 = location_tuple[1]  # The y-coordinate of the first point
            z1 = location_tuple[2]  # The z-coordinate of the first point
        location_tuple = eval(second_point)
        x2 = location_tuple[0]  # The x-coordinate of the second point
        y2 = location_tuple[1]  # The y-coordinate of the second point
        z2 = location_tuple[2]  # The z-coordinate of the second point
    
        return x1, x2, y1, y2, z1, z2
    
    
    def get_euclidean_distance(self, second_point, first_point=None):
        """
        Calculates the Euclidean distance between two 3D points.
    
        Returns:
            float: The Euclidean distance between the two points.
        """
        x1, x2, y1, y2, z1, z2 = self.get_coordinates(second_point, first_point=first_point)
        import math
        euclidean_distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)
    
        return euclidean_distance
    
    
    def get_absolute_position(self, second_point, first_point=None):
        """
        Calculates the absolute position of a point relative to another point.
        
        Parameters:
            second_point (tuple): The coordinates of the second point.
            first_point (tuple, optional): The coordinates of the first point. If not specified,
                the origin is retrieved from get_coordinates.
        
        Returns:
            tuple: The absolute coordinates of the second point.
        """
        x1, x2, y1, y2, z1, z2 = self.get_coordinates(second_point, first_point=first_point)
    
        return (round(x1 + x2, 1), round(y1 + y2, 1), round(z1 + z2, 1))
    
    
    ### Sub-sampling Functions ###
    
    
    @staticmethod
    def get_minority_combinations(sample_df, groupby_columns):
        """
        Get the minority combinations of a DataFrame.
        
        Parameters:
            sample_df: A Pandas DataFrame.
            groupby_columns: A list of column names to group by.
        
        Returns:
            A Pandas DataFrame containing a single sample row of each of the four smallest groups.
        """
        df = DataFrame([], columns=sample_df.columns)
        for bool_tuple in sample_df.groupby(groupby_columns).size().sort_values().index.tolist()[:4]:
            
            # Filter the name in the column to the corresponding value of the tuple
            mask_series = True
            for cn, cv in zip(groupby_columns, bool_tuple): mask_series &= (sample_df[cn] == cv)
            
            # Append a single record from the filtered data frame
            if mask_series.any(): df = concat([df, sample_df[mask_series].sample(1)], axis='index')
        
        return df
    
    
    @staticmethod
    def get_random_subdictionary(super_dict, n=5):
        """
        Extracts a random subdictionary with a specified number of key-value pairs from a given superdictionary.
        
        Parameters:
            super_dict (dict): The dictionary from which to extract a random subdictionary.
            n (int, optional): The number of key-value pairs to include in the sub-dictionary. Defaults to 5.
        
        Returns:
            dict: A random subdictionary with n key-value pairs from the superdictionary.
        """
        
        # Convert the dictionary's keys into a list
        keys = list(super_dict.keys())
        
        # Import the random module
        import random
        
        # Select a random sample of n keys from the list of keys
        random_keys = random.sample(keys, n)
        
        # Create an empty dictionary to store the sub-dictionary
        sub_dict = {}
        
        # Iterate over the randomly selected keys and add their corresponding values to the sub-dictionary
        for key in random_keys: sub_dict[key] = super_dict[key]
            
        return sub_dict
    
    
    ### Plotting Functions ###
    
    
    @staticmethod
    def get_color_cycler(n):
        """
        Generate a color cycler for plotting with a specified number of colors.
        
        Parameters:
            n (int): The number of colors to include in the cycler.
        
        Returns:
            cycler.Cycler: A color cycler object containing the specified number of colors.
        
        Example:
            color_cycler = nu.get_color_cycler(len(possible_cause_list))
            for possible_cause, face_color_dict in zip(possible_cause_list, color_cycler()):
                face_color = face_color_dict['color']
        """
        
        # Initialize an empty color cycler object
        color_cycler = None
        
        # Import the `cycler` module from matplotlib
        from cycler import cycler
        
        # Choose a color map based on the number of colors needed
        if n < 9: color_cycler = cycler('color', plt.cm.Accent(np.linspace(0, 1, n)))
        elif n < 11: color_cycler = cycler('color', plt.cm.tab10(np.linspace(0, 1, n)))
        elif n < 13: color_cycler = cycler('color', plt.cm.Paired(np.linspace(0, 1, n)))
        else: color_cycler = cycler('color', plt.cm.tab20(np.linspace(0, 1, n)))
        
        return color_cycler
    
    
    @staticmethod
    def plot_line_with_error_bars(df, xname, xlabel, xtick_text_fn, yname, ylabel, ytick_text_fn, title):
        """
        Creates a line plot with error bars to visualize the mean and standard deviation of a numerical variable
        grouped by another categorical variable.
        
        Parameters:
            df (pandas.DataFrame): The input DataFrame containing the data to plot.
            xname (str): The name of the categorical variable to group by and for the x-axis values.
            xlabel (str): The label for the x-axis.
            xtick_text_fn (function): A function to humanize x-axis tick labels.
            yname (str): The column name for the y-axis values.
            ylabel (str): The label for the y-axis.
            ytick_text_fn (function): A function to humanize y-axis tick labels.
            title (str): The title of the plot.
        
        Returns:
            None: The function plots the graph directly using matplotlib.
        """
        
        # Drop rows with NaN values, group by xname, and calculate mean and standard deviation
        groupby_list = [xname]
        columns_list = [xname, yname]
        aggs_list = ['mean', 'std']
        df = df.dropna(subset=columns_list).groupby(groupby_list)[yname].agg(aggs_list).reset_index()
        
        # Create the figure and subplot
        fig, ax = plt.subplots(figsize=(18, 9))
        
        # Plot the line with error bars
        ax.errorbar(
            x=df[xname],
            y=df['mean'],
            yerr=df['std'],
            label=ylabel,
            fmt='-o',  # Line style with markers
        )
        
        # Set plot title and labels
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        
        # Humanize x-axis tick labels
        xticklabels_list = []
        for text_obj in ax.get_xticklabels():
            text_obj.set_text(xtick_text_fn(text_obj))
            xticklabels_list.append(text_obj)
        ax.set_xticklabels(xticklabels_list)
        
        # Humanize y-axis tick labels
        yticklabels_list = []
        for text_obj in ax.get_yticklabels():
            text_obj.set_text(ytick_text_fn(text_obj))
            yticklabels_list.append(text_obj)
        ax.set_yticklabels(yticklabels_list);
    
    
    @staticmethod
    def plot_histogram(df, xname, xlabel, xtick_text_fn, title, ylabel=None, xticks_are_temporal=False, ax=None, color=None, bins=100):
        """
        Plots a histogram of a DataFrame column.
        
        Parameters:
            df: A Pandas DataFrame.
            xname: The name of the column to plot the histogram of.
            xlabel: The label for the x-axis.
            xtick_text_fn: A function that takes a text object as input and returns a new
            text object to be used as the tick label.
            title: The title of the plot.
            ylabel: The label for the y-axis.
            ax: A matplotlib axis object. If None, a new figure and axis will be created.
        
        Returns:
            A matplotlib axis object.
        """
        
        # Create the figure and subplot
        if ax is None: fig, ax = plt.subplots(figsize=(18, 9))
        
        # Plot the histogram with centered bars
        df[xname].hist(ax=ax, bins=bins, align='mid', edgecolor='black', color=color)
        
        # Set the grid, title and labels
        plt.grid(False)
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        if ylabel is None: ylabel = 'Count of Instances in Bin'
        ax.set_ylabel(ylabel)

        if xticks_are_temporal:
        
            # Set the minor x-axis tick labels to every 30 seconds
            thirty_seconds = 1_000 * 30
            minor_ticks = np.arange(0, df[xname].max() + thirty_seconds, thirty_seconds)
            ax.set_xticks(minor_ticks, minor=True)
            
            # Set the major x-axis tick labels to every 5 minutes
            if (len(minor_ticks) > 84):
                five_minutes = 1_000 * 60 * 5
                major_ticks = np.arange(0, df[xname].max() + five_minutes, five_minutes)
                ax.set_xticks(major_ticks)
            
            # Set the major x-axis tick labels to every 60 seconds
            else:
                sixty_seconds = 1_000 * 60
                major_ticks = np.arange(0, df[xname].max() + sixty_seconds, sixty_seconds)
                ax.set_xticks(major_ticks)
        
        # Humanize x tick labels
        xticklabels_list = []
        for text_obj in ax.get_xticklabels():
            
            # Call the xtick text function to convert numerical values into minutes and seconds format
            text_obj.set_text(xtick_text_fn(text_obj))
            
            xticklabels_list.append(text_obj)
        # print(len(xticklabels_list))
        if (len(xticklabels_list) > 17): ax.set_xticklabels(xticklabels_list, rotation=90)
        else: ax.set_xticklabels(xticklabels_list)
        
        # Humanize y tick labels
        yticklabels_list = []
        for text_obj in ax.get_yticklabels():
            text_obj.set_text(humanize.intword(int(text_obj.get_position()[1])))
            yticklabels_list.append(text_obj)
        ax.set_yticklabels(yticklabels_list)
        
        return ax
    
    
    @staticmethod
    def plot_grouped_box_and_whiskers(
        transformable_df,
        x_column_name,
        y_column_name,
        x_label,
        y_label,
        transformer_name='min',
        is_y_temporal=True
    ):    
        """
        Creates a grouped box plot visualization to compare the distribution of a numerical variable across different groups.
        
        Parameters:
            transformable_df (pandas.DataFrame): DataFrame containing the data to be plotted.
            x_column_name (str): The name of the categorical variable to group by and column name for the x-axis.
            y_column_name (str): Column name for the y-axis.
            x_label (str): Label for the x-axis.
            y_label (str): Label for the y-axis.
            transformer_name (str, optional): Name of the transformation applied to the y-axis values before plotting (default: 'min').
            is_y_temporal (bool, optional): If True, y-axis labels will be formatted as temporal values (default: True).
        
        Returns:
            None: The function plots the graph directly using seaborn and matplotlib.
        """
        import seaborn as sns
        
        # Get the transformed data frame
        if transformer_name is None: transformed_df = transformable_df
        else:
            groupby_columns = ['session_uuid', 'scene_index']
            transformed_df = (
                transformable_df.groupby(groupby_columns)
                .filter(lambda df: not df[y_column_name].isnull().any())
                .groupby(groupby_columns)
                .transform(transformer_name)
                .reset_index(drop=False)
                .sort_values(y_column_name)
            )
        
        # Create a figure and subplots
        fig, ax = plt.subplots(1, 1, figsize=(9, 9))
        
        # Create a box plot of the y column grouped by the x column
        sns.boxplot(
            x=x_column_name,
            y=y_column_name,
            showmeans=True,
            data=transformed_df,
            ax=ax
        )
        
        # Rotate the x-axis labels to prevent overlapping
        plt.xticks(rotation=45)
        
        # Label the x- and y-axis
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
        
        # Humanize y tick labels
        if is_y_temporal:
            yticklabels_list = []
            for text_obj in ax.get_yticklabels():
                text_obj.set_text(
                    humanize.precisedelta(
                        timedelta(milliseconds=text_obj.get_position()[1])
                    )
                    .replace(', ', ',\n')
                    .replace(' and ', ' and\n')
                )
                yticklabels_list.append(text_obj)
            ax.set_yticklabels(yticklabels_list)
        
        plt.show()
    
    
    def first_order_linear_scatterplot(
        self, df, xname, yname, xlabel_str='Overall Capitalism (explanatory variable)',
        ylabel_str='World Bank Gini % (response variable)',
        x_adj='capitalist', y_adj='unequal', title='"Wealth inequality is huge in the capitalist societies"',
        idx_reference='United States',
        annot_reference='most evil', aspect_ratio=None, least_x_xytext=(40, -10), most_x_xytext=(-150, 55),
        least_y_xytext=(-200, -10),
        most_y_xytext=(45, 0), reference_xytext=(-75, 25), color_list=None
    ):
        """
        Create a first-order (linear) scatter plot assuming the data frame
        has an index labeled with strings.
        
        Parameters:
            df (pandas.DataFrame): The data frame to be plotted.
            xname (str): The name of the x-axis variable.
            yname (str): The name of the y-axis variable.
            xlabel_str (str, optional): The label for the x-axis. Defaults to
                'Overall Capitalism (explanatory variable)'.
            ylabel_str (str, optional): The label for the y-axis. Defaults to
                'World Bank Gini % (response variable)'.
            x_adj (str, optional): The adjective to use for the x-axis variable in the annotations.
                Default is 'capitalist'.
            y_adj (str, optional): The adjective to use for the y-axis variable in the annotations.
                Default is 'unequal'.
            title (str, optional): The title of the plot. Defaults to
                'Wealth inequality is huge in the capitalist societies'.
            idx_reference (str, optional): The index of the data point to be used as the reference point for
                the annotations. Default is 'United States'.
            annot_reference (str, optional): The reference text to be used for the annotation of the
                reference point. Default is 'most evil'.
            aspect_ratio (float, optional): The aspect ratio of the plot. Default is the Facebook aspect
                ratio (1.91).
            least_x_xytext (tuple[float, float], optional): The xytext position for the annotation of the
                least x-value data point. Default is (40, -10).
            most_x_xytext (tuple[float, float], optional): The xytext position for the annotation of the
                most x-value data point. Default is (-150, 55).
            least_y_xytext (tuple[float, float], optional): The xytext position for the annotation of
                the least y-value data point. Default is (-200, -10).
            most_y_xytext (tuple[float, float], optional): The xytext position for the annotation of the
                most y-value data point. Default is (45, 0).
            reference_xytext (tuple[float, float], optional): The xytext position for the annotation of
                the reference point. Default is (-75, 25).
            color_list (list[str], optional): The list of colors to be used for the scatter plot.
                Default is None, which will use a default color scheme.
        
        Returns:
            figure(matplotlib.figure.Figure): The figure object for the generated scatter plot.
        """
    
        if aspect_ratio is None: aspect_ratio = self.facebook_aspect_ratio
        fig_width = 18
        fig_height = fig_width / aspect_ratio
        fig = plt.figure(figsize=(fig_width, fig_height))
        ax = fig.add_subplot(111, autoscale_on=True)
        line_kws = dict(color='k', zorder=1, alpha=.25)
    
        if color_list is None: scatter_kws = dict(s=30, lw=.5, edgecolors='k', zorder=2)
        else: scatter_kws = dict(s=30, lw=.5, edgecolors='k', zorder=2, color=color_list)
    
        import seaborn as sns
        merge_axes_subplot = sns.regplot(x=xname, y=yname, scatter=True, data=df, ax=ax,
                                         scatter_kws=scatter_kws, line_kws=line_kws)
    
        if not xlabel_str.endswith(' (explanatory variable)'): xlabel_str = f'{xlabel_str} (explanatory variable)'
        xlabel_text = plt.xlabel(xlabel_str)
    
        if not ylabel_str.endswith(' (response variable)'): ylabel_str = f'{ylabel_str} (response variable)'
        ylabel_text = plt.ylabel(ylabel_str)
    
        kwargs = dict(textcoords='offset points', ha='left', va='bottom',
                      bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5),
                      arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))
        
        xdata = df[xname].values
        least_x = xdata.min()
        most_x = xdata.max()
        
        ydata = df[yname].values
        most_y = ydata.max()
        least_y = ydata.min()
        
        least_x_tried = most_x_tried = least_y_tried = most_y_tried = False
    
        for label, x, y in zip(df.index, xdata, ydata):
            if (x == least_x) and not least_x_tried:
                annotation = plt.annotate('{} (least {})'.format(label, x_adj),
                                          xy=(x, y), xytext=least_x_xytext, **kwargs)
                least_x_tried = True
            elif (x == most_x) and not most_x_tried:
                annotation = plt.annotate('{} (most {})'.format(label, x_adj),
                                          xy=(x, y), xytext=most_x_xytext, **kwargs)
                most_x_tried = True
            elif (y == least_y) and not least_y_tried:
                annotation = plt.annotate('{} (least {})'.format(label, y_adj),
                                          xy=(x, y), xytext=least_y_xytext, **kwargs)
                least_y_tried = True
            elif (y == most_y) and not most_y_tried:
                annotation = plt.annotate('{} (most {})'.format(label, y_adj),
                                          xy=(x, y), xytext=most_y_xytext, **kwargs)
                most_y_tried = True
            elif (label == idx_reference):
                annotation = plt.annotate('{} ({})'.format(label, annot_reference),
                                          xy=(x, y), xytext=reference_xytext, **kwargs)
    
        title_obj = fig.suptitle(t=title, x=0.5, y=0.91)
        
        # Get r squared value
        inf_nan_mask = self.get_inf_nan_mask(xdata.tolist(), ydata.tolist())
        from scipy.stats import pearsonr
        pearsonr_tuple = pearsonr(xdata[inf_nan_mask], ydata[inf_nan_mask])
        pearson_r = pearsonr_tuple[0]
        pearsonr_statement = str('%.2f' % pearson_r)
        coefficient_of_determination_statement = str('%.2f' % pearson_r**2)
        p_value = pearsonr_tuple[1]
    
        if p_value < 0.0001: pvalue_statement = '<0.0001'
        else: pvalue_statement = '=' + str('%.4f' % p_value)
    
        s_str = r'$r^2=' + coefficient_of_determination_statement + ',\ p' + pvalue_statement + '$'
        text_tuple = ax.text(0.75, 0.9, s_str, alpha=0.5, transform=ax.transAxes, fontsize='x-large')
        
        return fig
    
    
    def plot_inauguration_age(
        self,
        inauguration_df,
        groupby_column_name,
        xname,
        leader_designation,
        label_infix,
        label_suffix,
        info_df,
        title_prefix,
        inaugruation_verb='Inauguration',
        legend_tuple=None,
        verbose=False
    ):
        """
        Plot a scatter plot of leaders' ages at inauguration over time, with optional groupings and background shading.
        
        Parameters:
            inauguration_df (pandas.DataFrame): DataFrame containing leadership inauguration data.
            groupby_column_name (str): Column name for grouping leaders (e.g., country, party).
            xname (str): The name of the x-axis variable, representing the year of inauguration.
            leader_designation (str): The designation of the leaders, such as "President" or "Governor".
            label_infix (str): Text to be inserted in the label between leader designation and groupby_column.
            label_suffix (str): Text to be appended to the label.
            info_df (pandas.DataFrame): DataFrame containing additional information about turning years.
            title_prefix (str): A prefix to add to the plot title.
            inaugruation_verb (str, optional): The verb to use for inauguration, such as "inauguration" or "swearing-in". Defaults to "Inauguration".
            legend_tuple (tuple, optional): A tuple specifying the location of the legend, such as (0.02, 0.76). Defaults to None.
            verbose (bool, optional): Whether to print debug info. Defaults to False.
        
        Returns:
            None: The function plots the graph directly using matplotlib.
        """

        # Configure the color dictionary
        color_cycler = self.get_color_cycler(info_df[groupby_column_name].unique().shape[0])
        face_color_dict = {}
        for groupby_column, fc_dict in zip(
            info_df[groupby_column_name].unique(), color_cycler()
        ):
            face_color_dict[groupby_column] = fc_dict['color']
        
        # Plot and annotate the figure
        figwidth = 18
        fig, ax = plt.subplots(figsize=(figwidth, figwidth/self.twitter_aspect_ratio))
        used_list = []
        import textwrap
        for groupby_column, df in inauguration_df.sort_values('office_rank').groupby(
            groupby_column_name
        ):
            if groupby_column[0] in ['A', 'U']: ana = 'an'
            else: ana = 'a'
            label = f'{leader_designation.title()} {label_infix} {ana} {groupby_column} {label_suffix}'.strip()

            # Convert the array to a 2-D array with a single row
            reshape_tuple = (1, -1)
            color = face_color_dict[groupby_column].reshape(reshape_tuple)

            # Plot and annotate all points from the index
            for leader_name, row_series in df.iterrows():
                if groupby_column not in used_list:
                    used_list.append(groupby_column)
                    df.plot(
                        x=xname,
                        y='age_at_inauguration',
                        kind='scatter',
                        ax=ax,
                        label=label,
                        color=color
                    )
                else:
                    df.plot(
                        x=xname,
                        y='age_at_inauguration',
                        kind='scatter',
                        ax=ax,
                        color=color
                    )
                plt.annotate(
                    textwrap.fill(leader_name, width=10),
                    (row_series[xname], row_series.age_at_inauguration),
                    textcoords='offset points',
                    xytext=(0, -4),
                    ha='center',
                    va='top',
                    fontsize=6
                )

        # Add 5 years to the height
        bottom, top = ax.get_ylim()
        height_tuple = (bottom, top+5)
        ax.set_ylim(height_tuple)
        bottom, top = ax.get_ylim()
        height = top - bottom

        # Get the background shading width
        left, right = ax.get_xlim()
        min_shading_width = 9999
        min_turning_name = ''
        wrap_width = info_df.turning_name.map(lambda x: len(x)).min()
        for row_index, row_series in info_df.iterrows():
            turning_year_begin = max(row_series.turning_year_begin, left)
            turning_year_end = min(row_series.turning_year_end, right)
            width = turning_year_end - turning_year_begin
            if (width > 0) and (width < min_shading_width):
                min_shading_width = width
                min_turning_name = row_series.turning_name
                wrap_width = len(min_turning_name)

        # Add the turning names as background shading
        from matplotlib.patches import Rectangle
        for row_index, row_series in info_df.iterrows():
            turning_year_begin = max(row_series.turning_year_begin, left)
            turning_year_end = min(row_series.turning_year_end, right)
            width = turning_year_end - turning_year_begin
            if (width > 0):
                groupby_column = row_series[groupby_column_name]
                turning_name = row_series.turning_name
                rect = Rectangle(
                    (turning_year_begin, bottom), width, height, color=face_color_dict[groupby_column],
                    fill=True, edgecolor=None, alpha=0.1
                )
                ax.add_patch(rect)
                plt.annotate(
                    textwrap.fill(turning_name, width=wrap_width, break_long_words=False),
                    (turning_year_begin+(width/2), top), textcoords='offset points', xytext=(0, -6),
                    ha='center', fontsize=7, va='top', rotation=-90
                )
        
        # Set legend
        if legend_tuple is None: legend_tuple = (0.02, 0.76)
        legend_obj = ax.legend(loc=legend_tuple)
        if verbose:
            
            # Get the bounding box of the legend relative to the anchor point
            bbox_to_anchor = legend_obj.get_bbox_to_anchor()
            
            # Print the size and position of the bounding box
            print(bbox_to_anchor.width, bbox_to_anchor.height, bbox_to_anchor.xmin, bbox_to_anchor.ymin, bbox_to_anchor.xmax, bbox_to_anchor.ymax)
            
            # Get the bounding box of the legend
            bounding_box = legend_obj.get_tightbbox()
            
            # Print the size and position of the bounding box
            print(bounding_box.width, bounding_box.height, bounding_box.xmin, bounding_box.ymin, bounding_box.xmax, bounding_box.ymax)
        
        # Set labels
        ax.set_xlabel(f'Year of {inaugruation_verb}')
        ax.set_ylabel(f'Age at {inaugruation_verb}')
        text_obj = ax.set_title(f'{title_prefix} {inaugruation_verb} Age vs Year')
    
    
    def plot_sequence(self, sequence, highlighted_ngrams=[], color_dict=None, suptitle=None, first_element='SESSION_START', last_element='SESSION_END', alphabet_list=None, verbose=False):
        """
        Creates a standard sequence plot where each element corresponds to a position on the y-axis.
        The optional highlighted_ngrams parameter can be one or more n-grams to be outlined in a red box.
        
        Parameters:
            sequence: A list of strings or integers representing the sequence to plot.
            highlighted_ngrams: A list of n-grams to be outlined in a red box.
            color_dict: An optional dictionary whose keys are the alphabet list and whose values are
                        a single color format string to allow consistent visualization between calls.
            suptitle: An optional title for the plot.
            first_element: The element in alphabet_list that will be forced to the beginning if
                           already in the list. Defaults to SESSION_START.
            last_element: The element in alphabet_list that will be forced to the end if
                           already in the list. Defaults to SESSION_END.
            alphabet_list: A list of strings or integers representing the set of elements in sequence.
            verbose: A boolean indicating whether to print verbose output.
        
        Returns:
            A matplotlib figure object.
        """
    
        # Convert the sequence to a NumPy array
        np_sequence = np.array(sequence)
        
        # Get the unique characters in the sequence and potentially use them to set up the color dictionary
        if alphabet_list is None:
            if highlighted_ngrams and (type(highlighted_ngrams[0]) is list):
                alphabet_list = sorted(self.get_alphabet(sequence+[el for sublist in highlighted_ngrams for el in sublist]))
            else: alphabet_list = sorted(self.get_alphabet(sequence+highlighted_ngrams))
        if last_element in alphabet_list:
            alphabet_list.remove(last_element)
            alphabet_list.append(last_element)
        if first_element in alphabet_list: alphabet_list.insert(0, alphabet_list.pop(alphabet_list.index(first_element)))
        
        # Set up the color dictionary so that its keys consist of the elements in alphabet_list
        if color_dict is None: color_dict = {a: None for a in alphabet_list}
        else: color_dict = {a: color_dict.get(a) for a in alphabet_list}
        
        # Get the length of the alphabet
        alphabet_len = len(alphabet_list)
        
        # Convert the sequence to integers
        int_sequence, _ = self.convert_strings_to_integers(np_sequence, alphabet_list=alphabet_list)
        
        # Create a string-to-integer map
        if highlighted_ngrams and (type(highlighted_ngrams[0]) is list):
            _, string_to_integer_map = self.convert_strings_to_integers(sequence+[el for sublist in highlighted_ngrams for el in sublist], alphabet_list=alphabet_list)
        else: _, string_to_integer_map = self.convert_strings_to_integers(sequence+highlighted_ngrams, alphabet_list=alphabet_list)
        # if verbose: print(string_to_integer_map)
        
        # If the sequence is not already in integer format, convert it
        if (np_sequence.dtype.str not in ['<U21', '<U11']): int_sequence = np_sequence
        
        # Create a figure
        fig = plt.figure(figsize=[len(sequence)*0.3, alphabet_len * 0.3])
        
        # Force the xticks to land on integers only
        xtick_locations = range(len(sequence))
        xtick_labels = [n+1 for n in xtick_locations]
        plt.xticks(ticks=xtick_locations, labels=xtick_labels, minor=False)
        
        # Extend the edges of the plot
        plt.xlim([-0.5, len(sequence)-0.5])
        
        # Iterate over the alphabet and plot the points for each character
        for i, value in enumerate(alphabet_list):
            # if verbose: print(i, value)
            
            # Get the positions of the current character in the sequence
            points = np.where(np_sequence == value, i, np.nan)
            # if verbose: print(range(len(np_sequence)))
            # if verbose: print(points)
            
            # Plot the points
            plt.scatter(x=range(len(np_sequence)), y=points, marker='s', label=value, s=35, color=color_dict[value])
            # if verbose:
                # color_cycle = plt.rcParams['axes.prop_cycle']
                # print('\nPrinting the colors in the color cycle:')
                # for color in color_cycle: print(color)
                # print()
        
        # Set the yticks label values
        plt.yticks(range(alphabet_len), alphabet_list)
        
        # Match the label colors with the color cycle and color dictionary
        from itertools import cycle
        
        # Get the color cycle from rcParams
        prop_cycle = plt.rcParams['axes.prop_cycle']
        colors = cycle(prop_cycle.by_key()['color'])
        
        colors_list = []
        for key in alphabet_list:
            value = color_dict[key]
            
            # Get the next color in the cycle
            if (value is None):
                color = next(colors)
                colors_list.append(color)
            
            else: colors_list.append(value)
        # if verbose: print(f'colors_list = {colors_list}')
        
        # Set the yticks label color
        for label, color in zip(plt.gca().get_yticklabels(), colors_list): label.set_color(color)
        
        # Set the y limits
        plt.ylim(-1, alphabet_len)
        
        # Highlight any of the n-grams given
        if highlighted_ngrams != []:
            # if verbose: display(highlighted_ngrams)
            
            def highlight_ngram(ngram):
                
                # Get the length of the n-gram
                n = len(ngram)
                
                # Find all matches of the n-gram in the sequence
                match_positions = []
                for x in range(len(int_sequence) - n + 1):
                    this_ngram = list(int_sequence[x:x + n])
                    if str(this_ngram) == str(ngram): match_positions.append(x)
                
                # Draw a red box around each match
                # if verbose: print(f'ngram={ngram}, min(ngram)={min(ngram)}, max(ngram)={max(ngram)}, match_positions={match_positions}')
                for position in match_positions:
                    bot = min(ngram) - 0.25
                    top = max(ngram) + 0.25
                    left = position - 0.25
                    right = left + n - 0.5
                    if verbose: print(f'bot={bot}, top={top}, left={left}, right={right}')
                    
                    line_width = 1
                    plt.plot([left,right], [bot,bot], color='red', linewidth=line_width)
                    plt.plot([left,right], [top,top], color='red', linewidth=line_width)
                    plt.plot([left,left], [bot,top], color='red', linewidth=line_width)
                    plt.plot([right,right], [bot,top], color='red', linewidth=line_width)
    
            # check if only one n-gram has been supplied
            if type(highlighted_ngrams[0]) is str: highlight_ngram([string_to_integer_map[x] for x in highlighted_ngrams])
            elif type(highlighted_ngrams[0]) is int: highlight_ngram(highlighted_ngrams)
    
            # multiple n-gram's found
            else:
                for ngram in highlighted_ngrams:
                    if type(ngram[0]) is str: highlight_ngram([string_to_integer_map[x] for x in ngram])
                    elif type(ngram[0]) is int: highlight_ngram(ngram)
                    else: raise Exception('Invalid data format', ngram)
        
        if suptitle is not None:
            if (alphabet_len <= 6):
                # from scipy.optimize import curve_fit
                # import matplotlib.pyplot as plt
                # import numpy as np
                # x = np.array([1, 4, 6])
                # y = np.array([1.95, 1.08, 1.0])
                # def linear_func(x, m, b): return m * x + b
                # def exp_decay_func(x, a, b, c): return a * np.exp(-b * x) + c
                # popt, pcov = curve_fit(linear_func, x, y)
                # popt, pcov = curve_fit(exp_decay_func, x, y)
                # m, b = popt
                # a, b, c = popt
                # fitted_equation = f'y = {m:.2f}*alphabet_len + {b:.2f}'
                # fitted_equation = f'y = {a:.2f} * np.exp(-{b:.2f} * alphabet_len) + {c:.2f}'
                # print(fitted_equation)
                # plt.plot(x, y, 'o', label='Data points')
                # plt.plot(x, linear_func(x, *popt), label='Linear line')
                # plt.plot(x, exp_decay_func(x, *popt), label='Exponential Decay line')
                # plt.xlabel('x')
                # plt.ylabel('y')
                # plt.legend()
                # plt.show()
                y = 2.06 * np.exp(-0.75 * alphabet_len) + 0.98
                if verbose: print(f'alphabet_len={alphabet_len}, y={y}')
            else: y = 0.95
            fig.suptitle(suptitle, y=y)
        
        return fig
    
    
    def plot_sequences(self, sequences, gap=True):
        """
        Creates a scatter-style sequence plot for a collection of sequences.
        
        Parameters:
            sequences (list): A list of sequences to plot.
            gap (bool, optional): Whether to leave a gap between different values in a sequence. Defaults to True.
        
        Returns:
            plt.Figure: The matplotlib figure object.
        """
        
        # Determine the maximum sequence length
        max_sequence_length = max([len(s) for s in sequences])
        
        # Create a figure with appropriate dimensions
        plt.figure(figsize=[max_sequence_length*0.3,0.3 * len(sequences)])
        
        for y, sequence in enumerate(sequences):
            
            # Convert the sequence to a NumPy array
            np_sequence = np.array(sequence)
            
            # Determine the number of unique values in the sequence
            alphabet_len = len(self.get_alphabet(sequence))
            
            # Disable automatic color cycling
            plt.gca().set_prop_cycle(None)
            
            # Get the unique values in the sequence
            unique_values = self.get_alphabet(sequence)
            
            for i, value in enumerate(unique_values):
                
                # Plot the value positions as scatter points with labels
                if gap:
                    points = np.where(np_sequence == value, y + 1, np.nan)
                    plt.scatter(
                        x=range(len(np_sequence)),
                        y=points,
                        marker='s',
                        label=value,
                        s=100
                    )
                else:
                    points = np.where(np_sequence == value, 1, np.nan)
                    plt.bar(
                        range(len(points)),
                        points,
                        bottom=[y for x in range(len(points))],
                        width=1,
                        align='edge',
                        label=value
                    )
        
        # Set the y-axis limits with or without gaps
        if gap:
            plt.ylim(0.4, len(sequences) + 0.6)
            plt.xlim(-0.6, max_sequence_length - 0.4)
        else:
            plt.ylim(0, len(sequences))
            plt.xlim(0, max_sequence_length)
        
        # Force x-ticks to land on integers only (assume all sequences are of equal length)
        xtick_locations = range(len(sequences[0]))
        xtick_labels = [n+1 for n in xtick_locations]
        plt.xticks(ticks=xtick_locations, labels=xtick_labels, minor=False)
        
        # Get the legend handles and labels
        handles, labels = plt.gca().get_legend_handles_labels()
        
        # Convert the legend handles and labels into a dictionary
        by_label = dict(zip(labels, handles))
        
        # Place the legend in the upper left corner
        plt.legend(by_label.values(), by_label.keys(), bbox_to_anchor=(1.0, 1.1), loc='upper left')
        
        # Hide the y-axis ticks and labels
        plt.tick_params(axis='y', which='both', left=False, labelleft=False)
        
        # Return the matplotlib figure object
        return plt