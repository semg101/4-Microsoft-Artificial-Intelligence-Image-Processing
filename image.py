import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

fig, ax = plt.subplots()
im = ax.imshow(np.array(Image.open("ed2.jpg")), cmap=plt.get_cmap('hot'), interpolation='nearest',
               vmin=0, vmax=1)
#fig.colorbar(im)
plt.show()