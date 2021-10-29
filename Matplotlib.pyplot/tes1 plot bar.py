from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

plt.style.use('seaborn-pastel')

data= pd.read_csv('dataset_programmer_salary.csv')
print(data.head())

width= 0.25
x_indexes= np.linspace(1,len(data['Age']), len(data['Age']))

plt.figure(figsize=(12,6))

plt.bar(x_indexes-width, data['Python'], width=width, label='Python')
plt.bar(x_indexes, data['JavaScript'], width=width, label='Java Script')
plt.bar(x_indexes+width, data['All_Devs'], width=width, label='All Developers')

plt.axis([0.5, (len(data['Age']))+0.5, 0, (np.amax(data['Python']))+1000])

plt.xticks(x_indexes, data['Age'])
plt.title('Bar Plot of Developer\'s salary')
plt.legend()
plt.show()