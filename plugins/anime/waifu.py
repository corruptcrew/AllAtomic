"""
🌸 Waifu Plugin for AllAtomic Userbot
Random anime girl images (trending feature!)
"""

import asyncio
import aiohttp
from telethon import events

from plugins import atomic_command
from app.utils import get_kaomoji

# Plugin metadata
__plugin__ = {
    "name": "Waifu",
    "description": "Random anime waifu images",
    "category": "anime"
}

# API endpoints for waifu pics
WAIFU_APIS = [
    "https://api.waifu.pics/sfw/waifu",
    "https://api.waifu.im/search",
]

@atomic_command(
    "waifu",
    pattern=r"\.waifu",
    help="Get random waifu image",
    usage=".waifu",
    category="anime"
)
async def waifu_handler(event):
    """Get random waifu image"""
    msg = await event.edit(f"🌸 Searching for waifu... {get_kaomoji('thinking')}")
    
    try:
        async with aiohttp.ClientSession() as session:
            # Try first API
            async with session.get(WAIFU_APIS[0]) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    url = data.get("url")
                    
                    if url:
                        await msg.delete()
                        await event.client.send_file(
                            event.chat_id,
                            url,
                            caption=f"🌸 Here's your waifu! {get_kaomoji('love')}\n\n💜 AllAtomic Userbot"
                        )
                        return
            
            # Try second API
            async with session.get(WAIFU_APIS[1]) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    images = data.get("images", [])
                    if images:
                        url = images[0].get("url")
                        await msg.delete()
                        await event.client.send_file(
                            event.chat_id,
                            url,
                            caption=f"🌸 Waifu! {get_kaomoji('happy')}\n\n💜 AllAtomic"
                        )
                        return
        
        await msg.edit(f"❌ Couldn't fetch waifu {get_kaomoji('sad')}")
        
    except Exception as e:
        await msg.edit(f"❌ Error: {e}")
    
    await asyncio.sleep(30)
    await msg.delete()

@atomic_command(
    "neko",
    pattern=r"\.neko",
    help="Get random neko image",
    usage=".neko",
    category="anime"
)
async def neko_handler(event):
    """Get random neko image"""
    msg = await event.edit(f"🐱 Finding neko... {get_kaomoji('excited')}")
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.waifu.pics/sfw/neko") as resp:
                if resp.status == 200:
                    data = await resp.json()
                    url = data.get("url")
                    
                    if url:
                        await msg.delete()
                        await event.client.send_file(
                            event.chat_id,
                            url,
                            caption=f"🐱 Nya~! {get_kaomoji('happy')}\n\n💜 AllAtomic"
                        )
                        return
        
        await msg.edit(f"❌ Couldn't fetch neko {get_kaomoji('sad')}")
        
    except Exception as e:
        await msg.edit(f"❌ Error: {e}")
    
    await asyncio.sleep(30)
    await msg.delete()

@atomic_command(
    "waifupic",
    pattern=r"\.waifupic",
    help="Another waifu command",
    usage=".waifupic",
    category="anime"
)
async def waifupic_handler(event):
    """Alternative waifu command"""
    await waifu_handler(event)

# Commands registry
commands = {
    "waifu": {
        "help": "Get random waifu image",
        "usage": ".waifu",
        "category": "anime"
    },
    "neko": {
        "help": "Get random neko image",
        "usage": ".neko",
        "category": "anime"
    },
    "waifupic": {
        "help": "Get waifu picture",
        "usage": ".waifupic",
        "category": "anime"
    }
}
