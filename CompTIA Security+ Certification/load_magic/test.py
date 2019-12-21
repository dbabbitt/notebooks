
#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
from starfade import Starfade
from xview_code.rectangle import Rectangle
from xview_code import wv_util
from storage import Storage

data_folder = r'../'*int(sys.argv[1]) + 'data/'
print('data_folder = ' + data_folder)

saves_folder = r'../'*int(sys.argv[1]) + 'saves/'
print('saves_folder = ' + saves_folder)

print(dir(Starfade))
print(dir(Rectangle))
print(dir(wv_util))
print(dir(Storage))