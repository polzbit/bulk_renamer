import os

def getListOfFiles(dirName, ext=[], recursive=True):
        # create a list of file and sub directories 
        # names in the given directory 
        allExt = False
        if not len(ext):
            allExt = True
        allFiles = list()
        if os.path.exists(dirName):
            listOfFile = os.listdir(dirName)
            # Iterate over all the entries
            for entry in listOfFile:
                # Create full path
                fullPath = os.path.join(dirName, entry)
                # If entry is a directory then get the list of files in this directory 
                if os.path.isdir(fullPath) and recursive:
                    allFiles = allFiles + getListOfFiles(fullPath, ext)
                elif allExt:
                    allFiles.append(fullPath)
                else:
                    for e in ext:
                        if entry.endswith(e):
                            # check file extention
                            allFiles.append(fullPath)
                            break

        return allFiles 