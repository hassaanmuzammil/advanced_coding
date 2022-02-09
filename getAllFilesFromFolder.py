"""
    Get all files of a specific type e.g. '.csv' from all subfolders within a folder  
"""


import os, shutil

def getAllFiles(src_folder, dest_folder, file_type):

    for root, dirs, files in os.walk(src_folder):
        for file in files:
            if file.lower().endswith(file_type) and not file.startswith("~$"):
                shutil.copy(os.path.join(root, file), os.path.join(dest_folder, file))
                
    return None
