'''
Alg:

Read polygon vertex coordinate
itertool combination



'''












import arcpy,os,sys
points = []
with arcpy.da.SearchCursor(r"C:\Users\Winrock\Documents\ArcGIS\Default.gdb\se",['SHAPE@']) as cursor:
     for row in cursor:
         centroid = row[0].centroid
         dist = 0
         for part in row[0]:
             for pnt in part:
                 cent_vert_dist = arcpy.PointGeometry(pnt).distanceTo(centroid)
                 if cent_vert_dist > dist:
                     dist = cent_vert_dist   
                     far_point = arcpy.PointGeometry(pnt)
         points.append(far_point)         
arcpy.CopyFeatures_management(points,'in_memory\points')

##Example for Points
import arcpy,os,sys
ar = []  ## standard array works here
ar.append(arcpy.PointGeometry(arcpy.Point(X=90.3561,Y=20.5671)))
arcpy.CopyFeatures_management(ar,r"C:\Users\Winrock\Documents\ArcGIS\Point_1.shp")



##Example for Polyline
ptList =[[20.000,43.000],[25.500, 45.085],[26.574, 46.025]]
pt = arcpy.Point()
ptGeoms =arcpy.Array() ## you must use arcpy array here
for p in ptList:
     pt.x = p[0]
     pt.Y = p[1]
     ptGeoms.add(pt)
polyline= arcpy.Polyline(ptGeoms)

arcpy.CopyFeatures_management(polyline, 'in_memory\lines')

##get coordinate of vertex of polygons

import arcpy

infc = 'in_memory\lines'

# Enter for loop for each feature
#
for row in arcpy.da.SearchCursor(infc, ["SHAPE@XY"]):
    # Print x,y coordinates of each point feature
    #
     x, y = row[0]
     print("{0}, {1}".format(x, y))















##Reading polygon geometry in arcpy. Here you can read the coordinate of the vertices of the each polygon
import arcpy

infc = r"C:\Users\Winrock\Documents\ArcGIS\delete.shp"

# Enter for loop for each feature
#
for row in arcpy.da.SearchCursor(infc, ["OID@", "SHAPE@"]):
    # Print the current multipoint's ID
    #
     print("Feature {0}:".format(row[0]))
     #print len(row[0])
     partnum = 0

    # Step through each part of the feature
    #
     for part in row[1]:
        # Print the part number
        #
          print("Part {0}:".format(partnum))

        # Step through each vertex in the feature
        #
          for pnt in part:
               if pnt:
                # Print x,y coordinates of current point
                #
                    print("{0}, {1}".format(pnt.X, pnt.Y))
          else:
                # If pnt is None, this represents an interior ring
                #
               print("Interior Ring:")
               partnum += 1
               
               
               
##Copy all feature into arcpy geometry objects and work natively

import arcpy

# Run the CopyFeatures tool, setting the output to the geometry object.
# geometries is returned as a list of geometry objects.
geometries = arcpy.CopyFeatures_management(r"C:\Users\Winrock\Documents\ArcGIS\delete.shp",
                                           arcpy.Geometry())

# Walk through each geometry, totalling the length
length = 0
for geometry in geometries:
     length += geometry.length
     pnt = geometry.trueCentroid
     print pnt.X

print("Total length: {0}".format(length))
               
