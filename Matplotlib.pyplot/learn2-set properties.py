from matplotlib import pyplot as plt
# from numpy import random
import numpy as np

# Menggenerate data yang bernilai random
a= np.random.randint(10,50, size=20)
b= np.random.randint(0,40, size=20)

# Menyetel properties, dengan setp()
# Untuk melakukan setp, kita harus mengassign plt.plot() ke dalam variabele

plot_a= plt.plot(a) # Btw walaupun diassign begini, nantinya plotnya tetap ditampilkan, dilakukan setp maupun tidak
plot_b= plt.plot(b)

# Misal mengubah warna plot_a, serta ketebalan garisnya
plt.setp(plot_a, color='brown', linewidth='2')

# Mengubah warna dan linestyle plot_b, serta markernya, marker=',' untuk menghilangkannya
plt.setp(plot_b, color='orange', linestyle=':', marker='o')

plt.show()

'''
List of all possible properties

agg_filter: a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array
alpha: scalar or None
animated: bool
antialiased or aa: bool
clip_box: `.Bbox`
clip_on: bool
clip_path: Patch or (Path, Transform) or None
color or c: color
contains: unknown
dash_capstyle: `.CapStyle` or {'butt', 'projecting', 'round'}
dash_joinstyle: `.JoinStyle` or {'miter', 'round', 'bevel'}
dashes: sequence of floats (on/off ink in points) or (None, None)
data: (2, N) array or two 1D arrays
drawstyle or ds: {'default', 'steps', 'steps-pre', 'steps-mid', 'steps-post'}, default: 'default'
figure: `.Figure`
fillstyle: {'full', 'left', 'right', 'bottom', 'top', 'none'}
gid: str
in_layout: bool
label: object
linestyle or ls: {'-', '--', '-.', ':', '', (offset, on-off-seq), ...}
linewidth or lw: float
marker: marker style string, `~.path.Path` or `~.markers.MarkerStyle`
markeredgecolor or mec: color
markeredgewidth or mew: float
markerfacecolor or mfc: color
markerfacecoloralt or mfcalt: color
markersize or ms: float
markevery: None or int or (int, int) or slice or list[int] or float or (float, float) or list[bool]
path_effects: `.AbstractPathEffect`
picker: float or callable[[Artist, Event], tuple[bool, dict]]
pickradius: float
rasterized: bool
sketch_params: (scale: float, length: float, randomness: float)
snap: bool or None
solid_capstyle: `.CapStyle` or {'butt', 'projecting', 'round'}
solid_joinstyle: `.JoinStyle` or {'miter', 'round', 'bevel'}
transform: `matplotlib.transforms.Transform`
url: str
visible: bool
xdata: 1D array
ydata: 1D array
zorder: float
'''



