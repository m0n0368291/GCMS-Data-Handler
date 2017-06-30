# GCMS Data Handler #

This tool provides file sorting and backup functionality for **gas chromatography** systems. 

## Features ##

- moving files from a default location into a specified location
- sorting of files into subfolders based on filename
- backup of zipped files into a specified backup folder
- the script provides a log file with all conducted operations

## How does it work? ##
![Workflow of GCMSDH](https://bytebucket.org/m0n0368291/copyscript/raw/9a2e060a2362809eb7d4fbd168f683a99f7a67b6/copyscript/static/workflow.png?token=8b29c9cb196c6746392a827122f217f5f33b2f90)


## How do I get set up? ##
The tool is written in pure Python (3.5). There are no third party modules needed. You just need a working install of Python 3.X.

- Copy the GCMSDH.py into the default location of the files to be sorted. For Agilent Systems this might be ``D:\MSD_data\``. 
- Create a backup folder which contains all necessary subfolders for the sorting operations. 
- Create a folder at a chosen location which contains all necessary subfolders for the sorting operations.
- Open GCMSDH.py and edit the configurations lines as needed:
    - ``path`` and ``files`` to declare where the default file location is.
    - acronyms to be used for sorting by adding them to the list of ``users``.
    - ``target_dir`` and ``target_dir2`` for the location where the files will be sorted.
    - ``pattern`` defines the regular expression that is used to associate the files with the subfolders that they will be sorted into.


## Contribution guidelines ##
There is no way to contribute yet.


## Who do I talk to? ##

Contact me via christopher_grimm@gmx.de