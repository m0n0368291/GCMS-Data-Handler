#!C:/Program Files (x86)/Python 3.5/python.exe

from time import gmtime, strftime
import shutil
import os
import re
import time
import zipfile

files = os.listdir(r'.')#relative path from Python Script to files

#list of user acronyms to be used:
users = ['CG', 'TG', 'MST', 'FM', 'JC', 'HB', 'LZ', 'NT', 'VP', 'MM', 'PP', 'SK', 'JK', 'ME', 'RE', 'SR']

#main loop for the copyscript
def copyscript():
    files = os.listdir(r'.')#relative path from Python Script to files
    timestamp = strftime("%Y-%m-%d %H:%M:%S", gmtime())#format of timestamp
    zipstamp = strftime("%H-%M-%S", gmtime())
    print('%s Beginning new copy cycle...'%(timestamp))
    for filename in files:
        if str(filename).endswith('.D'):
            run = str(filename)
            print('%s Run %s erkannt'%(timestamp,run))
            for user in users:
                #target_dir = "\\\\schulzdata\\GCMS\\%s\\"%(str(user).strip('\[\'\'\]')))#target directory in network
                #target_dir2 = "\\\\schulzdata\\GCMS\\%s\\%s"%(str(user).strip('\[\'\'\]')),str(zipstamp+' - '+run))#target directory in network for renamed files
                pattern = str(user)+'([pPnNaAgG0-9]|_|\s){1}'#regular expression to associate users to runs
                if re.match(pattern,run):
                    print('%s Zugehoerigkeit erkannt: %s -> %s' %(timestamp,run, user))
                    ziprun = run+zipstamp #name for duplicate zipfiles
                    shutil.make_archive(run, 'zip', run)#zip directory
                    try:
                        shutil.move('%s.zip'%(run), '..\\MSD_Data\\%s\\'%(str(user).strip('\[\'\'\]')))#moves zipfiles to MSD_Data
                    except:
                        shutil.move('%s.zip'%(run), '..\\MSD_Data\\%s\\%s'%(str(user).strip('\[\'\'\]'),str(zipstamp+' - '+run)+'.zip'))#moves zipfiles renamed to MSD_Data
                        pass
                    try:
                        shutil.move(run, 'Zielordner\\%s\\\\'%(str(user).strip('\[\'\'\]')))#move files to user folder
                        #shutil.move(run, str(target_dir))#move files to user folder
                    except:
                        shutil.move(run, 'Zielordner\\%s\\%s'%(str(user).strip('\[\'\'\]'),str(zipstamp+' - '+run)))#move files renamed to user folder
                        #shutil.move(run, str(target_dir2))#move files renamed to user folder
                        print('%s %s is a duplicate! File was renamed and moved.\n Please make sure the users folder exists!'%(timestamp,run))
                        pass
                else:
                    pass
    print('going to sleep...\n')
    time.sleep(20) #time between copy cycles (2700 = 45 min)

while True:
    copyscript()# the loop needs to be called as a function to delete all assigned variables after each loop