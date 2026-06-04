"""
AllAtomic - Startup Initialization
Dev: @GhostMarshal | Channel: @ComputeCode
(૨๑•̀ㅁ•́ฅา) Purple Anime Theme (#9A8CFF)
"""

import time
import asyncio
import os
from pathlib import Path
from .config import config, log
from .clients import clients
from .database import db

# Track start time for uptime calculation
_start_time = None


def get_uptime() -> str:
    """Get formatted uptime string (✿◠‿◠)"""
    global _start_time
    if not _start_time:
        _start_time = time.time()
        return "0s"
    
    uptime = time.time() - _start_time
    
    if uptime < 60:
        return f"{uptime:.0f}s"
    elif uptime < 3600:
        return f"{uptime/60:.0f}m"
    elif uptime < 86400:
        return f"{uptime/3600:.0f}h"
    else:
        return f"{uptime/86400:.0f}d"


async def initialize():
    """Initialize AllAtomic userbot (✿◠‿◠)"""
    
    # Validate configuration
    if not config.validate():
        log.error("Invalid configuration! Please check your .env file")
        return False
    
    log.info("Initializing AllAtomic...")
    
    # Connect to database
    try:
        await db.connect()
        log.info("Database connected")
    except Exception as e:
        log.error(f"Database connection failed: {e}")
        # Continue without database
    
    # Start clients
    try:
        await clients.start_all()
        log.info("Clients started successfully")
    except Exception as e:
        log.error(f"Failed to start clients: {e}")
        return False
    
    # Load plugins
    try:
        await load_plugins()
        log.info("Plugins loaded successfully")
    except Exception as e:
        log.error(f"Failed to load plugins: {e}")
    
    # Log startup message
    log_startup_message()
    
    return True


def log_startup_message():
    """Print startup message with theme"""
    msg = f"""
━━━━━━━━━━━━━━━━━━━━
  AllAtomic v{config.VERSION}
  Dev: @GhostMarshal
  Channel: @ComputeCode
  GitHub: {config.GIT_REPO}
━━━━━━━━━━━━━━━━━━━━
(૨๑•̀ㅁ•́ฅा) Ready to serve!
"""
    log.info(msg)


async def load_plugins():
    """Auto-discover and load plugins"""
    from pyrogram import filters
    from .clients import clients
    
    userbot = clients.user or clients.bot
    
    if not userbot:
        return
    
    # Load user plugins
    plugins_path = Path(__file__).parent.parent / "plugins" / "user"
    if plugins_path.exists():
        for plugin_file in plugins_path.glob("*.py"):
            if plugin_file.name.startswith("_"):
                continue
            
            try:
                module_name = f"AllAtomic.plugins.user.{plugin_file.stem}"
                __import__(module_name)
                log.debug(f"Loaded plugin: {plugin_file.stem}")
            except Exception as e:
                log.error(f"Failed to load plugin {plugin_file.stem}: {e}")
    
    # Load bot plugins
    bot_plugins_path = Path(__file__).parent.parent / "plugins" / "bot"
    if bot_plugins_path.exists():
        for plugin_file in bot_plugins_path.glob("*.py"):
            if plugin_file.name.startswith("_"):
                continue
            
            try:
                module_name = f"AllAtomic.plugins.bot.{plugin_file.stem}"
                __import__(module_name)
                log.debug(f"Loaded bot plugin: {plugin_file.stem}")
            except Exception as e:
                log.error(f"Failed to load bot plugin {plugin_file.stem}: {e}")


async def cleanup():
    """Cleanup on shutdown"""
    log.info("Cleaning up...")
    await db.disconnect()
    await clients.stop_all()
    log.info("Cleanup complete")
