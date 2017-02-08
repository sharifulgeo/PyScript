import arcpy
arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"C:\Users\USER_NAME\Documents\ArcGIS\my.gdb"
fcs = arcpy.ListFeatureClasses("One*") # select all fatures Starts with "One"
fc= []
pattern ="domain" # Merge all fetaures that have word "domain" in the name
output = "C:\Users\USER_NAME\Documents\ArcGIS\my.gdb\merged"
for i in fcs:
    if pattern in i:
        fc.append(i)
        arcpy.Merge_management(fc,output)
