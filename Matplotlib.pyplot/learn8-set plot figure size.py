from matplotlib import pyplot as plt
import numpy as np

x1= np.linspace(1,30,30)
y1= np.random.randint(40,60,30) * np.linspace(1,5,30)
y2= np.random.randint(30,55,30) * np.linspace(1,5,30)

# Untuk membuat figure plot besar, kita harus memanggi plt.figure(figsize=(besar x, besar y)) sebelum dilakukan plt.plot
plt.figure(figsize=(12,6))

plt.plot(x1,y1, c='r', label='MU')
# plt.bar(x1, y1, color='#F00000')

plt.plot(x1,y2, c='b', label='Man City')
# plt.bar(x1, y2)

plt.grid(True)
plt.legend()
plt.xlabel('Tahun')
plt.ylabel('Gol')
plt.title('Prebandingan Gol MU dan Man City dalam 30 tahun terakhir')

plt.show()
