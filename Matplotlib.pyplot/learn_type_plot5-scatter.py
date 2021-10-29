import pandas as pd
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from matplotlib import cm
from matplotlib import colors
from matplotlib.colors import ListedColormap

plt.style.use('seaborn-pastel')

x= np.random.randint(0, 20, 30)
y= np.random.randint(0, 20, 30)

# Arg s adalah size
plt.scatter(x, y, s=100, marker='X', color='black')

plt.title('Scatter angka random dengan color, size dan marker dimodifikasi')
plt.show()

# Scatter 2

# Kali ini size dan color akan berbentuk list
size= np.random.randint(100, 200, 30)
color= np.random.randint(1, 10, 30)

plt.scatter(x, y, s=size, c=color, cmap='Greens', edgecolors='black', linewidths=1)

plt.title('Scatter dengan color dan size berbentuk list dengan cmap Greens')
plt.tight_layout()
plt.show()

# Scatter 3
data= pd.read_csv('dataset_seeds_clustered.csv')[['kernel_length','kernel_width','som']]

x= data['kernel_length']
y= data['kernel_width']
color= data['som']


cmap = matplotlib.cm.get_cmap('Dark2')
color_list= [matplotlib.colors.rgb2hex(cmap(i)) for i in range(4)]
my_cmap= ListedColormap(color_list)

plt.scatter(x, y, s=20, c=color, cmap=my_cmap)

# # Jika datanya terlalu besar, kita bisa memakai scale log
# plt.xscale('log')

# Menyetel color bar
cbar= plt.colorbar()
cbar.set_label('Cluster')

plt.xlabel('Kernel Length')
plt.ylabel('Kernel Width')

plt.legend()
plt.title('Clustering SOM pada dataset seeds')

plt.show()

# Scatter 4, seperti scatter 3 tapi mempunyai label

colors= color.sort_values().unique()

temp= 0
fig, ax = plt.subplots()

cmap = matplotlib.cm.get_cmap('Dark2')
color_list= [matplotlib.colors.rgb2hex(cmap(i)) for i in range(4)]

for color in color_list:

    x= data[data['som']==temp]['kernel_length']
    y= data[data['som']==temp]['kernel_width']
    temp+=1

    labels= 'Cluster {}'.format(temp)
    ax.scatter(x, y, c=color, label=labels, edgecolors='none')

ax.legend()

plt.xlabel('Kernel Length')
plt.ylabel('Kernel Width')

plt.title('Clustering SOM pada dataset seeds dengan legend')

plt.show()


