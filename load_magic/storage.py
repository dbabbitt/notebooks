
import pickle
import pandas as pd
import os
import sys

# Change this to your data and saves folders
DATA_FOLDER = r'../data/'
print('DATA_FOLDER: {}'.format(DATA_FOLDER))
SAVES_FOLDER = r'../saves/'
print('SAVES_FOLDER: {}'.format(SAVES_FOLDER))

# Create the assumed directories
DATA_CSV_FOLDER = os.path.join(DATA_FOLDER, 'csv')
SAVES_PICKLE_FOLDER = os.path.join(SAVES_FOLDER, 'pickle')
SAVES_CSV_FOLDER = os.path.join(SAVES_FOLDER, 'csv')
if sys.version_info.major == 2:
    os.makedirs(name=DATA_CSV_FOLDER)
    os.makedirs(name=SAVES_PICKLE_FOLDER)
    os.makedirs(name=SAVES_CSV_FOLDER)
elif sys.version_info.major == 3:
    os.makedirs(name=DATA_CSV_FOLDER, exist_ok=True)
    os.makedirs(name=SAVES_PICKLE_FOLDER, exist_ok=True)
    os.makedirs(name=SAVES_CSV_FOLDER, exist_ok=True)

# Handy list of the different types of encodings
ENCODING_TYPE = ['latin1', 'iso8859-1', 'utf-8'][2]

def load_csv(csv_name=None, folder_path=None):
    if folder_path is None:
        csv_folder = DATA_CSV_FOLDER
    else:
        csv_folder = os.path.join(folder_path, 'csv')
    if csv_name is None:
        csv_path = max([os.path.join(csv_folder, f) for f in os.listdir(csv_folder)],
                       key=os.path.getmtime)
    else:
        csv_path = os.path.join(csv_folder, '{}.csv'.format(csv_name))
    data_frame = pd.read_csv(csv_path, encoding=ENCODING_TYPE)
    
    return(data_frame)

def load_dataframes(**kwargs):
    frame_dict = {}
    for frame_name in kwargs:
        pickle_path = os.path.join(SAVES_PICKLE_FOLDER, '{}.pickle'.format(frame_name))
        if not os.path.isfile(pickle_path):
            print('No pickle exists at {} - attempting to load a saves folder csv.'.format(os.path.abspath(pickle_path)))
            csv_name = '{}.csv'.format(frame_name)
            csv_path = os.path.join(SAVES_CSV_FOLDER, csv_name)
            if not os.path.isfile(csv_path):
                print('No csv exists at {} - trying the data folder.'.format(os.path.abspath(csv_path)))
                csv_path = os.path.join(DATA_CSV_FOLDER, csv_name)
                if not os.path.isfile(csv_path):
                    print('No csv exists at {} - just forget it.'.format(os.path.abspath(csv_path)))
                    frame_dict[frame_name] = None
                else:
                    frame_dict[frame_name] = load_csv(csv_name=frame_name)
            else:
                frame_dict[frame_name] = load_csv(csv_name=frame_name, folder_path=SAVES_FOLDER)
        else:
            frame_dict[frame_name] = load_object(frame_name)
    
    return frame_dict

def load_object(obj_name, download_url=None):
    pickle_path = os.path.join(SAVES_PICKLE_FOLDER, '{}.pickle'.format(obj_name))
    if not os.path.isfile(pickle_path):
        print('No pickle exists at {} - attempting to load as csv.'.format(os.path.abspath(pickle_path)))
        csv_path = os.path.join(SAVES_CSV_FOLDER, '{}.csv'.format(obj_name))
        if not os.path.isfile(csv_path):
            print('No csv exists at {} - attempting to download from URL.'.format(os.path.abspath(csv_path)))
            object = pd.read_csv(download_url, low_memory=False,
                                 encoding=ENCODING_TYPE)
        else:
            object = pd.read_csv(csv_path, low_memory=False,
                                 encoding=ENCODING_TYPE)
        if isinstance(object, pd.DataFrame):
            attempt_to_pickle(object, pickle_path, raise_exception=False)
        else:
            with open(pickle_path, 'wb') as handle:
                
                # Protocal 4 is not handled in python 2
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
    
    return(object)

def save_dataframes(include_index=False, **kwargs):
    for frame_name in kwargs:
        if isinstance(kwargs[frame_name], pd.DataFrame):
            csv_path = os.path.join(SAVES_CSV_FOLDER, '{}.csv'.format(frame_name))
            print('Saving to {}'.format(os.path.abspath(csv_path)))
            kwargs[frame_name].to_csv(csv_path, sep=',', encoding=ENCODING_TYPE,
                                      index=include_index)

# Classes, functions, and methods cannot be pickled
def store_objects(**kwargs):
    for obj_name in kwargs:
        if hasattr(kwargs[obj_name], '__call__'):
            raise RuntimeError('Functions cannot be pickled.')
        pickle_path = os.path.join(SAVES_PICKLE_FOLDER, '{}.pickle'.format(obj_name))
        if isinstance(kwargs[obj_name], pd.DataFrame):
            attempt_to_pickle(kwargs[obj_name], pickle_path, raise_exception=False)
        else:
            print('Pickling to {}'.format(os.path.abspath(pickle_path)))
            with open(pickle_path, 'wb') as handle:
                
                # Protocal 4 is not handled in python 2
                if sys.version_info.major == 2:
                    pickle.dump(kwargs[obj_name], handle, 2)
                elif sys.version_info.major == 3:
                    pickle.dump(kwargs[obj_name], handle, pickle.HIGHEST_PROTOCOL)

def attempt_to_pickle(df, pickle_path, raise_exception=False):
    try:
        print('Pickling to {}'.format(os.path.abspath(pickle_path)))
        
        # Protocal 4 is not handled in python 2
        if sys.version_info.major == 2:
            df.to_pickle(pickle_path, protocol=2)
        elif sys.version_info.major == 3:
            df.to_pickle(pickle_path, protocol=pickle.HIGHEST_PROTOCOL)
        
    except Exception as e:
        os.remove(pickle_path)
        print(e, ": Couldn't save {:,} cells as a pickle.".format(df.shape[0]*df.shape[1]))
        if raise_exception:
            raise