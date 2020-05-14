#View pixel value distribution
 #Plot a histogram
import numpy as np
from PIL import Image
import skimage.color as sc

i = np.array(Image.open("ed2.jpg"))
i_mono = sc.rgb2gray(i)

def im_hist(img):
	import matplotlib.pyplot as plt
	fig = plt.figure(figsize=(8, 6))
	fig.clf()
	ax = fig.gca()
	ax.hist(img.flatten(), bins = 256)
	#plt.show()

im_hist(i_mono)

 #Plot a cumulative histogram
def im_cdf(img):
	import matplotlib.pyplot as plt
	fig = plt.figure(figsize=(8, 6))
	fig.clf()
	ax = fig.gca()
	ax.hist(img.flatten(), bins = 256, cumulative=True)
	#plt.show()

im_cdf(i_mono)

#Equalize the image
from skimage import exposure
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

i_eq = exposure.equalize_hist(i_mono)

fig, ax = plt.subplots()
im = ax.imshow(i_eq, cmap=plt.get_cmap('gray'), interpolation='nearest',
               vmin=0, vmax=1)
#fig.colorbar(im)
im_hist(i_eq)
im_cdf(i_eq)
plt.show()
