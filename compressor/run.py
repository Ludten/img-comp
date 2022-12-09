import os
import sys
from timeit import default_timer as timer

try:
    import PIL
except ImportError:
    print("\n\tThis software needs Pillow installed")
    sys.exit()

try:
    import piexif
except ImportError:
    print("\n\tThis software needs Piexif installed")
    sys.exit()

from compressor.parser.argsparser import arguments
from compressor.datastructures.input import Input
from compressor.compression.compress import compress
from compressor.config import concurrency, DisplayConfiguration, Symbols
from compressor.reports.report import readable, fileStatus, finalReport, displayError
from compressor.exceptions import KeyboardInterupt, ImagesNotFoundError, InvalidPathError


def execute(imagePath, quality, width, height,
            keepExif, grayScale, compareSize, displayConfig):
    """
    Define execution sequence
    """
    start = timer()
    lineWidth = concurrency()[0]
    found = 0
    compressed = 0
    # skipped = 0
    totalImageSize = 0
    bytesSaved = 0
    if os.path.isfile(imagePath):
        found = 1 
        image = Input(imagePath, quality, width, height,
                      keepExif, grayScale, compareSize, displayConfig)
        result = compress(image)
        totalImageSize = result.initialSize
        if result.compressed:
            compressed = 1
            bytesSaved = result.initialSize - result.finalSize
        if not result.displayConfig.silent:
            symbols = Symbols()
            fileStatus(result, lineWidth, symbols)
    else:
        raise InvalidPathError("\nThe given image path can not be found\n")
    if found:
        finish = timer() - start
        finalReport(found, compressed, totalImageSize,
                    bytesSaved, finish, displayConfig)
    else:
        raise ImagesNotFoundError("\nImage format is not supported\n")


def run():
    args = arguments()
    try:
        execute(*args)
    except (KeyboardInterupt, ImagesNotFoundError, InvalidPathError) as e:
        print(e.message)


if __name__ == "__main__":
    run()
