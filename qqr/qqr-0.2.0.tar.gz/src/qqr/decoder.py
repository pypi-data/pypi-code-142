# flake8: noqa

import time
from .classifier import Classifier
from .deblur import Deblur
from .skew import Skew
import cv2


def read_qr_code(img):
    """Read an image and read the QR code.
    
    Args:
        filename (string): Path to file
    
    Returns:
        qr (string): Value from QR code
    """

    try:
        detect = cv2.QRCodeDetector()
        value, points, straight_qrcode = detect.detectAndDecode(img)
        return value
    except:
        return None


def Decoder(filename, verbose=False, deblurType="blind", saveFile=None, decode=True):
    """Decode an image and return the QR code.

    Args:
        filename (string): Path to file
        verbose (bool): Enable verbose logging
        deblurType (string): Type of deblur to use: blind or non-blind
        saveFile (string): Path to save the processed image
        decode (bool): Enable decoding of the image

    Returns:
        qr (string): Value from QR code
    """

    if verbose:
        print("Processing file: {}".format(filename))

    start = time.time()
    if verbose:
        print("Classifying image...")
    type = Classifier(filename, verbose)
    if verbose:
        print(
            f"Image classified as: {type}, took {time.time() - start:.2f} seconds")

    if verbose:
        print("Loading image...")
    img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    output = None

    start = time.time()
    if type == "Blurred":
        if verbose:
            print("Deblurring image...")
        output = Deblur(img, verbose, deblurType) * 255
        if verbose:
            print(
                f"Image deblurred, took {time.time() - start:.2f} seconds")

    elif type == "Skewed":
        if verbose:
            print("Deskewing image...")
        skew = Skew()
        output = skew.deskew(img)

    if output is None:
        print("Unfortunatly, we can't process this image")

    if saveFile:
        if verbose:
            print("Saving image...")
        cv2.imwrite(saveFile, output)

    if decode:
        if verbose:
            print("Decoding image...")
        start = time.time()
        decoded = read_qr_code(img)
        if verbose:
            print(
                f"Image decoded, took {time.time() - start:.2f} seconds")
        print(f"The result is: {decoded}")
        return decoded
