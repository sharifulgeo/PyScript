import arcpy,os,glob
arcpy.env.overwriteOutput= True
root_folder = "D:\BCASProjects\CREL\Carbon_Inentory\Carbon Inventory 3rd Year\Site Boundary\Geodatabase"
mxdList = glob.glob(root_folder+'\\'+'*.mxd')


for i in mxdList:
    path = i.replace('\\',"\\\\")
    out = i.replace('.mxd','.jpg')
    inp = arcpy.mapping.MapDocument(path)
    AI = out.replace('jpg','ai')
    #df = arcpy.mapping.ListDataFrames(inp,"LAYERS")
    arcpy.mapping.ExportToJPEG(inp,out,data_frame="PAGE_LAYOUT",resolution=300,color_mode='24-BIT_TRUE_COLOR')
    arcpy.mapping.ExportToAI(inp, AI, data_frame='PAGE_LAYOUT',resolution=350,image_quality='BEST',colorspace='CMYK')
del inp,out
#arcpy.mapping.ExportToAI(inp, AI, data_frame='PAGE_LAYOUT',resolution=350,image_quality='BEST',colorspace='CMYK')
