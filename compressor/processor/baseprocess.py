"""
Smart Image processing
"""
import os
from io import BytesIO
from typing import Tuple
from PIL import Image

from compressor.reports.report import displayError

def grayScaleImage(image: Image.Image) -> Image.Image:
    """
    Make grayscale out of the image
    """
    mode = image.mode
    if mode in ["RGB", "CMYK", "YCbCr" "LAB", "HSV"]:
        return image.convert("L")
    elif mode == "RGBA":
        return image.convert("LA").convert("RGBA")
    # Todo: add condition for mode 'P' for PNG images
    return image


def downsizeImage(image: Image.Image,
        maxWidth: int, maxHeight: int) -> Tuple[Image.Image, bool]:
    """
    Resizes the image to the specified size
    """
    width, height = image.size
    maxWidth = width if not maxWidth else maxWidth
    maxHeight = height if not maxHeight else maxHeight
    if (width, height) == (maxWidth, maxHeight):
        return image, False
    image.thumbnail((maxWidth, maxHeight), resample=Image.LANCZOS)
    return image, True


def save(source: str, buffer: BytesIO, compareSizes: bool,
         forceDelete: bool = False, output: str = "") -> Tuple[bool, int]:
    """
    save compressed image and decide if to delete source file
    """
    initialSize = os.path.getsize(source)
    finalSize = buffer.getbuffer().nbytes
    output = output if output else source
    if not compareSizes or (finalSize / initialSize < 0.99):
        buffer.seek(0)
        with open(output, 'wb') as file:
            file.write(buffer.getbuffer())
        compressed  = True
        if forceDelete:
            try:
                os.remove(source)
            except OSError as e:
                message = "Error occured while tryig to remove initial file"
                displayError(e, source, message)
    else:
        compressed = False
        finalSize = initialSize
    return compressed, finalSize
