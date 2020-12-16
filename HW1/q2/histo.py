import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img_address="sample.jpg"

###########################################

def caclculate_histo(img_address):
    img =cv.imread(img_address,0)
    histo = np.zeros(256)
    for i in range(0, img.shape[0]):
        for j in range(0, img.shape[1]):
            histo[img[i][j]] += 1
    plt.plot(histo)
    plt.show()

###########################################

# caculate given image histogram
caclculate_histo(img_address)