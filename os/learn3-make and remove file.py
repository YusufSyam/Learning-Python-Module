import os

print('Daftar folder dan file: \n{}\n'.format(os.listdir()))

# ------------------------------------- Membuat file -----------------------------------------
# Membuat file baru, misal file a.py
# Maksud dari parameter w adalah write
with open('a.py', 'w') as fp:
    pass

# Adapun penjelasan lain selain w:
'''
Write Only (‘w’): Open the file for writing. For an existing file, the data is truncated and over-written.
Write and Read (‘w+’): Open the file for reading and writing. For an existing file, data is truncated and over-written.
Append Only (‘a’): Open the file for writing. The data being written will be inserted at the end, after the existing data.
Append and Read (‘a+’): Open the file for reading and writing. The data being written will be inserted at the end, after the existing data. '''

print('Daftar folder dan file: \n{}\n'.format(os.listdir()))

# ------------------------------------------ Menghapus file -----------------------------------------------

# Jika folder tidak ada maka akan error
os.remove('a.py')

print('Daftar folder dan file: \n{}\n'.format(os.listdir()))