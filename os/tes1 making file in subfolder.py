import os

# Membuat folder baru
os.makedirs('tes1_folder\\tes1_subfolder')

# Mengganti cwd ke folder baru tersebut
os.chdir('tes1_folder\\tes1_subfolder')

# Membuat file baru
with open('tes1_new_file.txt', 'w') as fp:
    pass
