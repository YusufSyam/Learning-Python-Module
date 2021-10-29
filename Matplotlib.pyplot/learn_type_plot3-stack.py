import numpy as np
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

# Membuat array untuk plot stack
x= np.linspace(1,10,10)
stack1= np.random.randint(10000,20000,10) * np.linspace(0.3,1,10)
stack2= np.random.randint(10000,20000,10) * np.linspace(0.3,1,10)
stack3= np.random.randint(10000,20000,10) * np.linspace(0.3,1,10)

plt.figure(figsize=(10,6))
plt.stackplot(x, stack1, stack2, stack3, labels=['Person 1', 'Person 2', 'Person 3'])

plt.legend(loc='lower right')
plt.xlabel('Month')
plt.ylabel('Salary')

plt.title('Team\'s total salary each month ')
plt.tight_layout()

plt.show()
