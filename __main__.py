"""
AllAtomic - Main Entry Point
Dev: @GhostMarshal | Channel: @ComputeCode
(૨๑•̀ㅁ•́ฅา) Purple Anime Theme (#9A8CFF)
"""

import asyncio
import signal
import sys
from pathlib import Path

# Add workspace to path
workspace_path = Path(__file__).parent.parent.parent
sys.path.insert(0, str(workspace_path))

from AllAtomic.core.config import config, log
from AllAtomic.core.initializer import initialize, cleanup
from AllAtomic.core.clients import clients


async def main():
    """Main entry point (✿◠‿◠)"""
    
    # Setup signal handlers
    loop = asyncio.get_event_loop()
    
    def signal_handler():
        log.info("Shutdown signal received...")
        asyncio.create_task(shutdown())
    
    for sig in (signal.SIGINT, signal.SIGTERM):
        loop.add_signal_handler(sig, signal_handler)
    
    try:
        # Initialize
        if not await initialize():
            log.error("Initialization failed!")
            sys.exit(1)
        
        # Keep running
        await asyncio.Event().wait()
        
    except KeyboardInterrupt:
        log.info("KeyboardInterrupt received")
    except Exception as e:
        log.error(f"Unhandled exception: {e}")
    finally:
        await shutdown()


async def shutdown():
    """Shutdown sequence"""
    log.info("Shutting down...")
    await cleanup()
    log.info("Goodbye! (◕‿◕)")
    sys.exit(0)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        log.info("Forcefully terminated")
