from matplotlib import pyplot as plt
import numpy as np

# Kita akan memplot beberapa bar sekaligus
ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

# Misal terdapat 3 y yang akan diplot bar
dev_y = np.array([38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752])

py_dev_y = np.array([45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640])

js_dev_y = np.array([37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583])

plt.plot(ages_x, dev_y, color="#444444", label="All Devs")
plt.plot(ages_x, py_dev_y, color="#008fd5", label="Python")
plt.plot(ages_x, js_dev_y, color="#e5ae38", label="JavaScript")

plt.title('Tampilan data yang akan diplot bar')

plt.show()

# Cara 1: meng stack bar
# Dengan menambahkan bottom= variabel_y pada bar yang akan berada di atas bar yg lain

plt.bar(ages_x, dev_y, color="#444444", label="All Devs")
plt.bar(ages_x, py_dev_y, color="#008fd5", label="Python", bottom=dev_y)
plt.bar(ages_x, js_dev_y, color="#e5ae38", label="JavaScript", bottom=(dev_y+py_dev_y)) # bottom yg ditambah dengan syarat merupakan array dari numpy

plt.title('Tampilan data yang telah diplot bar (stacked bar)')

plt.show()

# Cara2: mengelompokkan bar

# pertama kita tentukan width
width= 0.25

# Lalu kita membuat variabel x_indexes yang akan mengganti ages_x di plot
x_indexes= np.arange(len(ages_x))

# Lalu dalam argumen x, kita melakukan aritmatika width dengan x_indexes sesuai posisi
# Lalu memberi argumen baru, 'width' yg diisi dengan variabel width
plt.bar(x_indexes-width, dev_y, color="#444444", label="All Devs", width=width)
plt.bar(x_indexes, py_dev_y, color="#008fd5", label="Python", width=width)
plt.bar(x_indexes+width, js_dev_y, color="#e5ae38", label="JavaScript", width=width)

plt.title('Tampilan data yang telah diplot bar (dengan cara dikelompokkan)')

# Menyetel kembali label x axis setelah diubah
plt.xticks(ticks=x_indexes, labels=ages_x)
plt.legend()
# plt.tight_layout()

plt.xlabel('Umur')
plt.ylabel('Gaji')

plt.show()