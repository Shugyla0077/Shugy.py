import os

path = '/your/path/here/filename.txt'

if os.path.exists(path):
    dir_name = os.path.dirname(path)
    file_name = os.path.basename(path)
    print(f"Directory: {dir_name}, Filename: {file_name}")
else:
    print("The path does not exist.")
