import arcpy,os,sys
arcpy.env.workspace= r"D:\Database\CREL_Database\CREL_DATABASE\Master_Geodatabase.gdb"
d=arcpy.ListDatasets()
for i in d:
    print i

