import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

data= pd.read_csv('dataset_programmer_salary.csv')

ages= data['Age']
python= data['Python']
all_devs= data['All_Devs']
js= data['JavaScript']

plt.style.use('seaborn-pastel')

# -------------------------------- Plot 2 axes dan 1 figure ----------------------------------------
# share x artinya akan meng share x ticks antara 2 sub axes
fig, ax= plt.subplots(nrows= 2, ncols=1, sharex=True)

# Mengatur fig size
fig.set_figheight(5)
fig.set_figwidth(8)

ax[0].plot(ages, python, label='Python')
ax[0].plot(ages, all_devs, label='All Devs')

ax[0].legend()
# Untuk menyetel x y label dan title, seperti ini
ax[0].set_title('Perbandingan Python dengan All Devs')
ax[0].set_ylabel('Rata-rata gaji')
# Karena akan jelek jika dikasi x label pada subplot di atas, maka saya tidak kasi

ax[1].plot(ages, js, label='Javascript')
ax[1].plot(ages, all_devs, label='All Devs')

ax[1].legend()
ax[1].set_title('Perbandingan JavaScript dengan All Devs')
ax[1].set_xlabel('Umur')
ax[1].set_ylabel('Rata-rata gaji')

# Untuk show dan tight_layout tetap plt

plt.tight_layout()
plt.show()

# -------------------------------- Plot 2 axes dan 2 figure ----------------------------------------

# Misal figure pertama kita kasi sama dengan figure sebelumnya
fig1, ax= plt.subplots(nrows= 2, ncols=1, sharex=True)

ax[0].plot(ages, python, label='Python')
ax[0].plot(ages, all_devs, label='All Devs')

ax[0].legend()
ax[0].set_title('Perbandingan Python dengan All Devs')
ax[0].set_ylabel('Rata-rata gaji')

ax[1].plot(ages, js, label='Javascript')
ax[1].plot(ages, all_devs, label='All Devs')

ax[1].legend()
ax[1].set_title('Perbandingan JavaScript dengan All Devs')
ax[1].set_xlabel('Umur')
ax[1].set_ylabel('Rata-rata gaji')

# Figure ke2
fig2, ax2= plt.subplots(figsize=(12,6))

x_indexes= np.arange(len(ages))
width= 0.25

ax2.bar(x_indexes-width, python, width=width, label='Python')
ax2.bar(x_indexes, all_devs, width=width, label='All Devs')
ax2.bar(x_indexes+width, js, width=width, label='JavaScript')

plt.setp(ax2, xticks=x_indexes, xticklabels=ages)
ax2.set_xlabel('Median Gaji')
ax2.set_ylabel('Umur')
ax2.set_title('Figure 2: Bar plot perbandingan ketiga bahasa pemrograman')
ax2.legend()

plt.tight_layout()
plt.show()