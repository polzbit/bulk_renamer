from utils import getListOfFiles
from os import path, rename

class Renamer:
    ''' Class to bulk rename files in directory '''
    def __init__(self, filepath, name='', seq=0, ext=[], recursive=False, verbose=True):
        self.path = path.abspath(filepath)
        self.name = name
        self.ext = ext
        self.seq = seq
        self.recursive = recursive
        self.verbose = verbose
        self._stop = False
        self.setup()
    
    def setup(self):
        ''' first check '''
        if not path.exists(self.path):
            print(f'[!] Path not found: {self.path}')
            return
        if path.isfile(self.path):
            self.run(True)
        elif path.isdir(self.path):
            self.run()
        else:
            print(f"[!] Unknown file: {self.path}")
    
    def run(self, isFile=False):
        ''' Run renamer '''
        if isFile:
            newName = self.path
            # check for new name
            if self.name != '':
                newName = self.name
            name, fileext = path.splitext(self.path)
            filedir = path.dirname(self.path)
            file_path = f"{filedir}\{newName}{fileext}"
            #change filename
            rename(self.path, file_path)
            if self.verbose:
                print(f'[*] Naming file: {self.path}')
        else:
            files = getListOfFiles(self.path, ext=self.ext, recursive=self.recursive)
            if not len(files):
                print(f"[!] No files were found on given path.")
                return

            seq_index = 1
            for f in files:
                if self.isStopped():
                    break
                filename = path.basename(f)
                filedir = path.dirname(f)
                newName = filename
                # check for new name
                if self.name != '':
                    newName = self.name
                name, fileext = path.splitext(filename)
                file_path = f"{filedir}\{newName}{fileext}"
                # check for seq
                if self.seq:
                    # remove last sequence if exists
                    split = filename.split('_')
                    if len(split) > 1:
                        filename = split[-2]
                    # create sequence string
                    seq_str = str(seq_index)
                    while len(seq_str) < self.seq:
                        seq_str = '0' + seq_str
                    seq_index+=1
                    filename = f"{newName}_{seq_str}{fileext}"
                    file_path = f"{filedir}\{filename}"
                #change filename
                rename(f, file_path)
                if self.verbose:
                    print(f'[*] Naming file: {f}')    
    
    def isStopped(self):
        return self._stop

    def stop(self):
        self._stop = True