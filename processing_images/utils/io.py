from skimage.io import imread, imsave


def img_read(path, is_gray=False):
    image = imread(path, as_gray = is_gray)
    return image

def save_image(image, path):
    imsave(path, image)

