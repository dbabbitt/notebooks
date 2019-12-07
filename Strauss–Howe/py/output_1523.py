
import bpy

# Get spiral data
patriarch_coords_dict = {}
patriarch_coords_dict['(No Name), Sr.'] = [(125, 8, 1), (125, 9, 1), (125, 10, 1), (125, 11, 1), (125, 12, 1), (125, 13, 1), (125, 14, 1), (125, 15, 1), (125, 16, 1), (125, 17, 1), (125, 18, 1), (125, 19, 1), (125, 20, 1), (125, 21, 1), (125, 22, 1), (125, 23, 1), (125, 24, 1), (125, 25, 1), (125, 26, 1), (125, 27, 1), (125, 28, 1), (125, 29, 1), (125, 30, 1), (125, 31, 1), (124, 31, 1), (124, 32, 1), (124, 33, 1), (124, 34, 1), (124, 35, 1), (124, 36, 1), (124, 37, 1), (124, 38, 1), (123, 38, 1), (123, 39, 1), (123, 40, 1), (123, 41, 1), (123, 42, 1), (123, 43, 1), (122, 43, 1), (122, 44, 1), (122, 45, 1), (122, 46, 1), (122, 47, 1), (121, 47, 1), (121, 48, 1)]


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