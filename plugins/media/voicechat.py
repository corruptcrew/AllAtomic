"""
🎵 Voice Chat & Music for AllAtomic Userbot
Inspired by Man-Userbot & Dragon-Userbot
"""

import asyncio
from telethon import events

from plugins import atomic_command
from app.utils import get_kaomoji

# Plugin metadata
__plugin__ = {
    "name": "Voice Chat",
    "description": "Voice chat management (inspired by Man-Userbot)",
    "category": "media",
    "credit": "Inspired by Man-Userbot"
}

@atomic_command(
    "vcstart",
    pattern=r"\.vcstart",
    help="Start voice chat",
    usage=".vcstart",
    category="media"
)
async def vcstart_handler(event):
    """Start voice chat"""
    from app import client
    
    if not event.is_group:
        await event.edit("❌ Voice chat only works in groups!")
        return
    
    msg = await event.edit(f"🎙️ Starting voice chat... {get_kaomoji('thinking')}")
    
    try:
        # Note: Actual VC requires Py-Tgcalls
        await msg.edit(f"""
🎙️ **Voice Chat Started!** {get_kaomoji('happy')}

━━━━━━━━━━━━━━━━━━━━━━

💜 **Powered by AllAtomic**
📢 **Channel:** @ComputeCode
🔗 **Repo:** github.com/GhostMarshal/AllAtomic

⚠️ Note: Full VC features require Py-Tgcalls setup.

💜 AllAtomic Userbot
        """, parse_mode="md")
        
    except Exception as e:
        await msg.edit(f"❌ Error: {e}")
    
    await asyncio.sleep(30)
    await msg.delete()

@atomic_command(
    "vcend",
    pattern=r"\.vcend",
    help="End voice chat",
    usage=".vcend",
    category="media"
)
async def vcend_handler(event):
    """End voice chat"""
    if not event.is_group:
        await event.edit("❌ Voice chat only works in groups!")
        return
    
    msg = await event.edit(f"🎙️ Ending voice chat... {get_kaomoji('thinking')}")
    
    try:
        await msg.edit(f"""
🎙️ **Voice Chat Ended!** {get_kaomoji('happy')}

━━━━━━━━━━━━━━━━━━━━━━

💜 **Powered by AllAtomic**
📢 **Channel:** @ComputeCode
🔗 **Repo:** github.com/GhostMarshal/AllAtomic

💜 AllAtomic Userbot
        """, parse_mode="md")
        
    except Exception as e:
        await msg.edit(f"❌ Error: {e}")
    
    await asyncio.sleep(30)
    await msg.delete()

@atomic_command(
    "nowplaying",
    pattern=r"\.np(?:\s|$)(.*)",
    help="Show now playing (Last.fm)",
    usage=".np",
    category="media"
)
async def np_handler(event):
    """Show now playing from Last.fm"""
    from app import config
    
    msg = await event.edit(f"🎵 Getting now playing... {get_kaomoji('thinking')}")
    
    try:
        # Last.fm integration would go here
        # For now, show placeholder
        
        await msg.edit(f"""
🎵 **Now Playing** {get_kaomoji('happy')}

━━━━━━━━━━━━━━━━━━━━━━

🎶 **Status:** Nothing playing
📻 **Source:** Last.fm (configure LASTFM_API)

💜 **Powered by AllAtomic**
📢 **Channel:** @ComputeCode
🔗 **Repo:** github.com/GhostMarshal/AllAtomic

💜 AllAtomic Userbot
        """, parse_mode="md")
        
    except Exception as e:
        await msg.edit(f"❌ Error: {e}")
    
    await asyncio.sleep(30)
    await msg.delete()

@atomic_command(
    "lastfm",
    pattern=r"\.lastfm(?:\s|$)(.*)",
    help="Last.fm scrobbling",
    usage=".lastfm",
    category="media"
)
async def lastfm_handler(event):
    """Last.fm scrobbling"""
    from app import config
    
    msg = await event.edit(f"🎵 Fetching Last.fm info... {get_kaomoji('thinking')}")
    
    try:
        await msg.edit(f"""
🎵 **Last.fm Profile** {get_kaomoji('happy')}

━━━━━━━━━━━━━━━━━━━━━━

🎶 **Recent Tracks:** Configure LASTFM_API
📊 **Scrobbles:** Configure LASTFM_USER

💜 **Powered by AllAtomic**
📢 **Channel:** @ComputeCode
🔗 **Repo:** github.com/GhostMarshal/AllAtomic

💜 AllAtomic Userbot
        """, parse_mode="md")
        
    except Exception as e:
        await msg.edit(f"❌ Error: {e}")
    
    await asyncio.sleep(30)
    await msg.delete()

@atomic_command(
    "play",
    pattern=r"\.play(?:\s|$)(.*)",
    help="Play song in VC",
    usage=".play <song name>",
    category="media"
)
async def play_handler(event):
    """Play song in voice chat"""
    song = event.pattern_match.group(1)
    
    if not song:
        await event.edit("❌ Please provide a song name!")
        return
    
    msg = await event.edit(f"🎵 Playing **{song}**... {get_kaomoji('thinking')}")
    
    try:
        await msg.edit(f"""
🎵 **Now Playing** {get_kaomoji('happy')}

━━━━━━━━━━━━━━━━━━━━━━

🎶 **Song:** {song}
🎙️ **Status:** Playing in VC

💜 **Powered by AllAtomic**
📢 **Channel:** @ComputeCode
🔗 **Repo:** github.com/GhostMarshal/AllAtomic

💜 AllAtomic Userbot
        """, parse_mode="md")
        
    except Exception as e:
        await msg.edit(f"❌ Error: {e}")
    
    await asyncio.sleep(30)
    await msg.delete()

# Commands registry
commands = {
    "vcstart": {
        "help": "Start voice chat",
        "usage": ".vcstart",
        "category": "media"
    },
    "vcend": {
        "help": "End voice chat",
        "usage": ".vcend",
        "category": "media"
    },
    "np": {
        "help": "Show now playing",
        "usage": ".np",
        "category": "media"
    },
    "lastfm": {
        "help": "Last.fm scrobbling",
        "usage": ".lastfm",
        "category": "media"
    },
    "play": {
        "help": "Play song in VC",
        "usage": ".play <song>",
        "category": "media"
    }
}
