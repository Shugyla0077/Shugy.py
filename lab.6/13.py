import os

file_path = '/your/file/to/delete.txt'

if os.path.exists(file_path) and os.access(file_path, os.W_OK):
    os.remove(file_path)
    print(f"File {file_path} deleted successfully.")
else:
    print("File does not exist or is not writable.")
