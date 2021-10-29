import matplotlib.pyplot as plt

# Membuat 2 data yang akan ditampilkan/diplot
var_x= [0,10,20,30,40,50,60,70]
var_y= [1,2,4,8,16,32,64,128]

# Membuat plotnya
# var_x akan berada sebagai sumbu x, sedangkan var_y akan sebagai sumbu y
plt.plot(var_x, var_y)

# Menampilkan plot
plt.show()

# Membuat plot tapi kali ini kita menambahkan garis/line baru dengan var_y sebagai sumbu x dan sebaliknya
plt.plot(var_y, var_x)
plt.show()

# Membuat n line dalam satu plot, cukup lakukan plt.plot() n kali lalu plt.show()
plt.plot(var_y)
plt.plot(var_x)
plt.show()

# Tampilkan ulang ke-3
# Mumpung akan ditampilkan ulang, kali ini kita akan menampilkan kedua line ini dengan cara yang berbeda

# Line 1, Mengganti warna line ke 1, dengan argumen c
plt.plot(var_x, var_y, c='r')

# Line 2, mengganti marker/jenis line, dengan linestyle
# Possible linestyle: '-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'
plt.plot(var_y, var_x, linestyle='--')

# Line 3Mengganti color sekaligus linestyle
plt.plot(var_y, var_y, 'yo')

plt.show()