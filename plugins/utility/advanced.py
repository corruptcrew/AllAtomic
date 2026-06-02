"""
🔧 Advanced Utility Plugins for AllAtomic Userbot
Paste, Git Info, QR Code, Translate, Reminders
"""

import asyncio
import aiohttp
import qrcode
from telethon import events

from plugins import atomic_command
from app.utils import get_kaomoji, code_block

# Plugin metadata
__plugin__ = {
    "name": "Advanced Utilities",
    "description": "Paste, Git, QR, Translate, Reminders",
    "category": "utility"
}

@atomic_command(
    "paste",
    pattern=r"\.paste(?:\s|$)(.*)",
    help="Paste text to bin",
    usage=".paste (reply to text)",
    category="utility"
)
async def paste_handler(event):
    """Paste text to service"""
    reply = await event.get_reply_message()
    
    if reply:
        text = reply.text
    else:
        text = event.pattern_match.group(1)
    
    if not text:
        await event.edit("❌ Please provide text or reply to a message!")
        return
    
    msg = await event.edit(f"📝 Pasting... {get_kaomoji('thinking')}")
    
    try:
        async with aiohttp.ClientSession() as session:
            # Use nekobin or similar service
            async with session.post(
                "https://nekobin.com/api/documents",
                json={"content": text}
            ) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    key = data.get("result", {}).get("key")
                    
                    if key:
                        paste_url = f"https://nekobin.com/{key}"
                        
                        paste_msg = f"""
📋 **Paste Created!** {get_kaomoji('happy')}

━━━━━━━━━━━━━━━━━━━━━━

🔗 **URL:** [nekobin.com/{key}]({paste_url})

💜 AllAtomic Userbot
                        """
                        
                        await msg.edit(paste_msg, parse_mode="md", link_preview=False)
                        return
        
        await msg.edit("❌ Paste service unavailable!")
        
    except Exception as e:
        await msg.edit(f"❌ Error: {e}")
    
    await asyncio.sleep(60)
    await msg.delete()

@atomic_command(
    "gitinfo",
    pattern=r"\.git(?:\s|$)(.*)",
    help="Get GitHub repo info",
    usage=".git <username/repo>",
    category="utility"
)
async def git_handler(event):
    """Get GitHub repository info"""
    repo = event.pattern_match.group(1)
    
    if not repo:
        await event.edit("❌ Please provide repo in format `username/repo`!")
        return
    
    msg = await event.edit(f"🔍 Fetching repo info... {get_kaomoji('thinking')}")
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://api.github.com/repos/{repo}") as resp:
                if resp.status == 200:
                    data = await resp.json()
                    
                    name = data.get("full_name", "Unknown")
                    description = data.get("description", "No description") or "No description"
                    stars = data.get("stargazers_count", 0)
                    forks = data.get("forks_count", 0)
                    issues = data.get("open_issues_count", 0)
                    language = data.get("language", "Unknown")
                    url = data.get("html_url", "")
                    
                    git_msg = f"""
🐙 **GitHub: {name}** {get_kaomoji('excited')}

━━━━━━━━━━━━━━━━━━━━━━

📝 **Description:** {description[:200]}...

⭐ **Stars:** `{stars}`
🍴 **Forks:** `{forks}`
⚠️ **Issues:** `{issues}`
💻 **Language:** `{language}`

🔗 [View on GitHub]({url})

💜 AllAtomic Userbot
                    """
                    
                    await msg.edit(git_msg, parse_mode="md", link_preview=False)
                    return
        
        await msg.edit(f"❌ Repository not found! {get_kaomoji('sad')}")
        
    except Exception as e:
        await msg.edit(f"❌ Error: {e}")
    
    await asyncio.sleep(60)
    await msg.delete()

@atomic_command(
    "qr",
    pattern=r"\.qr(?:\s|$)(.*)",
    help="Generate QR code",
    usage=".qr <text/url>",
    category="utility"
)
async def qr_handler(event):
    """Generate QR code"""
    text = event.pattern_match.group(1)
    
    if not text:
        # Try reply
        reply = await event.get_reply_message()
        if reply and reply.text:
            text = reply.text
        else:
            await event.edit("❌ Please provide text or URL for QR code!")
            return
    
    msg = await event.edit(f"🔲 Generating QR... {get_kaomoji('thinking')}")
    
    try:
        # Generate QR
        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=5
        )
        qr.add_data(text)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Save temporarily
        qr_path = f"qr_{event.id}.png"
        img.save(qr_path)
        
        await msg.delete()
        
        await event.client.send_file(
            event.chat_id,
            qr_path,
            caption=f"🔲 QR Code Generated! {get_kaomoji('happy')}\n\n💜 AllAtomic",
            force_document=False
        )
        
        # Cleanup
        import os
        os.remove(qr_path)
        
    except Exception as e:
        await msg.edit(f"❌ Error: {e}")
    
    await asyncio.sleep(60)
    await msg.delete()

@atomic_command(
    "tr",
    pattern=r"\.tr(?:\s|$)(.*)",
    help="Translate text",
    usage=".tr <lang> (reply to text)",
    category="utility"
)
async def translate_handler(event):
    """Translate text"""
    reply = await event.get_reply_message()
    
    if not reply and not event.pattern_match.group(1):
        await event.edit("❌ Reply to a message or provide text!")
        return
    
    # Get target language (default: en)
    args = event.pattern_match.group(1)
    target_lang = "en"
    text = None
    
    if reply:
        text = reply.text
        if args:
            target_lang = args.split()[0].lower()
    else:
        # Parse lang and text from args
        parts = args.split(" ", 1)
        if len(parts) > 1:
            target_lang = parts[0]
            text = parts[1]
        else:
            text = parts[0]
    
    msg = await event.edit(f"🌐 Translating to `{target_lang}`... {get_kaomoji('thinking')}")
    
    try:
        # Use free translation API
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"https://api.mymemory.translated.net/get",
                params={
                    "q": text,
                    "langpair": f"en|{target_lang}"
                }
            ) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    translated = data.get("responseData", {}).get("translatedText", "Translation failed")
                    
                    tr_msg = f"""
🌐 **Translation** {get_kaomoji('happy')}

━━━━━━━━━━━━━━━━━━━━━━

**Original:**
{text[:500]}

**Translated ({target_lang}):**
{translated[:500]}

💜 AllAtomic Userbot
                    """
                    
                    await msg.edit(tr_msg, parse_mode="md")
                    return
        
        await msg.edit("❌ Translation failed!")
        
    except Exception as e:
        await msg.edit(f"❌ Error: {e}")
    
    await asyncio.sleep(60)
    await msg.delete()

@atomic_command(
    "remind",
    pattern=r"\.remind(?:\s|$)(.*)",
    help="Set a reminder",
    usage=".remind <minutes> <message>",
    category="utility"
)
async def remind_handler(event):
    """Set a reminder"""
    args = event.pattern_match.group(1)
    
    if not args:
        await event.edit("❌ Usage: `.remind <minutes> <message>`")
        return
    
    try:
        parts = args.split(" ", 1)
        minutes = int(parts[0])
        message = parts[1] if len(parts) > 1 else "Reminder!"
        
        await event.edit(f"⏰ Reminder set for `{minutes}` minutes! {get_kaomoji('happy')}")
        
        # Wait
        await asyncio.sleep(minutes * 60)
        
        # Send reminder
        reminder_msg = f"""
⏰ **REMINDER!** {get_kaomoji('excited')}

━━━━━━━━━━━━━━━━━━━━━━

📝 {message}

⏱️ Set {minutes} minutes ago

💜 AllAtomic Userbot
        """
        
        await event.respond(reminder_msg, parse_mode="md")
        
    except ValueError:
        await event.edit("❌ Invalid format! Use: `.remind 5 Take a break`")
    except Exception as e:
        await event.edit(f"❌ Error: {e}")

# Commands registry
commands = {
    "paste": {
        "help": "Paste text to bin",
        "usage": ".paste (reply to text)",
        "category": "utility"
    },
    "git": {
        "help": "Get GitHub repo info",
        "usage": ".git <username/repo>",
        "category": "utility"
    },
    "qr": {
        "help": "Generate QR code",
        "usage": ".qr <text/url>",
        "category": "utility"
    },
    "tr": {
        "help": "Translate text",
        "usage": ".tr <lang> (reply)",
        "category": "utility"
    },
    "remind": {
        "help": "Set a reminder",
        "usage": ".remind <min> <msg>",
        "category": "utility"
    }
}
