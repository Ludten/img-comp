"""
Defines raw image data structure to be processed
"""
from typing import NamedTuple, Tuple

from compressor.config import DisplayConfiguration


class Input(NamedTuple):
    """
    Defines attributes of input image to be processed
    """
    backgroundColor: Tuple[int, int, int]
    compareSize: bool
    fastMode: bool
    forceDelete: bool
    grayScale: bool
    imageQuality: int
    imageSource: str
    keepExif: bool
    maximumColors: int
    maximumHeight: int
    maximumWidth: int
    reduceColor: bool
    removeTransparency: bool
    displayConfiguration: DisplayConfiguration
