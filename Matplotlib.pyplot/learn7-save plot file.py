from matplotlib import pyplot as plt
import numpy as np

x= np.linspace(0, 10, num=10)
y= np.random.randint(40,70, size=10) * np.linspace(0,7, num=10)
plt.xkcd()

# Cara biasa untuk menyimpan file adlah mengklik tombol memori saat plot ditampilkan

# Cara kedua adalah secara programatically:
plt.plot(x,y)

# Menyimpan gambar, parameter pertama adalah nama file
plt.savefig('learn7.png')

plt.show()