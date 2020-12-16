import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img_address = "images.jpg"

###########################################

# enhance image useing opencv library
def enhance_img_with_library(img_address):
    img = cv.imread(img_address, 0)
    equ_img = cv.equalizeHist(img)
    plt.hist(img.flat, bins=256, range=(0, 255), color='red')
    plt.hist(equ_img.flat, bins=256, range=(0, 255), color='blue')
    plt.title("Enhanced image histogram vs old histogram using opencv")
    plt.show()
    result = np.hstack([equ_img, img])
    # save the enhanced img  in result.png
    cv.imwrite('result.png', result)
    # show the enhanced image
    plt.imshow(cv.cvtColor(result, cv.COLOR_GRAY2BGR))
    plt.title("Enhanced image vs old image(with library)")
    plt.show()
    return


# implement the method from scratch without using library
def enhance_img_from_scratch(img_address):
    img = cv.imread(img_address, 0)
    new_img = np.zeros((img.shape[0], img.shape[1]), np.int32)
    histo, min_index, max_index = caclculate_histo(img)
    new_histo = np.zeros(256, np.int32)
    for i in range(0, img.shape[0]):
        for j in range(0, img.shape[1]):
            new_img[i][j] = int(((img[i][j] - min_index) / (max_index - min_index)) * 255)
            intensity = int(((img[i][j] - min_index) / (max_index - min_index)) * 255)
            new_histo[intensity] += 1
    plt.plot(histo, color='red')
    plt.plot(new_histo, color='blue')
    plt.title("Enhanced image histogram vs old histogram")
    plt.show()

    result = np.hstack([new_img, img])
    # save the enhanced img  in result.png
    cv.imwrite('result2.png', result)
    # show the enhanced image
    plt.imshow(result, cmap=plt.get_cmap('gray'))
    plt.title("Enhanced image vs old image(without library)")
    plt.show()
    return


# calculate histogram of the given image
def caclculate_histo(img):
    histo = np.zeros(256, np.int32)
    for i in range(0, img.shape[0]):
        for j in range(0, img.shape[1]):
            histo[img[i][j]] += 1
    for i in range(0, 256):
        if (histo[i] != 0):
            min_index = i
            break
    for i in range(255, -1, -1):
        if (histo[i] != 0):
            max_index = i
            break
    return histo, min_index, max_index


###########################################

# enhance the given img
enhance_img_with_library(img_address)
enhance_img_from_scratch(img_address)
