import urllib
import urllib2
import requests
"""
print "downloading with urllib"
urllib.urlretrieve(url, "code.zip")
"""
def fetc (whr):
    try:
        print type(whr)
        qry = "OBJECTID>"+str(whr)
        print type(qry)
        name = str(whr)+".zip"
        print type(name)
        urllib.urlretrieve('http://203.190.254.41:6080/arcgis/rest/services/emoc/Mapserver/12/query?where='+qry+'&text=&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&relationParam=&outFields=*&returnGeometry=true&maxAllowableOffset=&geometryPrecision=&outSR=&returnIdsOnly=false&returnCountOnly=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&returnZ=false&returnM=false&gdbVersion=&f=kmz',name)
        #urllib2.urlopen('http://203.112.218.67/arcgis/rest/services/bbs84/MapServer/5/query?where='+whr+'&text=&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&relationParam=&outFields=*&returnGeometry=true&maxAllowableOffset=&geometryPrecision=&outSR=&returnIdsOnly=false&returnCountOnly=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&returnZ=false&returnM=false&gdbVersion=&f=kmz')
    except urllib2.HTTPError, e:
        print(e.code)
    except urllib2.URLError, e:
        print(e.args)

##Total 157202 objectids
i =150000   
while i <160000:
    i = i+1000
    fetc(i)
    
    
