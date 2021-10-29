import os

# Get current working directory (cwd)
first_cwd= os.getcwd()
print('First cwd: {}'.format(first_cwd))

# Memeriksa daftar folder dan file pada scw
print(os.listdir())

# Set cwd baru
os.chdir('D:')
print('Changed cwd: {}'.format(os.getcwd()))

print(os.listdir())

# Set cwd baru ke parent folder
os.chdir(first_cwd+'\..')
# os.chdir('..\..')
print(os.listdir())



