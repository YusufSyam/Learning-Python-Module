from matplotlib import pyplot as plt
import pandas as pd

plt.style.use('seaborn-pastel')

data= pd.read_csv('dataset_programmer_salary.csv')

# print(data)

ages= data['Age']
python_salary= data['Python']
js_salary= data['JavaScript']
ad_salary= data['All_Devs']

salary_mean= (python_salary.mean()+js_salary.mean()+ad_salary.mean())/3
# print(salary_mean)

# --------------------------- fill area di bawah line python salary ------------------------
plt.plot(ages, python_salary)

# Jika x adalah ages, maka akan memfill sampai ke bawah, argumen alpha untuk mengatur opacity
plt.fill_between(ages, python_salary, alpha=0.25)

plt.title('Python salary')
plt.tight_layout()
plt.show()

# ----------------------------- Fill area antara dua line --------------------------
plt.plot(ages, python_salary)
plt.plot(ages, js_salary)

# Mengubah color fill
plt.fill_between(ages, python_salary, js_salary, color='r', alpha=0.25)

plt.title('Fill between js and python salary')
plt.tight_layout()
plt.show()

# ------------------ Fill merah jika dibawah rata2, hijau jika di atas -----------------
plt.plot(ages, python_salary, label='Python salary')

# argumen where merupakan kondisi kapan fill betweennya dilakukan, interpolate untuk merapikan/mengisi bagian yg kosong
plt.fill_between(ages, salary_mean, python_salary, where=(python_salary<=salary_mean), interpolate=True, color='r' ,alpha=0.25, label='Below average')
plt.fill_between(ages, salary_mean, python_salary, where=(python_salary>salary_mean), interpolate=True, color='g', alpha=0.25, label='Above average')

plt.legend()
plt.title('Fill red if below, green if above')
plt.tight_layout()
plt.show()
