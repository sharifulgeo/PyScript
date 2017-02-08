# Feature Class or Table Name; fc means feature class.
# You'll need to change "hssanitation_24122014" to your table name with double quotes; i.e., Shift + single quote.
# And of cource, you'll need to add your file into arcmap TOC before running this script.
fc = "hssanitation_24122014"

# Field or Fields Name
# To Summarize all the fields in a table use this.
# For this case please delete or comment out line 18
fl = [] # fl stands for field
for i in arcpy.ListFields(fc):
    # Nothing good comes out of summarizing OID, FID or any field with unique values.
    # It's better to skip OID, FID and such
    if i.name not in ['OID', ]: # you can add other field(s) with unique value after the comma with singe quote
        fl.append(str(i.name))

# Or you can provide your own field list for summarizing. Best practice is to specify your fields
# In this case please delete or comment out lines 8, 9, 12, 13
fl = ['impr_latr', 'hyg_latr', 'impr_hyg', 'impr_latr1', 'impr_hyg1', 'impr_latr2', 'impr_hyg2']

# Setting the output text file path
import os
cwd = os.path.expanduser("~")
fname1 = "summary1.txt" # change the name as you like
fname2 = str(cwd) + "\\Documents\\" + fname1
fwrite = open(fname2, 'w') # this will create a summury1.txt file on your My Documents folder

# Alternate Documents path setting
# If you use alternate Python executables like Anaconda or WinPython,
# above output path settings won't work.
# Comment out line 21-25
import getpass
# get current user name
cuser = getpass.getuser() # it gets logged in user name
fname1 = "summary1.txt" # change the name as you like
fname2 = "C:\\Users\\" + str(cuser) + "\\Documents\\" + fname1
fwrite = open(fname2, 'w') # this will create a summury1.txt file on your My Documents folder


# This for loop checks each field and populate result and print them out
for i in fl: # Here i stands for consequtive fields one at a time; hence the first i == 'impr_latr'
    # This is an empty list which collects all the cell values from a field.
    values = []
    # For accessing attributes, arcpy uses Cursor.
    # There are SearchCursor (for searching values), InsertCursor (for adding new value), (UpdateCursor for changing existing value)
    with arcpy.da.SearchCursor(fc, i) as cursor: # for the first field this will work as "with arcpy.da.SearchCursor('hssanitation_24122014', 'impr_latr')"
        # Here, we're assessing each row value from the field and concatenating them in List values
        for row in cursor:
            values.append('{}'.format(row[0])) # values now have all the cell value for iterating field.
        # getting the unique values only from all cell values to build the summary.
        uniqueValues = set(values) # set is unordered collection of objects
        # sorting the unique values
        u = sorted(uniqueValues)
        print i # printing the field name
        fwrite.write(i)
        fwrite.write("\n")
        for j in u:
            # printing the unique field value and their counts
            print "%s, %s" % (j, values.count(str(j)))
            fwrite.write("%s, %s\n" % (j, values.count(str(j))))
fwrite.close() # after writing all the values, we need to close the output file.