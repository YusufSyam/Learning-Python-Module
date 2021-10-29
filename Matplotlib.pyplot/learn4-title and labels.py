import matplotlib.pyplot as plt
from plot_preset_function import *

x= consecutive_generator(10)
y= random_generator(10)*consecutive_generator(10, 0.2)

plot_1= plt.plot(x,y, c='r')
plt.setp(plot_1, linewidth='2')

# Membuat label untuk x dan y axis
plt.xlabel('Ini x axis label')
plt.ylabel('Ini y axis label uwau')

# Membuat title
plt.title('Ini title ahah')

plt.show()

