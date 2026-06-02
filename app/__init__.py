"""
╔═══════════════════════════════════════════════════════╗
║           ⚛️  AllAtomic Userbot Core                  ║
║                                                       ║
║  A turbocharged Telegram userbot with purple anime    ║
║  aesthetic. Built for @ComputeCode community.         ║
║                                                       ║
║  Dev: @GhostMarshal                                   ║
║  Theme: Purple Anime 💜🌸                             ║
╚═══════════════════════════════════════════════════════╝
"""

import os
import sys
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(
    format="[%(levelname)s] - %(name)s - %(message)s",
    level=logging.INFO,
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler("allatomic.log")
    ]
)

logger = logging.getLogger("AllAtomic")

# Paths
ROOT_DIR = Path(__file__).parent.parent
PLUGIN_DIR = ROOT_DIR / "plugins"
ASSETS_DIR = ROOT_DIR / "assets"

# Version
__version__ = "1.0.0"
__author__ = "@GhostMarshal"
__channel__ = "@ComputeCode"

# Import core components
from .config import Config
from .database import Database
from .client import AtomicClient

# Global instances
config = None
db = None
client = None

def initialize():
    """Initialize the bot"""
    global config, db, client
    
    logger.info("⚛️  Initializing AllAtomic Userbot...")
    
    # Load config
    config = Config()
    logger.info("✓ Configuration loaded")
    
    # Initialize database
    db = Database(config.DATABASE_URL)
    logger.info("✓ Database connected")
    
    # Initialize client
    client = AtomicClient(config)
    logger.info("✓ Telethon client initialized")
    
    logger.info(f"💜 AllAtomic v{__version__} ready!")
    
    return config, db, client

def get_bot_info():
    """Get bot information"""
    return {
        "name": "AllAtomic",
        "version": __version__,
        "dev": __author__,
        "channel": __channel__,
        "theme": "Purple Anime"
    }

# Exports
__all__ = [
    "Config",
    "Database", 
    "AtomicClient",
    "initialize",
    "get_bot_info",
    "logger",
    "PLUGIN_DIR",
    "ASSETS_DIR",
    "__version__"
]
