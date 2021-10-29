import os

print(os.listdir())

# -------------------------------------- Membuat folder -------------------------------------------

# Membuat folder baru, args pertama adalah nama folder
# Jika folder sudah ada, maka akan error
os.mkdir('Tes os bikin folder2')

# Membuat sub-folder baru di dalam folder yg juga baru dibuat sekaligus
# Jika folder sudah ada, maka yg dibuat hanya sub folder
# Jika sub folder sudah ada, maka akan error
os.makedirs('Tes os bikin folder3/Tes os bikin sub folder2')

print(os.listdir())

# ------------------------------------ Menghapus folder -------------------------------------------

# Menghapus folder
os.rmdir('Tes os bikin folder2')

# Menghapus folder sekaligus sub folder
os.removedirs('Tes os bikin folder3/Tes os bikin sub folder2')

print(os.listdir())

# ------------------------------ Mengecek keberadaan file/folder -------------------------------------

print(os.path.exists('Tes os bikin folder2'))
