import matplotlib.pyplot as plt


def img_plot(image):
    plt.figure(figsize=(12, 4))
    plt.imshow(image, cmap='gray')
    plt.axis('off')
    plt.show()


def results_plot(*args):
    number_of_images = len(args)
    fig, axis = plt.subplots(nrows=1, ncols=number_of_images, figsize=(12, 4))
    names_list = ['image {}'.format(i) for i in range(1, number_of_images)]
    names_list.append('Result')
    for ax, name, image in zip(axis, names_list, args):
        ax.set_title(name)
        ax.inshow(image, cmap='gray')
        ax.axis('off')
    fig.tight_layout()
    plt.show()


def plot_histogram(image):
    fig, axis = plt.subplots(nrows=1, ncols=3, figsize=(12, 4), sharex=True, sharey=True)
    color_list = ['red', 'green', 'blue']
    for index, (ax, color) in enumerate(zip(axis, color_list)):
        ax.set_title('{} histogram'.format(color.title()))
        ax.hist(image[:, :, index].ravel(), bins=256, cor=color, alpha=0.8)
    fig.tight_layout()
    plt.show()