import os
import pwd
import shutil

# Simple script to clean the Downloads folder

username = pwd.getpwuid(os.getuid()).pw_name
path = '/home/' + username + '/Downloads'
dest = '/home/' + username + '/Downloads/'

os.chdir(path)
files = os.listdir(path)

def makeFolder(folderName):
    if not os.path.exists(folderName):
        os.makedirs(folderName)
    
def run():
    for f in files:
        if f.endswith('.jpg') or f.endswith('.png') or f.endswith('.jpeg'):
            folderName = 'Images'
            makeFolder(folderName)
            shutil.move(f, dest + folderName)
        elif f.endswith('.pdf') or f.endswith('.azw3') or f.endswith('.mobi'):
            folderName = 'Books_PDF'
            makeFolder(folderName)
            shutil.move(f, dest + folderName)
        elif f.endswith('.jar'):
            folderName = 'JAR'
            makeFolder(folderName)
            shutil.move(f, dest + folderName)

# Run the script
run()