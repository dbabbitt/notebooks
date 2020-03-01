
from difflib import SequenceMatcher
import time
import pandas as pd


def conjunctify_list(noun_list):
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

# Handy list of the different types of encodings
encoding = ['latin1', 'iso8859-1', 'utf-8'][2]

def check_4_doubles(item_list, verbose=False):
    if verbose:
        t0 = time.time()
    rows_list = []
    n = len(item_list)
    for i in range(n-1):
        first_item = item_list[i]
        max_similarity = 0.0
        max_item = first_item
        for j in range(i+1, n):
            second_item = item_list[j]

            # Assume the first item is never identical to the second item
            this_similarity = similar(str(first_item), str(second_item))
            
            if this_similarity > max_similarity:
                max_similarity = this_similarity
                max_item = second_item

        # Get input row in dictionary format; key = col_name
        row_dict = {}
        row_dict['first_item'] = first_item
        row_dict['second_item'] = max_item
        row_dict['first_bytes'] = '-'.join(str(x) for x in bytearray(str(first_item),
                                                                     encoding=encoding, errors="replace"))
        row_dict['second_bytes'] = '-'.join(str(x) for x in bytearray(str(max_item),
                                                                      encoding=encoding, errors="replace"))
        row_dict['max_similarity'] = max_similarity

        rows_list.append(row_dict)

    column_list = ['first_item', 'second_item', 'first_bytes', 'second_bytes', 'max_similarity']
    item_similarities_df = pd.DataFrame(rows_list, columns=column_list)
    if verbose:
        t1 = time.time()
        print(t1-t0, time.ctime(t1))

    return item_similarities_df

def similar(a, b):
    return SequenceMatcher(None, str(a), str(b)).ratio()

#Check the closest names for typos
def check_for_typos(left_list, right_list, verbose=False):
    if verbose:
        t0 = time.time()
    rows_list = []
    for left_item in left_list:
        max_similarity = 0.0
        max_item = left_item
        for right_item in right_list:
            this_similarity = similar(left_item, right_item)
            if this_similarity > max_similarity:
                max_similarity = this_similarity
                max_item = right_item

        # Get input row in dictionary format; key = col_name
        row_dict = {}
        row_dict['left_item'] = left_item
        row_dict['right_item'] = max_item
        row_dict['max_similarity'] = max_similarity

        rows_list.append(row_dict)

    column_list = ['left_item', 'right_item', 'max_similarity']
    name_similarities_df = pd.DataFrame(rows_list, columns=column_list)
    if verbose:
        t1 = time.time()
        print(t1-t0, time.ctime(t1))
    
    return name_similarities_df