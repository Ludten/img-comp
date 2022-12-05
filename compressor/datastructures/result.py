"""
Defines data attributes of a processed image
"""
from typing import NamedTuple

from compressor.config import DisplayConfiguration


class Result(NamedTuple):
    """
    Defines properties of processed image
    """
    hadExif: bool
    hasExif: bool
    finalColors: int
    finalFormat: str
    finalMode: str
    finalSize: int
    image: str
    initialColors: int
    initialFormat: str
    initialMode: int
    initialSize: int
    optimized: bool
    downsized: bool
    displayConfig: DisplayConfiguration
