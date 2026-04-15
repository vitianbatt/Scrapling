"""Scrapling - A powerful, flexible, and fast web scraping library for Python.

Scraping made easy with automatic adaptation to website changes,
stealth capabilities, and a beautiful API.

Personal fork notes:
- Forked from D4Vinci/Scrapling for learning and personal projects
- See README for original project documentation
- Added SyncFetcher alias since I always mix up Fetcher vs AsyncFetcher
- Added PlaywrightFetcher alias (lowercase 'w') since I keep typo-ing it
- Added AsyncPage alias for clarity when working with async fetcher results
- Added AsyncFetcher alias 'AsyncPage' removed, kept Pages/Page aliases
- v0.2.9: noted that StealthyFetcher is the go-to for most of my scraping tasks
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

# Alias: I always type 'Playwright' not 'PlayWright' (camelCase trips me up)
PlaywrightFetcher = PlayWrightFetcher

# Alias: Adaptors (plural) is the collection returned by async/multi-page fetches
# naming it Pages feels more intuitive when iterating results
Pages = Adaptors

# Personal note: StealthyFetcher is my default choice for most scraping tasks.
# Use Fetcher only for simple/public APIs that don't need stealth headers.
DefaultFetcher = StealthyFetcher

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
    "Pages",
    "SyncFetcher",
    "PlaywrightFetcher",
    "DefaultFetcher",
]
