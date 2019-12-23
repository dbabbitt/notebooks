
import ipykernel
import urllib
from notebook import notebookapp
import json
import os
from jupyter_core.paths import jupyter_config_dir
from traitlets.config import Config

def get_notebook_path():
    """Returns the absolute path of the Notebook or None if it cannot be determined
    NOTE: works only when the security is token-based or there is also no password
    """
    connection_file = os.path.basename(ipykernel.get_connection_file())
    kernel_id = connection_file.split('-', 1)[1].split('.')[0]

    # Assumes you've already run `jupyter notebook --generate-config` to generate
    # `jupyter_notebook_config.py` and have edited and uncommented the line
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