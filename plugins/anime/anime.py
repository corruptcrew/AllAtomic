"""
🌸 Anime Info Plugin for AllAtomic Userbot
Anime and manga search using Jikan API
"""

import asyncio
import aiohttp
from telethon import events

from plugins import atomic_command
from app.utils import get_kaomoji, truncate_text

# Plugin metadata
__plugin__ = {
    "name": "Anime Search",
    "description": "Search anime and manga info",
    "category": "anime"
}

@atomic_command(
    "anime",
    pattern=r"\.anime(?:\s|$)(.*)",
    help="Search anime info",
    usage=".anime <name>",
    category="anime"
)
async def anime_handler(event):
    """Search anime information"""
    query = event.pattern_match.group(1)
    
    if not query:
        await event.edit("❌ Please provide anime name!\n\nUsage: `.anime <name>`")
        return
    
    msg = await event.edit(f"🌸 Searching for **{query}**... {get_kaomoji('thinking')}")
    
    try:
        async with aiohttp.ClientSession() as session:
            # Search anime
            async with session.get(f"https://api.jikan.moe/v4/anime?q={query}&limit=1") as resp:
                if resp.status == 200:
                    data = await resp.json()
                    
                    if data.get("data"):
                        anime = data["data"][0]
                        
                        # Build info message
                        title = anime.get("title_english") or anime.get("title")
                        score = anime.get("score", "N/A")
                        episodes = anime.get("episodes") or "Unknown"
                        status = anime.get("status", "Unknown")
                        genres = ", ".join([g["name"] for g in anime.get("genres", [])[:5]])
                        synopsis = truncate_text(anime.get("synopsis", "No synopsis"), 500)
                        image = anime.get("images", {}).get("jpg", {}).get("large_image_url")
                        
                        anime_msg = f"""
🌸 **{title}** {get_kaomoji('happy')}

━━━━━━━━━━━━━━━━━━━━━━

⭐ **Score:** `{score}/10`
📺 **Episodes:** `{episodes}`
📊 **Status:** `{status}`
🎭 **Genres:** {genres}

📝 **Synopsis:**
_{synopsis}_

━━━━━━━━━━━━━━━━━━━━━━

💜 AllAtomic Userbot
                        """
                        
                        await msg.delete()
                        
                        if image:
                            await event.client.send_file(
                                event.chat_id,
                                image,
                                caption=anime_msg,
                                parse_mode="md"
                            )
                        else:
                            await msg.edit(anime_msg, parse_mode="md")
                        return
        
        await msg.edit(f"❌ Anime not found {get_kaomoji('sad')}")
        
    except Exception as e:
        await msg.edit(f"❌ Error: {e}")
    
    await asyncio.sleep(60)
    await msg.delete()

@atomic_command(
    "manga",
    pattern=r"\.manga(?:\s|$)(.*)",
    help="Search manga info",
    usage=".manga <name>",
    category="anime"
)
async def manga_handler(event):
    """Search manga information"""
    query = event.pattern_match.group(1)
    
    if not query:
        await event.edit("❌ Please provide manga name!\n\nUsage: `.manga <name>`")
        return
    
    msg = await event.edit(f"📚 Searching for **{query}**... {get_kaomoji('thinking')}")
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://api.jikan.moe/v4/manga?q={query}&limit=1") as resp:
                if resp.status == 200:
                    data = await resp.json()
                    
                    if data.get("data"):
                        manga = data["data"][0]
                        
                        title = manga.get("title_english") or manga.get("title")
                        score = manga.get("score", "N/A")
                        chapters = manga.get("chapters") or "Unknown"
                        volumes = manga.get("volumes") or "Unknown"
                        status = manga.get("status", "Unknown")
                        genres = ", ".join([g["name"] for g in manga.get("genres", [])[:5]])
                        synopsis = truncate_text(manga.get("synopsis", "No synopsis"), 500)
                        image = manga.get("images", {}).get("jpg", {}).get("large_image_url")
                        
                        manga_msg = f"""
📚 **{title}** {get_kaomoji('happy')}

━━━━━━━━━━━━━━━━━━━━━━

⭐ **Score:** `{score}/10`
📖 **Chapters:** `{chapters}`
📕 **Volumes:** `{volumes}`
📊 **Status:** `{status}`
🎭 **Genres:** {genres}

📝 **Synopsis:**
_{synopsis}_

━━━━━━━━━━━━━━━━━━━━━━

💜 AllAtomic Userbot
                        """
                        
                        await msg.delete()
                        
                        if image:
                            await event.client.send_file(
                                event.chat_id,
                                image,
                                caption=manga_msg,
                                parse_mode="md"
                            )
                        else:
                            await msg.edit(manga_msg, parse_mode="md")
                        return
        
        await msg.edit(f"❌ Manga not found {get_kaomoji('sad')}")
        
    except Exception as e:
        await msg.edit(f"❌ Error: {e}")
    
    await asyncio.sleep(60)
    await msg.delete()

# Commands registry
commands = {
    "anime": {
        "help": "Search anime information",
        "usage": ".anime <name>",
        "category": "anime"
    },
    "manga": {
        "help": "Search manga information",
        "usage": ".manga <name>",
        "category": "anime"
    }
}
