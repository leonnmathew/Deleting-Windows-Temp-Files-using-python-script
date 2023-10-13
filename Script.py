#Proper Documentation has been provided for the code for a better understanding 
# Importing necessary modules
import os, subprocess

# Specifying the directory to clean
del_dir = r'c:\windows\temp'

# Running a shell command to delete files in the specified directory
pObj = subprocess.Popen('del /S /Q /F %s\\*.*' % del_dir, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Communicating with the process and capturing the output and errors
rTup = pObj.communicate()

# Getting the return code of the process
rCod = pObj.returncode

# Checking if the process was successful
if rCod == 0:
    print 'Success: Cleaned Windows Temp Folder'
else:
    print 'Fail: Unable to Clean Windows Temp Folder'
