import os
import sys

if len(sys.argv) > 1:
    folder_path = sys.argv[1]
else:
    folder_path = os.getcwd()

small_files = []

for root, _, files in os.walk(folder_path):
    for file in files:
        file_path = os.path.join(root, file)
        if os.path.getsize(file_path) < 2000:
            small_files.append(file_path)

if not small_files:
    print("Файлы размером менее 2К не найдены.")
else:
    os.makedirs("small")
    for file_path in small_files:
        print(file_path)
        with open(file_path, 'r') as source_file:
            copy_to_path = source_file.read()
            with open(os.path.join("small", os.path.basename(file_path)), 'w') as dest_file:
                dest_file.write(copy_to_path)