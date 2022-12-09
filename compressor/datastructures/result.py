"""
Defines data attributes of a processed image
"""
from typing import NamedTuple

from compressor.config import DisplayConfiguration


class Result(NamedTuple):
    """
    Defines properties of processed image
    """
    imageSource: str
    initialFormat: str
    finalFormat: str
    initialMode: str
    finalMode: str
    initialColors: int
    finalColors: int
    initialSize: int
    finalSize: int
    compressed: bool
    downsized: bool
    exifBefore: bool
    exifNow: bool
    displayConfig: DisplayConfiguration
