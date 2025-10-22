import os

path = '/your/path/here'

exists = os.path.exists(path)
readable = os.access(path, os.R_OK)
writable = os.access(path, os.W_OK)
executable = os.access(path, os.X_OK)

print(f"Path exists: {exists}")
print(f"Readable: {readable}")
print(f"Writable: {writable}")
print(f"Executable: {executable}")
