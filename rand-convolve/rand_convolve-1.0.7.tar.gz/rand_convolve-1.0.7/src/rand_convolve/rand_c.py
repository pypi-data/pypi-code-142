"""
"PIL.Image", "scipy.signal.convolve2d", and "numpy" imported.

PIL.Image - Main image manipulation/saving module.
scipy.signal.convolve2d - Powerful 2-dimensional convolution.
numpy - Powerful multi-use module, used for its power in array manipulation.

---

The purpose of this python script is to run a convolution on an image with random kernels.
"""

from time import perf_counter
from PIL import Image
from scipy.signal import convolve2d
import numpy as np

if __name__ == "__main__":
    ti = perf_counter()


def create_gen(list_, width):
    """
    Yields a generator for splitting a list into equal segments of length `width`.

    Arguments:
        list_: The list to split.
        width: The length of the segments to split `list_` into.

    Returns:
        A generator of the list segments.
    """
    if len(list_) % width:
        raise ValueError(
            f"'width' ({width}) must fit cleanly within length of 'path' ({len(list_)})")

    for i in range(int(len(list_)/width)):
        yield list_[i*width:(i+1)*width]


def create_kernel(size, sign=0):
    """
    Creates a randomized kernel of shape: (`size`,`size`).


    Arguments:
        size: Integer providing the size of the kernel.

        sign: Integer that determines the signs used for kernels. (default: 0)
            0:
                All Positive.
            1:
                Random Negative/Positive.
            2:
                All Negative.

    Returns:
        A 2-dimensional NDArray of floating point numbers.
    """
    # create kernel of dimensions KERNEL_SIZE x KERNEL_SIZE.
    kernel = np.random.default_rng().random((size, size))

    if sign == 1:
        kernel = kernel * \
            np.reshape((2*np.random.randint(0, 2, size=size**2)) -
                       1, (size, size))
    elif sign == 2:
        kernel = kernel * np.reshape([-1]*(size**2), (size, size))

    return kernel / np.sum(kernel)


def convolve_img(list_: tuple, kernel: list, width: int):
    """
    Convolves an image given a tuple of R, G, and B PIL.Image objects using `scipy.signal.convolve2d`.

    Arguments:
        list_: A tuple of R, G, and B Image objects.
            Format: `(Image, Image, Image)`
        kernel: A 2-dimensional kernel list to perform the convolution with.
        width: The width of the image.

    Returns:
        A flattened list of tuples holding RGB values.
            Format: [(R,G,B), ... ,(R,G,B)]
    """
    r, g, b = (list(create_gen(list(x.getdata()), width)) for x in list_)
    return list(zip(np.concatenate(np.int_(convolve2d(r, kernel, mode="same"))), np.concatenate(np.int_(convolve2d(g, kernel, mode="same"))), np.concatenate(np.int_(convolve2d(b, kernel, mode="same")))))


def rand_convolve(image: str, ksize=3, knum=20, ksign=0):
    """
    Convolves a given image to a set of randomized kernels.

    Arguments:
        image: The image path for the convolution.
        ksize: The size of the 2 dimensional kernel. The shape of the kernel is: (size, size). (default: 3)
        knum: The number of random kernels to generate and use. (default: 20)
            int n>0: The number of kernels.
            -1: Use a new kernel for each pixel.
        ksign: The signs to be used for the kernels. (default: 0)
            0: All kernel values are positive.
            1: Kernel signs are randomly mixed between negative and positive.
            2: All kernel values are negative.

    Returns:
        A PIL.Image object of the convoluted image.
    """
    img = Image.open(image)
    if img.width < ksize or img.height < ksize:
        raise ValueError(
            f"Image is too small ({img.width}px x {img.height}px) for kernel of size {ksize}.")
    width = img.width
    img = Image.Image.split(img.convert("RGB"))

    new_list = []
    kernels = [create_kernel(ksize, sign=ksign) for x in range(knum)]

    for i in range(knum):
        new_list.append(convolve_img(img, kernels[i], width))
    z = list(zip(*new_list))

    new_list = list(create_gen([z[x][x % knum] for x in range(len(z))], width))

    return Image.fromarray(np.array(new_list, dtype=np.uint8))


if __name__ == "__main__":
    print(f"Time to run: {perf_counter()-ti:0.4f} seconds")
