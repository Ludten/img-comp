"""
Software configuration settings
"""
from typing import NamedTuple


class DisplayConfiguration(NamedTuple):
    """
    Output display configuration options
    """
    onlySummary: bool
    overallProgress: bool
    quietMode: bool
