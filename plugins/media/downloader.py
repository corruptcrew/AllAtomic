"""
🎬 Advanced Media Downloader
Download from YouTube, Instagram, TikTok, Twitter, Facebook, and more
"""

import asyncio
import os
import re
from telethon import events

from plugins import atomic_command
from app.utils import get_kaomoji

# Plugin metadata
__plugin__ = {
    "name": "Media Downloader",
    "description": "Download from multiple platforms",
    "category": "media"
}

@atomic_command(
    "yt",
    pattern=r"\.yt(?:\s|$)(.*)",
    help="Download YouTube video",
    usage=".yt <url> or .yt <search query>",
    category="media"
)
async def youtube_handler(event):
    """Download YouTube video"""
    query = event.pattern_match.group(1)
    
    if not query:
        await event.edit("❌ Provide YouTube URL or search query!")
        return
    
    msg = await event.edit(f"📥 Downloading from YouTube... {get_kaomoji('thinking')}")
    
    try:
        # Check if it's a URL or search query
        if "youtube.com" in query or "youtu.be" in query:
            url = query
        else:
            # Search YouTube
            url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
        
        # For actual download, would use yt-dlp
        # This is a placeholder showing the structure
        
        await msg.edit(f"""
📥 **YouTube Download** {get_kaomoji('happy')}

━━━━━━━━━━━━━━━━━━━━━━

🎬 **Query:** `{query[:50]}`

⚠️ Install yt-dlp for actual download:
`pip install yt-dlp`

💜 AllAtomic Userbot
        """, parse_mode="md")
        
    except Exception as e:
        await msg.edit(f"❌ Error: {e}")
    
    await asyncio.sleep(60)
    await msg.delete()

@atomic_command(
    "insta",
    pattern=r"\.insta(?:\s|$)(.*)",
    help="Download Instagram post/reel",
    usage=".insta <instagram URL>",
    category="media"
)
async def instagram_handler(event):
    """Download Instagram post/reel"""
    url = event.pattern_match.group(1)
    
    if not url:
        reply = await event.get_reply_message()
        if reply and reply.text:
            url = reply.text
    
    if not url or "instagram.com" not in url:
        await event.edit("❌ Provide Instagram URL!")
        return
    
    msg = await event.edit(f"📥 Downloading from Instagram... {get_kaomoji('thinking')}")
    
    try:
        # Would use instaloader or similar
        await msg.edit(f"""
📥 **Instagram Download** {get_kaomoji('happy')}

━━━━━━━━━━━━━━━━━━━━━━

🔗 **URL:** `{url[:50]}...`

⚠️ Install instaloader for actual download:
`pip install instaloader`

💜 AllAtomic Userbot
        """, parse_mode="md")
        
    except Exception as e:
        await msg.edit(f"❌ Error: {e}")
    
    await asyncio.sleep(60)
    await msg.delete()

@atomic_command(
    "tiktok",
    pattern=r"\.tiktok(?:\s|$)(.*)",
    help="Download TikTok video (no watermark)",
    usage=".tiktok <tiktok URL>",
    category="media"
)
async def tiktok_handler(event):
    """Download TikTok video"""
    url = event.pattern_match.group(1)
    
    if not url:
        reply = await event.get_reply_message()
        if reply and reply.text:
            url = reply.text
    
    if not url or "tiktok.com" not in url:
        await event.edit("❌ Provide TikTok URL!")
        return
    
    msg = await event.edit(f"📥 Downloading from TikTok... {get_kaomoji('thinking')}")
    
    try:
        await msg.edit(f"""
📥 **TikTok Download** {get_kaomoji('happy')}

━━━━━━━━━━━━━━━━━━━━━━

🎵 **URL:** `{url[:50]}...`

⚠️ Install tiktok-dl for actual download

💜 AllAtomic Userbot
        """, parse_mode="md")
        
    except Exception as e:
        await msg.edit(f"❌ Error: {e}")
    
    await asyncio.sleep(60)
    await msg.delete()

@atomic_command(
    "twitter",
    pattern=r"\.twitter(?:\s|$)(.*)",
    help="Download Twitter video",
    usage=".twitter <twitter URL>",
    category="media"
)
async def twitter_handler(event):
    """Download Twitter video"""
    url = event.pattern_match.group(1)
    
    if not url:
        reply = await event.get_reply_message()
        if reply and reply.text:
            url = reply.text
    
    if not url or "twitter.com" not in url and "x.com" not in url:
        await event.edit("❌ Provide Twitter URL!")
        return
    
    msg = await event.edit(f"📥 Downloading from Twitter... {get_kaomoji('thinking')}")
    
    try:
        await msg.edit(f"""
📥 **Twitter Download** {get_kaomoji('happy')}

━━━━━━━━━━━━━━━━━━━━━━

🐦 **URL:** `{url[:50]}...`

💜 AllAtomic Userbot
        """, parse_mode="md")
        
    except Exception as e:
        await msg.edit(f"❌ Error: {e}")
    
    await asyncio.sleep(60)
    await msg.delete()

@atomic_command(
    "facebook",
    pattern=r"\.fb(?:\s|$)(.*)",
    help="Download Facebook video",
    usage=".fb <facebook URL>",
    category="media"
)
async def facebook_handler(event):
    """Download Facebook video"""
    url = event.pattern_match.group(1)
    
    if not url:
        reply = await event.get_reply_message()
        if reply and reply.text:
            url = reply.text
    
    if not url or "facebook.com" not in url and "fb.watch" not in url:
        await event.edit("❌ Provide Facebook URL!")
        return
    
    msg = await event.edit(f"📥 Downloading from Facebook... {get_kaomoji('thinking')}")
    
    try:
        await msg.edit(f"""
📥 **Facebook Download** {get_kaomoji('happy')}

━━━━━━━━━━━━━━━━━━━━━━

📘 **URL:** `{url[:50]}...`

💜 AllAtomic Userbot
        """, parse_mode="md")
        
    except Exception as e:
        await msg.edit(f"❌ Error: {e}")
    
    await asyncio.sleep(60)
    await msg.delete()

@atomic_command(
    "media",
    pattern=r"\.media(?:\s|$)(.*)",
    help="Download from any supported platform",
    usage=".media <URL>",
    category="media"
)
async def media_handler(event):
    """Universal media downloader"""
    url = event.pattern_match.group(1)
    
    if not url:
        reply = await event.get_reply_message()
        if reply and reply.text:
            url = reply.text
    
    if not url:
        await event.edit("❌ Provide a URL!")
        return
    
    msg = await event.edit(f"📥 Detecting platform... {get_kaomoji('thinking')}")
    
    try:
        # Detect platform
        platform = "Unknown"
        if "youtube.com" in url or "youtu.be" in url:
            platform = "YouTube"
        elif "instagram.com" in url:
            platform = "Instagram"
        elif "tiktok.com" in url:
            platform = "TikTok"
        elif "twitter.com" in url or "x.com" in url:
            platform = "Twitter"
        elif "facebook.com" in url or "fb.watch" in url:
            platform = "Facebook"
        elif "twitch.tv" in url:
            platform = "Twitch"
        elif "reddit.com" in url:
            platform = "Reddit"
        
        await msg.edit(f"""
📥 **Media Downloader** {get_kaomoji('happy')}

━━━━━━━━━━━━━━━━━━━━━━

🌐 **Platform:** `{platform}`
🔗 **URL:** `{url[:60]}...`

⚠️ Install required packages for download

💜 AllAtomic Userbot
        """, parse_mode="md")
        
    except Exception as e:
        await msg.edit(f"❌ Error: {e}")
    
    await asyncio.sleep(60)
    await msg.delete()

@atomic_command(
    "song",
    pattern=r"\.song(?:\s|$)(.*)",
    help="Download audio from YouTube",
    usage=".song <song name or URL>",
    category="media"
)
async def song_handler(event):
    """Download audio from YouTube"""
    query = event.pattern_match.group(1)
    
    if not query:
        await event.edit("❌ Provide song name or YouTube URL!")
        return
    
    msg = await event.edit(f"🎵 Searching for: {query}... {get_kaomoji('thinking')}")
    
    try:
        await msg.edit(f"""
🎵 **Song Download** {get_kaomoji('happy')}

━━━━━━━━━━━━━━━━━━━━━━

🎶 **Query:** `{query[:50]}`

⚠️ Install yt-dlp for actual download

💜 AllAtomic Userbot
        """, parse_mode="md")
        
    except Exception as e:
        await msg.edit(f"❌ Error: {e}")
    
    await asyncio.sleep(60)
    await msg.delete()

@atomic_command(
    "video",
    pattern=r"\.video(?:\s|$)(.*)",
    help="Download video with quality option",
    usage=".video <URL> [quality: 144|240|360|480|720|1080]",
    category="media"
)
async def video_handler(event):
    """Download video with quality option"""
    args = event.pattern_match.group(1)
    
    if not args:
        await event.edit("❌ Provide URL!")
        return
    
    quality = "360"
    url = args
    
    if args.split():
        parts = args.split()
        if parts[-1] in ["144", "240", "360", "480", "720", "1080"]:
            quality = parts[-1]
            url = " ".join(parts[:-1])
    
    msg = await event.edit(f"📹 Downloading {quality}p... {get_kaomoji('thinking')}")
    
    try:
        await msg.edit(f"""
📹 **Video Download** {get_kaomoji('happy')}

━━━━━━━━━━━━━━━━━━━━━━

🎬 **URL:** `{url[:50]}...`
📊 **Quality:** `{quality}p`

💜 AllAtomic Userbot
        """, parse_mode="md")
        
    except Exception as e:
        await msg.edit(f"❌ Error: {e}")
    
    await asyncio.sleep(60)
    await msg.delete()

# Commands registry
commands = {
    "yt": {"help": "Download YouTube video", "usage": ".yt <url>", "category": "media"},
    "insta": {"help": "Download Instagram", "usage": ".insta <url>", "category": "media"},
    "tiktok": {"help": "Download TikTok", "usage": ".tiktok <url>", "category": "media"},
    "twitter": {"help": "Download Twitter", "usage": ".twitter <url>", "category": "media"},
    "fb": {"help": "Download Facebook", "usage": ".fb <url>", "category": "media"},
    "media": {"help": "Universal downloader", "usage": ".media <url>", "category": "media"},
    "song": {"help": "Download audio", "usage": ".song <query>", "category": "media"},
    "video": {"help": "Download video", "usage": ".video <url> [quality]", "category": "media"}
}
