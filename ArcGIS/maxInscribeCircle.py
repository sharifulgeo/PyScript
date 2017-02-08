'''

Note it is very slow (10 polygons like one on the picture per second). Try on selection and use reasonable tolerance.

There is faster raster solution:

Convert polygons to outlines
Calculate Euclidean distance
Convert polygons to raster
Calculate Zonal statistics (max)
Raster calculator Con (abs(distance-max)
Convert to points
Spatial join to polygons and remove duplicates of points. Raster value field in points is radius of max circle to fit into your polygon. Control precision by cell size, does not work for overlapping polygons



'''


import arcpy, traceback, os, sys

from arcpy import env

env.overwriteOutput = True

infc = arcpy.GetParameterAsText(0)

outfc=arcpy.GetParameterAsText(1)

tolerance=float(arcpy.GetParameterAsText(2))

d=arcpy.Describe(infc)

SR=d.spatialReference

try:
    def showPyMessage():

        arcpy.AddMessage(str(time.ctime()) + " - " + message)

    theFolder,theFile=os.path.split(outfc)
    arcpy.CreateFeatureclass_management(theFolder, theFile, "POINT", infc, "DISABLED", "DISABLED", SR)
    arcpy.AddField_management(outfc, "theDist", "DOUBLE")
    shapefield,fidName = d.ShapeFieldName,d.OIDFieldName
    fileds2add=[]
    fields = [f.name for f in arcpy.ListFields(infc)]
    for f in fields:
        if f not in (shapefield,fidName,"Shape_Length","Shape_Area"):
            fileds2add.append(f)
    tbl=arcpy.da.TableToNumPyArray(infc,fileds2add)
    nF=len(tbl)

    arcpy.SetProgressor("step", "", 0, nF,1)
    arcpy.AddMessage("Creating points... ")
    fileds2add=["SHAPE@","theDist"]+fileds2add
    curT = arcpy.da.InsertCursor(outfc,fileds2add)
    theM=0
    with arcpy.da.SearchCursor(infc, "SHAPE@") as rows:
        for row in rows:
            feat = row[0]; prt=feat.getPart(0)
            feat=arcpy.Polygon(prt,SR)
            outLine=feat.boundary(); pSave=feat.trueCentroid
            d=outLine.distanceTo(pSave)
            if d<=tolerance:break
            while (True):
                theLine=feat.boundary()
                p=feat.labelPoint                
                d=theLine.distanceTo(p)
                try:
                    buf=theLine.buffer(d)
                except:
                    pSave=feat.labelPoint
                    break
                intR=feat.difference(buf)
                n=intR.partCount;aMax=0
                for i in xrange (n):
                    prt=intR.getPart(i)
                    pgon=arcpy.Polygon(prt,SR)
                    aCur=pgon.area
                    if aCur>aMax:
                        aMax=aCur;feat=pgon
                pN=feat.labelPoint
                d=arcpy.PointGeometry(p).distanceTo(pN)
                if d<=tolerance:
                    pSave=pN; break
            d=outLine.distanceTo(pSave)
            theRow=[pSave,d]; theP=list(tbl[theM])
            theRow+=theP
            curT.insertRow(theRow)
            theM+=1
            arcpy.SetProgressorPosition()
    del tbl

except:

    message = "\n*** PYTHON ERRORS *** "; showPyMessage()
    message = "Python Traceback Info: " + traceback.format_tb(sys.exc_info()[2])[0]; showPyMessage()
    message = "Python Error Info: " +  str(sys.exc_type)+ ": " + str(sys.exc_value) + "\n"; showPyMessage()