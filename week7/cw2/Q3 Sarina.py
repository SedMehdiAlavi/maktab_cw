import os

class FileHandling:
    def __new__(cls, file_name, mode):
        obj = object.__new__(cls)
        return obj
    
    def __init__(self, file_name, mode):
        if os.path.exists(file_name):
            with open(file_name, mode) as f:
                x = f.readlines()
                print(x)
        else:
            raise FileNotFoundError ("The file you are searching for doesn't exist.")
    
    def __del__(self):
        print("File deleted.")

sarina = FileHandling("text.txt", "r")