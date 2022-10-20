#!/usr/bin/env python
# coding: utf-8



# Soli Deo gloria



# cd C:\Users\daveb\OneDrive\Documents\GitHub\notebooks\py

from tqdm.notebook import tqdm
tqdm.pandas()

import warnings
warnings.filterwarnings('ignore')

import storage
s = storage.Storage()

def f(row_series):
    
    # Reshape your data using array.reshape(1, -1) if your data contains a single sample
    X = row_series[numeric_columns_list].fillna(0).values.reshape(1, -1)
    
    return rfclf.predict(X)[0]

climates_df = s.load_object('climates_df')
climates_df['is_like_flagstaff'] = climates_df.progress_apply(f, axis='columns')