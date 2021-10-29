import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# Kali ini kita akan memplot data dari file csv
data= pd.read_csv('dataset_popular_programming_languanges_cleaned.csv')
print(data.head())

x= np.array(data.iloc[:,0])
y= np.array(data.iloc[:,1])

plt.bar(x,y)
plt.show()

# Untuk membuat barnya horizontal, dengan plt.barh()
plt.barh(x,y)
plt.show()


