import arcpy

arcpy.env.overwriteOutput = True

pth = r"C:\Users\Winrock\Documents\ArcGIS\Packages\ProtectedAreas_E2D35D8B-F6A3-4E6A-932B-248E04EBC8FD\v103\ipac1.gdb"
#C:\Users\Winrock\Documents\ArcGIS\Packages\ProtectedAreas_E2D35D8B-F6A3-4E6A-932B-248E04EBC8FD\v103\master_geodatabase.gdb
#C:\Users\Winrock\Documents\ArcGIS\Packages\ProtectedAreas_E2D35D8B-F6A3-4E6A-932B-248E04EBC8FD\v103\ipac1.gdb

areafieldname = 'Area_Hactres'

for r,d,fcs in arcpy.da.Walk(pth,datatype= "FeatureClass"):
    for fc in fcs:
        print fc
        p = arcpy.os.path.join(r,fc)
        fields = arcpy.ListFields(p)
        keepFields = ["OBJECTID", "Shape_Area","Shape","Shape_Length"]
        odis = [fields[0].name]#[x.name for x in fields if x.name.startswith('OBJECTID')]
        keepFields = list(set(keepFields+odis))
        #Some featureclass needs to keep the other fields e.g. to keep the block/beat name for Himchari NP
        if 'hws' in fc.lower() or 'hlh' in fc.lower() or 'hnp' in fc.lower() or 'cws' in fc.lower() or 'bdnp' in fc.lower():
            arcpy.DeleteField_management(p, 'Area_Ha')
            arcpy.AddField_management(in_table=p, field_name=areafieldname, field_type="DOUBLE", field_precision="", field_scale="", field_length="", field_alias="", field_is_nullable="NULLABLE", field_is_required="NON_REQUIRED", field_domain="")
            exp = "!SHAPE.AREA@HECTARES!"
            arcpy.CalculateField_management(p, areafieldname, exp, "PYTHON_9.3")            
        else:
            dropFields = [x.name for x in fields if x.name not in keepFields]
            arcpy.DeleteField_management(p, dropFields)
            arcpy.AddField_management(in_table=p, field_name=areafieldname, field_type="DOUBLE", field_precision="", field_scale="", field_length="", field_alias="", field_is_nullable="NULLABLE", field_is_required="NON_REQUIRED", field_domain="")
            exp = "!SHAPE.AREA@HECTARES!"
            arcpy.CalculateField_management(p, areafieldname, exp, "PYTHON_9.3")