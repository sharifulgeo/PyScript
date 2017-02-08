import urllib
import urllib2
import requests
"""
print "downloading with urllib"
urllib.urlretrieve(url, "code.zip")
"""
urls = ['http://maps.six.nsw.gov.au/arcgis/rest/services/sixmaps/Boundaries/MapServer/'+ str(i)+'/query' for i in range(0,23)]

def fetc (link,whr):
    try:
        print type(whr)
        qry = "OBJECTID<"+str(whr)
        print type(qry)
        print qry
        name = str(whr)+"__"+link.split("/")[-2]+".zip"
        print type(name)
        whr = str(whr)
        urllib.urlretrieve(link+'?text=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&relationParam=&objectIds=&where='+qry+'&time=&returnCountOnly=false&returnIdsOnly=false&returnGeometry=true&maxAllowableOffset=&outSR=&outFields=*&f=kmz',name)
        #urllib.urlretrieve(link+'?where='+qry+'&text=&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&relationParam=&outFields=*&returnGeometry=true&maxAllowableOffset=&geometryPrecision=&outSR=&returnIdsOnly=false&returnCountOnly=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&returnZ=false&returnM=false&gdbVersion=&f=kmz',name)
        #urllib.urlretrieve(link+'?text=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&relationParam=&objectIds=&where='+whr+'&time=&returnCountOnly=false&returnIdsOnly=false&returnGeometry=true&maxAllowableOffset=&outSR=&outFields=*&f=kmz')
        #urllib.urlretrieve(link+'?where='+qry+'&text=&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&relationParam=&outFields=*&returnGeometry=true&maxAllowableOffset=&geometryPrecision=&outSR=&returnIdsOnly=false&returnCountOnly=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&returnZ=false&returnM=false&gdbVersion=&f=kmz',name)
        #urllib2.urlopen('http://203.112.218.67/arcgis/rest/services/bbs84/MapServer/5/query?where='+whr+'&text=&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&relationParam=&outFields=*&returnGeometry=true&maxAllowableOffset=&geometryPrecision=&outSR=&returnIdsOnly=false&returnCountOnly=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&returnZ=false&returnM=false&gdbVersion=&f=kmz')
    except urllib2.HTTPError, e:
        print(e.code)
    except urllib2.URLError, e:
        print(e.args)

##Total 157202 objectids
#for url in urls:
    #i =150000   
    #while i <160000:
        #i = i+1000
        #print i
        #print url
        #fetc(url,i)
        #print 'Completed: ',i
for i in urls:
    fetc(i,100)
    print "Completed: ",i
    
