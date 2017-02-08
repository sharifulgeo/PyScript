import arcpy
w=r'C:\\Users\\Winrock\\Documents\\ArcGIS\\Packages\\Untit\\KML'
o= r"D:\Database\CREL_Database\CREL_DATABASE\SRF_Shoronkhola_Range\KMLs\\"
arcpy.env.workspace=w
f=arcpy.ListFiles()
for i in f:
    out= o+i+'.kmz'
    arcpy.LayerToKML_conversion(i,out)

