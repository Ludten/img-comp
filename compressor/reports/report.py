"""
Defines report functions and helpers
"""
from functools import lru_cache

from compressor.config import Symbols
from compressor.datastructures.result import Result
from compressor.config import DisplayConfiguration


@lru_cache(maxsize=None)
def readable(num: int, suffix="B") -> str:
    """
    Produces a human readable memory image size in string format
    """
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if abs(num) < 1024:
            return f"{num:3.1f} {unit}{suffix}"
        num = num / 1024
    return f"{num:.1f}{'Yi'}{suffix}"


def fileStatus(result: Result, lineWidth: int, symbols: Symbols):
    """
    This fuction monitors and displays file status
    """
    displayConfig = result.displayConfig
    if displayConfig.summary or \
            displayConfig.progress or displayConfig.silent:
        return
    if result.compressed:
        initialSize = readable(result.initialSize)
        finalSize = readable(result.finalSize)
        percentage = 100 - (result.finalSize / result.initialSize * 100)
        shortImage = result.imageSource[-(lineWidth - 17):].ljust(lineWidth - 17)
        initialFormat = result.initialFormat.replace("JPEG", "JPG")
        finalFormat = result.finalFormat.replace("JPEG", "JPG")
        exifBefore = symbols.info if result.exifBefore else ""
        exifNow = symbols.info if result.exifNow else ""
        downsized = symbols.downsized if result.downsized else ""
        if result.initialMode == "P":
            initalColors = f"{result.initalColors}"
        else:
            initalColors = ""
        if result.finalMode == "P":
            finalColors = f"{result.finalColors}"
        else:
            finalColors = ""
        imageStatus = f"\n{symbols.compressed}  [COMPRESSED] {shortImage}\n" \
            f"  {exifBefore} " \
            f" {initialFormat}/{result.initialMode}{initalColors}: {initialSize}" \
            f"  -> " \
            f"{downsized}{exifNow}{finalFormat}/{result.finalMode}{finalColors}: " \
            f"{finalSize} {symbols.reduced} {percentage:.1f}%"
    else:
        shortImage = result.imageSource[-(lineWidth - 15):].ljust(lineWidth - 15)
        imageStatus = f"\n{symbols.skipped} [SKIPPED] {shortImage}"
    print(imageStatus, end="")


def finalReport(foundFiles: int, compressedFiles: int,
                sourceSize: int, bytesSaved: int,
                time: float, displayConfig: DisplayConfiguration):
    """
    Displays final report with bytes saved and time spent to perform the operations
    """
    if displayConfig.silent:
        return
    filesPerSec = foundFiles / time
    average = bytesSaved / compressedFiles if bytesSaved else 0
    percentage = bytesSaved / sourceSize * 100 if bytesSaved else 0
    report = f"\n{40 * '-'}\n"
    if time == -1:
        report += f"\n  Processed {foundFiles} files ({readable(sourceSize)})."
    else:
        report += f"\n  Processed {foundFiles} files ({readable(sourceSize)}) in " \
            f"{time:.1f}s ({filesPerSec:.1f} files/sec)."
    report += f"\n  Compressed {compressedFiles} files." \
        f"\n  Average savings: {readable(average)} per processed file" \
        f"\n  Total space saved: {readable(bytesSaved)} / {percentage:.1f}%\n"
    print(report)


def displayError(exception: Exception, path: str, message: str = "") -> None:
    """
    Displays errors ecncouterd while processing image
    """
    print(f"\nAn error occured while trying to compress this file:\n{path}")
    if message:
        print(f"\n{message}")
    print(f"\nUse the infomation to better understand what went wrong:\n{exception}")
