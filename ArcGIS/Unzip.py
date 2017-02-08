import zipfile  
import arcpy,os,os.path,sys
from arcpy import env


pattern = '.zip'
folder = r"C:\Users\Winrock\Desktop\ziptest" 
files_process = []

def unzip(inp,out):
    zipp=zipfile.ZipFile(inp,'r')
    zipp.extractall(path=None, members=None, pwd=None)
for root,dirs,files in os.walk(folder):
    for filenames in files:
        if filenames.endswith(pattern):
            files_process.append(os.path.join(root, filenames))
            for i in files_process:
                #zip_ref = zipfile.ZipFile(i, 'r')
                #zip_ref.extractall(i)
                #zip_ref.close()                
                z = zipfile.ZipFile(i)
                print i
                for f in z.namelist():
                    print f
                    if f.endswith('zip'):
                        os.makedirs(f)
                        