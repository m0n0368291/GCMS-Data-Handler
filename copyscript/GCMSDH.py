#!C:\Users\Stefan Schulz\AppData\Local\Programs\Python\Python35\python.exe

from time import gmtime, strftime
import shutil
import os
import re
import time
import zipfile
import logging
import win32security
import ntsecuritycon as con

'''
+ The script will not overwrite existing folders on the network drive! Make sure that you remove duplicates by hand if necessary.
+ the script has to be in the same folders as the runs
+ the backup folder MUST contain a folder with the according user acronym  or the script will not work!!!
+ a logfile is created by the script. To begin a new logfile, the old one needs to be moved to a separate directory (e.g. 'backup')
+ folders can only be copied, when no other program is using these files
'''

###CONFIGURATION###

#logging module parameters for the logfile
logging.basicConfig(level=logging.DEBUG, filename='GCMSDH_logfile', filemode='a+', format='%(asctime)-15s, %(levelname)-8s, %(message)s')

#relative path from Python Script to files
files = os.listdir(r'.')
# r'.' means it is the same directory

account = r"Stefan"
#user account of the computer

#list of acronyms to be used:
users = ['XX','CG', 'TG', 'MST', 'FM', 'JB','JC', 'HB', 'LZ', 'NT', 'VP', 'MM', 'MS', 'PP', 'SK', 'JK', 'ME', 'RE', 'SR', 'DV']

#the default path for the data files to be handled
path = r"..\\MSD_data\\"

def copyscript():
	timestamp = strftime("%Y-%m-%d %H:%M:%S", gmtime())#format of timestamp
	zipstamp = strftime("%H-%M-%S", gmtime())# format of timestamp for zipped files
	files = sorted(os.listdir(r'.'), key=os.path.getctime)# creates list of files ordered by creation time
	print('%s Beginning new copy cycle...'%(timestamp))
	files2 = []#empty list
####################WINDOWS FILE SYSTEM PERMISSION##############################################################
	userx, domain, type = win32security.LookupAccountName ("", account)
	sd = win32security.GetFileSecurity(path, win32security.DACL_SECURITY_INFORMATION)
	dacl = sd.GetSecurityDescriptorDacl()   # instead of dacl = win32security.ACL()
	dacl.AddAccessAllowedAce(win32security.ACL_REVISION, con.FILE_GENERIC_READ | con.FILE_GENERIC_WRITE, userx)
	sd.SetSecurityDescriptorDacl(1, dacl, 0)   # may not be necessary
	win32security.SetFileSecurity(path, win32security.DACL_SECURITY_INFORMATION, sd)
#################################################################################################################
	#os.chmod(path, 0o777)#this enables write access to all files on linux systems
	for filename in files:
		if str(filename).endswith('.D'):#only selects files ending with '.D'
			files2.append(filename)#list is filled with all run names
		else:
			pass
	#print(files2)
	files = files2[:-1]#last item, which is the newest, is sliced out from list
	#print(files)
	for filename in files:
		if str(filename).endswith('.D'):#only selects files ending with '.D'
			run = str(filename)
			print('%s Data %s found'%(timestamp,run))
			logging.info('%s Data %s found'%(timestamp,run))
			for user in users:
				target_dir = r"Z:\GCMS\%s\%s"%(str(user).strip('\[\'\'\]'), str(run))#target directory in network
				target_dir2 = r"Z:\GCMS\%s\%s"%(str(user).strip('\[\'\'\]'),str(zipstamp+' - '+run))#target directory in network for renamed files
				pattern = str(user)+'([pPnNaAgG0-9]|_|\s){1}'#regular expression to associate users to runs
				if re.match(pattern,run.upper()): #makes sure upper and lower case dont matter
					print('%s File allocated: %s -> %s' %(timestamp,run, user))
					logging.info('%s File allocated: %s -> %s' %(timestamp,run, user))
					ziprun = run+zipstamp #name for duplicate zipfiles
					shutil.make_archive(run, 'zip', run)#compress folder to zipfile with the filename 'run'
					try:#tries to move zipfile to backup folder
						shutil.move('%s.zip'%(run), r'Backup\\%s\\'%(str(user).strip('\[\'\'\]')))#moves zipfiles to MSD_Data
					except:#if error occurs, renames zipfile and tries to move again
						shutil.move('%s.zip'%(run), r'Backup\\%s\\%s'%(str(user).strip('\[\'\'\]'),str(zipstamp+' - '+run)+'.zip'))#moves zipfiles renamed to MSD_Data
						pass
					try:#tries to move folder to GCMS folder
						shutil.move(run, str(target_dir))#move files to user folder
						print('Folder moved successfully!')
						logging.info('Folder moved successfully!')
					except:#tries to move folder to GCMS folder
						pass

						try:
							shutil.move(run, str(target_dir2))#move files renamed to user folder
							print('%s %s is a duplicate! File was renamed and moved.\n Please make sure the users folder exists on server and in backup folder!'%(timestamp,run))#prints warning for duplicate file names
							logging.info('%s %s is a duplicate! File was renamed and moved.\n Please make sure the users folder exists on server and in backup folder!'%(timestamp,run))
						except:
							pass
							print('Problem with this file. Don\'t know what, sorry.')
							logging.info('Problem with this file. Don\'t know what, sorry.')
				else:
					pass
		else:
			pass
	print('going to sleep...\n')
	time.sleep(1800) #time between copy cycles (2700 = 45 min)

#while True:
copyscript()# the loop needs to be called as a function to delete all assigned variables after each loop
