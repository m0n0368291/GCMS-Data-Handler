#!C:/Program Files (x86)/Python 3.5/python.exe

from time import gmtime, strftime
import shutil
import os
import re
import time
import zipfile

timestamp = strftime("%Y-%m-%d %H:%M:%S", gmtime())#aktueller Zeitstempel
files = os.listdir(r'.')#relative path from Python Script to files

#https://stackoverflow.com/questions/1855095/how-to-create-a-zip-archive-of-a-directory
def make_zipfile(output_filename, source_dir):
    relroot = os.path.abspath(os.path.join(source_dir, os.pardir))
    with zipfile.ZipFile(output_filename, "w", zipfile.ZIP_DEFLATED) as zip:
        for root, dirs, files in os.walk(source_dir):
            # add directory (needed for empty dirs)
            zip.write(root, os.path.relpath(root, relroot))
            for file in files:
                filename = os.path.join(root, file)
                if os.path.isfile(filename): # regular files only
                    arcname = os.path.join(os.path.relpath(root, relroot), file)
                    zip.write(filename, arcname)



#list of user acronyms to be used:
users = ['CG', 'TG', 'MST', 'FM', 'JC', 'HB', 'LZ', 'NT', 'VP', 'MM', 'PP', 'SK', 'JK', 'ME', 'RE', 'SR']



#main loop for the copyscript
while True:
    for filename in files:
        if str(filename).endswith('.D'):
            run = str(filename)
            print('%s Run %s erkannt'%(timestamp,run))
            for user in users:
        #        target_dir = "\\\\schulzdata\\GCMS\\%s\\"%(str(user).strip('\[\'\'\]')))#Zielordner auf dem Server
        #        print(target_dir)
        #        pattern = str(user)+r"[a-zA-Z]*[0-9]"
                if run.startswith(user):
                    print('%s Zugehoerigkeit erkannt: %s -> %s' %(timestamp,run, user))
                    make_zipfile('%s.zip'%(run),'.')#zips the run files into archive at location '.'
                    shutil.move('%s.zip'%(run), '..\\MSD_Data\\%s\\'%(str(user).strip('\[\'\'\]')))
                    try:
                        shutil.move(run, 'Zielordner\\%s\\'%(str(user).strip('\[\'\'\]')))
        #                shutil.move(run, str(target_dir))
                    except shutil.Error:
                        shutil.move(run, 'Zielordner\\%s\\%s'%(str(user).strip('\[\'\'\]'),run+'(duplicate)'))
                        print('%s %s is a duplicate! File was renamed and moved.'%(timestamp,run))
                        pass
                    except:
                        print('%s No directory for %s at target location.' %(timestamp,run))
                else:
                    pass
    time.sleep(2700) #time between copy cycles (2700 = 45 min)

