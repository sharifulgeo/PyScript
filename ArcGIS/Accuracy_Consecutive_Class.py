rec = 0
def x():
    global rec
    s=1
    I=1
    if (rec==0):
        rec = s
    else:
        rec =rec+I
    return str(rec)

!Class_name!+"_"+x()

# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "fishnet"
arcpy.CalculateField_management("fishnet","ID","x()","PYTHON","rec = 0/ndef x():/n    global rec/n    s=1/n    I=1/n    if (rec==0):/n        rec = s/n    else:/n        rec =rec+I/n    return str(rec)")


"rec = 0/ndef x():/n    global rec/n    s=1/n    I=1/n    if (rec==0):/n        rec = s/n    else:/n        rec =rec+I/n    return str(rec)







for i in fc:
...     arcpy.ExportCAD_conversion(i,"DWG_R2010",r'C:\\test_script\\export\ID_'+str(i),"Use_Filenames_in_Tables","Append_To_Existing_Files","")
...     scribe geometry object object at 0x320C94C0>
>>> 