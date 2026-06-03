"""
AllAtomic - Configuration Management
Dev: @GhostMarshal | Channel: @ComputeCode
(૨๑•̀ㅁ•́ฅა) Purple Anime Theme (#9A8CFF)
"""

import os
from typing import Optional
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Configuration manager for AllAtomic userbot (✿◠‿◠)"""
    
    # Bot Configuration
    API_ID = int(os.getenv("API_ID", "0"))
    API_HASH = os.getenv("API_HASH", "")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "")
    STRING_SESSION = os.getenv("STRING_SESSION", "")
    
    # Database
    MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
    DB_NAME = os.getenv("DB_NAME", "AllAtomic")
    
    # Owners & Auth
    OWNER_ID = int(os.getenv("OWNER_ID", "0"))
    SUDO_USERS = list(map(int, os.getenv("SUDO_USERS", "0").split()))
    
    # Settings
    PM_PERMIT = os.getenv("PM_PERMIT", "True").lower() == "true"
    GCAST_BLACKLIST = list(map(int, os.getenv("GCAST_BLACKLIST", "").split()))
    MAX_MESSAGE_LENGTH = int(os.getenv("MAX_MESSAGE_LENGTH", "4096"))
    
    # URLs
    GIT_REPO = "https://github.com/corruptcrew/AllAtomic"
    SUPPORT_CHAT = "@ComputeCode"
    UPDATE_CHANNEL = "@ComputeCode"
    
    # Theme
    THEME_COLOR = "#9A8CFF"
    
    # Version
    VERSION = "2.0.0"
    
    @classmethod
    def validate(cls) -> bool:
        """Validate required configuration (◕‿◕)"""
        required = ["API_ID", "API_HASH"]
        for item in required:
            if not getattr(cls, item):
                return False
        return True
    
    @classmethod
    def is_heroku(cls) -> bool:
        """Check if running on Heroku"""
        return os.getenv("HEROKU_APP_NAME") is not None


class Symbols:
    """Kaomoji and symbols for AllAtomic (૨๑•̀ㅁ•́ฅა)"""
    
    # Kaomoji
    HAPPY = "(✿◠‿◠)"
    CUTE = "(૨๑•̀ㅁ•́ฅა)"
    WINK = "(◕‿◕)"
    LOVE = "(♡⌂♡)"
    STAR = "(★^O^★)"
    WAVE = "(^_^)/"
    HEART = "♥"
    SPARKLE = "✨"
    FIRE = "🔥"
    THUNDER = "⚡"
    
    # Decorations
    LINE = "━━━━━━━━━━━━━━━━━━━━"
    DASH = "▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬"
    ARROW = "➤"
    CHECK = "✓"
    CROSS = "✗"
    WARN = "⚠"


# Export config instance
config = Config()
symbols = Symbols()
