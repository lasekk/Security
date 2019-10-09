#!/usr/bin/env python3
import os
import zipfile

# This function will back up an entire folder to a .zip file
def backup_zip(folder):
    folder = os.path.abspath(folder) # Use absolute path

    #determine filename to back up to
    ver = 1
    while True:
        zip_filename = os.path.basename(folder) + '_' + str(ver) + '.zip'
        if not os.path.exists(zip_filename):
            break
        ver += 1

    # Create the zip file
    print("\nArchiving %s..." % (zip_filename))
    backup_zip_file = zipfile.ZipFile(zip_filename, 'w')

    # Walk the folder tree in it's entirety to compress all files in sub folders as wee
    # During each iteration of the for loop os.walk returns the current folder name,
    # sub folders in that folder, as well as all the file names withing that folder
    for foldername, subfolders, filenames in os.walk(folder):
        print("\nAdding files in %s..." % (foldername))
        backup_zip_file.write(foldername)
        for filename in filenames:
            new_base = os.path.basename(folder) + '_'
            if filename.startswith(new_base) and filename.endswith('.zip'):
                continue # we don't want to back zip files
            backup_zip_file.write(os.path.join(foldername, filename))
    backup_zip_file.close()
    print("\nArchiving complete. {}created successfully!".format(zip_filename))

backup_zip('C:\\Users\\plaskows\\PycharmProjects\\Security\\Automation course')