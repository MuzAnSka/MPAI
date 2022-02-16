import numpy as np
import argparse
from matplotlib import pyplot as plt
from skimage.io import imread, imshow, show, imsave
from skimage.transform import resize
from skimage.exposure import histogram

parser = argparse.ArgumentParser(description= '')
parser.add_argument('-p','--path', type=str, required=True)
parser.add_argument('-a','--axis',type=int, default=0)
parser.add_argument('-r','--result', type=str, required=True)
args = parser.parse_args()

path1 = 'C:/Users/MuzAn/Downloads/123.jpg'
path2 = args.path
img_first = imread(path1)
img_second = imread(path2)

img_first = img_first/255
img_second = img_second/255

img_first = resize(img_first, (img_second.shape[0], img_second.shape[1]))

img = np.concatenate((img_second, img_first), axis=args.axis, out=None, casting='same_kind')
imsave(args.result+'/result.jpg', img)

fig = plt.figure(figsize=(15, 5))
fig.add_subplot(2, 3, 1)
imshow(img_second)
fig.add_subplot(2, 3, 2)
imshow(img_first)
fig.add_subplot(2, 3, 3)
imshow(img)

hist_red, bins_red = histogram(img_second[:, :, 2])
hist_green, bins_green = histogram(img_second[:, :, 1])
hist_blue, bins_blue = histogram(img_second[:, :, 0])

fig.add_subplot(2, 3, 4)
plt.plot(bins_green, hist_green, color='green', linestyle='-', linewidth=1)
plt.plot(bins_red, hist_red, color='red', linestyle='-', linewidth=1)
plt.plot(bins_blue, hist_blue, color='blue', linestyle='-', linewidth=1)

hist_red, bins_red = histogram(img_first[:, :, 2])
hist_green, bins_green = histogram(img_first[:, :, 1])
hist_blue, bins_blue = histogram(img_first[:, :, 0])

fig.add_subplot(2, 3, 5)
plt.plot(bins_green, hist_green, color='green', linestyle='-', linewidth=1)
plt.plot(bins_red, hist_red, color='red', linestyle='-', linewidth=1)
plt.plot(bins_blue, hist_blue, color='blue', linestyle='-', linewidth=1)


hist_red, bins_red = histogram(img[:, :, 2])
hist_green, bins_green = histogram(img[:, :, 1])
hist_blue, bins_blue = histogram(img[:, :, 0])
fig.add_subplot(2, 3, 6)
plt.plot(bins_green, hist_green, color='green', linestyle='-', linewidth=1)
plt.plot(bins_red, hist_red, color='red', linestyle='-', linewidth=1)
plt.plot(bins_blue, hist_blue, color='blue', linestyle='-', linewidth=1)

plt.tight_layout()
show()
