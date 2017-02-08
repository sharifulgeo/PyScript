
import arcpy

# Script arguments
Search_Distance = arcpy.GetParameterAsText(0)

Selection_type = arcpy.GetParameterAsText(1)
if Selection_type == '#' or not Selection_type:
    Selection_type = "NEW_SELECTION" # provide a default value if unspecified

Source_Layer = arcpy.GetParameterAsText(2)

Relationship = arcpy.GetParameterAsText(3)
if Relationship == '#' or not Relationship:
    Relationship = "INTERSECT" # provide a default value if unspecified

Target_Layers__Select_From_ = arcpy.GetParameterAsText(4)

Output_Layer_Name = arcpy.GetParameterAsText(5)

Output_Layer = arcpy.GetParameterAsText(6)

Workspace_or_Feature_Dataset = arcpy.GetParameterAsText(7)

# Local variables:

# Process: Select Layer By Location
arcpy.SelectLayerByLocation_management(Target_Layers__Select_From_, Relationship, Source_Layer, Search_Distance, Selection_type)

# Process: Make Feature Layer
arcpy.MakeFeatureLayer_management(Output_Layer_Name, Output_Layer, "", Workspace_or_Feature_Dataset, "")

