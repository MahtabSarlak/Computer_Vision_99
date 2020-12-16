import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img_address = "images.jpg"
img_matrix = cv.imread(img_address, 0)


#######################################################
def flat_histogram():
    constant = int((img_matrix.shape[0] * img_matrix.shape[1]) / 256)
    print(constant)

    for i in range(0, 255):
        tmp_histo = np.zeros(256, np.int32)
        tmp_histo = caclculate_histo(img_matrix)
        number = tmp_histo[i]
        if(i%40==0):
            plt.plot(tmp_histo, color='red')
            plt.show()
        print(i.__str__() + " " + number.__str__())
        if(i != 0):
            print("after move : " +tmp_histo[i-1].__str__())
        if (number < constant):
            print("less than")
            difference = constant - number
            print((i + 1).__str__() + " " + i.__str__() + " " + difference.__str__() + " " + tmp_histo[
                i + 1].__str__() + " " +
                  tmp_histo[i].__str__())
            movePixels(i + 1, i, difference)
        else:
            print("more than")
            difference = number - constant
            print((i + 1).__str__() + " " + i.__str__() + " " + difference.__str__() + " " + tmp_histo[
                i + 1].__str__() + " " +
                  tmp_histo[i].__str__())
            movePixels(i, i + 1, difference)

    show_result(img_matrix)
    return


#######################################################
def movePixels(from_index, to_index, difference):
    counter = 0
    is_done = False
    added = 0
    while (not is_done):
        for x in range(img_matrix.shape[0]):
            if (not is_done):
                for y in range(img_matrix.shape[1]):
                    if (not is_done):
                        if (img_matrix[x, y] == from_index + added):
                            img_matrix[x, y] = to_index
                            counter += 1
                            if (counter >= difference):
                                is_done = True
                                break
                    else:
                        break
            else:
                break
        if (from_index < to_index):
            is_done = True
        else:
            if (is_done):
                break
            else:
                added += 1
    return


#######################################################
# calculate histogram of the given image
def caclculate_histo(img):
    histo = np.zeros(256, np.int32)
    for i in range(0, img.shape[0]):
        for j in range(0, img.shape[1]):
            histo[img[i][j]] += 1
    return histo


#######################################################
# show the flat histogram
def show_result(img):
    new_histo = np.zeros(256, np.int32)
    new_histo = caclculate_histo(img)
    plt.plot(new_histo, color='blue')
    plt.title("Enhanced image histogram")
    plt.show()
    # save the enhanced img  in result.png
    cv.imwrite('result3.png', img)
    # show the enhanced image
    plt.imshow(img, cmap=plt.get_cmap('gray'))
    plt.title("Enhanced image")
    plt.show()
    return


#######################################################
# main
# enhance the given img
flat_histogram()
