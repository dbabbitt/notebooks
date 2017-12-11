
# coding: utf-8

# In[1]:



# https://www.kaggle.com/andrewfager/mobile-phone-activity-exploratory-analysis
# https://www.kaggle.com/marcodena/mobile-phone-activity/data
# https://www.nature.com/articles/sdata201555
import pickle
import pandas as pd
from gensim import corpora, models, similarities

# Handy list of the different types of encodings
encoding = ['latin1', 'iso8859-1', 'utf-8'][1]

def load_object(obj_name):
    pickle_path = '../saves/pickle/' + obj_name + '.pickle'
    try:
        object = pd.read_pickle(pickle_path)
    except:
        with open(pickle_path, 'rb') as handle:
            object = pickle.load(handle)
    
    return(object)

def save_dataframes(**kwargs):
    csv_folder = '../saves/csv/'
    for frame_name in kwargs:
        csv_path = csv_folder + frame_name + '.csv'
        kwargs[frame_name].to_csv(csv_path, sep=',', encoding=encoding, index=False)

# Classes, functions, and methods cannot be pickled
def store_objects(**kwargs):
    for obj_name in kwargs:
        if hasattr(kwargs[obj_name], '__call__'):
            raise RuntimeError('Functions cannot be pickled.')
        obj_path = '../saves/pickle/' + str(obj_name)
        pickle_path = obj_path + '.pickle'
        if isinstance(kwargs[obj_name], pd.DataFrame):
            kwargs[obj_name].to_pickle(pickle_path)
        else:
            with open(pickle_path, 'wb') as handle:
                pickle.dump(kwargs[obj_name], handle, pickle.HIGHEST_PROTOCOL)

correlation_df = load_object('correlation_df')


# In[ ]:



temp_links_list = []
source_target_list = []
for source, row_series in correlation_df.iterrows():
    for target, value in row_series.iteritems():
        if (source != target) and ((target, source) not in source_target_list):
            temp_links_list.append({'source': source, 'target': target, 'value': value})
            source_target_list.append((source, target))


# In[ ]:



store_objects(correlation_df=correlation_df)
print(temp_links_list[:3])

