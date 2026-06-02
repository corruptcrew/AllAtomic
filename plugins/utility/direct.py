"""
🔗 Direct Links & URL Tools
Inspired by Man-Userbot
"""

import asyncio
import aiohttp
import re
from telethon import events

from plugins import atomic_command
from app.utils import get_kaomoji, code_block

# Plugin metadata
__plugin__ = {
    "name": "Direct Links",
    "description": "Generate direct download links (Man-Userbot inspired)",
    "category": "utility",
    "credit": "Inspired by Man-Userbot"
}

@atomic_command(
    "direct",
    pattern=r"\.direct(?:\s|$)(.*)",
    help="Generate direct link",
    usage=".direct <url>",
    category="utility"
)
async def direct_handler(event):
    """Generate direct download link"""
    url = event.pattern_match.group(1)
    
    # Try reply if no URL provided
    if not url:
        reply = await event.get_reply_message()
        if reply and reply.text:
            url = reply.text
    
    if not url:
        await event.edit("❌ Please provide a URL!")
        return
    
    msg = await event.edit(f"🔗 Generating direct link... {get_kaomoji('thinking')}")
    
    try:
        # Check for supported services
        direct_link = await generate_direct_link(url)
        
        if direct_link:
            await msg.edit(f"""
🔗 **Direct Link Generated!** {get_kaomoji('happy')}

━━━━━━━━━━━━━━━━━━━━━━

**Original:**
`{url[:100]}`

**Direct:**
`{direct_link}`

━━━━━━━━━━━━━━━━━━━━━━

💜 **AllAtomic Userbot**
📢 **Channel:** @ComputeCode
🔗 **Repo:** github.com/GhostMarshal/AllAtomic
            """, parse_mode="md")
        else:
            await msg.edit(f"""
🔗 **Direct Link** {get_kaomoji('sad')}

━━━━━━━━━━━━━━━━━━━━━━

❌ No direct link generator found for this URL.

**Supported:**
• MediaFire
• Google Drive
• Mega.nz
• ZippyShare
• AndroidFileHost

💜 AllAtomic Userbot
            """, parse_mode="md")
        
    except Exception as e:
        await msg.edit(f"❌ Error: {e}")
    
    await asyncio.sleep(60)
    await msg.delete()

async def generate_direct_link(url: str) -> str:
    """Generate direct link for supported services"""
    
    # MediaFire
    if 'mediafire.com' in url:
        return await mediafire_direct(url)
    
    # Google Drive
    elif 'drive.google.com' in url:
        return google_drive_direct(url)
    
    # Mega.nz
    elif 'mega.nz' in url:
        return f"mega:// (use mega app for: {url})"
    
    return None

async def mediafire_direct(url: str) -> str:
    """Get MediaFire direct link"""
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status == 200:
                    html = await resp.text()
                    # Extract download link
                    match = re.search(r"href='(https://download[^']+)'", html)
                    if match:
                        return match.group(1)
    except:
        pass
    return None

def google_drive_direct(url: str) -> str:
    """Convert Google Drive to direct link"""
    # Extract file ID
    if '/file/d/' in url:
        file_id = url.split('/file/d/')[1].split('/')[0]
        return f"https://drive.google.com/uc?id={file_id}&export=download"
    elif 'id=' in url:
        file_id = url.split('id=')[1].split('&')[0]
        return f"https://drive.google.com/uc?id={file_id}&export=download"
    return url

@atomic_command(
    "source",
    pattern=r"\.source(?:\s|$)(.*)",
    help="Get message source",
    usage=".source (reply to message)",
    category="utility"
)
async def source_handler(event):
    """Get message source (Dragon-Userbot inspired)"""
    reply = await event.get_reply_message()
    
    if not reply:
        await event.edit("❌ Reply to a message!")
        return
    
    try:
        # Get forwarded info
        if reply.fwd_from:
            fwd = reply.fwd_from
            
            source_msg = f"""
📬 **Message Source** {get_kaomoji('happy')}

━━━━━━━━━━━━━━━━━━━━━━

**From:** `{fwd.from_name or 'Unknown'}`
**Date:** `{fwd.date}`
**Channel:** `{fwd.channel_id if fwd.channel_id else 'N/A'}`

━━━━━━━━━━━━━━━━━━━━━━

💜 **AllAtomic Userbot**
📢 **Channel:** @ComputeCode
            """
        else:
            source_msg = f"""
📬 **Message Source** {get_kaomoji('thinking')}

━━━━━━━━━━━━━━━━━━━━━━

Not a forwarded message.

**Sender:** {reply.sender.first_name}
**Chat:** {event.chat.title if event.chat else 'DM'}

━━━━━━━━━━━━━━━━━━━━━━

💜 AllAtomic Userbot
            """
        
        await event.edit(source_msg, parse_mode="md")
        
    except Exception as e:
        await event.edit(f"❌ Error: {e}")
    
    await asyncio.sleep(60)
    await event.delete()

@atomic_command(
    "readmore",
    pattern=r"\.readmore(?:\s|$)(.*)",
    help="Fake read more effect",
    usage=".readmore <text>",
    category="utility"
)
async def readmore_handler(event):
    """Fake read more effect"""
    text = event.pattern_match.group(1)
    
    if not text:
        text = "Your message here"
    
    try:
        # Zero-width character to create read more effect
        await event.edit(f"\u2063{text}")
    except:
        await event.edit(text)

@atomic_command(
    "glitch",
    pattern=r"\.glitch(?:\s|$)(.*)",
    help="Glitch text effect",
    usage=".glitch <text>",
    category="utility"
)
async def glitch_handler(event):
    """Glitch text effect"""
    text = event.pattern_match.group(1)
    
    if not text:
        reply = await event.get_reply_message()
        if reply and reply.text:
            text = reply.text
        else:
            await event.edit("❌ Provide text!")
            return
    
    try:
        # Apply glitch effect
        glitched = ''.join([chr(ord(c) + 1) if c.isalpha() else c for c in text])
        
        await event.edit(f"""
👾 **Glitch Text** {get_kaomoji('happy')}

━━━━━━━━━━━━━━━━━━━━━━

{glitched}

━━━━━━━━━━━━━━━━━━━━━━

💜 AllAtomic Userbot
        """, parse_mode="md")
    except:
        await event.edit(text)

@atomic_command(
    "font",
    pattern=r"\.font(?:\s|$)(.*)",
    help="Change text font",
    usage=".font <text>",
    category="utility"
)
async def font_handler(event):
    """Change text font (TechnoAyanBOT inspired)"""
    text = event.pattern_match.group(1)
    
    if not text:
        await event.edit("❌ Provide text!")
        return
    
    # Font mappings
    fonts = {
        'bold': ''.join(chr(ord(c) + 119790) if c.isalpha() else c for c in text),
        'italic': ''.join(chr(ord(c) + 119834) if c.isalpha() else c for c in text),
        'mono': ''.join(chr(ord(c) + 120102) if c.isalpha() else c for c in text),
    }
    
    font_msg = f"""
🔤 **Font Styles** {get_kaomoji('happy')}

━━━━━━━━━━━━━━━━━━━━━━

**Bold:** {fonts['bold']}
**Italic:** {fonts['italic']}
**Mono:** {fonts['mono']}

━━━━━━━━━━━━━━━━━━━━━━

💜 **AllAtomic Userbot**
📢 **Channel:** @ComputeCode
    """
    
    await event.edit(font_msg, parse_mode="md")

# Commands registry
commands = {
    "direct": {
        "help": "Generate direct link",
        "usage": ".direct <url>",
        "category": "utility"
    },
    "source": {
        "help": "Get message source",
        "usage": ".source (reply)",
        "category": "utility"
    },
    "readmore": {
        "help": "Fake read more",
        "usage": ".readmore <text>",
        "category": "utility"
    },
    "glitch": {
        "help": "Glitch text",
        "usage": ".glitch <text>",
        "category": "utility"
    },
    "font": {
        "help": "Change font style",
        "usage": ".font <text>",
        "category": "utility"
    }
}
