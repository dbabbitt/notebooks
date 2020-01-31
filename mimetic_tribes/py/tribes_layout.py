
import pandas as pd

canvas_width = 2000
canvas_height = 961
rows_list = []
row_dict = {}

row_dict['layout_x'] = -canvas_width/2 + canvas_width/8

row_dict['tribe_name'] = 'Modern Neo-Marxists'
row_dict['layout_y'] = -520
rows_list.append(row_dict.copy())

row_dict['tribe_name'] = 'Antifa'
row_dict['layout_y'] = -561
rows_list.append(row_dict.copy())

row_dict['tribe_name'] = 'Occupy'
row_dict['layout_y'] = -602
rows_list.append(row_dict.copy())

row_dict['tribe_name'] = 'Dirtbag Left'
row_dict['layout_y'] = -643
rows_list.append(row_dict.copy())

row_dict['tribe_name'] = 'DSA (Democratic Socialists of America)'
row_dict['layout_y'] = -684
rows_list.append(row_dict.copy())

row_dict['tribe_name'] = 'SJAs (Social Justice Activists)'
row_dict['layout_y'] = -800
rows_list.append(row_dict.copy())

row_dict['tribe_name'] = 'Black Lives Matter'
row_dict['layout_y'] = -841
rows_list.append(row_dict.copy())

row_dict['tribe_name'] = '#MeToo'
row_dict['layout_y'] = -882
rows_list.append(row_dict.copy())

row_dict['tribe_name'] = 'Gender-Critical Feminists'
row_dict['layout_y'] = -923
rows_list.append(row_dict.copy())

row_dict['layout_x'] = -canvas_width/2 + 3*canvas_width/8

row_dict['tribe_name'] = 'Establishment Left'
row_dict['layout_y'] = -696
rows_list.append(row_dict.copy())

row_dict['layout_x'] = -canvas_width/2 + canvas_width/2

row_dict['tribe_name'] = 'Optimists'
row_dict['layout_y'] = -111
rows_list.append(row_dict.copy())

row_dict['tribe_name'] = 'Integral Theorists'
row_dict['layout_y'] = -152
rows_list.append(row_dict.copy())

row_dict['tribe_name'] = 'Street Epistemologists'
row_dict['layout_y'] = -193
rows_list.append(row_dict.copy())

row_dict['tribe_name'] = 'New Atheists'
row_dict['layout_y'] = -234
rows_list.append(row_dict.copy())

row_dict['tribe_name'] = 'Rationalist Diaspora'
row_dict['layout_y'] = -275
rows_list.append(row_dict.copy())

row_dict['tribe_name'] = 'Post-Rationalists'
row_dict['layout_y'] = -316
rows_list.append(row_dict.copy())

row_dict['tribe_name'] = 'Intellectual Dark Web'
row_dict['layout_y'] = -357
rows_list.append(row_dict.copy())

row_dict['tribe_name'] = 'Sorters'
row_dict['layout_y'] = -398
rows_list.append(row_dict.copy())

row_dict['layout_x'] = -canvas_width/2 + 5*canvas_width/8

row_dict['tribe_name'] = 'Establishment Right'
row_dict['layout_y'] = -696
rows_list.append(row_dict.copy())

row_dict['layout_x'] = -canvas_width/2 + 7*canvas_width/8

row_dict['tribe_name'] = 'Benedictines'
row_dict['layout_y'] = -484
rows_list.append(row_dict.copy())

row_dict['tribe_name'] = 'Christian Right'
row_dict['layout_y'] = -525
rows_list.append(row_dict.copy())

row_dict['tribe_name'] = 'Tea Party'
row_dict['layout_y'] = -566
rows_list.append(row_dict.copy())

row_dict['tribe_name'] = 'Trumpists'
row_dict['layout_y'] = -607
rows_list.append(row_dict.copy())

row_dict['tribe_name'] = 'InfoWarriors'
row_dict['layout_y'] = -648
rows_list.append(row_dict.copy())

row_dict['tribe_name'] = 'QAnoners'
row_dict['layout_y'] = -689
rows_list.append(row_dict.copy())

row_dict['tribe_name'] = 'Alt-Lite'
row_dict['layout_y'] = -730
rows_list.append(row_dict.copy())

row_dict['tribe_name'] = 'Alt-Right'
row_dict['layout_y'] = -751
rows_list.append(row_dict.copy())

row_dict['tribe_name'] = 'Modern Neo-Nazis'
row_dict['layout_y'] = -792
rows_list.append(row_dict.copy())

row_dict['tribe_name'] = 'Neoreactionaries'
row_dict['layout_y'] = -833
rows_list.append(row_dict.copy())

row_dict['tribe_name'] = 'MRA (Mens Right Advocates)'
row_dict['layout_y'] = -874
rows_list.append(row_dict.copy())

row_dict['tribe_name'] = 'Manosphere'
row_dict['layout_y'] = -915
rows_list.append(row_dict.copy())

row_dict['tribe_name'] = 'MGTOW (Men Going Their Own Way)'
row_dict['layout_y'] = -956
rows_list.append(row_dict.copy())

row_dict['tribe_name'] = 'Incels'
row_dict['layout_y'] = -997
rows_list.append(row_dict.copy())

layout_df = pd.DataFrame(rows_list)