import numpy as np
import argparse
from matplotlib import pyplot as plt
from skimage.io import imread, imshow, show, imsave
from skimage.transform import resize
from skimage.exposure import histogram

path1 = 'C:/Users/MuzAn/Downloads/123.jpg'
path2 = 'C:/Users/MuzAn/Downloads/1234.jpg'
img_first = imread(path1)
img_second = imread(path2)

img_first = img_first/255
img_second = img_second/255

img_first = resize(img_first, (img_second.shape[0], img_second.shape[1]))

img = np.concatenate((img_second, img_first), axis=0, out=None, casting='same_kind')

fig = plt.figure(figsize=(15, 5))
fig.add_subplot(2, 3, 1)
imshow(img_second)
fig.add_subplot(2, 3, 2)
imshow(img_first)
fig.add_subplot(2, 3, 3)
imshow(img)

show()
