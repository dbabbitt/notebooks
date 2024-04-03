#!/usr/bin/env python
# coding: utf-8



# Soli Deo gloria



try:
    import dill as pickle
except:
    try:
        import pickle5 as pickle
    except:
        import pickle
import pandas as pd
import os
import sys
import csv

class Storage(object):
    """Storage class."""

    def __init__(self, data_folder_path=None, saves_folder_path=None, verbose=False):

        # Change this to your data and saves folders
        if data_folder_path is None:
            self.data_folder = r'../data/'
        else:
            self.data_folder = data_folder_path
        if verbose:
            print('data_folder: {}'.format(self.data_folder))
        if saves_folder_path is None:
            self.saves_folder = r'../saves/'
        else:
            self.saves_folder = saves_folder_path
        if verbose:
            print('saves_folder: {}'.format(self.saves_folder))

        # Create the assumed directories
        self.data_csv_folder = os.path.join(self.data_folder, 'csv')
        self.saves_pickle_folder = os.path.join(self.saves_folder, 'pkl')
        self.saves_csv_folder = os.path.join(self.saves_folder, 'csv')
        if sys.version_info.major == 2:
            try:
                os.makedirs(name=self.data_csv_folder)
            except:
                pass
            try:
                os.makedirs(name=self.saves_pickle_folder)
            except:
                pass
            try:
                os.makedirs(name=self.saves_csv_folder)
            except:
                pass
        elif sys.version_info.major == 3:
            os.makedirs(name=self.data_csv_folder, exist_ok=True)
            os.makedirs(name=self.saves_pickle_folder, exist_ok=True)
            os.makedirs(name=self.saves_csv_folder, exist_ok=True)
        
        # Handy list of the different types of encodings
        self.encoding_type = ['latin1', 'iso8859-1', 'utf-8'][2]
        self.encoding_types_list = ['ascii', 'cp037', 'cp437', 'cp863', 'utf_32',
                                    'utf_32_be', 'utf_32_le', 'utf_16', 'utf_16_be',
                                    'utf_16_le', 'utf_7', 'utf_8', 'utf_8_sig',
                                    'latin1', 'iso8859-1', 'utf-8']
        self.encoding_errors_list = ['ignore', 'replace', 'xmlcharrefreplace']
        self.decoding_types_list = self.encoding_types_list.copy()
        self.decoding_errors_list = self.encoding_errors_list.copy()
        self.encoding_type = self.encoding_types_list[15]
        self.encoding_error = self.encoding_errors_list[2]
        self.decoding_type = self.decoding_types_list[15]
        self.decoding_error = self.decoding_errors_list[0]
    
    def csv_exists(self, csv_name, folder_path=None, verbose=False):
        if folder_path is None:
            csv_folder = self.saves_csv_folder
        if csv_name.endswith('.csv'):
            csv_path = os.path.join(folder_path, csv_name)
        else:
            csv_path = os.path.join(folder_path, f'{csv_name}.csv')
        if verbose:
            print(os.path.abspath(csv_path))

        return os.path.isfile(csv_path)
    
    def load_csv(self, csv_name=None, folder_path=None):
        if folder_path is None:
            csv_folder = self.data_csv_folder
        else:
            csv_folder = os.path.join(folder_path, 'csv')
        if csv_name is None:
            csv_path = max([os.path.join(csv_folder, f) for f in os.listdir(csv_folder)],
                           key=os.path.getmtime)
        else:
            if csv_name.endswith('.csv'):
                csv_path = os.path.join(csv_folder, csv_name)
            else:
                csv_path = os.path.join(csv_folder, f'{csv_name}.csv')
        data_frame = pd.read_csv(os.path.abspath(csv_path), encoding=self.encoding_type)
        
        return(data_frame)

    def pickle_exists(self, pickle_name):
        pickle_path = os.path.join(self.saves_pickle_folder, '{}.pkl'.format(pickle_name))
        
        return os.path.isfile(pickle_path)

    def load_data_frames(self, **kwargs):
        frame_dict = {}
        for frame_name in kwargs:
            pickle_path = os.path.join(self.saves_pickle_folder, '{}.pkl'.format(frame_name))
            print('Attempting to load {}.'.format(os.path.abspath(pickle_path)))
            if not os.path.isfile(pickle_path):
                csv_name = '{}.csv'.format(frame_name)
                csv_path = os.path.join(self.saves_csv_folder, csv_name)
                print('No pickle exists - attempting to load {}.'.format(os.path.abspath(csv_path)))
                if not os.path.isfile(csv_path):
                    csv_path = os.path.join(self.data_csv_folder, csv_name)
                    print('No csv exists - trying {}.'.format(os.path.abspath(csv_path)))
                    if not os.path.isfile(csv_path):
                        print('No csv exists - just forget it.')
                        frame_dict[frame_name] = None
                    else:
                        frame_dict[frame_name] = self.load_csv(csv_name=frame_name)
                else:
                    frame_dict[frame_name] = self.load_csv(csv_name=frame_name, folder_path=self.saves_folder)
            else:
                frame_dict[frame_name] = self.load_object(frame_name)
        
        return frame_dict

    def load_object(self, obj_name, pickle_path=None, download_url=None, verbose=True):
        if pickle_path is None:
            pickle_path = os.path.join(self.saves_pickle_folder, '{}.pkl'.format(obj_name))
        if not os.path.isfile(pickle_path):
            if verbose:
                print('No pickle exists at {} - attempting to load as csv.'.format(os.path.abspath(pickle_path)))
            csv_path = os.path.join(self.saves_csv_folder, '{}.csv'.format(obj_name))
            if not os.path.isfile(csv_path):
                if verbose:
                    print('No csv exists at {} - attempting to download from URL.'.format(os.path.abspath(csv_path)))
                object = pd.read_csv(download_url, low_memory=False,
                                     encoding=self.encoding_type)
            else:
                object = pd.read_csv(csv_path, low_memory=False,
                                     encoding=self.encoding_type)
            if isinstance(object, pd.DataFrame):
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
        
        return(object)

    def save_data_frames(self, include_index=False, verbose=True, **kwargs):
        for frame_name in kwargs:
            if isinstance(kwargs[frame_name], pd.DataFrame):
                csv_path = os.path.join(self.saves_csv_folder, '{}.csv'.format(frame_name))
                if verbose:
                    print('Saving to {}'.format(os.path.abspath(csv_path)))
                kwargs[frame_name].to_csv(csv_path, sep=',', encoding=self.encoding_type,
                                          index=include_index)

    # Classes, functions, and methods cannot be pickled
    def store_objects(self, verbose=True, **kwargs):
        for obj_name in kwargs:
            if hasattr(kwargs[obj_name], '__call__'):
                raise RuntimeError('Functions cannot be pickled.')
            pickle_path = os.path.join(self.saves_pickle_folder, '{}.pkl'.format(obj_name))
            if isinstance(kwargs[obj_name], pd.DataFrame):
                self.attempt_to_pickle(kwargs[obj_name], pickle_path, raise_exception=False, verbose=verbose)
            else:
                if verbose:
                    print('Pickling to {}'.format(os.path.abspath(pickle_path)))
                with open(pickle_path, 'wb') as handle:
                
                    # Protocol 4 is not handled in python 2
                    if sys.version_info.major == 2:
                        pickle.dump(kwargs[obj_name], handle, 2)
                    
                    # Pickle protocol must be <= 4
                    elif sys.version_info.major == 3:
                        pickle.dump(kwargs[obj_name], handle, min(4, pickle.HIGHEST_PROTOCOL))

    def attempt_to_pickle(self, df, pickle_path, raise_exception=False, verbose=True):
        try:
            if verbose:
                print('Pickling to {}'.format(os.path.abspath(pickle_path)))
        
            # Protocol 4 is not handled in python 2
            if sys.version_info.major == 2:
                df.to_pickle(pickle_path, protocol=2)
            
            # Pickle protocol must be <= 4
            elif sys.version_info.major == 3:
                df.to_pickle(pickle_path, protocol=min(4, pickle.HIGHEST_PROTOCOL))
        
        except Exception as e:
            os.remove(pickle_path)
            if verbose:
                print(e, ": Couldn't save {:,} cells as a pickle.".format(df.shape[0]*df.shape[1]))
            if raise_exception:
                raise
    
    def store_dir_tree(self, module_name, prefix_str='', max_level=3, verbose=False):
        if max_level==0:
            
            return None
        param_name = f'{prefix_str}{module_name}'
        successfully_pickled = True
        try:
            s.store_objects(**{param_name: eval(param_name)}, verbose=False)
        except Exception as e:
            # print(f'Pickling the module {param_name} gets a {e.__class__.__name__} error: {str(e).strip()}')
            successfully_pickled = False
        if successfully_pickled:
            if verbose:
                pickle_path = os.path.join(s.saves_pickle_folder, f'{param_name}.pkl')
                print(f'Pickling to {os.path.abspath(pickle_path)}')
        else:
            try:
                if verbose:
                    print(param_name, type(eval(param_name)))
            except Exception as e:
                pass
            base_eval_str = f"[f'{param_name}.{{fn}}' for fn in dir({param_name}) if not fn.startswith('_')]"
            base_dir_list = []
            try:
                base_dir_list = eval(base_eval_str)
            except Exception as e:
                # print(f'The evaluated list {base_eval_str} gets a {e.__class__.__name__} error: {str(e).strip()}')
                pass
            for sub_obj in base_dir_list:

                # Check the type of the object
                if type(eval(sub_obj)) not in [
                    type(ihu.build_pos_stochastic_gradient_descent_elements), type(None), float, bool, type(ihu.classifier.classes_), str, dict, int, set
                ]:
                    self.store_dir_tree(sub_obj, prefix_str=f'', max_level=max_level-1, verbose=verbose)