
import os
from shutil import copyfile
import re

os.getcwd()

# Copy all notebooks from the repositories
rootdir = r'C:\Users\Dave\Documents\My Repositories\notebooks'
black_list = ['.ipynb_checkpoints']

for subdir, dirs, files in os.walk(rootdir):
    for src_file in files:
        if all(map(lambda x: x not in subdir, black_list)):
            if src_file.endswith('.ipynb'):
                src_path = os.path.join(subdir, src_file)
                dst_dir = os.path.normpath(os.getcwd() + '\\'.join(subdir.rsplit(rootdir)))
                if not os.path.isdir(dst_dir):
                    os.makedirs(dst_dir)
                dst_path = dst_dir + '\\' + src_file
                if not os.path.isfile(dst_path):
                    copyfile(src_path, dst_path)
                    print(dst_path)

# Where are any wav files?
rootdir = '/'
black_list = ['.Trash']

for subdir, dirs, files in os.walk(rootdir):
    for src_file in files:
        if all(map(lambda x: x not in subdir, black_list)):
            if src_file.endswith('.wav'):
                src_path = os.path.join(subdir, src_file)
                dst_dir = os.path.normpath(os.getcwd() + '../data/wav' +
                                           '/'.join(subdir.rsplit(rootdir)))
                if not os.path.isdir(dst_dir):
                    os.makedirs(dst_dir)
                dst_path = dst_dir + '/' + src_file
                if not os.path.isfile(dst_path):
                    #copyfile(src_path, dst_path)
                    print(dst_path)