
import os
from shutil import copyfile
import re

os.getcwd()

# Copy all notebooks from the repositories
ROOR_DIR = r'C:\\Users\\577342\\Documents\\Repositories\\hanscom-afb-data-science'
BLACK_LIST = ['.ipynb_checkpoints']

for sub_dir, dir_list, file_list in os.walk(ROOR_DIR):
    for file_name in file_list:
        if all(map(lambda x: x not in sub_dir, BLACK_LIST)):
            if file_name.endswith('.ipynb'):
                src_path = os.path.join(sub_dir, file_name)
                dst_dir = os.path.normpath(os.path.join(os.getcwd(), *sub_dir.rsplit(ROOR_DIR)))
                if not os.path.isdir(dst_dir):
                    os.makedirs(dst_dir)
                dst_path = os.path.join(dst_dir, file_name)
                if not os.path.isfile(dst_path):
                    copyfile(src_path, dst_path)
                    print(dst_path)

# Where are any wav files?
ROOR_DIR = '/'
BLACK_LIST = ['.Trash']

for sub_dir, dir_list, file_list in os.walk(ROOR_DIR):
    for file_name in file_list:
        if all(map(lambda x: x not in sub_dir, BLACK_LIST)):
            if file_name.endswith('.wav'):
                src_path = os.path.join(sub_dir, file_name)
                dst_dir = os.path.normpath(os.path.join(os.getcwd(), '../data/wav', *sub_dir.rsplit(ROOR_DIR)))
                if not os.path.isdir(dst_dir):
                    os.makedirs(dst_dir)
                dst_path = os.path.join(dst_dir, file_name)
                if not os.path.isfile(dst_path):
                    #copyfile(src_path, dst_path)
                    print(dst_path)