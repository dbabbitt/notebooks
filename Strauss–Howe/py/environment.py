
import ipykernel
import urllib
from notebook import notebookapp
import json
import os
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

def get_notebook_path():
    """Returns the absolute path of the Notebook or None if it cannot be determined
    NOTE: works only when the security is token-based or there is also no password
    """
    connection_file = os.path.basename(ipykernel.get_connection_file())
    kernel_id = connection_file.split('-', 1)[1].split('.')[0]

    for srv in notebookapp.list_running_servers():
        try:
            if srv['token']=='' and not srv['password']:  # No token and no password, ahem...
                req = urllib.request.urlopen(srv['url']+'api/sessions')
            else:
                req = urllib.request.urlopen(srv['url']+'api/sessions?token='+srv['token'])
            sessions = json.load(req)
            for sess in sessions:
                if sess['kernel']['id'] == kernel_id:
                    
                    return os.path.abspath(os.path.join(r'D:\Documents\Repositories', sess['notebook']['path']))
        except:
            pass  # There may be stale entries in the runtime directory 
    
    return None

def get_module_version(python_module):
    for attr in dir(python_module):
        if '_version' in attr.lower():
            print('{}: {}'.format(attr, getattr(python_module, attr, '????')))



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



def get_struct_name(data_struct):
    struct_name = str(type(data_struct)).split("'")[1]
    if struct_name == 'type':
        try:
            struct_name = data_struct.__name__
        except:
            struct_name = str(data_struct)
            struct_name_list = struct_name.split("'")
            if len(struct_name_list) > 2:
                struct_name = struct_name_list[1]
            else:
                print(struct_name)
    
    return struct_name