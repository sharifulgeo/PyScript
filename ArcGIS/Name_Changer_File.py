import arcpy,os
for r,d,f in os.walk(r'F:\CREL_GDB_COPY\CREL_DB'):
    for i in f:
        if "LC" in i:
            p= os.path.join(r,i)
            newp = os.path.join(r,p.split("\\")[-1].replace("LC","Landcover"))
            print p
            os.rename(p,newp)