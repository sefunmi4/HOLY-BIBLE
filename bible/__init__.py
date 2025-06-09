"""Bible package configuration and shared utilities."""

from __future__ import annotations

import logging
import os


def _configure_logging() -> None:
    """Configure basic logging for the package.

    The log level can be controlled with the ``BIBLE_LOG_LEVEL`` environment
    variable. By default ``INFO`` messages and above are shown.
    """

    level_name = os.getenv("BIBLE_LOG_LEVEL", "INFO").upper()
    level = getattr(logging, level_name, logging.INFO)
    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )


_configure_logging()
