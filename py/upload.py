
# coding: utf-8

import youtube_dl
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

downloads_folder = r'C:\Users\dev\Downloads\\'
youtube_url_list = ['https://www.youtube.com/watch?v=husJZ2THQdU']

ydl_opts = {
    'format': 'bestaudio/best',
    'nocheckcertificate': False,
    'outtmpl': downloads_folder+youtube_dl.DEFAULT_OUTTMPL,
    'postprocessors': [{'key': 'FFmpegExtractAudio',
                       'preferredcodec': 'mp3',
                       'preferredquality': '192'}],
    'verbose': False,
    }
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    try:
        result = ydl.download(youtube_url_list)
    except Exception as e:
        print(e)
print('Conversion completed.')


# The URL that gets displeyed here is not suitable for public consumption
GoogleAuth.DEFAULT_SETTINGS['client_config_file'] = r'C:\Users\dev\Documents\repositories\notebooks\Miscellaneous\json\client_secrets.json'
gauth = GoogleAuth()
gauth.LocalWebserverAuth()


# Create GoogleDrive instance with authenticated GoogleAuth instance
drive = GoogleDrive(gauth)

# ID of the "Reading Material" folder
tgt_folder_id = '1syfUx6jukbW1CWIEy8xoM9veGGr5MBUh'

# Upload all mp3s from the Downloads folder to Google Drive's "Reading Material" folder
gfile_dict = {}
for subdir, dirs, files in os.walk(downloads_folder):
    for src_file in files:
        if src_file.endswith('.mp3'):
            src_path = os.path.join(subdir, src_file)
            gfile_dict[src_file] = drive.CreateFile({'title':src_file, 'mimeType':'audio/mp3',
                                                     'parents': [{'kind': 'drive#fileLink',
                                                                  'id': tgt_folder_id}]})

            # Read mp3 file and set it as a content of this instance.
            gfile_dict[src_file].SetContentFile(src_path)
            
            # Upload the file
            try:
                gfile_dict[src_file].Upload()
                print('Uploaded %s (%s)' % (gfile_dict[src_file]['title'],
                                            gfile_dict[src_file]['mimeType']))
            except Exception as e:
                print('Upload failed for %s (%s): %s' % (gfile_dict[src_file]['title'],
                                                         gfile_dict[src_file]['mimeType'], e))
print('Upload completed.')

# Trash all mp3s from Google Drive's "Reading Material" folder
for src_file in gfile_dict.keys():

    # Trash mp3 file
    try:
        gfile_dict[src_file].Trash()
        print('Trashed %s (%s)' % (gfile_dict[src_file]['title'],
                                   gfile_dict[src_file]['mimeType']))
    except Exception as e:
        print('Trash failed for %s (%s): %s' % (gfile_dict[src_file]['title'],
                                                gfile_dict[src_file]['mimeType'], e))
    
print('Trashing completed.')

# Delete all mp3s in the Downloads folder
for src_file in gfile_dict.keys():
    src_path = os.path.join(downloads_folder, src_file)

    # Delete the file
    try:
        os.remove(src_path)
        print('Deleted %s (%s)' % (src_file,
                                   gfile_dict[src_file]['mimeType']))
    except Exception as e:
        print('Failed to delete %s (%s): %s' % (src_file,
                                                gfile_dict[src_file]['mimeType'], e))
print('Deleting completed.')