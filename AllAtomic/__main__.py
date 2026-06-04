import asyncio

from pyrogram import idle

from AllAtomic import __version__
from AllAtomic.core import (
    Config,
    ForcesubSetup,
    GachaBotsSetup,
    TemplateSetup,
    UserSetup,
    db,
    AllAtomic,
)
from AllAtomic.core.logger import LOGS
from AllAtomic.functions.tools import initialize_git
from AllAtomic.functions.utility import BList, Flood, TGraph


async def main():
    """Main startup function for AllAtomic userbot"""
    LOGS.info(f"Starting AllAtomic v{__version__}...")
    
    # Initialize the bot
    await AllAtomic.start_bot()
    await AllAtomic.start_user()
    
    # Initialize database
    await db.connect()
    
    # Run database setups
    await UserSetup()
    await ForcesubSetup()
    await GachaBotsSetup()
    await TemplateSetup()
    
    # Update dynamic lists
    await Flood.updateFromDB()
    await BList.updateBlacklists()
    await TGraph.setup()
    
    # Initialize git plugins
    await initialize_git(Config.PLUGINS_REPO)
    
    # Send startup message to logger
    await AllAtomic.start_message(__version__)
    
    LOGS.info("AllAtomic is running...")
    
    # Keep the bot running
    await idle()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        LOGS.info("AllAtomic stopped by user")
    except Exception as e:
        LOGS.error(f"Fatal error: {e}")
