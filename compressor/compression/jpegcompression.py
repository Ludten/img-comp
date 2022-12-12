"""
JPEG compression
"""
import os
import piexif
from io import BytesIO
from PIL import Image, ImageFile

from compressor.datastructures.input import Input
from compressor.datastructures.result import Result
from compressor.processor.qualityprocess import jpegQuality
from compressor.processor.baseprocess import downsizeImage, grayScaleImage, save


def compressJPEG(input: Input) -> Result:
    """
    Compresses an image of type jpg
    """
    image: Image.Image = Image.open(input.imageSource)
    initalFormat = image.format
    initialMode = image.mode
    initialSize = os.path.getsize(input.imageSource)
    initialColors, finalColors = 0, 0
    finalFormat = "JPEG"
    try:
        exifBefore = True if piexif.load(input.imageSource)['Exif'] else False
    except piexif.InvalidImageDataError:
        exifBefore = False
    except ValueError:
        exifBefore = False
    except Exception:
        exifBefore = False
    if input.maxWidth or input.maxHeight:
        image, downsized = downsizeImage(image, input.maxWidth, input.maxHeight)
    else:
        downsized = False
    if input.grayScale:
        image = grayScaleImage(image)
    useProgressive = initialSize > 10000
    quality = jpegQuality(image)[0]
    buffer = BytesIO()
    try:
        image.save(buffer, quality=quality, optimize=True,
                    progressive=useProgressive, format=finalFormat)
    except IOError:
        ImageFile.MAXBLOCK = image.size[0] * image.size[1]
        image.save(buffer, quality=quality, optimize=True,
                    progressive=useProgressive, format=finalFormat)
    if input.keepExif and exifBefore:
        try:
            piexif.transplant(os.path.expanduser(input.imageSource), buffer)
            exifNow = True
        except ValueError:
            exifNow = False
        except Exception:
            exifNow = False
    else:
        exifNow = False
    finalMode = image.mode
    image.close()
    compareSize = not input.compareSize
    compressed, finalSize = save(input.imageSource, buffer,
                                 compareSize, output=input.imagedestination)
    return Result(input.imageSource, initalFormat, finalFormat, initialMode,
            finalMode, initialColors, finalColors, initialSize, finalSize,
            compressed, downsized, exifBefore, exifNow, input.displayConfig)
