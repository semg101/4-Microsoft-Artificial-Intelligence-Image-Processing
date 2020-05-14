#Sobel edge detection

#Denoising with filters
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
i_n = skimage.util.random_noise(i_eq)

fig, ax = plt.subplots()
im = ax.imshow(i_n, cmap=plt.get_cmap('gray'), interpolation='nearest', vmin=0, vmax=1)
#plt.show()

def edge_sobel(image):
	from scipy import ndimage
	import skimage.color as sc
	import numpy as np
	image = sc.rgb2gray(image) #convert the image color to gray scale
	dx = ndimage.sobel(image, 1) #horizontal derivative
	dy = ndimage.sobel(image, 0) #vertical derivative
	mag = np.hypot(dx, dy) #magnitude
	mag *= 255.0 / np.amax(mag) #normalize (Q&D)
	mag = mag.astype(np.uint8)
	return mag

#Use a median filter
def med_filter(im, size = 10):
	from scipy.ndimage.filters import median_filter as mf
	import numpy as np
	return mf(im, size = size)
i_m = med_filter(i_n)

i_edge = edge_sobel(i_m)

fig, ax = plt.subplots()
im = ax.imshow(i_edge, cmap=plt.get_cmap('gray'), interpolation='nearest', vmin=0, vmax=1)
plt.show()