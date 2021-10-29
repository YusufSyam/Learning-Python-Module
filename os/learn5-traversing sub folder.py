import os

# Kita bisa traverse menggunakan os.walk()
# Namun terlebih dulu kita harus menggunakan loop

for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    print('Current path: ', dirpath)
    print('Folder in path: ', dirnames)
    print('Files in path: ', filenames)
    print()