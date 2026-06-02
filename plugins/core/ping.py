"""
⚛️  Ping Command for AllAtomic Userbot
Shows response time with purple anime style
"""

import asyncio
import time
from telethon import events

from plugins import atomic_command
from app.utils import get_kaomoji, progress_bar, THEME

# Plugin metadata
__plugin__ = {
    "name": "Ping",
    "description": "Check bot response time",
    "category": "core"
}

PING_TEXTS = [
    "⚛️  Pong!",
    "💜 Pong!",
    "🌸 Pong!",
    "⚡ Pong!",
]

@atomic_command(
    "ping",
    pattern=r"\.ping",
    help="Check bot response time",
    usage=".ping",
    category="core"
)
async def ping_handler(event):
    """Ping command handler"""
    start = time.time()
    
    # Initial message
    msg = await event.edit(f"⚛️  {get_kaomoji('thinking')}")
    
    # Calculate ping
    end = time.time()
    ping_ms = int((end - start) * 1000)
    
    # Get Telegram latency
    tg_start = time.time()
    await event.client.get_me()
    tg_end = time.time()
    tg_ms = int((tg_end - tg_start) * 1000)
    
    # Create response
    pong_text = random.choice(PING_TEXTS)
    
    ping_msg = f"""
{pong_text} {get_kaomoji('happy')}

━━━━━━━━━━━━━━━━━━━━━━

⚡ **Bot Ping:** `{ping_ms}ms`
📡 **Telegram:** `{tg_ms}ms`

{'━' * 22}

{progress_bar(min(ping_ms, 500), 500, width=20)}

💜 AllAtomic v1.0
    """
    
    await msg.edit(ping_msg, parse_mode="md")
    
    # Auto-delete after 30 seconds
    await asyncio.sleep(30)
    await msg.delete()

@atomic_command(
    "speed",
    pattern=r"\.speed",
    help="Quick speed test",
    usage=".speed",
    category="core"
)
async def speed_handler(event):
    """Quick speed check"""
    msg = await event.edit("⚛️  Testing speed...")
    
    import speedtest
    
    try:
        st = speedtest.Speedtest()
        
        await msg.edit("⚛️  Testing download...")
        download = st.download() / 1_000_000  # Mbps
        
        await msg.edit("⚛️  Testing upload...")
        upload = st.upload() / 1_000_000  # Mbps
        
        await msg.edit("⚛️  Getting ping...")
        ping = st.results.ping
        
        speed_msg = f"""
⚡ **Speed Test Results** {get_kaomoji('excited')}

━━━━━━━━━━━━━━━━━━━━━━

📥 **Download:** `{download:.2f} Mbps`
📤 **Upload:** `{upload:.2f} Mbps`
📡 **Ping:** `{ping:.0f} ms`

{'━' * 22}

💜 Tested with AllAtomic
        """
        
        await msg.edit(speed_msg, parse_mode="md")
        
    except Exception as e:
        await msg.edit(f"❌ Speed test failed: {e}")
    
    await asyncio.sleep(60)
    await msg.delete()

# Commands registry
commands = {
    "ping": {
        "help": "Check bot response time",
        "usage": ".ping",
        "category": "core"
    },
    "speed": {
        "help": "Internet speed test",
        "usage": ".speed",
        "category": "core"
    }
}
