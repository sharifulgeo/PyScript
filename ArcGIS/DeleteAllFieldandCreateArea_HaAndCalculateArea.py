import arcpy

arcpy.env.overwriteOutput = True
areafieldname = 'Area_Hactres'
pth = r"C:\Users\Winrock\Documents\ArcGIS\Packages\LandscapeAreas_968FCC99-19AE-48A1-A2A6-1BAEEBBD34DB\v103\master_geodatabase.gdb"
#C:\Users\Winrock\Documents\ArcGIS\Packages\ProtectedAreas_0BAEC837-1F93-4285-AA7F-B19671FB2E9B\v103\master_geodatabase.gdb
#C:\Users\Winrock\Documents\ArcGIS\Packages\ProtectedAreas_0BAEC837-1F93-4285-AA7F-B19671FB2E9B\v103\ipac1.gdb

for r,d,fcs in arcpy.da.Walk(pth,datatype= "FeatureClass"):
    for fc in fcs:
        print fc
        p = arcpy.os.path.join(r,fc)
        fields = arcpy.ListFields(p)
        keepFields = ["OBJECTID", "Shape_Area","Shape","Shape_Length"]
        odis = [x.name for x in fields if x.name.startswith('OBJECTID')]
        keepFields = keepFields+odis
        dropFields = [x.name for x in fields if x.name not in keepFields]
        #arcpy.DeleteField_management(p, dropFields)
        arcpy.AddField_management(in_table=p, field_name = areafieldname, field_type="DOUBLE", field_precision="", field_scale="", field_length="", field_alias="", field_is_nullable="NULLABLE", field_is_required="NON_REQUIRED", field_domain="")
        exp = "!SHAPE.AREA@HECTARES!"
        arcpy.CalculateField_management(p, areafieldname, exp, "PYTHON_9.3")