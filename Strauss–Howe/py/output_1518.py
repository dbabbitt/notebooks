
import bpy

# Get spiral data
patriarch_coords_dict = {}
patriarch_coords_dict['(No Name), Sr.'] = [(125, 8, 1)]


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