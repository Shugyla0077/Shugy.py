import shutil

source_file = '/your/source/file.txt'
destination_file = '/your/destination/file.txt'

shutil.copy(source_file, destination_file)
print(f"Contents copied from {source_file} to {destination_file}")
