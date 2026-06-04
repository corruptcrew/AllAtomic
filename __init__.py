"""
AllAtomic - Telegram Userbot
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Dev: @GhostMarshal | Channel: @ComputeCode
GitHub: corruptcrew/AllAtomic
Theme: Purple Anime (#9A8CFF)
(૨๑•̀ㅁ•́ฅา) (✿◠‿◠) (◕‿◕)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

__version__ = "2.0.0"
__author__ = "GhostMarshal"
__license__ = "GPL-3.0"

from .core.config import config, symbols
from .core.logger import log, setup_logger
from .core.database import db
from .core.clients import clients, get_client
from .core.initializer import initialize, cleanup

__all__ = [
    "__version__",
    "__author__",
    "__license__",
    "config",
    "symbols",
    "log",
    "setup_logger",
    "db",
    "clients",
    "get_client",
    "initialize",
    "cleanup",
]
