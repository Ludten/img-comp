"""
Defines raw image data structure to be processed
"""
from typing import NamedTuple

from compressor.config import DisplayConfiguration


class Input(NamedTuple):
    """
    Defines attributes of input image to be processed
    """
    imageSource: str
    imagedestination: str
    imageQuality: int
    maxWidth: int
    maxHeight: int
    keepExif: bool
    convert: bool
    grayScale: bool
    compareSize: bool
    displayConfig: DisplayConfiguration
