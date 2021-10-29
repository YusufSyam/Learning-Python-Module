import matplotlib.pyplot as plt
import numpy as np
# from plot_preset_function import sinus_generator # Mengimport fungsi dari file di seblah

def sinus_generator(amplitudo, frekuensi, t_akhir, theta):
    t= np.arange(0, t_akhir, 0.1)
    y= amplitudo * np.sin(2 * frekuensi * t + np.deg2rad(theta))

    return t, y

t, y= sinus_generator(1,1,4,0)

plt.plot(t,y)

# Misal kita mau mengatur batas axis x atau y
# format: plt.axis= ([xmin, xmax, ymin, ymax])
plt.axis= ([1,4,-2,2])

# Mengaktifkan grid
plt.grid(True)

plt.show()