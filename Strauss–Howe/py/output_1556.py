
import bpy

# Get spiral data
patriarch_coords_dict = {}
patriarch_coords_dict['(No Name), Jr.'] = [(-81, 162, 1), (-82, 162, 1), (-83, 162, 1), (-84, 162, 1), (-84, 161, 1), (-85, 161, 1), (-86, 161, 1), (-86, 160, 1), (-87, 160, 1), (-88, 160, 1), (-89, 159, 1), (-90, 159, 1), (-91, 159, 1), (-91, 158, 1), (-92, 158, 1), (-93, 158, 1), (-93, 157, 1), (-94, 157, 1), (-95, 157, 1), (-95, 156, 1), (-96, 156, 1), (-97, 156, 1), (-97, 155, 1), (-98, 155, 1), (-99, 155, 1), (-99, 154, 1), (-100, 154, 1), (-101, 154, 1), (-101, 153, 1), (-102, 153, 1), (-102, 152, 1), (-103, 152, 1), (-104, 152, 1), (-104, 151, 1), (-105, 151, 1), (-106, 151, 1), (-106, 150, 1), (-107, 150, 1), (-108, 150, 1), (-108, 149, 1), (-109, 149, 1), (-109, 148, 1), (-110, 148, 1), (-111, 148, 1), (-111, 147, 1), (-112, 147, 1), (-113, 146, 1), (-114, 146, 1), (-114, 145, 1), (-115, 145, 1), (-116, 145, 1), (-116, 144, 1), (-117, 144, 1), (-117, 143, 1), (-118, 143, 1), (-119, 142, 1), (-120, 142, 1), (-120, 141, 1), (-121, 141, 1), (-121, 140, 1), (-122, 140, 1), (-123, 140, 1), (-123, 139, 1), (-124, 139, 1), (-124, 138, 1), (-125, 138, 1), (-125, 137, 1), (-126, 137, 1), (-127, 137, 1), (-127, 136, 1), (-128, 136, 1), (-128, 135, 1), (-129, 135, 1), (-129, 134, 1), (-130, 134, 1), (-130, 133, 1), (-131, 133, 1), (-132, 133, 1), (-132, 132, 1), (-133, 132, 1), (-133, 131, 1), (-134, 131, 1), (-134, 130, 1), (-135, 130, 1), (-135, 129, 1), (-136, 129, 1), (-136, 128, 1)]
patriarch_coords_dict['(No Name), Sr.'] = [(125, 8, 1), (125, 9, 1), (125, 10, 1), (125, 11, 1), (125, 12, 1), (125, 13, 1), (125, 14, 1), (125, 15, 1), (125, 16, 1), (125, 17, 1), (125, 18, 1), (125, 19, 1), (125, 20, 1), (125, 21, 1), (125, 22, 1), (125, 23, 1), (125, 24, 1), (125, 25, 1), (125, 26, 1), (125, 27, 1), (125, 28, 1), (125, 29, 1), (125, 30, 1), (125, 31, 1), (124, 31, 1), (124, 32, 1), (124, 33, 1), (124, 34, 1), (124, 35, 1), (124, 36, 1), (124, 37, 1), (123, 38, 1), (123, 39, 1), (123, 40, 1), (123, 41, 1), (123, 42, 1), (123, 43, 1), (122, 43, 1), (122, 44, 1), (122, 45, 1), (122, 46, 1), (122, 47, 1), (121, 47, 1), (121, 48, 1), (121, 49, 1), (121, 50, 1), (121, 51, 1), (120, 51, 1), (120, 52, 1), (120, 53, 1), (120, 54, 1), (119, 54, 1), (119, 55, 1), (119, 56, 1), (119, 57, 1), (118, 57, 1), (118, 58, 1), (118, 59, 1), (117, 60, 1), (117, 61, 1), (117, 62, 1), (116, 63, 1), (116, 64, 1), (116, 65, 1), (115, 65, 1), (115, 66, 1), (115, 67, 1), (114, 67, 1), (114, 68, 1), (114, 69, 1), (113, 70, 1), (113, 71, 1), (112, 72, 1), (112, 73, 1), (112, 74, 1), (111, 74, 1), (111, 75, 1), (110, 76, 1), (110, 77, 1), (109, 77, 1), (109, 78, 1), (109, 79, 1), (108, 80, 1), (108, 81, 1), (107, 81, 1), (107, 82, 1), (107, 83, 1), (106, 83, 1), (106, 84, 1), (105, 84, 1), (105, 85, 1), (105, 86, 1), (104, 86, 1), (104, 87, 1), (103, 87, 1), (103, 88, 1), (103, 89, 1), (102, 89, 1), (102, 90, 1), (101, 90, 1), (101, 91, 1), (101, 92, 1), (100, 92, 1), (100, 93, 1), (99, 93, 1), (99, 94, 1), (98, 95, 1), (98, 96, 1), (97, 96, 1), (97, 97, 1), (96, 97, 1), (96, 98, 1), (95, 98, 1), (95, 99, 1), (94, 100, 1), (93, 101, 1), (93, 102, 1), (92, 102, 1), (92, 103, 1), (91, 103, 1), (91, 104, 1), (90, 104, 1), (90, 105, 1), (89, 105, 1), (89, 106, 1), (88, 106, 1), (88, 107, 1), (87, 107, 1), (87, 108, 1), (86, 108, 1), (86, 109, 1), (85, 109, 1), (85, 110, 1), (84, 110, 1), (84, 111, 1), (83, 111, 1), (83, 112, 1), (82, 112, 1), (82, 113, 1), (81, 113, 1), (81, 114, 1), (80, 114, 1), (80, 115, 1), (79, 115, 1), (79, 116, 1), (78, 116, 1), (77, 117, 1), (76, 117, 1), (76, 118, 1), (75, 118, 1), (75, 119, 1), (74, 119, 1), (74, 120, 1), (73, 120, 1), (73, 121, 1), (72, 121, 1), (71, 122, 1), (70, 122, 1), (70, 123, 1), (69, 123, 1), (68, 124, 1), (67, 124, 1), (67, 125, 1), (66, 125, 1), (65, 126, 1), (64, 126, 1), (64, 127, 1), (63, 127, 1), (63, 128, 1), (62, 128, 1), (61, 128, 1), (61, 129, 1), (60, 129, 1), (59, 130, 1), (58, 130, 1), (58, 131, 1), (57, 131, 1), (56, 131, 1), (56, 132, 1), (55, 132, 1), (54, 132, 1), (54, 133, 1), (53, 133, 1), (52, 133, 1), (52, 134, 1), (51, 134, 1), (50, 134, 1), (50, 135, 1), (49, 135, 1), (48, 136, 1), (47, 136, 1), (46, 137, 1), (45, 137, 1), (44, 137, 1), (44, 138, 1), (43, 138, 1), (42, 138, 1), (41, 139, 1), (40, 139, 1), (39, 140, 1), (38, 140, 1), (37, 140, 1), (37, 141, 1), (36, 141, 1), (35, 141, 1), (34, 141, 1), (34, 142, 1), (33, 142, 1), (32, 142, 1), (31, 142, 1), (31, 143, 1), (30, 143, 1), (29, 143, 1), (28, 144, 1), (27, 144, 1), (26, 144, 1), (25, 144, 1), (25, 145, 1), (24, 145, 1), (23, 145, 1), (22, 145, 1), (21, 145, 1), (21, 146, 1), (20, 146, 1), (19, 146, 1), (18, 146, 1), (17, 147, 1), (16, 147, 1), (15, 147, 1), (14, 147, 1), (13, 147, 1), (12, 148, 1), (11, 148, 1), (10, 148, 1), (9, 148, 1), (8, 148, 1), (7, 148, 1), (7, 149, 1), (6, 149, 1), (5, 149, 1), (4, 149, 1), (3, 149, 1), (2, 149, 1), (1, 149, 1), (0, 149, 1), (0, 150, 1), (-1, 150, 1), (-2, 150, 1), (-3, 150, 1), (-4, 150, 1), (-5, 150, 1), (-6, 150, 1), (-7, 150, 1), (-8, 150, 1), (-9, 150, 1), (-10, 150, 1), (-11, 150, 1), (-12, 150, 1), (-13, 150, 1), (-14, 150, 1), (-15, 150, 1), (-16, 150, 1), (-17, 150, 1), (-18, 150, 1), (-19, 150, 1), (-20, 150, 1), (-21, 150, 1), (-22, 150, 1), (-23, 150, 1), (-24, 150, 1), (-25, 150, 1), (-26, 150, 1), (-27, 150, 1), (-28, 150, 1), (-29, 150, 1), (-30, 150, 1), (-31, 150, 1), (-31, 149, 1), (-32, 149, 1), (-33, 149, 1), (-34, 149, 1), (-35, 149, 1), (-36, 149, 1), (-37, 149, 1), (-38, 149, 1), (-39, 149, 1), (-39, 148, 1), (-40, 148, 1), (-41, 148, 1), (-42, 148, 1), (-43, 148, 1), (-44, 148, 1), (-45, 147, 1), (-46, 147, 1), (-47, 147, 1), (-48, 147, 1), (-49, 147, 1), (-49, 146, 1), (-50, 146, 1), (-51, 146, 1), (-52, 146, 1), (-53, 146, 1), (-54, 145, 1), (-55, 145, 1), (-56, 145, 1), (-57, 145, 1), (-57, 144, 1), (-58, 144, 1), (-59, 144, 1), (-60, 144, 1), (-61, 143, 1), (-62, 143, 1), (-63, 143, 1), (-64, 143, 1), (-64, 142, 1), (-65, 142, 1), (-66, 142, 1), (-67, 141, 1), (-68, 141, 1), (-69, 141, 1), (-70, 140, 1), (-71, 140, 1), (-72, 140, 1), (-72, 139, 1), (-73, 139, 1), (-74, 139, 1), (-74, 138, 1), (-75, 138, 1), (-76, 138, 1), (-77, 138, 1), (-77, 137, 1), (-78, 137, 1), (-79, 137, 1), (-79, 136, 1), (-80, 136, 1), (-81, 136, 1), (-81, 135, 1), (-82, 135, 1), (-83, 135, 1), (-83, 134, 1), (-84, 134, 1), (-85, 134, 1), (-85, 133, 1), (-86, 133, 1), (-87, 133, 1), (-88, 132, 1), (-89, 132, 1), (-89, 131, 1), (-90, 131, 1), (-91, 130, 1), (-92, 130, 1), (-93, 129, 1), (-94, 129, 1), (-95, 128, 1), (-96, 128, 1), (-96, 127, 1), (-97, 127, 1), (-98, 126, 1), (-99, 126, 1), (-99, 125, 1), (-100, 125, 1), (-101, 125, 1), (-101, 124, 1), (-102, 124, 1), (-103, 123, 1), (-104, 122, 1), (-105, 122, 1), (-105, 121, 1), (-106, 121, 1), (-107, 120, 1), (-108, 120, 1), (-108, 119, 1), (-109, 119, 1), (-109, 118, 1), (-110, 118, 1), (-111, 117, 1), (-112, 117, 1), (-112, 116, 1), (-113, 116, 1), (-113, 115, 1), (-114, 115, 1), (-114, 114, 1), (-115, 114, 1), (-116, 113, 1), (-117, 113, 1), (-117, 112, 1), (-118, 112, 1), (-118, 111, 1)]


for patriarch_name, coords in patriarch_coords_dict.items():
    
    # create the Curve Datablock
    curveData = bpy.data.curves.new(patriarch_name, type='CURVE')
    curveData.dimensions = '3D'
    curveData.resolution_u = 2
    
    # map coords to spline
    polyline = curveData.splines.new('NURBS')
    polyline.points.add(len(coords))
    for i, coord in enumerate(coords):
        x,y,z = coord
        polyline.points[i].co = (x, y, z, 1)

    # create Object
    curveOB = bpy.data.objects.new(patriarch_name, curveData)

    # attach to scene and validate context
    scn = bpy.context.scene
    scn.objects.link(curveOB)
    scn.objects.active = curveOB
    curveOB.select = True