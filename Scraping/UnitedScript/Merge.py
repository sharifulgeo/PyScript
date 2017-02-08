import arcpy,os


'''
change in THREE places:
Add field change does it need??????-line 44-55
fc -line 13
wildcard -line 36
out and name in  -line 79 and line 54 for calculated field
'''


fc = r"C:\Users\Winrock\Desktop\EMOCGISSETTLEMENT\Vectors\Settlement.gdb"
arcpy.env.overwriteOutput = True
if arcpy.Exists(fc):
    print "Yes"
arcpy.env.workspace= fc#r"F:\Drives\C\Winrock\Desktop\LMet\sixmaps\Data\Up\RoadSeg\Vectors"

#fcs = []

#get all feature class
#arcpy.ListFeatureClasses(feature_type='feature')

#print type(dsets)

#for r,d,f in arcpy.da.Walk(fc):
    #for i in f:
        ##print i
        #fcs.append(os.path.join(r,i))

#ff = arcpy.ListFeatureClasses()
#print ff

#for dataset in arcpy.ListDatasets():  
    #print "Adding:", arcpy.ListFeatureClasses(feature_dataset=dataset)  
fcs = [f for f in arcpy.ListFeatureClasses("Sett_*")]# if f.startswith('slic')]     "*",'feature',None      
#fcs = arcpy.ListFeatureClasses('slic_merge1_*')#[f for f in arcpy.ListFeatureClasses(feature_type='feature') if f.endswith("slic_merge1_*")]
print len(fcs)
print fcs

##Retains Original ObjectIDs

#Add field  --Toggle the below block
#count = len(fcs)
#for i in fcs:
    #global count
    #flds = arcpy.ListFields(i)
    #fld_name = [j.name for j in flds]
    #print fld_name
    #if "Original_ID" not in fld_name:
        #table = os.path.join(fc,i)
        #print table
        #arcpy.AddField_management(in_table=table, field_name="Original_ID", field_type="LONG", field_precision="", field_scale="", field_length="", field_alias="Original_ID", field_is_nullable="NULLABLE", field_is_required="NON_REQUIRED", field_domain="")
        ##Calculate Fields
        ##arcpy.CalculateField_management(in_table=i, field="Obj_ID", expression="!RID!", expression_type="PYTHON_9.3", code_block="")
        #arcpy.CalculateField_management(in_table=table, field="Original_ID", expression="!objectid!", expression_type="PYTHON_9.3", code_block="")  
        #print "Done field processong!!!!"
    #else:
        #print "Did not Process field!!!!!!"
    #print "Processing Reamining  %s  !"%count
    #count-=1




#slice 
fcssl = [fcs[i:i+100] for i in xrange(0,len(fcs),100)]   #result = [urls[i:i+1000] for i in xrange(0, len(urls), 1000)]


#for i in fcssl:
    #print i
#fcsslice =# ''.join(i  for i in fcssl)

print fcssl
#print "Starting!"
merg_cnt = len(fcs)
nam = 0
for j in fcssl:
    print j
    global nam,merg_cnt
    out  = fc+"\Final_Sett_%s"%str(nam) ## Change Output GDB and Name too Here!!!!!!!!
    print out
    if arcpy.Exists(out):
        print "Avoided Megring since it Exists!!!!!!"
    else:
        #arcpy.SetProgressor("step","Merging FCs",0,len(fcs),1)
        print "Doing Merge! %s"%str(nam)
        arcpy.Merge_management(j,out)
        nam+=1
        print "Completed Merge %s !"%nam
    #print "Merge Raining %s"%merg_cnt
    #merg_cnt-=out.index("%")-out.index("%")-
print "Done!"


'''

arcpy.Merge_management(inputs="Lot_1;Lot_1000003;Lot_1000905;Lot_100102;Lot_1001830;Lot_1002739;Lot_1003647;Lot_1004;Lot_1004557;Lot_1005467", output="C:/Users/Winrock/Desktop/Up/Address/1.shp", field_mappings="""cadid "cadid" true true false 4 Long 0 0 ,First,#,Lot_1,cadid,-1,-1,Lot_1000003,cadid,-1,-1,Lot_1000905,cadid,-1,-1,Lot_100102,cadid,-1,-1,Lot_1001830,cadid,-1,-1,Lot_1002739,cadid,-1,-1,Lot_1003647,cadid,-1,-1,Lot_1004,cadid,-1,-1,Lot_1004557,cadid,-1,-1,Lot_1005467,cadid,-1,-1;createdate "createdate" true true false 8 Date 0 0 ,First,#,Lot_1,createdate,-1,-1,Lot_1000003,createdate,-1,-1,Lot_1000905,createdate,-1,-1,Lot_100102,createdate,-1,-1,Lot_1001830,createdate,-1,-1,Lot_1002739,createdate,-1,-1,Lot_1003647,createdate,-1,-1,Lot_1004,createdate,-1,-1,Lot_1004557,createdate,-1,-1,Lot_1005467,createdate,-1,-1;modifiedda "modifieddate" true true false 8 Date 0 0 ,First,#,Lot_1,modifieddate,-1,-1,Lot_1000003,modifieddate,-1,-1,Lot_1000905,modifieddate,-1,-1,Lot_100102,modifieddate,-1,-1,Lot_1001830,modifieddate,-1,-1,Lot_1002739,modifieddate,-1,-1,Lot_1003647,modifieddate,-1,-1,Lot_1004,modifieddate,-1,-1,Lot_1004557,modifieddate,-1,-1,Lot_1005467,modifieddate,-1,-1;controllin "controllingauthorityoid" true true false 4 Long 0 0 ,First,#,Lot_1,controllingauthorityoid,-1,-1,Lot_1000003,controllingauthorityoid,-1,-1,Lot_1000905,controllingauthorityoid,-1,-1,Lot_100102,controllingauthorityoid,-1,-1,Lot_1001830,controllingauthorityoid,-1,-1,Lot_1002739,controllingauthorityoid,-1,-1,Lot_1003647,controllingauthorityoid,-1,-1,Lot_1004,controllingauthorityoid,-1,-1,Lot_1004557,controllingauthorityoid,-1,-1,Lot_1005467,controllingauthorityoid,-1,-1;planoid "planoid" true true false 4 Long 0 0 ,First,#,Lot_1,planoid,-1,-1,Lot_1000003,planoid,-1,-1,Lot_1000905,planoid,-1,-1,Lot_100102,planoid,-1,-1,Lot_1001830,planoid,-1,-1,Lot_1002739,planoid,-1,-1,Lot_1003647,planoid,-1,-1,Lot_1004,planoid,-1,-1,Lot_1004557,planoid,-1,-1,Lot_1005467,planoid,-1,-1;plannumber "plannumber" true true false 4 Long 0 0 ,First,#,Lot_1,plannumber,-1,-1,Lot_1000003,plannumber,-1,-1,Lot_1000905,plannumber,-1,-1,Lot_100102,plannumber,-1,-1,Lot_1001830,plannumber,-1,-1,Lot_1002739,plannumber,-1,-1,Lot_1003647,plannumber,-1,-1,Lot_1004,plannumber,-1,-1,Lot_1004557,plannumber,-1,-1,Lot_1005467,plannumber,-1,-1;planlabel "planlabel" true true false 15 Text 0 0 ,First,#,Lot_1,planlabel,-1,-1,Lot_1000003,planlabel,-1,-1,Lot_1000905,planlabel,-1,-1,Lot_100102,planlabel,-1,-1,Lot_1001830,planlabel,-1,-1,Lot_1002739,planlabel,-1,-1,Lot_1003647,planlabel,-1,-1,Lot_1004,planlabel,-1,-1,Lot_1004557,planlabel,-1,-1,Lot_1005467,planlabel,-1,-1;itstitlest "ITSTitleStatus" true true false 2 Short 0 0 ,First,#,Lot_1,itstitlestatus,-1,-1,Lot_1000003,itstitlestatus,-1,-1,Lot_1000905,itstitlestatus,-1,-1,Lot_100102,itstitlestatus,-1,-1,Lot_1001830,itstitlestatus,-1,-1,Lot_1002739,itstitlestatus,-1,-1,Lot_1003647,itstitlestatus,-1,-1,Lot_1004,itstitlestatus,-1,-1,Lot_1004557,itstitlestatus,-1,-1,Lot_1005467,itstitlestatus,-1,-1;itslotid "itslotid" true true false 4 Long 0 0 ,First,#,Lot_1,itslotid,-1,-1,Lot_1000003,itslotid,-1,-1,Lot_1000905,itslotid,-1,-1,Lot_100102,itslotid,-1,-1,Lot_1001830,itslotid,-1,-1,Lot_1002739,itslotid,-1,-1,Lot_1003647,itslotid,-1,-1,Lot_1004,itslotid,-1,-1,Lot_1004557,itslotid,-1,-1,Lot_1005467,itslotid,-1,-1;stratumlev "StratumLevel" true true false 2 Short 0 0 ,First,#,Lot_1,stratumlevel,-1,-1,Lot_1000003,stratumlevel,-1,-1,Lot_1000905,stratumlevel,-1,-1,Lot_100102,stratumlevel,-1,-1,Lot_1001830,stratumlevel,-1,-1,Lot_1002739,stratumlevel,-1,-1,Lot_1003647,stratumlevel,-1,-1,Lot_1004,stratumlevel,-1,-1,Lot_1004557,stratumlevel,-1,-1,Lot_1005467,stratumlevel,-1,-1;hasstratum "HasStratum" true true false 2 Short 0 0 ,First,#,Lot_1,hasstratum,-1,-1,Lot_1000003,hasstratum,-1,-1,Lot_1000905,hasstratum,-1,-1,Lot_100102,hasstratum,-1,-1,Lot_1001830,hasstratum,-1,-1,Lot_1002739,hasstratum,-1,-1,Lot_1003647,hasstratum,-1,-1,Lot_1004,hasstratum,-1,-1,Lot_1004557,hasstratum,-1,-1,Lot_1005467,hasstratum,-1,-1;classsubty "ClassSubtype" true true false 4 Long 0 0 ,First,#,Lot_1,classsubtype,-1,-1,Lot_1000003,classsubtype,-1,-1,Lot_1000905,classsubtype,-1,-1,Lot_100102,classsubtype,-1,-1,Lot_1001830,classsubtype,-1,-1,Lot_1002739,classsubtype,-1,-1,Lot_1003647,classsubtype,-1,-1,Lot_1004,classsubtype,-1,-1,Lot_1004557,classsubtype,-1,-1,Lot_1005467,classsubtype,-1,-1;lotnumber "lotnumber" true true false 6 Text 0 0 ,First,#,Lot_1,lotnumber,-1,-1,Lot_1000003,lotnumber,-1,-1,Lot_1000905,lotnumber,-1,-1,Lot_100102,lotnumber,-1,-1,Lot_1001830,lotnumber,-1,-1,Lot_1002739,lotnumber,-1,-1,Lot_1003647,lotnumber,-1,-1,Lot_1004,lotnumber,-1,-1,Lot_1004557,lotnumber,-1,-1,Lot_1005467,lotnumber,-1,-1;sectionnum "sectionnumber" true true false 3 Text 0 0 ,First,#,Lot_1,sectionnumber,-1,-1,Lot_1000003,sectionnumber,-1,-1,Lot_1000905,sectionnumber,-1,-1,Lot_100102,sectionnumber,-1,-1,Lot_1001830,sectionnumber,-1,-1,Lot_1002739,sectionnumber,-1,-1,Lot_1003647,sectionnumber,-1,-1,Lot_1004,sectionnumber,-1,-1,Lot_1004557,sectionnumber,-1,-1,Lot_1005467,sectionnumber,-1,-1;planlotare "planlotarea" true true false 8 Double 0 0 ,First,#,Lot_1,planlotarea,-1,-1,Lot_1000003,planlotarea,-1,-1,Lot_1000905,planlotarea,-1,-1,Lot_100102,planlotarea,-1,-1,Lot_1001830,planlotarea,-1,-1,Lot_1002739,planlotarea,-1,-1,Lot_1003647,planlotarea,-1,-1,Lot_1004,planlotarea,-1,-1,Lot_1004557,planlotarea,-1,-1,Lot_1005467,planlotarea,-1,-1;planlota_1 "planlotareaunits" true true false 6 Text 0 0 ,First,#,Lot_1,planlotareaunits,-1,-1,Lot_1000003,planlotareaunits,-1,-1,Lot_1000905,planlotareaunits,-1,-1,Lot_100102,planlotareaunits,-1,-1,Lot_1001830,planlotareaunits,-1,-1,Lot_1002739,planlotareaunits,-1,-1,Lot_1003647,planlotareaunits,-1,-1,Lot_1004,planlotareaunits,-1,-1,Lot_1004557,planlotareaunits,-1,-1,Lot_1005467,planlotareaunits,-1,-1;_x_centroi "_x_centroid" true true false 8 Double 0 0 ,First,#,Lot_1,_x_centroid,-1,-1,Lot_1000003,_x_centroid,-1,-1,Lot_1000905,_x_centroid,-1,-1,Lot_100102,_x_centroid,-1,-1,Lot_1001830,_x_centroid,-1,-1,Lot_1002739,_x_centroid,-1,-1,Lot_1003647,_x_centroid,-1,-1,Lot_1004,_x_centroid,-1,-1,Lot_1004557,_x_centroid,-1,-1,Lot_1005467,_x_centroid,-1,-1;_y_centroi "_y_centroid" true true false 8 Double 0 0 ,First,#,Lot_1,_y_centroid,-1,-1,Lot_1000003,_y_centroid,-1,-1,Lot_1000905,_y_centroid,-1,-1,Lot_100102,_y_centroid,-1,-1,Lot_1001830,_y_centroid,-1,-1,Lot_1002739,_y_centroid,-1,-1,Lot_1003647,_y_centroid,-1,-1,Lot_1004,_y_centroid,-1,-1,Lot_1004557,_y_centroid,-1,-1,Lot_1005467,_y_centroid,-1,-1;urbanity "urbanity" true true false 1 Text 0 0 ,First,#,Lot_1,urbanity,-1,-1,Lot_1000003,urbanity,-1,-1,Lot_1000905,urbanity,-1,-1,Lot_100102,urbanity,-1,-1,Lot_1001830,urbanity,-1,-1,Lot_1002739,urbanity,-1,-1,Lot_1003647,urbanity,-1,-1,Lot_1004,urbanity,-1,-1,Lot_1004557,urbanity,-1,-1,Lot_1005467,urbanity,-1,-1;lotidstrin "lotidstring" true true false 50 Text 0 0 ,First,#,Lot_1,lotidstring,-1,-1,Lot_1000003,lotidstring,-1,-1,Lot_1000905,lotidstring,-1,-1,Lot_100102,lotidstring,-1,-1,Lot_1001830,lotidstring,-1,-1,Lot_1002739,lotidstring,-1,-1,Lot_1003647,lotidstring,-1,-1,Lot_1004,lotidstring,-1,-1,Lot_1004557,lotidstring,-1,-1,Lot_1005467,lotidstring,-1,-1;Shape_Leng "Shape_Leng" false true true 8 Double 0 0 ,First,#,Lot_1,Shape_Length,-1,-1,Lot_1000003,Shape_Length,-1,-1,Lot_1000905,Shape_Length,-1,-1,Lot_100102,Shape_Length,-1,-1,Lot_1001830,Shape_Length,-1,-1,Lot_1002739,Shape_Length,-1,-1,Lot_1003647,Shape_Length,-1,-1,Lot_1004,Shape_Length,-1,-1,Lot_1004557,Shape_Length,-1,-1,Lot_1005467,Shape_Length,-1,-1;Shape_Area "Shape_Area" false true true 8 Double 0 0 ,First,#,Lot_1,Shape_Area,-1,-1,Lot_1000003,Shape_Area,-1,-1,Lot_1000905,Shape_Area,-1,-1,Lot_100102,Shape_Area,-1,-1,Lot_1001830,Shape_Area,-1,-1,Lot_1002739,Shape_Area,-1,-1,Lot_1003647,Shape_Area,-1,-1,Lot_1004,Shape_Area,-1,-1,Lot_1004557,Shape_Area,-1,-1,Lot_1005467,Shape_Area,-1,-1""")


arcpy.Merge_management(inputs="Lot_1;Lot_1000003;Lot_1000905;Lot_100102;Lot_1001830;Lot_1002739;Lot_1003647;Lot_1004;Lot_1004557;Lot_1005467", output="C:/Users/Winrock/Desktop/Up/Address/1.shp", field_mappings="""cadid "cadid" true true false 4 Long 0 0 ,First,#,Lot_1,cadid,-1,-1,Lot_1000003,cadid,-1,-1,Lot_1000905,cadid,-1,-1,Lot_100102,cadid,-1,-1,Lot_1001830,cadid,-1,-1,Lot_1002739,cadid,-1,-1,Lot_1003647,cadid,-1,-1,Lot_1004,cadid,-1,-1,Lot_1004557,cadid,-1,-1,Lot_1005467,cadid,-1,-1;createdate "createdate" true true false 8 Date 0 0 ,First,#,Lot_1,createdate,-1,-1,Lot_1000003,createdate,-1,-1,Lot_1000905,createdate,-1,-1,Lot_100102,createdate,-1,-1,Lot_1001830,createdate,-1,-1,Lot_1002739,createdate,-1,-1,Lot_1003647,createdate,-1,-1,Lot_1004,createdate,-1,-1,Lot_1004557,createdate,-1,-1,Lot_1005467,createdate,-1,-1;modifiedda "modifieddate" true true false 8 Date 0 0 ,First,#,Lot_1,modifieddate,-1,-1,Lot_1000003,modifieddate,-1,-1,Lot_1000905,modifieddate,-1,-1,Lot_100102,modifieddate,-1,-1,Lot_1001830,modifieddate,-1,-1,Lot_1002739,modifieddate,-1,-1,Lot_1003647,modifieddate,-1,-1,Lot_1004,modifieddate,-1,-1,Lot_1004557,modifieddate,-1,-1,Lot_1005467,modifieddate,-1,-1;controllin "controllingauthorityoid" true true false 4 Long 0 0 ,First,#,Lot_1,controllingauthorityoid,-1,-1,Lot_1000003,controllingauthorityoid,-1,-1,Lot_1000905,controllingauthorityoid,-1,-1,Lot_100102,controllingauthorityoid,-1,-1,Lot_1001830,controllingauthorityoid,-1,-1,Lot_1002739,controllingauthorityoid,-1,-1,Lot_1003647,controllingauthorityoid,-1,-1,Lot_1004,controllingauthorityoid,-1,-1,Lot_1004557,controllingauthorityoid,-1,-1,Lot_1005467,controllingauthorityoid,-1,-1;planoid "planoid" true true false 4 Long 0 0 ,First,#,Lot_1,planoid,-1,-1,Lot_1000003,planoid,-1,-1,Lot_1000905,planoid,-1,-1,Lot_100102,planoid,-1,-1,Lot_1001830,planoid,-1,-1,Lot_1002739,planoid,-1,-1,Lot_1003647,planoid,-1,-1,Lot_1004,planoid,-1,-1,Lot_1004557,planoid,-1,-1,Lot_1005467,planoid,-1,-1;plannumber "plannumber" true true false 4 Long 0 0 ,First,#,Lot_1,plannumber,-1,-1,Lot_1000003,plannumber,-1,-1,Lot_1000905,plannumber,-1,-1,Lot_100102,plannumber,-1,-1,Lot_1001830,plannumber,-1,-1,Lot_1002739,plannumber,-1,-1,Lot_1003647,plannumber,-1,-1,Lot_1004,plannumber,-1,-1,Lot_1004557,plannumber,-1,-1,Lot_1005467,plannumber,-1,-1;planlabel "planlabel" true true false 15 Text 0 0 ,First,#,Lot_1,planlabel,-1,-1,Lot_1000003,planlabel,-1,-1,Lot_1000905,planlabel,-1,-1,Lot_100102,planlabel,-1,-1,Lot_1001830,planlabel,-1,-1,Lot_1002739,planlabel,-1,-1,Lot_1003647,planlabel,-1,-1,Lot_1004,planlabel,-1,-1,Lot_1004557,planlabel,-1,-1,Lot_1005467,planlabel,-1,-1;itstitlest "ITSTitleStatus" true true false 2 Short 0 0 ,First,#,Lot_1,itstitlestatus,-1,-1,Lot_1000003,itstitlestatus,-1,-1,Lot_1000905,itstitlestatus,-1,-1,Lot_100102,itstitlestatus,-1,-1,Lot_1001830,itstitlestatus,-1,-1,Lot_1002739,itstitlestatus,-1,-1,Lot_1003647,itstitlestatus,-1,-1,Lot_1004,itstitlestatus,-1,-1,Lot_1004557,itstitlestatus,-1,-1,Lot_1005467,itstitlestatus,-1,-1;itslotid "itslotid" true true false 4 Long 0 0 ,First,#,Lot_1,itslotid,-1,-1,Lot_1000003,itslotid,-1,-1,Lot_1000905,itslotid,-1,-1,Lot_100102,itslotid,-1,-1,Lot_1001830,itslotid,-1,-1,Lot_1002739,itslotid,-1,-1,Lot_1003647,itslotid,-1,-1,Lot_1004,itslotid,-1,-1,Lot_1004557,itslotid,-1,-1,Lot_1005467,itslotid,-1,-1;stratumlev "StratumLevel" true true false 2 Short 0 0 ,First,#,Lot_1,stratumlevel,-1,-1,Lot_1000003,stratumlevel,-1,-1,Lot_1000905,stratumlevel,-1,-1,Lot_100102,stratumlevel,-1,-1,Lot_1001830,stratumlevel,-1,-1,Lot_1002739,stratumlevel,-1,-1,Lot_1003647,stratumlevel,-1,-1,Lot_1004,stratumlevel,-1,-1,Lot_1004557,stratumlevel,-1,-1,Lot_1005467,stratumlevel,-1,-1;hasstratum "HasStratum" true true false 2 Short 0 0 ,First,#,Lot_1,hasstratum,-1,-1,Lot_1000003,hasstratum,-1,-1,Lot_1000905,hasstratum,-1,-1,Lot_100102,hasstratum,-1,-1,Lot_1001830,hasstratum,-1,-1,Lot_1002739,hasstratum,-1,-1,Lot_1003647,hasstratum,-1,-1,Lot_1004,hasstratum,-1,-1,Lot_1004557,hasstratum,-1,-1,Lot_1005467,hasstratum,-1,-1;classsubty "ClassSubtype" true true false 4 Long 0 0 ,First,#,Lot_1,classsubtype,-1,-1,Lot_1000003,classsubtype,-1,-1,Lot_1000905,classsubtype,-1,-1,Lot_100102,classsubtype,-1,-1,Lot_1001830,classsubtype,-1,-1,Lot_1002739,classsubtype,-1,-1,Lot_1003647,classsubtype,-1,-1,Lot_1004,classsubtype,-1,-1,Lot_1004557,classsubtype,-1,-1,Lot_1005467,classsubtype,-1,-1;lotnumber "lotnumber" true true false 6 Text 0 0 ,First,#,Lot_1,lotnumber,-1,-1,Lot_1000003,lotnumber,-1,-1,Lot_1000905,lotnumber,-1,-1,Lot_100102,lotnumber,-1,-1,Lot_1001830,lotnumber,-1,-1,Lot_1002739,lotnumber,-1,-1,Lot_1003647,lotnumber,-1,-1,Lot_1004,lotnumber,-1,-1,Lot_1004557,lotnumber,-1,-1,Lot_1005467,lotnumber,-1,-1;sectionnum "sectionnumber" true true false 3 Text 0 0 ,First,#,Lot_1,sectionnumber,-1,-1,Lot_1000003,sectionnumber,-1,-1,Lot_1000905,sectionnumber,-1,-1,Lot_100102,sectionnumber,-1,-1,Lot_1001830,sectionnumber,-1,-1,Lot_1002739,sectionnumber,-1,-1,Lot_1003647,sectionnumber,-1,-1,Lot_1004,sectionnumber,-1,-1,Lot_1004557,sectionnumber,-1,-1,Lot_1005467,sectionnumber,-1,-1;planlotare "planlotarea" true true false 8 Double 0 0 ,First,#,Lot_1,planlotarea,-1,-1,Lot_1000003,planlotarea,-1,-1,Lot_1000905,planlotarea,-1,-1,Lot_100102,planlotarea,-1,-1,Lot_1001830,planlotarea,-1,-1,Lot_1002739,planlotarea,-1,-1,Lot_1003647,planlotarea,-1,-1,Lot_1004,planlotarea,-1,-1,Lot_1004557,planlotarea,-1,-1,Lot_1005467,planlotarea,-1,-1;planlota_1 "planlotareaunits" true true false 6 Text 0 0 ,First,#,Lot_1,planlotareaunits,-1,-1,Lot_1000003,planlotareaunits,-1,-1,Lot_1000905,planlotareaunits,-1,-1,Lot_100102,planlotareaunits,-1,-1,Lot_1001830,planlotareaunits,-1,-1,Lot_1002739,planlotareaunits,-1,-1,Lot_1003647,planlotareaunits,-1,-1,Lot_1004,planlotareaunits,-1,-1,Lot_1004557,planlotareaunits,-1,-1,Lot_1005467,planlotareaunits,-1,-1;_x_centroi "_x_centroid" true true false 8 Double 0 0 ,First,#,Lot_1,_x_centroid,-1,-1,Lot_1000003,_x_centroid,-1,-1,Lot_1000905,_x_centroid,-1,-1,Lot_100102,_x_centroid,-1,-1,Lot_1001830,_x_centroid,-1,-1,Lot_1002739,_x_centroid,-1,-1,Lot_1003647,_x_centroid,-1,-1,Lot_1004,_x_centroid,-1,-1,Lot_1004557,_x_centroid,-1,-1,Lot_1005467,_x_centroid,-1,-1;_y_centroi "_y_centroid" true true false 8 Double 0 0 ,First,#,Lot_1,_y_centroid,-1,-1,Lot_1000003,_y_centroid,-1,-1,Lot_1000905,_y_centroid,-1,-1,Lot_100102,_y_centroid,-1,-1,Lot_1001830,_y_centroid,-1,-1,Lot_1002739,_y_centroid,-1,-1,Lot_1003647,_y_centroid,-1,-1,Lot_1004,_y_centroid,-1,-1,Lot_1004557,_y_centroid,-1,-1,Lot_1005467,_y_centroid,-1,-1;urbanity "urbanity" true true false 1 Text 0 0 ,First,#,Lot_1,urbanity,-1,-1,Lot_1000003,urbanity,-1,-1,Lot_1000905,urbanity,-1,-1,Lot_100102,urbanity,-1,-1,Lot_1001830,urbanity,-1,-1,Lot_1002739,urbanity,-1,-1,Lot_1003647,urbanity,-1,-1,Lot_1004,urbanity,-1,-1,Lot_1004557,urbanity,-1,-1,Lot_1005467,urbanity,-1,-1;lotidstrin "lotidstring" true true false 50 Text 0 0 ,First,#,Lot_1,lotidstring,-1,-1,Lot_1000003,lotidstring,-1,-1,Lot_1000905,lotidstring,-1,-1,Lot_100102,lotidstring,-1,-1,Lot_1001830,lotidstring,-1,-1,Lot_1002739,lotidstring,-1,-1,Lot_1003647,lotidstring,-1,-1,Lot_1004,lotidstring,-1,-1,Lot_1004557,lotidstring,-1,-1,Lot_1005467,lotidstring,-1,-1;Shape_Leng "Shape_Leng" false true true 8 Double 0 0 ,First,#,Lot_1,Shape_Length,-1,-1,Lot_1000003,Shape_Length,-1,-1,Lot_1000905,Shape_Length,-1,-1,Lot_100102,Shape_Length,-1,-1,Lot_1001830,Shape_Length,-1,-1,Lot_1002739,Shape_Length,-1,-1,Lot_1003647,Shape_Length,-1,-1,Lot_1004,Shape_Length,-1,-1,Lot_1004557,Shape_Length,-1,-1,Lot_1005467,Shape_Length,-1,-1;Shape_Area "Shape_Area" false true true 8 Double 0 0 ,First,#,Lot_1,Shape_Area,-1,-1,Lot_1000003,Shape_Area,-1,-1,Lot_1000905,Shape_Area,-1,-1,Lot_100102,Shape_Area,-1,-1,Lot_1001830,Shape_Area,-1,-1,Lot_1002739,Shape_Area,-1,-1,Lot_1003647,Shape_Area,-1,-1,Lot_1004,Shape_Area,-1,-1,Lot_1004557,Shape_Area,-1,-1,Lot_1005467,Shape_Area,-1,-1""")

'''
