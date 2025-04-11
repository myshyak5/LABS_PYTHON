import os
import sys

if '--dirpath' in sys.argv:
    dirpath_index = sys.argv.index('--dirpath') + 1
    dirpath = sys.argv[dirpath_index]
else:
    dirpath = os.getcwd()

if '--files' in sys.argv:
    files_index = sys.argv.index('--files') + 1
    files_to_check = sys.argv[files_index:]
else:
    files_to_check = []

if not files_to_check:
    total_files = 0
    total_size = 0

    for entry in os.listdir(dirpath):
        if os.path.isfile(os.path.join(dirpath, entry)):
            total_files += 1
            total_size += os.path.getsize(os.path.join(dirpath, entry))

    print(f"В папке найдено {total_files} файлов.")
    print(f"Общий размер: {total_size} байт.")
else:
    existing_files = []
    missing_files = []

    for filename in files_to_check:
        file_path = os.path.join(dirpath, filename)
        if os.path.isfile(file_path):
            existing_files.append(filename)
        else:
            missing_files.append(filename)

    with open('existing_files.txt', 'w') as ef_file:
        ef_file.write('\n'.join(existing_files))
    with open('missing_files.txt', 'w') as mf_file:
        mf_file.write('\n'.join(missing_files))

    for file in existing_files:
        print(file)
    print()
    for file in missing_files:
        print(file)
