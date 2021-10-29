from matplotlib import pyplot as plt
import numpy as np

# Plot style adalah semacam atribut untuk mengubah style plot menjadi preset style lain
x= np.linspace(0, 10, num=10)
y= np.random.randint(40,70, size=10) * np.linspace(0,7, num=10)

plt.plot(x,y)
plt.title('Style default')

plt.show()

# Memprint style plot yang tersedia
print(plt.style.available)

# Mengubah style plot (harus dilakukan sebelum plt.plot()
plt.style.use('fivethirtyeight')

plt.plot(x,y)
plt.title('Style plot yang telah diubah')

plt.show()

# Mengubah style plot dengan plt.xkcd()
plt.xkcd()

plt.plot(x,y)
plt.title('Style plot yang diganti dengan xkcd')

plt.show()