from matplotlib import pyplot as plt
import numpy as np

x= np.linspace(0, 10, num=10)
y1= np.random.randint(20, 40, size=10) * np.linspace(0,4, num=10)
y2= np.random.randint(30, 50, size=10) * np.linspace(0,4, num=10)
y3= np.random.randint(40, 60, size=10) * np.linspace(0,4, num=10)

# Legend merupakan semacam box yang menjelaskan line tertentu adalah line yang berwarna apa
# Menyetel legend, ada dua cara:

# Cara pertama
plt.plot(x,y1, label='y1')
plt.plot(x,y2, label='y2')
plt.plot(x,y3, label='y3')

plt.title('Legend cara 1')

# Cara ini wajib memanggil fungsi, argumen loc untuk mengubah posisi legend
# Contoh lain value loc: loc=(0.07,0.05)
plt.legend(loc='upper left')

plt.show()

# Cara kedua (tidak direkomendasikan)
plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)

# plt.tight_layout()

plt.title('Legend cara 2')

# Cara ini menyetel legend pada plot yg dipanggil duluan secara berurutan
plt.legend(['y1', 'y2', 'y3'])

plt.show()