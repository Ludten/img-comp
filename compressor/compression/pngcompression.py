#!/usr/bin/python3
"""
PNG compression algorithm
"""
import os
from io import BytesIO

from PIL import Image, ImageFile

from compressor.datastructures.input import Input
from compressor.datastructures.result import Result
from compressor.processor.baseprocess import (downsizeImage, grayScaleImage,
                                              save, removeAlphaTransprency)


def compressPNG(input: Input) -> Result:
    """
    Compresses an image of type png
    """
    image: Image.Image = Image.open(input.imageSource)
    initalFormat = image.format
    initialMode = image.mode
    initialSize = os.path.getsize(input.imageSource)
    initialColors, finalColors = 0, 0
    directory, _ = os.path.split(input.imageSource)
    directory = os.getcwd() if directory == '' else directory
    exifBefore = exifNow = False
    if initialMode == 'P':
        finalColors = initialColors = len(image.getcolors())
    if input.convert:
        basename = os.path.splitext(os.path.basename(input.imageSource))[0]
        resultPath = os.path.join(directory + '/' + basename + '.jpg')
        if input.maxWidth or input.maxHeight:
            image, downsized = downsizeImage(image, input.maxWidth, input.maxHeight)
        else:
            downsized = False
        image = removeAlphaTransprency(image=image)
        image = image.convert("RGB")
        if input.grayScale:
            image = grayScaleImage(image)
        buffer = BytesIO()
        try:
            image.save(buffer, quality=input.imageQuality,
                       optimize=True, progressive=True, format='JPEG')
        except IOError:
            ImageFile.MAXBLOCK = image.size[0] * image.size[1]
            image.save(buffer, quality=input.imageQuality,
                       optimize=True, progressive=True, format='JPEG')
        finalMode = image.mode
        image.close()
        compareSize = not (input.compareSize or input.convert)
        compressed, finalSize = save(input.imageSource, buffer,
                                     compareSize, output=resultPath)
        return Result(input.imageSource, initalFormat, 'JPEG', initialMode,
            finalMode, initialColors, finalColors, initialSize, finalSize,
            compressed, downsized, exifBefore, exifNow, input.displayConfig)
    else:
        image = removeAlphaTransprency(image=image)
        if input.maxWidth or input.maxHeight:
            image, downsized = downsizeImage(image, input.maxWidth, input.maxHeight)
        else:
            downsized = False
        if input.grayScale:
            image = grayScaleImage(image)
        buffer = BytesIO()
        try:
            image.save(buffer, optimize=True, format="PNG")
        except IOError:
            ImageFile.MAXBLOCK = image.size[0] * image.size[1]
            image.save(buffer, optimize=True, format="PNG")
        finalMode = image.mode
        image.close()
        compareSize = not (input.compareSize)
        compressed, finalSize = save(input.imageSource,
                                     buffer, compareSize,
                                     output=input.imagedestination)
        return Result(input.imageSource, initalFormat, "PNG", initialMode,
            finalMode, initialColors, finalColors, initialSize, finalSize,
            compressed, downsized, exifBefore, exifNow, input.displayConfig)
