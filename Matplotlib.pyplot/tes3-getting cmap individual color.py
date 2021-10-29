import matplotlib
from matplotlib import cm
from matplotlib import colors

cmap = matplotlib.cm.get_cmap('Dark2')

rgba = cmap(0.5)
print(rgba) # (0.99807766255210428, 0.99923106502084169, 0.74602077638401709, 1.0)

for i in range(cmap.N):
    rgba = cmap(i)
    # rgb2hex accepts rgb or rgba
    print(matplotlib.colors.rgb2hex(rgba))

print('adsasd',matplotlib.colors.rgb2hex(cmap(0)))
print([matplotlib.colors.rgb2hex(cmap(i)) for i in range(4)])