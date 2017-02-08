#----------------------------------------------------------------------
# Purpose:     Updates layer properties of a layer in the ArcMap TOC
#              based on properties of an existing layer file.
#
# Author:      Ian Broad
# Website:     www.ianbroad.com
#
# Created:     10/31/2014
#----------------------------------------------------------------------

import arcpy

input_feature_class = arcpy.GetParameterAsText(0)
input_layer_file = arcpy.GetParameterAsText(1)

mxd = arcpy.mapping.MapDocument("CURRENT")
df = arcpy.mapping.ListDataFrames(mxd)[0]

layer_file_object = arcpy.mapping.Layer(input_layer_file)
original_fc_name = str(layer_file_object.name)

input_layer_object = arcpy.mapping.ListLayers(mxd, input_feature_class)[0]
input_fc_name = str(input_layer_object.datasetName)
input_fc_toc_name = str(input_layer_object.name)
input_fc_workspace = str(input_layer_object.workspacePath)

workspace_id = str(arcpy.Describe(input_fc_workspace).workspaceFactoryProgID)

if workspace_id == "esriDataSourcesGDB.AccessWorkspaceFactory.1":
     workspace_type = "ACCESS_WORKSPACE"
elif workspace_id == "esriDataSourcesGDB.FileGDBWorkspaceFactory.1":
     workspace_type = "FILEGDB_WORKSPACE"
elif workspace_id == "esriDataSourcesGDB.SdeWorkspaceFactory.1":
     workspace_type = "SDE_WORKSPACE"
else:
    workspace_type = "SHAPEFILE_WORKSPACE"

arcpy.mapping.UpdateLayer(df, input_layer_object, layer_file_object, False)

refocus_layer = arcpy.mapping.ListLayers(mxd, original_fc_name)[0]

refocus_layer.replaceDataSource(input_fc_workspace, workspace_type, input_fc_name)

refocus_layer.name = input_fc_toc_name

arcpy.RefreshTOC()