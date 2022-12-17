"""
Defines the call to compress Image
"""
import os
import piexif
from PIL import Image

from compressor.datastructures.input import Input
from compressor.datastructures.result import Result
from compressor.compression.pngcompression import compressPNG
from compressor.compression.jpegcompression import compressJPEG


def compress(input: Input) -> Result:
    """
    The entry compression function
    """
    try:
        image: Image.Image
        with Image.open(input.imageSource) as image:
            imageFormat: str = image.format.upper()
            imageMode: str = image.mode
        if imageFormat in ("JPEG"):
            return compressJPEG(input)
        if imageFormat in ("PNG"):
            return compressPNG(input)
    except OSError:
        return Result(imageSource=input.imageSource,
                      initialFormat="", finalFormat="",
                      initialMode="", finalMode="",
                      initialColors=0, finalColors=0,
                      initialSize=os.path.getsize(input.imageSource),
                      finalSize=0, compressed=False, downsized=False,
                      exifBefore=False, exifNow=False,
                      displayConfig=input.displayConfig)
    try:
        exifBefore = True if piexif.load(input.imageSource)['Exif'] else False
    except piexif.InvalidImageDataError:
        exifBefore = False
    except ValueError:
        exifBefore = False
    return Result(imageSource=input.imageSource,
                  initialFormat=imageFormat, finalFormat=imageFormat,
                  initialMode=imageMode, finalMode=imageMode,
                  initialColors=0, finalColors=0,
                  initialSize=os.path.getsize(input.imageSource),
                  finalSize=0, compressed=False, downsized=False,
                  exifBefore=exifBefore, exifNow=exifBefore,
                  displayConfig=input.displayConfig)
