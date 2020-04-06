
import ipykernel
import urllib
from notebook import notebookapp
import json
import os
from jupyter_core.paths import jupyter_config_dir
from traitlets.config import Config
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import re

def get_notebook_path():
    """Returns the absolute path of the Notebook or None if it cannot be determined
    NOTE: works only when the security is token-based or there is also no password
    """
    connection_file = os.path.basename(ipykernel.get_connection_file())
    kernel_id = connection_file.split('-', 1)[1].split('.')[0]

    # Assumes you've already run `jupyter notebook --generate-config` to generate
    # `jupyter_notebook_config.py` and have edited and/or uncommented the line
    # containing `c.FileContentsManager.root_dir =`:
    c = Config()
    file_path = os.path.join(jupyter_config_dir(), 'jupyter_notebook_config.py')
    exec(open(file_path).read())
    root_dir = c['FileContentsManager']['root_dir']

    for srv in notebookapp.list_running_servers():
        try:
            if srv['token']=='' and not srv['password']:  # No token and no password, ahem...
                req = urllib.request.urlopen(srv['url']+'api/sessions')
            else:
                req = urllib.request.urlopen(srv['url']+'api/sessions?token='+srv['token'])
            sessions = json.load(req)
            for sess in sessions:
                if sess['kernel']['id'] == kernel_id:
                    
                    return os.path.abspath(os.path.join(root_dir, sess['notebook']['path']))
        except:
            pass  # There may be stale entries in the runtime directory 
    
    return None

def get_module_version(python_module):
    for attr in dir(python_module):
        if '_version' in attr.lower():
            print('{}: {}'.format(attr, getattr(python_module, attr, '????')))

def get_dir_tree(module_name, max_levels=2):
    if max_levels < 1:
        return None
    dir_list = eval("['{}.{{}}'.format(fn) for fn in dir({}) if not fn.startswith('_')]".format(module_name, module_name))
    if len(dir_list):
        print()
        print(module_name)
        print(dir_list)
        for m in dir_list:
            get_dir_tree(m, max_levels=max_levels-1)



def get_data_structs_dataframe(data_struct_list):
    """
    # Create a comprehensive dataset to train on

    def f():

        return None

    class C(object):
        def __init__(self):
            self.its = ''
        def im_a_method(self):
            self.its = 'method'

    c = C()
    data_struct_list = [list, tuple, set, dict, str, pd.DataFrame, pd.np.ndarray, bytearray, range, os, pd, f, c.im_a_method]
    data_structs_df = get_data_structs_dataframe(data_struct_list=data_struct_list)
    X, y = preprocess_data(data_structs_df)
    print('The shape of X is:', X.shape)
    print('The shape of y is:', y.shape)
    clf = get_classifier(X, y)
    get_importances(data_structs_df, clf)[:10]
    
    f_str = 'Type: {}, Given Name: {}, Actual Name: {}, Prediction: {}'
    for (s_str, data_struct) in [('s.{}'.format(fn), eval('s.{}'.format(fn))) for fn in dir(s) if not fn.startswith('_')]:
        print(f_str.format(str(type(data_struct)).split("'")[1], get_struct_name(data_struct),
                           s_str,
                           get_datastructure_prediction(df=data_structs_df, clf=clf, func=data_struct)))
    """
    data_struct_set_dict = {}
    for data_struct in data_struct_list:
        struct_name = get_struct_name(data_struct)
        data_struct_set_dict[struct_name] = set([fn for fn in dir(data_struct) if fn.startswith('_')])
    attrs_set = set()
    for attr_set in data_struct_set_dict.values():
        attrs_set = attrs_set.union(attr_set)
    columns_list = list(attrs_set)
    rows_list = []
    index_list = []
    for data_struct, attr_set in data_struct_set_dict.items():
        index_list.append(data_struct)
        row_dict = {}
        for column_name in columns_list:
            row_dict[column_name] = (column_name in attr_set)
        rows_list.append(row_dict)
    data_structs_df = pd.DataFrame(rows_list, columns=columns_list, index=index_list)
    
    return data_structs_df



def get_input_sample(df, func):
    bool_list = []
    attr_list = dir(func)
    for column_name in df.columns:
        bool_list.append(column_name in attr_list)
    
    return pd.np.array(bool_list).reshape(1, -1)



def preprocess_data(df):
    struct_cats = df.index.astype('category')
    X = df.values
    y = struct_cats.codes
    
    return X, y




def get_classifier(X, y):
    clf = RandomForestClassifier(n_estimators=13)
    clf.fit(X, y)
    
    return clf



def get_importances(df, clf):
    importances_list = [(fn, fi) for fn, fi in zip(df.columns, clf.feature_importances_)]
    importances_list.sort(key=lambda x: x[1], reverse=True)
    
    return importances_list



def get_datastructure_prediction(df, clf, func):
    idx = df.index
    codes_list = list(idx.astype('category').codes)
    prediction = clf.predict(get_input_sample(df, func))
    
    return idx[codes_list.index(prediction[0])]


# <class '__main__.ObjectClass'> is a type of <class 'type'>
def get_struct_name(data_struct):
    if isinstance(data_struct, bool):
        struct_name = 'boolean'
    elif isinstance(data_struct, str):
        struct_name = 'string'
    elif isinstance(data_struct, dict):
        struct_name = 'dictionary'
    elif isinstance(data_struct, list):
        struct_name = 'list'
    elif isinstance(data_struct, tuple):
        struct_name = 'tuple'
    elif isinstance(data_struct, set):
        struct_name = 'set'
    elif isinstance(data_struct, pd.DataFrame):
        struct_name = 'DataFrame'
    elif isinstance(data_struct, pd.np.ndarray):
        struct_name = 'ndarray'
    elif isinstance(data_struct, bytearray):
        struct_name = 'bytearray'
    elif isinstance(data_struct, range):
        struct_name = 'range'
    else:
        struct_name = str(type(data_struct)).split("'")[1]
        obj_classification = str(data_struct)
        display_regex = re.compile(r'^<(class|module|function|__main__\.\w+ object|bound method)')
        match_obj = display_regex.search(obj_classification)
        if match_obj:
            obj_classification = match_obj.group(1).split(' ')[-1]
        if obj_classification == 'object':
            struct_name = 'instantiation'
        elif obj_classification == 'class':
            print(struct_name)
            if struct_name == 'type':
                struct_name = str(data_struct)
                if '__main__.' in struct_name:
                    struct_name = obj_classification
                elif '.' in struct_name:
                    struct_name = 'import'
                else:
                    try:
                        struct_name = data_struct.__name__
                    except:
                        struct_name_list = struct_name.split("'")
                        if len(struct_name_list) > 2:
                            struct_name = struct_name_list[1]
                        else:
                            print(struct_name)
            elif callable(data_struct):
                struct_name = 'function'
    
    return struct_name