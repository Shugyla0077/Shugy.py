import os

path = '/your/path/here'

# List only directories
directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
print("Directories:", directories)

# List only files
files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
print("Files:", files)

# List all directories and files
all_files_and_dirs = os.listdir(path)
print("All files and directories:", all_files_and_dirs)
