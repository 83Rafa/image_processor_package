import numpy as np
from skimage.color import rgb2gray
from skimage.exposure import match_histograms
from skimage.metrics import structural_similarity

def find_diferences (img_1, img_2):
    assert img_1.shape == img_2.shape, "Specify 2 images with de same shape."
    gray_img1 = rgb2gray(img_1)
    gray_img2 = rgb2gray(img_2)
    (score, img_differences) = structural_similarity(gray_img1, gray_img2, full=True)
    print("Similarity of the images: ", score)
    normalized_img_differences = (img_differences-np.min(img_differences))/(np.max(img_differences)-np.min(img_differences))
    return normalized_img_differences

def histogram_transfer(image1, image2):
    matched_image = match_histograms(image1, image2, multichannel=True)
    return matched_image