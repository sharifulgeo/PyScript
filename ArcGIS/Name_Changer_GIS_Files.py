import arcpy,os
counter = 0
for r,d,f in arcpy.da.Walk(r'C:\Users\Winrock\Desktop\CREL_SITES\GISDATA\Landscapes.gdb',datatype= "FeatureClass"):
    for i in f:
        global counter
        counter = counter+1
        p = arcpy.os.path.join(r,i)
        print p
        if "IRF" in i:
            #newName = i.replace ("lu","LC")
            arcpy.Rename_management(p,p.replace("LA","Landscape_"))
        print p
print counter
