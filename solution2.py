import numpy as np
from math import exp
from math import pi
import matplotlib.pyplot as plt

def filter(img, windows_size,sigma):
   img2 = np.zeros_like(img)
   padding = windows_size//2
   elements = [ (exp(-((x-padding)**2 /(2.0*(sigma**2)))))/(sigma*(2.0*pi)**(1/2)) for x in range(windows_size)]
   kernel = [[i * j for i in elements] for j in elements]
   div = sum([sum(x) for x in kernel])
   kernel = [[x/div for x in i] for i in kernel]
   kernel = np.array([np.array(x) for x in kernel])
   for i in range(windows_size//2, img.shape[0] - windows_size//2):
      for j in range(windows_size//2, img.shape[1] - windows_size//2):
         for c in range(img.shape[2]):
            conv = img[i - padding:i + padding, j-padding:j+padding, c] * kernel
            img2[i, j, c] = conv.sum()
   return img2

def main():
   img = plt.imread("1.png")[:, :, :3]
   img2 = filter(img,6,20)
   fig, axs = plt.subplots(1, 2)
   axs = axs.ravel()
   axs[0].imshow(img)
   axs[1].imshow(img2)
   plt.show()
main()