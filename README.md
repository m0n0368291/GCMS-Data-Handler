# GCMS Data Handler #

This tool provides file sorting and backup functionality for **gas chromatography** systems. These systems normally save all aqcuired data in a default file location. Depending on the IT-infrastructure one might want to save these files in a backup location for safety reasons or to sort them into categories of a certain kind. This way it is possible to better control access to files for individual people or groups of people.

## Features ##

- moving files from a default location into a specified location
- sorting of files into subfolders based on filename
- backup of zipped files into a specified backup folder
- the script provides a log file with all conducted operations

![Workflow of GCMSDH](https://bytebucket.org/m0n0368291/copyscript/raw/9a2e060a2362809eb7d4fbd168f683a99f7a67b6/copyscript/static/workflow.png?token=8b29c9cb196c6746392a827122f217f5f33b2f90)


### How does it work? ###

The script is in a **timed loop**. After a given time it iterates over all files in the default location and recognizes all files that have been specified in the configuration of the script. It **creates a zipped copy** of that file **in the backup folder**. Then the original file is moved to a target directory where multpile subfolders may exist. The script **places the files in specified subfolders**. The subfolder corresponding to a file is computed by using a regular expression. So the **name of a file determines the subfolder** it is placed in. This way one can **sort the files by person, date, project etc**.

### Handling of duplicates ###

The script was written to **never delete or overwrite anything** so that no data is lost. In order to work, the script can deal with duplicate files. If the script tries to back up a zipped file that already exists in the backup folder, it renames the new file to begin with a **unique timestamp**. The same applies for the files in the respective subfolders.

### Logging ###

The script keeps a log of alle performed actions. This should make it easier to **troubleshoot** a non-working script and to **track down missing files**. The log file is a simple text document in the same folder as the copyscript.


# How do I get set up? #
The tool is written in pure Python (3.5). There are no third party modules needed. You just need a working install of Python 3.X.

- Copy the GCMSDH.py into the default location of the files to be sorted. For Agilent Systems this might be ``D:\MSD_data\``.
- Create a backup folder which contains all necessary subfolders for the sorting operations.
- Create a folder at a chosen location which contains all necessary subfolders for the sorting operations.
- Open GCMSDH.py and edit the configurations lines as needed:
    - ``path`` and ``files`` to declare where the default file location is.
    - acronyms to be used for sorting by adding them to the list of ``users``.
    - ``target_dir`` and ``target_dir2`` for the location where the files will be sorted.
    - ``pattern`` defines the regular expression that is used to associate the files with the subfolders that they will be sorted into.

# Troubleshooting #

There are several factors that may prevent the script from working. If the script is not working as intended, follow these steps:

- check whether all necessary folders are created and the respective acronym has been added to the list of ``users``
- make sure the user executing the script has the right permissions for the folder containíng the data
- execute the script with elevated privileges
- manually check for duplicates

# Notes #

- The script will **never** try to **handle the newest file** in the default location. This is because the newest file is usually opened in the software that created the data file. Therefore an attempt to delete the file after backing up and moving will fail, causing duplicates.
- Unhandled duplicates essentially cause the script to create an **unlimited number of renamed data files and backups**. This is because of the *never delete anything* approach.

### Contribution guidelines ###

There is no way to contribute yet.


### Who do I talk to? ###

Contact me via christopher_grimm@gmx.de
