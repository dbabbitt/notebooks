
from IPython.display import HTML

notebook_viewer_url = 'https://nbviewer.jupyter.org/github/dbabbitt/notebooks/blob/master/'
notebook_viewer_url += '/'.join(notebook_path.split('/')[1:])
message_str = 'Click <a href="{}" target="_blank">here</a> to view notebook in nbviewer.'
HTML(message_str.format(notebook_viewer_url))