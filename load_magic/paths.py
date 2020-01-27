
import os
from shutil import copyfile
import re
import subprocess




def print_all_files_ending_starting_with(root_dir=r'D:\Documents\Repositories', ends_with='.yml', starts_with='install_config_',
                                         black_list=['$RECYCLE.BIN', '$Recycle.Bin']):
    if type(root_dir) == list:
        root_dir_list = root_dir
    else:
        root_dir_list = [root_dir]
    if type(ends_with) == list:
        endswith_list = ends_with
    else:
        endswith_list = [ends_with]
    if type(starts_with) == list:
        startswith_list = starts_with
    else:
        startswith_list = [starts_with]
    for root_dir in root_dir_list:
        for sub_directory, directories_list, files_list in os.walk(root_dir):
            if all(map(lambda x: x not in sub_directory, black_list)):
                for file_name in files_list:
                    endswith_bool = False
                    for ends_with in endswith_list:
                        endswith_bool = endswith_bool or file_name.endswith(ends_with)
                    startswith_bool = False
                    for starts_with in startswith_list:
                        startswith_bool = startswith_bool or file_name.startswith(starts_with)
                    if endswith_bool and startswith_bool:
                        file_path = os.path.join(sub_directory, file_name)
                        print(file_path)




def print_all_files_starting_with(root_dir=r'D:\Vagrant_Projects\local-vagrant', starts_with='host',
                                  black_list=['$RECYCLE.BIN', '$Recycle.Bin']):
    if type(root_dir) == list:
        root_dir_list = root_dir
    else:
        root_dir_list = [root_dir]
    if type(starts_with) == list:
        startswith_list = starts_with
    else:
        startswith_list = [starts_with]
    for root_dir in root_dir_list:
        for sub_directory, directories_list, files_list in os.walk(root_dir):
            if all(map(lambda x: x not in sub_directory, black_list)):
                for file_name in files_list:
                    startswith_bool = False
                    for starts_with in startswith_list:
                        startswith_bool = startswith_bool or file_name.startswith(starts_with)
                    if startswith_bool:
                        file_path = os.path.join(sub_directory, file_name)
                        print(file_path)




def print_all_files_ending_with(root_dir=r'D:\\', ends_with='.box', black_list=['$RECYCLE.BIN', '$Recycle.Bin']):
    if type(root_dir) == list:
        root_dir_list = root_dir
    else:
        root_dir_list = [root_dir]
    if type(ends_with) == list:
        endswith_list = ends_with
    else:
        endswith_list = [ends_with]
    for root_dir in root_dir_list:
        for sub_directory, directories_list, files_list in os.walk(root_dir):
            if all(map(lambda x: x not in sub_directory, black_list)):
                for file_name in files_list:
                    endswith_bool = False
                    for ends_with in endswith_list:
                        endswith_bool = endswith_bool or file_name.endswith(ends_with)
                    if endswith_bool:
                        file_path = os.path.join(sub_directory, file_name)
                        print(file_path)



def get_git_lfs_track_commands(repository_name, repository_dir=r'D:\Documents\Repositories'):
    black_list = [os.path.join(repository_dir, repository_name, '.git')]
    file_types_set = set()
    for sub_directory, directories_list, files_list in os.walk(os.path.join(repository_dir, repository_name)):
            if all(map(lambda x: x not in sub_directory, black_list)):
                for file_name in files_list:
                    file_path = os.path.join(sub_directory, file_name)
                    bytes_count = os.path.getsize(file_path)
                    if bytes_count > 50_000_000:
                        file_types_set.add(file_name.split('.')[-1])
    print('git lfs install')
    for file_type in file_types_set:
        print('git lfs track "*.{}"'.format(file_type))
    print('git add .gitattributes')


#repository_dir = r'D:\Vagrant_Projects'
#text_editor_path = r'C:\Program Files\Sublime Text 3\sublime_text.exe'
def get_specific_gitignore_files(repository_name, repository_dir=r'D:\Documents\Repositories',
                                 text_editor_path=r'C:\Program Files\Notepad++\notepad++.exe'):
    print('''# Ignore big files (GitHub will warn you when pushing files larger than 50 MB. You will not be allowed to
# push files larger than 100 MB.) Tip: If you regularly push large files to GitHub, consider introducing
# Git Large File Storage (Git LFS) as part of your workflow.''')
    repository_path = os.path.join(repository_dir, repository_name)
    black_list = [os.path.join(repository_path, '.git')]
    for sub_directory, directories_list, files_list in os.walk(repository_path):
            if all(map(lambda x: x not in sub_directory, black_list)):
                for file_name in files_list:
                    file_path = os.path.join(sub_directory, file_name)
                    bytes_count = os.path.getsize(file_path)
                    if bytes_count > 50_000_000:
                        print('/'.join(os.path.relpath(file_path, repository_path).split(os.sep)))
    file_path = os.path.join(repository_dir, repository_name, '.gitignore')
    print()
    subprocess.run([text_editor_path, os.path.abspath(file_path)])


#file_path = os.path.join(mov_dir, file_name)
#bytes_count = os.path.getsize(file_path)
#print(file_name, humanize_bytes(bytes_count))
def humanize_bytes(bytes_count, precision=1):
    """Return a humanized string representation of a number of bytes.

    Assumes `from __future__ import division`.

    >>> humanize_bytes(1)
    '1 byte'
    >>> humanize_bytes(1024)
    '1.0 kB'
    >>> humanize_bytes(1024*123)
    '123.0 kB'
    >>> humanize_bytes(1024*12342)
    '12.1 MB'
    >>> humanize_bytes(1024*12342,2)
    '12.05 MB'
    >>> humanize_bytes(1024*1234,2)
    '1.21 MB'
    >>> humanize_bytes(1024*1234*1111,2)
    '1.31 GB'
    >>> humanize_bytes(1024*1234*1111,1)
    '1.3 GB'
    """
    abbrevs = (
        (1<<50, 'PB'),
        (1<<40, 'TB'),
        (1<<30, 'GB'),
        (1<<20, 'MB'),
        (1<<10, 'kB'),
        (1, 'bytes')
    )
    if bytes_count == 1:
        return '1 byte'
    for factor, suffix in abbrevs:
        if bytes_count >= factor:
            break
    
    return '{0:.{1}f} {2}'.format(bytes_count / factor, precision, suffix)


def remove_empty_folders(folder_path, remove_root=True):
    '''Function to remove empty folders'''
    if not os.path.isdir(folder_path):
        
        return

    # Remove empty subfolders
    files = os.listdir(folder_path)
    if len(files):
        for f in files:
            full_path = os.path.join(folder_path, f)
            if os.path.isdir(full_path):
                remove_empty_folders(full_path)

    # If folder empty, delete it
    files = os.listdir(folder_path)
    if len(files) == 0 and remove_root:
        print('Removing empty folder: {}'.format(folder_path))
        os.rmdir(folder_path)