"""
╔═══════════════════════════════════════════════════════╗
║           ⚛️  AllAtomic Userbot - Main Entry          ║
║                                                       ║
║  Dev: @GhostMarshal                                   ║
║  Channel: @ComputeCode                                ║
║  Theme: Purple Anime 💜                               ║
╚═══════════════════════════════════════════════════════╝
"""

import sys
import asyncio
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from app.logger import logger, log_startup, log_shutdown
from app.config import Config
from app.database import Database
from app.client import AtomicClient
from app.utils import get_kaomoji
from plugins import load_all_plugins

# ───────────────────────────────────────────────────────
# Global Variables
# ───────────────────────────────────────────────────────

config = None
db = None
client = None

# ───────────────────────────────────────────────────────
# Main Function
# ───────────────────────────────────────────────────────

async def main():
    """Main entry point"""
    global config, db, client
    
    try:
        # Log startup
        log_startup()
        
        # Initialize config
        logger.info("📋 Loading configuration...")
        config = Config()
        
        if not config.is_valid():
            logger.error("❌ Invalid configuration! Check .env file")
            sys.exit(1)
        
        logger.info("✓ Configuration loaded")
        
        # Initialize database
        logger.info("🗄️  Connecting to database...")
        db = Database(config.DATABASE_URL)
        logger.info("✓ Database connected")
        
        # Initialize client
        logger.info("🔌 Initializing Telethon client...")
        client = AtomicClient(config)
        await client.start()
        logger.info("✓ Client started")
        
        # Load plugins
        logger.info("🔌 Loading plugins...")
        loaded_count = load_all_plugins(client, config)
        logger.info(f"✓ Loaded {loaded_count} plugins")
        
        # Bot info
        logger.info("╔═══════════════════════════════════════════════════╗")
        logger.info(f"║  ⚛️  AllAtomic is Online! {get_kaomoji('happy')}                    ║")
        logger.info(f"║                                                   ║")
        logger.info(f"║  Logged in as: {client.full_name}")
        logger.info(f"║  User ID: {client.user_id}")
        logger.info(f"║  Theme: Purple Anime 💜")
        logger.info(f"║  Dev: @GhostMarshal")
        logger.info(f"║  Channel: @ComputeCode")
        logger.info(f"╚═══════════════════════════════════════════════════╝")
        
        # Run until disconnected
        logger.info("🚀 AllAtomic is ready! Press Ctrl+C to stop.")
        await client.run_until_disconnected()
        
    except KeyboardInterrupt:
        logger.info("\n⚛️  Received interrupt signal")
    except Exception as e:
        logger.exception(f"❌ Fatal error: {e}")
        sys.exit(1)
    finally:
        # Cleanup
        if client:
            await client.stop()
        log_shutdown()

# ───────────────────────────────────────────────────────
# Run
# ───────────────────────────────────────────────────────

if __name__ == "__main__":
    logger.info("⚛️  Starting AllAtomic Userbot v1.0...")
    asyncio.run(main())
