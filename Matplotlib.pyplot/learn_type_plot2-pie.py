from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

# Misal datanya seperti ini
slices= [40,27,23,10]

# Membuat label, index label harus sama dengan index slices
slc_labels= ['Fourty', 'Twenty seven', 'Twenty', 'Ten']
slc_colors= ['r', 'b', 'y', 'g']

# '%1d%%'
plt.pie(slices, labels=slc_labels, colors=slc_colors)

plt.title('Pie chart biasa dengan label dan color yang diubah')

plt.show()

# Pie chart dengan edge color, percentage, shadow, explode, dan start angle yang diubah

# Membuat explode, explode terdiri dari array yang panjang indexnya sama dengan slice
# Jika elemen ke 0 dari explode disetel ke 0, maka tidak terjadi apa2
# Jika elemen ke 1 dari explode disetel ke 0.1, maka itu akan bergeser sebesar 0.1 jari2 lingkaran ke luar
slc_explode= [0,0,0,0.2]

# Secara berurutan setelah argumen label
plt.pie(slices, labels=slc_labels, wedgeprops={'edgecolor':'black'}, autopct='%1.1f%%', shadow=True, explode=slc_explode, startangle=90)
# autopct: %1d%%' untuk integer

plt.title('Pie chart dengan edge color, percentage, shadow, explode, dan start angle yang diubah')

plt.show()