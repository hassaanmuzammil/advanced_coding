def getAllFiles(src_folder, dest_folder, file_type):

    for root, dirs, files in os.walk(srcDir):
        for file in files:
            if file.endswith().lower() == '.xlsx' and not file.startswith("~$"):
                # shutil.copy(os.path.join(root, file), os.path.join(dest, file))
                
    return None
