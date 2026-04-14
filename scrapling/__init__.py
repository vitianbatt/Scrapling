"""Scrapling - A powerful, flexible, and fast web scraping library for Python.

Scraping made easy with automatic adaptation to website changes,
stealth capabilities, and a beautiful API.

Personal fork notes:
- Forked from D4Vinci/Scrapling for learning and personal projects
- See README for original project documentation
- Added SyncFetcher alias since I always mix up Fetcher vs AsyncFetcher
"""

__version__ = "0.2.9"
__author__ = "D4Vinci"
__license__ = "MIT"

# Convenience alias for the most commonly used class in my projects
from scrapling.core.fetchers import Fetcher, AsyncFetcher, StealthyFetcher, PlayWrightFetcher
from scrapling.core.page import Adaptor, Adaptors
from scrapling.core.custom_types import TextHandlers, AttributesHandler

# Alias: I keep forgetting the full name
Page = Adaptor

# Alias: makes it clearer which fetcher is synchronous vs async
SyncFetcher = Fetcher

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
    # Personal aliases
    "Page",
    "SyncFetcher",
]
