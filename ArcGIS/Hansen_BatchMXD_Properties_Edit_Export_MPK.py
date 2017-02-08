import arcpy,os,sys


mxd_path=r'D:\BCASProjects\CREL\Co-Management\CWS\CWS_a4.mxd'

Map_title = "Chunati WS Total Forest Loss (2001-2012)"

mpk_path =r'D:\Database\CREL_Database\CREL_DATABASE\Satchari_National_Park\MPKs'




full_mpk_path = os.path.join(mpk_path,Map_title+'_Hansen_Analysis')
mxd=arcpy.mapping.MapDocument('CURRENT')
mxd.title= Map_title
mxd.summary="These data is generated from Rapid Eye (2013-2014) and Landsat images are used"
mxd.description="This map is produced after an analysis of Hansen data and RapidEye images to track the land cover change over 12 years (2001-20012) in the CREL sites."
mxd.author="CREL"
mxd.credits="CREL,BCAS"
mxd.tags="Hansen,Landcover Change"
mxd.hyperlinkBase = mxd_path.split("'")[0]
mxd.relativePaths = 'True'
arcpy.RefreshTOC()

arcpy.PackageMap_management(mxd_path,full_mpk_path+'.mpk',"CONVERT","PRESERVE_ARCSDE","DISPLAY","ALL","DESKTOP","NOT_REFERENCED","ALL")
