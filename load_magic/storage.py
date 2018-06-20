
import pickle
import pandas as pd
import os

# Change this to your data and saves folders
DATA_FOLDER = r'../data/'
print('DATA_FOLDER:', DATA_FOLDER)
SAVES_FOLDER = r'../saves/'
print('SAVES_FOLDER:', SAVES_FOLDER)

# Create the assumed directories
os.makedirs(name=DATA_FOLDER+'csv', exist_ok=True)
os.makedirs(name=SAVES_FOLDER+'pickle', exist_ok=True)
os.makedirs(name=SAVES_FOLDER+'csv', exist_ok=True)

# Handy list of the different types of encodings
ENCODING_TYPE = ['latin1', 'iso8859-1', 'utf-8'][2]

def load_csv(csv_name=None, folder_path=None):
    if folder_path is None:
        csv_folder = DATA_FOLDER + 'csv/'
    else:
        csv_folder = folder_path + 'csv/'
    if csv_name is None:
        csv_path = max([os.path.join(csv_folder, f) for f in os.listdir(csv_folder)],
                       key=os.path.getmtime)
    else:
        csv_path = csv_folder + csv_name + '.csv'
    data_frame = pd.read_csv(csv_path, encoding=ENCODING_TYPE)
    
    return(data_frame)

def load_dataframes(**kwargs):
    frame_dict = {}
    for frame_name in kwargs:
        pickle_path = SAVES_FOLDER + 'pickle/' + frame_name + '.pickle'
        if not os.path.isfile(pickle_path):
            print('No pickle exists at ' + pickle_path + ' - attempting to load a saves folder csv.')
            csv_folder = SAVES_FOLDER + 'csv/'
            csv_path = csv_folder + frame_name + '.csv'
            if not os.path.isfile(csv_path):
                print('No csv exists at ' + csv_path + ' - trying the data folder.')
                csv_path = DATA_FOLDER + 'csv/' + frame_name + '.csv'
                if not os.path.isfile(csv_path):
                    print('No csv exists at ' + csv_path + ' - just forget it.')
                    frame_dict[frame_name] = None
                else:
                    frame_dict[frame_name] = load_csv(csv_name=frame_name)
            else:
                frame_dict[frame_name] = load_csv(csv_name=frame_name, folder_path=csv_folder)
        else:
            frame_dict[frame_name] = load_object(frame_name)
    
    return frame_dict

def load_object(obj_name, download_url=None):
    pickle_path = SAVES_FOLDER + 'pickle/' + obj_name + '.pickle'
    if not os.path.isfile(pickle_path):
        print('No pickle exists at ' + pickle_path + ' - attempting to load as csv.')
        csv_path = SAVES_FOLDER + 'csv/' + obj_name + '.csv'
        if not os.path.isfile(csv_path):
            print('No csv exists at ' + csv_path + ' - attempting to download from URL.')
            object = pd.read_csv(download_url, low_memory=False,
                                 encoding=ENCODING_TYPE)
        else:
            object = pd.read_csv(csv_path, low_memory=False,
                                 encoding=ENCODING_TYPE)
        if isinstance(object, pd.DataFrame):
            attempt_to_pickle(object, pickle_path, raise_exception=False)
        else:
            with open(pickle_path, 'wb') as handle:
                pickle.dump(object, handle, pickle.HIGHEST_PROTOCOL)
    else:
        try:
            object = pd.read_pickle(pickle_path)
        except:
            with open(pickle_path, 'rb') as handle:
                object = pickle.load(handle)
    
    return(object)

def save_dataframes(include_index=False, **kwargs):
    csv_folder = SAVES_FOLDER + 'csv/'
    for frame_name in kwargs:
        if isinstance(kwargs[frame_name], pd.DataFrame):
            csv_path = csv_folder + frame_name + '.csv'
            print('Saving to {}'.format(csv_path))
            kwargs[frame_name].to_csv(csv_path, sep=',', encoding=ENCODING_TYPE,
                                      index=include_index)

# Classes, functions, and methods cannot be pickled
def store_objects(**kwargs):
    for obj_name in kwargs:
        if hasattr(kwargs[obj_name], '__call__'):
            raise RuntimeError('Functions cannot be pickled.')
        obj_path = SAVES_FOLDER + 'pickle/' + str(obj_name)
        pickle_path = obj_path + '.pickle'
        if isinstance(kwargs[obj_name], pd.DataFrame):
            attempt_to_pickle(kwargs[obj_name], pickle_path, raise_exception=False)
        else:
            print('Pickling to ' + pickle_path)
            with open(pickle_path, 'wb') as handle:
                pickle.dump(kwargs[obj_name], handle, pickle.HIGHEST_PROTOCOL)

def attempt_to_pickle(df, pickle_path, raise_exception=False):
    try:
        print('Pickling to ' + pickle_path)
        df.to_pickle(pickle_path)
    except Exception as e:
        os.remove(pickle_path)
        print(e, ': Couldn\'t save ' + '{:,}'.format(df.shape[0]*df.shape[1]) + ' cells as a pickle.')
        if raise_exception:
            raise