import numpy as np
from PIL import Image
import skimage.color as sc

i = np.array(Image.open("ed1.jpg"))
i_mono = sc.rgb2gray(i)

 #Equalize the image and add noise
from skimage import exposure
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import skimage

i_eq = exposure.equalize_hist(i_mono)


def corner_harr(im, min_distance = 10):
	from skimage.feature import corner_harris, corner_peaks
	mag = corner_harris(im)
	return corner_peaks(mag, min_distance = min_distance)

harris = corner_harr(i_eq, 10)

def plot_harris(im, harris, markersize = 20, color = 'red'):
	import matplotlib.pyplot as plt
	import numpy as np
	fig = plt.figure(figsize=(6, 6))
	fig.clf()
	ax = fig.gca()
	ax.imshow(np.array(im).astype(float), cmap=plt.get_cmap('gray'), interpolation='nearest', vmin=0, vmax=1)
	ax.plot(harris[:, 1], harris[:, 0], 'r+', color = color, markersize=markersize)
	plt.show()
	return 'Done'

plot_harris(i_eq, harris)