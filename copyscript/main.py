#!C:/Program Files (x86)/Python 3.5/python.exe

import shutil
import os


users = ['CG', 'TG']
files = os.listdir(r'.')
print(files)
for user in users:
    print('------\nSuche nach: ',str(user), '\n')
    for filename in files:
#        print(filename)
        if str(filename).startswith(str(user)):
            print('Datei', filename, 'erkannt')
        else:
            pass


#        shutil.copy(
#    shutil.copy(re.match(*), r'Zielordner\CG0241.D')
