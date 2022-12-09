import os
from argparse import ArgumentParser

from compressor.config import DisplayConfiguration
from compressor.constants import DEFAULT_IMAGE_QUALITY, SUPPORTED_FORMATS


def supportedFormats() -> str:
    """
    Display supported image formats
    """
    formats = ", ".join(SUPPORTED_FORMATS).strip().upper()
    message = "This software supports the following image formats only:"
    return "\n{0} {1}\n\n".format(message, formats)


def arguments():
    """
    Detailed description of software and it's options
    """
    description = "An image compression software that reduces the size of an image, " \
                  "just by passing the path to the image to be processed."

    parser = ArgumentParser(description=description)

    helpPath = 'The path to the image file to be processed'
    
    parser.add_argument("src", nargs="?", type=str, help=helpPath)
    
    helpSupportedFormat = "Displays a list of supported image formats by the software"
    
    parser.add_argument("-f", "--formats", dest="supportedFormats",
        action="store_true", help=helpSupportedFormat)
    
    parser.add_argument("--summary", action="store_true",
        help="Shows only the summary of the compression process")
    
    parser.add_argument("-p", "--progress", action="store_true",
        help="Shows only the progress of the compression process")
    
    parser.add_argument("--silent", action="store_true",
        help="Processes the image quietly, without displaying progress or summary")

    generalGroup = parser.add_argument_group('CUSTOMIZE IMAGE PROCESS SETTINGS',
            description="This options can be used to modify the image compression process")
    
    generalGroup.add_argument("-mw", "--max-width", dest="maxWidth",
        type=int, default=0, help="Maximum width in pixels")
    
    generalGroup.add_argument("-mh", "--max-height", dest="maxHeight",
        type=int, default=0, help="Maximum height in pixels")
    
    generalGroup.add_argument("-gs", "--grayscale", dest="grayScale", action="store_true", help="Convert grayscale")
    
    helpNoComparison = "Do not compare the initial and final image, but save the final image"
    
    generalGroup.add_argument("-nc", "--no-comparison", dest="noComparison", action="store_true", help=helpNoComparison)

    jpegGroup = parser.add_argument_group("JPEG specific options",
        description="These options apply only to JPEG images")
    
    jpegGroup.add_argument("-q", "--quality", dest="imageQuality", type=int,
        help="Specify a fixed quality setting for JPEG files (an integer value, between 1 and 100).")
    
    jpegGroup.add_argument("-ke", "--keep-exif", dest="keepExif", action="store_true",
        help="Keep image EXIF data (this is discarded by defualt).")

    parser._positionals.title = parser._positionals.title.upper()
    parser._optionals.title = parser._optionals.title.upper()

    args = parser.parse_args()

    if args.supportedFormats:
        parser.exit(status=0, message=supportedFormats())
    if args.src:
        sourcePath = os.path.expanduser(args.src)
    else:
        parser.exit(status=0, message="\nPlease specify the path of the image to be processed\n")

    if not args.imageQuality:
        args.imageQuality = DEFAULT_IMAGE_QUALITY
    elif args.imageQuality > 100 or args.imageQuality < 1:
        parser.exit(status=0, message="\nImage quality must be between 1 and 100\n")

    if args.maxWidth < 0 or args.maxHeight < 0:
        parser.exit(status=0, message="\nImage dimensions should be positive integers\n")

    displayConfig = DisplayConfiguration(args.summary, args.progress, args.silent)
    return sourcePath, args.imageQuality, args.maxWidth, args.maxHeight, \
           args.keepExif, args.grayScale, args.noComparison, displayConfig
