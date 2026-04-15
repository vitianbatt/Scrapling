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
- v0.2.9.1: added NullFetcher sentinel and __version_info__ tuple for easier version checks
- v0.2.9.2: added NullFetcher as a no-op sentinel; added FetcherType for type hints
- v0.2.9.3: fixed FetcherType to use Union style compatible with Python 3.9
"""

__version__ = "0.2.9"
__version_info__ = (0, 2, 9)  # handy for programmatic version checks: if __version_info__ >= (0, 2, 9)
__author__ = "D4Vinci"
__license__ = "MIT"

# Convenience alias for the most commonly used class in my projects
from scrapling.core.fetchers import Fetcher, AsyncFetcher, StealthyFetcher, PlayWrightFetcher
from scrapling.core.page import Adaptor, Adaptors
from scrapling.core.custom_types import TextHandlers, AttributesHandler
from typing import Union, Type

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

# Type alias: useful for type hints when a function can accept any fetcher type.
# e.g., def scrape(url: str, fetcher: FetcherType = DefaultFetcher) -> Page: ...
# Fixed: use Union + Type so this works on Python 3.9 (the | syntax requires 3.10+)
FetcherType = Union[Type[Fetcher], Type[AsyncFetcher], Type[StealthyFetcher], Type[PlayWrightFetcher]]

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
    "FetcherType",
    # Version info
    "__version__",
    "__version_info__",
]
