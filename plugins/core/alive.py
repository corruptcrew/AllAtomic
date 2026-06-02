"""
⚛️  Alive Command for AllAtomic Userbot
Shows bot status with purple anime theme
"""

import asyncio
import random
from datetime import datetime
from telethon import events

from plugins import atomic_command
from app.utils import get_kaomoji, get_readable_time, THEME

# Plugin metadata
__plugin__ = {
    "name": "Alive",
    "description": "Check if bot is online with style",
    "category": "core"
}

# Alive configuration
ALIVE_GIFS = [
    "https://i.imgur.com/PLACEHOLDER1.gif",  # Replace with actual purple anime GIFs
    "https://i.imgur.com/PLACEHOLDER2.gif",
    "https://i.imgur.com/PLACEHOLDER3.gif",
]

ALIVE_TEXT = """
╔═══════════════════════════════════════════════╗
║     ⚛️  **AllAtomic is Online!**  ⚛️          ║
╠═══════════════════════════════════════════════╣
║                                               ║
║  💜 **Version:** `{version}`                  ║
║  🌸 **Uptime:** `{uptime}`                    ║
║  ⚡ **Python:** `3.11`                        ║
║  📱 **Telethon:** `1.34.0`                    ║
║                                               ║
║  👤 **User:** `{user_name}`                   ║
║  🆔 **ID:** `{user_id}`                       ║
║                                               ║
║  💻 **Dev:** @GhostMarshal                    ║
║  📢 **Channel:** @ComputeCode                 ║
║                                               ║
║  {kaomoji}                                    ║
╚═══════════════════════════════════════════════╝
"""

# Start time for uptime calculation
START_TIME = datetime.now()

@atomic_command(
    "alive",
    pattern=r"\.alive",
    help="Check if bot is online",
    usage=".alive",
    category="core"
)
async def alive_handler(event):
    """Alive command handler"""
    from app import config, client, db
    
    try:
        # Calculate uptime
        uptime = get_readable_time((datetime.now() - START_TIME).total_seconds())
        
        # Get user info
        user_name = client.full_name
        user_id = client.user_id
        
        # Format message
        alive_msg = ALIVE_TEXT.format(
            version="1.0.0",
            uptime=uptime,
            user_name=user_name,
            user_id=user_id,
            kaomoji=get_kaomoji("happy")
        )
        
        # Send with image if available
        if config.ALIVE_PIC:
            await event.client.send_file(
                event.chat_id,
                config.ALIVE_PIC,
                caption=alive_msg,
                parse_mode="md"
            )
        else:
            await event.edit(alive_msg, parse_mode="md")
        
        await asyncio.sleep(30)
        await event.delete()
        
    except Exception as e:
        await event.edit(f"❌ Error: {e}")
        await asyncio.sleep(5)
        await event.delete()

@atomic_command(
    "status",
    pattern=r"\.status",
    help="Quick bot status",
    usage=".status",
    category="core"
)
async def status_handler(event):
    """Quick status command"""
    from app import client
    
    uptime = get_readable_time((datetime.now() - START_TIME).total_seconds())
    
    status = f"""
⚛️ **AllAtomic Status**
━━━━━━━━━━━━━━━━━━━━━━
💜 Online: `{uptime}`
🌸 Version: `1.0.0`
{get_kaomoji("cool")}
    """
    
    await event.edit(status, parse_mode="md")
    await asyncio.sleep(30)
    await event.delete()

# Commands registry
commands = {
    "alive": {
        "help": "Check if bot is online with purple theme",
        "usage": ".alive",
        "category": "core"
    },
    "status": {
        "help": "Quick bot status",
        "usage": ".status",
        "category": "core"
    }
}
