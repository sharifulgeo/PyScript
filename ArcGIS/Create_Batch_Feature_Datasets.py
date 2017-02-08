import arcpy,os,sys
from arcpy import env
gdb = r'\\UMMESALMA\CREL_GIS_Database\CREL_DB\Master_Geodatabase.gdb'
env.workspace = gdb
gdb = r'\\UMMESALMA\CREL_GIS_Database\CREL_DB\Master_Geodatabase.gdb'
site46 = ["BDNP","CWS","DDWS","FKWS","HH","HHLNP","HWS","HNP","IRF","KNP","KhNP","LNP","MNP","MKNP","NNP","RRF","RKWS","SMECA","SNP","SECA","TH","TWS","TGWS"]
site45 = ["Chandpai_Range","SSWS","SWWS","SEWS"]
WGS_1984_UTM_Zone_46N = "PROJCS['WGS_1984_UTM_Zone_46N',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',500000.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',93.0],PARAMETER['Scale_Factor',0.9996],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]];-5120900 -9998100 10000;-100000 10000;-100000 10000;0.001;0.001;0.001;IsHighPrecision"

WGS_1984_UTM_Zone_45N = "PROJCS['WGS_1984_UTM_Zone_45N',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',500000.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',87.0],PARAMETER['Scale_Factor',0.9996],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]];-5120900 -9998100 10000;-100000 10000;-100000 10000;0.001;0.001;0.001;IsHighPrecision"
for i in site46:
    if arcpy.Exists(i):
        print i +'  alreday exists'
    else:
        arcpy.CreateFeatureDataset_management(gdb,i,WGS_1984_UTM_Zone_46N)
for i in site45:
    if arcpy.Exists(i):
        print i +'  alreday exists'
    else:
        arcpy.CreateFeatureDataset_management(gdb,i,WGS_1984_UTM_Zone_45N)

#arcpy.CreateFeatureDataset_management("//UMMESALMA/CREL_GIS_Database/CREL_DB/Master_Geodatabase.gdb","BNDP",)
#arcpy.CreateFeatureDataset_management("C:/Users/Winrock/Documents/ArcGIS/Default.gdb","try45","PROJCS['WGS_1984_UTM_Zone_45N',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',500000.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',87.0],PARAMETER['Scale_Factor',0.9996],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]];-5120900 -9998100 10000;-100000 10000;-100000 10000;0.001;0.001;0.001;IsHighPrecision")
