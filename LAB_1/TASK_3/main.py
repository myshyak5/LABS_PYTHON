import os
import sys

if len(sys.argv) > 1:
    dirpath = sys.argv[1]
else:
    dirpath = os.getcwd()
    
with open("missing_files.txt", "r") as mf:
    missing_files = [line.strip() for line in mf.readlines()]

for filename in missing_files:
    file_path = os.path.join(dirpath, filename)
    with open(file_path, "w") as f:
        pass