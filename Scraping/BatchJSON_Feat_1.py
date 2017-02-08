import os,sys,arcpy
arcpy.env.overwriteOutput = True

'''
change in three places:

location -line 13
output -line 28
name  -line 26
'''
#F:\Drives\C\Winrock\Desktop\LMet\sixmaps\Data\Property\Vectors\Property.gdb

location = r"C:\Users\Winrock\Desktop\EMOCGISSETTLEMENT\JSData"
arcpy.env.workspace = location #r"F:\Drives\C\Winrock\Desktop\LMet\sixmaps\Data\Address\Vectors\New File Geodatabase.gdb"
arcpy.env.overwriteOutput = 1
#I:\Drives\C\Winrock\Desktop\LMet\sixmaps\Data\DwellingBldg\Vectors\New File Geodatabase.gdb
f = arcpy.ListFiles()
files = []
for i in f:
    files.append(os.path.join(location,i))
  

#print files
shps = []
for i in files:
    name = "Sett_"+i.split("\\")[-1].replace(".json","")
    print name
    output = os.path.join(location.replace("\JSData",""),"Vectors","Settlement.gdb",name)#.replace("\","/")
    print output
    shps.append(output)
    if arcpy.Exists(output):
        print "Avoid It!"
        #arcpy.JSONToFeatures_conversion(i,output)
    else:
        print "Do It! %s"%output
        arcpy.JSONToFeatures_conversion(i,output)


#merged = os.path.join(location.replace("\JSON",""),"Vectors","Merged")
#print merged
#print shps
#arcpy.Merge_management(shps,merged)
