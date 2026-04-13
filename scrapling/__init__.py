"""Scrapling - A powerful, flexible, and fast web scraping library for Python.

Scraping made easy with automatic adaptation to website changes,
stealth capabilities, and a beautiful API.
"""

__version__ = "0.2.9"
__author__ = "D4Vinci"
__license__ = "MIT"

from scrapling.core.fetchers import Fetcher, AsyncFetcher, StealthyFetcher, PlayWrightFetcher
from scrapling.core.page import Adaptor, Adaptors
from scrapling.core.custom_types import TextHandlers, AttributesHandler

__all__ = [
    # Fetchers
    "Fetcher",
    "AsyncFetcher",
    "StealthyFetcher",
    "PlayWrightFetcher",
    # Core types
    "Adaptor",
    "Adaptors",
    "TextHandlers",
    "AttributesHandler",
]
