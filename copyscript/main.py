#!C:/Program Files (x86)/Python 3.5/python.exe

import shutil
import os
import re

users = ['CG', 'TG', 'MST', 'FM', 'JC', 'HB', 'LZ', 'NT', 'VP', 'MM', 'PP', 'SK', 'JK', 'ME', 'RE', 'SR']
files = os.listdir(r'.')
print(files)
    #    print('------\nSuche nach: ',str(user), '\n')
for filename in files:
#        print(filename)
    if str(filename).endswith('.D'):
        print('Datei ' + filename + ' erkannt')
    for user in users:
        #pattern = str(user)+r"[A-Za-z]?[0-9]"
        if filename.startswith(user):
            print('Dateinamen erkannt')
            #MOVE BEFEHLE
        else:
            pass


#        shutil.copy(
#    shutil.copy(re.match(*), r'Zielordner\CG0241.D')
