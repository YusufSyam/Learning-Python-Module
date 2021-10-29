import os
import matplotlib

home_cwd= os.getcwd()

os.chdir('..\\Matplotlib')

print(os.listdir())

# Ternyata tidak bisa

# Pakai cara lain
import sys
# sys.path.insert(1, 'C:\\Users\LENOVO\PycharmProjects\ProgramPythonDasar\Learn Library')
sys.path.append('../')
from plot_preset_function import sinus_generator

sin_x= sinus_generator(1,1,4,0)

# Wkwkw nda tau