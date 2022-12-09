"""
Defines Exception class

NB: The attribute `message` is the explanation of the error
"""

class KeyboardInterupt(KeyboardInterrupt):
    """Exception raised on keyboard interrupt (typically CTRL-C)."""

    def __init__(self, message=""):
        self.message = message
        super().__init__(self.message)

class ImagesNotFoundError(FileNotFoundError):
    """Exception raised when there were no images found."""

    def __init__(self, message=""):
        self.message = message
        super().__init__(self.message)

class InvalidPathError(ValueError):
    """Exception raised when there were no images found."""
    
    def __init__(self, message=""):
        self.message = message
