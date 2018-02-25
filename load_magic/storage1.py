
current_directory = !echo %cd%
folder_list = current_directory[0].split('\\')
%run ../../../load_magic/storage2.py {len(folder_list) - folder_list.index('ipynb')}
%who