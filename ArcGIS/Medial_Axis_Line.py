##Reading polygon geometry in arcpy. Here you can read the coordinate of the vertices of the each polygon
import arcpy,os,sys,itertools

infc = r"C:\Users\Winrock\Documents\ArcGIS\delete.shp"
arr = []
mid_pnt = []
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
                    print("{0}, {1}".format(pnt.X,pnt.Y))
                    
                    #arr.append(pnt.X,pnt.Y)
                    XX= str(pnt.X)
                    YY = str(pnt.Y)
                    pnts  = '('+XX+','+YY+')'
                    ar.append(pnts)
                    #for pair in itertools.combinations(for i in ar,2):
                         #print pair
                    
          else:
                # If pnt is None, this represents an interior ring
                #
               print("Interior Ring:")
               partnum += 1              


#arcpy.CopyFeatures_management(ar, 'in_memory\lines')
##curI = arcpy.da.InsertCursor(arr,"n_memory\mid_line.shp")

#for i in itertools.combinations