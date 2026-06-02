"""
⚛️  Alive Command for AllAtomic Userbot
Shows bot status with purple anime theme
"""

import asyncio
from datetime import datetime

from plugins import atomic_command
from app.utils import get_kaomoji, get_readable_time, THEME

# Plugin metadata
__plugin__ = {
    "name": "Alive",
    "description": "Check if bot is online with style",
    "category": "core"
}

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
        alive_msg = f"""
╔═══════════════════════════════════════════╗
║     ⚛️  **AllAtomic is Online!**  ⚛️          ║
╠═══════════════════════════════════════════════╣
║                                               ║
║  💜 **Version:** `1.0.0`                  ║
║  🌸 **Uptime:** `{uptime}`                    ║
║  ⚡ **Python:** `3.12`                        ║
║  📱 **Telethon:** `1.34.0`                    ║
║                                               ║
║  👤 **User:** `{user_name}`                   ║
║  🆔 **ID:** `{user_id}`                       ║
║                                               ║
║  💻 **Dev:** @GhostMarshal                    ║
║  📢 **Channel:** @ComputeCode                 ║
║                                               ║
║  {get_kaomoji('happy')}                                    ║
╚═══════════════════════════════════════════════╝
"""
        
        # Respond to the command
        await event.respond(alive_msg, parse_mode="md")
        
        # Delete command message after 5 seconds
        await asyncio.sleep(5)
        await event.delete()
        
    except Exception as e:
        await event.respond(f"❌ Error: {e}")
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
{get_kaomoji('cool')}
    """
    
    await event.respond(status, parse_mode="md")
    await asyncio.sleep(5)
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
