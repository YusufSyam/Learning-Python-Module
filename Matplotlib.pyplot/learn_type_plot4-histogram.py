import pandas as pd
import numpy as np
from matplotlib import  pyplot as plt

# Beda histogram dengan bar adalah
# Histogram berfungsi lebih kepada data interval
# Misal: satu batang pada histogram yaitu 21-25, 25-30, dst, sementara bar satu variabel satu batang

plt.style.use('seaborn-pastel')

ages= np.random.randint(16,50, 100)

# Argumen bins adalah seberapa banyak data mau dibagi, atau seberapa banyak batang
# Argumen linewidth untuk edgecolor
plt.hist(ages, bins=6, color='#bbbbbb' ,edgecolor='black', linewidth=0.4)

plt.title('Histogram dengan 6 bins')

plt.show()

data= pd.read_csv('dataset_ages.csv')['Age']

# Bins juga bisa berupa list
# Misal
bins= [0,10,20,30,40,50,60,70,80,90,100]

plt.hist(data, bins=bins, edgecolor='black', linewidth=0.5)

plt.title('Histogram dengan list bins')

plt.show()

# History dengan log

plt.hist(data, bins=bins, edgecolor='black', linewidth=0.5, log=True)

plt.title('Histogram dengan log')

plt.show()