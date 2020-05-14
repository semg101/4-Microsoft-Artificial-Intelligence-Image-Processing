#Denoising with filters
import numpy as np
from PIL import Image
import skimage.color as sc

i = np.array(Image.open("ed2.jpg"))
i_mono = sc.rgb2gray(i)

 #Equalize the image and add noise
from skimage import exposure
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import skimage

i_eq = exposure.equalize_hist(i_mono)
i_n = skimage.util.random_noise(i_eq)

fig, ax = plt.subplots()
im = ax.imshow(i_n, cmap=plt.get_cmap('gray'), interpolation='nearest', vmin=0, vmax=1)
#plt.show()

 #Use a Gaussian filter
def gauss_filter(im, sigma = 10):
	from scipy.ndimage.filters import gaussian_filter as gf
	import numpy as np
	return gf(im, sigma = sigma)
i_g = gauss_filter(i_n)
fig, ax = plt.subplots()
im = ax.imshow(i_g, cmap=plt.get_cmap('gray'), interpolation='nearest', vmin=0, vmax=1)
#plt.show()

 #Use a median filter
def med_filter(im, size = 10):
	from scipy.ndimage.filters import median_filter as mf
	import numpy as np
	return mf(im, size = size)
i_m = med_filter(i_n)
fig, ax = plt.subplots()
im = ax.imshow(i_m, cmap=plt.get_cmap('gray'), interpolation='nearest', vmin=0, vmax=1)
plt.show()