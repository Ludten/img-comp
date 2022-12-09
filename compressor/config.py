"""
Software configuration settings
"""
import shutil
from typing import NamedTuple, Tuple, Union
from functools import lru_cache
from multiprocessing import cpu_count
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import ThreadPoolExecutor


class DisplayConfiguration(NamedTuple):
    """
    Output display configuration options
    """
    summary: bool
    progress: bool
    silent: bool


class Symbols:
    """
    configure icons for result display
    """
    def __init__(self) -> None:
        print("\nSymbols definition:\n\n"
              "  OK -> Compressed file      i -> Exif information present\n\n"
              "  -- -> Skipped file         V -> Image was downsize          "
              "  v -> Size was reduced\n")
        self.info = "i"
        self.downsized = "V"
        self.compressed = "OK"
        self.skipped = '--'
        self.reduced = 'v'


@lru_cache(maxsize=None)
def concurrency() -> Tuple[int,
        Union[ThreadPoolExecutor, ProcessPoolExecutor], int]:
    """
    Setting up for concurrency
    """
    lineWidth = shutil.get_terminal_size((80, 24)).columns
    workers = cpu_count() + 1
    return lineWidth, ProcessPoolExecutor, workers
