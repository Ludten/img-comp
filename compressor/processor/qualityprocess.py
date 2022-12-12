"""
Engineers the quality of the image to be proccessed
"""
from math import log
from io import BytesIO
from PIL import Image
from PIL import ImageStat, ImageChops
from typing import Tuple, Optional
from functools import lru_cache

from compressor.constants import DEFAULT_IMAGE_QUALITY


def compareImage(image1: Image.Image, image2: Image.Image) -> Optional[float]:
    """
    Calculates the differnce between two images of the same size using
    their channel values at pixel level
    """
    if (image1.size != image2.size) \
            or (image1.mode != image2.mode) \
            or (image1.getbands() != image2.getbands()):
        return None
    tempImage = ImageChops.difference(image1, image2)
    stats = ImageStat.Stat(tempImage)
    diffRatio = sum(stats.mean) / (len(stats.mean) * 255)
    return diffRatio * 100


def getQualityDiffrence(image, quality: int) -> float:
    """
    Calculates and returns score difference
    for the `picture` image saved at the specified quality
    """
    tempImage = BytesIO()
    image.save(tempImage, quality=quality, format="JPEG", progressive=True)
    tempImage.seek(0)
    diffScore = compareImage(image, Image.open(tempImage))
    if diffScore < 0:
        diff = -1 + diffScore / 100
    else:
        diff = 1 - diffScore / 100
    return diff


@lru_cache(maxsize=None)
def bstIterCount(low: int, high: int) -> int:
    """
    Calculates and returns the binary search tree within the given range
    """
    if high <= low:
        return 0
    else:
        return int(log(high - low, 2)) + 1


def jpegQuality(image: Image.Image, dynamic: bool = True) -> Tuple[int, float]:
    """
    Calculates and returns an optimum quality
    to meet the quality required by the image class
    """
    desired = 0.992
    high = DEFAULT_IMAGE_QUALITY
    low = high - 5
    pic = image.resize((400, 400))
    if not dynamic:
        defaultDiffrence = getQualityDiffrence(pic, high)
        return high, defaultDiffrence
    normalDifference = getQualityDiffrence(pic, 95)
    selectedDifference = selectedQuality = None
    for _ in range(bstIterCount(low, high)):
        currentQuality = (low + high) // 2
        currentDifference = getQualityDiffrence(pic, currentQuality)
        differenceRatio = currentDifference / normalDifference
        if differenceRatio >= desired:
            selectedQuality = currentQuality
            selectedDifference = currentDifference
            high = currentQuality
        else:
            low = currentQuality
    if selectedQuality:
        return selectedQuality, selectedDifference
    else:
        defaultDiffrence = getQualityDiffrence(pic, high)
        return high, defaultDiffrence
