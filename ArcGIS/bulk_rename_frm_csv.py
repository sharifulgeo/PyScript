import os
import csv
import re
import glob
import shutil
 
#CSV File Location. Use the absolute path to the csv file.
csv_file = "C:/Users/Winrock/Desktop/CREL_BD_Structure.csv"
 
#Base Dir of the folders that should be renamed. Use the 
#absolute path.
base_dir = "F:/GIS_Documents/CREL_DB/New Folder"
 
# Set the index (column) of the CSV file the contains
# the current and new directory names.
curr_dir_index = 0
new_dir_index = 2
 
 
# Filename sanitation. Based off Django Framework.
# Solution found on:
# http://stackoverflow.com/questions/295135
# /turn-a-string-into-a-valid-filename-in-python
def slugify(value):
 
    """
    Normalizes string, converts to lowercase, removes non-alpha characters,
    and converts spaces to hyphens.
    """
    import unicodedata
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore')
    value = unicode(re.sub('[^\w\s-]', '', value).strip().lower())
    value = re.sub('[-\s]+', '-', value)
    return value
 
 
def batch_rename(csv_file, base_url):
 
    """
    ASSUMPTIONS:
        - The CSV file columns with the current and desired directory names will
        ONLY contain the name of the directory, not the path to the directory.
        The base_dir path should be set accordingly to the base of the dir.

    LOGIC:
        - For every row of the CSV file, check to see if the current directory
            exists.

            - If it does, check to see if the desired directory name also
            exists.
                - If the desired directory DOES NOT exist, then rename the
                    folder to the desired name.
                - If the desired directory DOES exist, then move all files
                    contained within the current directory to the new folder
                    that already exists.
    """
    # with open(csv_file, 'rb') as csvfile:
    csv_read = csv.reader(open(csv_file, "rbU"))
    for row in csv_read:
 
        # Pull the data from each column
        curr_dir_name = row[curr_dir_index]
        new_dir_name = slugify(unicode(row[new_dir_index]))
 
        # Append the base_url
        path_to_curr_dir = base_dir + curr_dir_name
        path_to_renamed_dir = base_dir + new_dir_name
 
        # Check to see if the current directory in the CSV
        # file actually exists.
        if(os.path.exists(path_to_curr_dir)):
            # There could be a case where the desired rename directory
            # already exists. If this is the case, we need to account
            # for it.
            if(os.path.exists(path_to_renamed_dir)):
                # The desired directory already exists. We should move the
                # file in this directory into the already created directory
                files_in_curr_dir = glob.glob(path_to_curr_dir + "/*.*")
                for f in files_in_curr_dir:
                    #move each file to the existing folder that has the
                    #same name as what the renamed folder would have been
                    shutil.move(f,
                        path_to_renamed_dir + '/' + os.path.basename(f))
            else:
                # The desired directory does not exist yet.
                shutil.move(path_to_curr_dir, path_to_renamed_dir)
 
            if(os.path.exists(path_to_renamed_dir)):
                print "Rename: Sucessful"
            else:
                print "Rename: FAILED"
 
        else:
            print curr_dir_name + ": Folder does NOT exist"
 
batch_rename(csv_file, base_dir)
