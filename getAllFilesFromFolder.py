import os, shutil

def getAllFiles(src_folder, dest_folder, file_type):

    for root, dirs, files in os.walk(src_folder):
        for file in files:
            if file.endswith().lower() == file_type and not file.startswith("~$"):
                shutil.copy(os.path.join(root, file), os.path.join(dest_folder, file))
                
    return None
