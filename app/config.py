"""
Configuration Loader for AllAtomic Userbot
Loads environment variables from .env file
"""

import os
from pathlib import Path
from dotenv import load_dotenv

class Config:
    """Configuration manager for AllAtomic"""
    
    def __init__(self):
        # Load .env file
        env_path = Path(__file__).parent.parent / ".env"
        load_dotenv(env_path)
        
        # ─────────────────────────────────────────────
        # 🔐 MANDATORY
        # ─────────────────────────────────────────────
        self.APP_ID = int(os.getenv("APP_ID", 0))
        self.API_HASH = os.getenv("API_HASH", "")
        self.SESSION_STRING = os.getenv("SESSION_STRING", "")
        self.DATABASE_URL = os.getenv("DATABASE_URL", "")
        self.BOT_TOKEN = os.getenv("BOT_TOKEN", "")
        self.HANDLER = os.getenv("HANDLER", ".")
        
        # ─────────────────────────────────────────────
        # 👤 USER CONFIG
        # ─────────────────────────────────────────────
        self.OWNER_ID = int(os.getenv("OWNER_ID", 0))
        self.LOGGER_ID = int(os.getenv("LOGGER_ID", 0))
        self.SUPPORT_GROUP = os.getenv("SUPPORT_GROUP", "ComputeCode")
        self.UPDATE_CHANNEL = os.getenv("UPDATE_CHANNEL", "ComputeCode")
        
        # ─────────────────────────────────────────────
        # 🎨 CUSTOMIZATION
        # ─────────────────────────────────────────────
        self.ALIVE_MSG = os.getenv("ALIVE_MSG", "⚛️ AllAtomic is Online!")
        self.ALIVE_PIC = os.getenv("ALIVE_PIC", "")
        self.PMPERMIT_MSG = os.getenv("PMPERMIT_MSG", "⚠️ Please wait for my master to approve you.")
        self.MAX_SPAM = int(os.getenv("MAX_SPAM", 5))
        self.STICKER_PACKNAME = os.getenv("STICKER_PACKNAME", "AllAtomic")
        
        # ─────────────────────────────────────────────
        # 🔧 TOGGLES
        # ─────────────────────────────────────────────
        self.PM_PERMIT = os.getenv("PM_PERMIT", "True").lower() == "true"
        self.INSTANT_BLOCK = os.getenv("INSTANT_BLOCK", "False").lower() == "true"
        self.ABUSE_MODE = os.getenv("ABUSE_MODE", "False").lower() == "true"
        self.AI_ENABLED = os.getenv("AI_ENABLED", "False").lower() == "true"
        
        # ─────────────────────────────────────────────
        # 🔑 API KEYS
        # ─────────────────────────────────────────────
        self.WEATHER_API = os.getenv("WEATHER_API", "")
        self.REMOVE_BG_API = os.getenv("REMOVE_BG_API", "")
        self.OPENAI_API = os.getenv("OPENAI_API", "")
        self.CURRENCY_API = os.getenv("CURRENCY_API", "")
        self.OCR_API = os.getenv("OCR_API", "")
        self.LYRICS_API = os.getenv("LYRICS_API", "")
        
        # ─────────────────────────────────────────────
        # 🔄 UPDATES
        # ─────────────────────────────────────────────
        self.UPSTREAM_REPO = os.getenv("UPSTREAM_REPO", "https://github.com/GhostMarshal/AllAtomic")
        self.UPSTREAM_BRANCH = os.getenv("UPSTREAM_BRANCH", "main")
        
        # ─────────────────────────────────────────────
        # 🎨 THEME (Purple Anime)
        # ─────────────────────────────────────────────
        self.THEME_COLOR = "#9A8CFF"
        self.THEME_EMOJI = "💜"
        self.KAOMOJI = "૮๑•̀ㅁ•́ฅა"
        
        # Validate mandatory
        self._validate()
    
    def _validate(self):
        """Validate mandatory configuration"""
        required = {
            "APP_ID": self.APP_ID,
            "API_HASH": self.API_HASH,
            "SESSION_STRING": self.SESSION_STRING,
            "DATABASE_URL": self.DATABASE_URL
        }
        
        missing = [key for key, value in required.items() if not value]
        
        if missing:
            raise ValueError(f"❌ Missing required config: {', '.join(missing)}")
    
    def is_valid(self) -> bool:
        """Check if config is valid"""
        try:
            self._validate()
            return True
        except ValueError:
            return False
    
    def get_all(self) -> dict:
        """Get all config as dict"""
        return {
            "APP_ID": self.APP_ID,
            "API_HASH": self.API_HASH,
            "SESSION_STRING": self.SESSION_STRING,
            "DATABASE_URL": self.DATABASE_URL,
            "BOT_TOKEN": self.BOT_TOKEN,
            "HANDLER": self.HANDLER,
            "OWNER_ID": self.OWNER_ID,
            "LOGGER_ID": self.LOGGER_ID,
            "SUPPORT_GROUP": self.SUPPORT_GROUP,
            "UPDATE_CHANNEL": self.UPDATE_CHANNEL,
            "ALIVE_MSG": self.ALIVE_MSG,
            "ALIVE_PIC": self.ALIVE_PIC,
            "PMPERMIT_MSG": self.PMPERMIT_MSG,
            "MAX_SPAM": self.MAX_SPAM,
            "STICKER_PACKNAME": self.STICKER_PACKNAME,
            "PM_PERMIT": self.PM_PERMIT,
            "INSTANT_BLOCK": self.INSTANT_BLOCK,
            "ABUSE_MODE": self.ABUSE_MODE,
            "AI_ENABLED": self.AI_ENABLED,
            "THEME_COLOR": self.THEME_COLOR,
            "THEME_EMOJI": self.THEME_EMOJI,
            "KAOMOJI": self.KAOMOJI,
        }
    
    def __repr__(self):
        return f"<AllAtomic Config v1.0 - Purple Anime Theme>"
