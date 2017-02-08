import arcpy

r = arcpy.Raster(in_raster)
point = arcpy.Point()
array = arcpy.Array()

corners = ["lowerLeft", "lowerRight", "upperRight", "upperLeft"]

cursor = arcpy.InsertCursor(fc)
feat = cursor.newRow()
for corner in corners:    
    point.X = getattr(r.extent, "%s" % corner).X
    point.Y = getattr(r.extent, "%s" % corner).Y
    array.add(point)
array.add(array.getObject(0))
print len(array)
polygon = arcpy.Polygon(array)
feat.shape = polygon
cursor.insertRow(feat)
array.removeAll()
del feat
del cursor