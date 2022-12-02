# flake8: noqa

import numpy as np
import pylops
from skimage import io, util
import cv2
from pathlib import Path


def conv(image, kernel):
    """ An implementation of convolution filter.

    This function uses element-wise multiplication and np.sum()
    to efficiently compute weighted sum of neighborhood at each
    pixel.

    Args:
        image: numpy array of shape (Hi, Wi)
        kernel: numpy array of shape (Hk, Wk)

    Returns:
        out: numpy array of shape (Hi, Wi)
    """
    Hi, Wi = image.shape
    Hk, Wk = kernel.shape
    out = np.zeros((Hi, Wi))

    # For this assignment, we will use edge values to pad the images.
    # Zero padding as used in the previous assignment can make
    # derivatives at the image boundary very big.

    pad_width0 = Hk // 2
    pad_width1 = Wk // 2
    pad_width = ((pad_width0, pad_width0), (pad_width1, pad_width1))
    padded = np.pad(image, pad_width, mode='edge')

    #####################################
    #       START YOUR CODE HERE        #
    #####################################
    kernel = np.flip(np.flip(kernel, 0), 1)
    for i in range(Hi):
        for j in range(Wi):
            out[i, j] = np.sum(padded[i:i+Hk, j:j+Wk] * kernel)
    ######################################
    #        END OF YOUR CODE            #
    ######################################

    return out


def non_blind(imblur):

    #####################################
    #       START YOUR CODE HERE        #
    #####################################
    Nz = 300
    Nx = 300
    size = 10
    R = 30

    h = uniform_disk_kernel(size, R)

    imblur = cv2.resize(imblur, dsize=(Nz, Nx), interpolation=cv2.INTER_CUBIC)

    imdeblur = deblur(imblur, h)

    imdeblur = cv2.normalize(
        imdeblur, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
    for i in range(Nz):
        for j in range(Nx):
            if (imdeblur[i][j] >= 0.52):
                imdeblur[i][j] = 1.
            else:
                imdeblur[i][j] = 0.
    ######################################
    #        END OF YOUR CODE            #
    ######################################

    return imdeblur


def blind(imblur):

    #####################################
    #       START YOUR CODE HERE        #
    #####################################
    Nz = 300
    Nx = 300
    imblur = util.img_as_float(imblur)
    imblur = cv2.resize(imblur, dsize=(Nz, Nx), interpolation=cv2.INTER_CUBIC)
    imblur1 = imblur
    binar = np.zeros((Nz, Nx))
    mean = np.mean(imblur)
    for i in range(Nz):
        for j in range(Nx):
            if (imblur[i][j] >= mean):
                binar[i][j] = 1.
            else:
                binar[i][j] = 0.
    binar, xl, xr, xu, xd = crop_edges(binar)
    imblur = imblur[xl:xr, xu:xd]
    Nz, Nx = binar.shape
    mean = np.mean(imblur)
    for i in range(Nz):
        for j in range(Nx):
            if (imblur[i][j] >= mean):
                binar[i][j] = 1.
            else:
                binar[i][j] = 0.
    u = 25
    for j in range(Nx):
        if (binar[u][j] == 0):
            xu = j
            break
    for i in range(Nz):
        if (binar[i][u] == 0):
            xl = i
            break
    t = 0
    for j in range(Nx):
        if (binar[u][j] == 1 and binar[u][j-1] == 0):
            t = t+1
            if (t == 3):
                xd = j
                break
    t = 0
    for i in range(Nz):
        if (binar[u][i] == 1 and binar[u][i-1] == 0):
            t = t+1
            if (t == 3):
                xr = i
                break
    finder_blur = imblur[xl:xr, xu:xd]
    finder_clear = io.imread(
        f"{Path(__file__).parent.absolute()}/clear.png", as_gray=True)
    finder_blur = cv2.resize(finder_blur, dsize=(
        80, 80), interpolation=cv2.INTER_CUBIC)
    finder_clear = cv2.resize(finder_clear, dsize=(
        80, 80), interpolation=cv2.INTER_CUBIC)
    finder_blur = cv2.normalize(
        finder_blur, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
    finder_clear = cv2.normalize(
        finder_clear, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
    l = -1000
    for i in range(1, 31, 1):
        for j in range(1, 31, 1):
            h = uniform_disk_kernel(i, j)
            a = gaussian_kernel(i, j)
            blur1 = blurry(finder_clear, h)
            blur1 = cv2.normalize(
                blur1, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
            y = finder_blur
            xm = np.mean(blur1)
            ym = np.mean(y)
            sigmaxy = np.sum(((blur1-xm)*(y-ym))**2)**0.5
            sigmax = np.sum((blur1-xm)**2)**0.5
            sigmay = np.sum((y-ym)**2)**0.5
            mse1 = (sigmaxy*4*xm*ym)/((xm**2+ym**2)*(sigmax**2+sigmay**2))
            blur2 = blurry(finder_clear, a)
            blur2 = cv2.normalize(
                blur2, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
            xm = np.mean(blur2)
            ym = np.mean(finder_blur)
            sigmaxy = np.sum(((blur2-xm)*(finder_blur-ym))**2)**0.5
            sigmax = np.sum((blur2-xm)**2)**0.5
            sigmay = np.sum((finder_blur-ym)**2)**0.5
            mse2 = (sigmaxy*4*xm*ym)/((xm**2+ym**2)*(sigmax**2+sigmay**2))
            if (mse1 < mse2):
                mse = mse1
            else:
                mse = mse2
            if (mse > l):
                l = mse
            # print(mse)
                h_ker = h
                t = i
                p = j
    imdeblur = deblur(imblur1, h_ker)
    imdeblur = cv2.normalize(
        imdeblur, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
    Nz, Nx = imdeblur.shape
    for i in range(Nz):
        for j in range(Nx):
            if (imdeblur[i][j] >= 0.52):
                imdeblur[i][j] = 1
            else:
                imdeblur[i][j] = 0
    ######################################
    #        END OF YOUR CODE            #
    ######################################

    return imdeblur


def gaussian_kernel(size, sigma):
    """ Implementation of Gaussian Kernel.
    
    This function follows the gaussian kernel formula,
    and creates a kernel matrix.

    Hints:
    - Use np.pi and np.exp to compute pi and exp
    
    Args:
        size: int of the size of output matrix
        sigma: float of sigma to calculate kernel

    Returns:
        kernel: numpy array of shape (size, size)
    """

    kernel = np.zeros((size, size))

    #####################################
    #       START YOUR CODE HERE        #
    #####################################
    for i in range(size):
        for j in range(size):
            kernel[i, j] = (1/(2*np.pi*sigma**2)) * np.exp(-((i - size//2)
                                                             ** 2 + (j - size//2)**2) / float(2*sigma**2))
    ######################################
    #        END OF YOUR CODE            #
    ######################################

    return kernel


def uniform_disk_kernel(size, R):
    """ Implementation of Gaussian Kernel.
    
    This function follows the gaussian kernel formula,
    and creates a kernel matrix.

    Hints:
    - Use np.pi and np.exp to compute pi and exp
    
    Args:
        size: int of the size of output matrix
        sigma: float of sigma to calculate kernel

    Returns:
        kernel: numpy array of shape (size, size)
    """

    kernel = np.zeros((size, size))

    #####################################
    #       START YOUR CODE HERE        #
    #####################################
    for i in range(size):
        for j in range(size):
            if (i**2+j**2 <= R**2):
                kernel[i][j] = 1./(np.pi*R**2)
    ######################################
    #        END OF YOUR CODE            #
    ######################################

    return kernel


def blurry(img, h):

    #####################################
    #       START YOUR CODE HERE        #
    #####################################
    Nz, Nx = img.shape
    size1, size2 = h.shape
    Cop = pylops.signalprocessing.Convolve2D(
        (Nz, Nx), h=h, offset=(size1 // 2, size2 // 2), dtype="float32")

    imblur = Cop * img
    ######################################
    #        END OF YOUR CODE            #
    ######################################

    return imblur


def deblur(img, h):

    #####################################
    #       START YOUR CODE HERE        #
    #####################################
    Nz, Nx = img.shape
    size1, size2 = h.shape

    Cop = pylops.signalprocessing.Convolve2D(
        (Nz, Nx), h=h, offset=(size1 // 2, size2 // 2), dtype="float32")

    imdeblur = pylops.optimization.leastsquares.normal_equations_inversion(
        Cop, img.ravel(), None, maxiter=50)[0]
    imdeblur = imdeblur.reshape(Cop.dims)

    ######################################
    #        END OF YOUR CODE            #
    ######################################

    return imdeblur


# def show(img):
#     fig, ax = plt.subplots(1, 1, figsize=(5, 3))
#     him = ax.imshow(img)
#     ax.set_title("Blurring operator")
#     fig.colorbar(him, ax=ax)
#     ax.axis("tight")

#     return


def lighting_image(img, coef):
    img = np.array(img) / 255
    img = img + img * coef
    img[img > 1] = 1
    return img


def crop_edges(binar):
    Nz, Nx = binar.shape
    for j in range(3, Nx):
        if (binar[49][j] == 0):
            xu = j
            break

    for i in range(3, Nz):
        if (binar[i][49] == 0):
            xl = i
            break

    for j in range(Nx-4, 0, -1):
        if (binar[49][j] == 0):
            xd = j
            break
    for i in range(Nz-4, 0, -1):
        if (binar[i][49] == 0):
            xr = i
            break
    img = binar[xl:xr, xu:xd]
    return img, xl, xr, xu, xd


def Deblur(img, verbose, deblurType):
    if deblurType == 'blind':
        if verbose:
            print("Blind deblurring...")
        return blind(img)
    else:
        if verbose:
            print("Non-blind deblurring...")
        return non_blind(img)
