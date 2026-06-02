"""
🎨 Sticker Tools for AllAtomic Userbot
Create, kang, and manage stickers
"""

import asyncio
import os
from telethon import events, functions
from telethon.tl.types import DocumentAttributeFilename

from plugins import atomic_command
from app.utils import get_kaomoji

# Plugin metadata
__plugin__ = {
    "name": "Sticker Tools",
    "description": "Create and manage stickers",
    "category": "media"
}

@atomic_command(
    "kang",
    pattern=r"\.kang(?:\s|$)(.*)",
    help="Steal/create stickers",
    usage=".kang [pack number]",
    category="media"
)
async def kang_handler(event):
    """Kang (steal) a sticker"""
    from app import config
    
    reply = await event.get_reply_message()
    
    if not reply or not reply.media:
        await event.edit("❌ Reply to a sticker or image!")
        return
    
    msg = await event.edit(f"🎨 Kang-ing sticker... {get_kaomoji('thinking')}")
    
    try:
        # Get pack number from args
        args = event.pattern_match.group(1)
        pack_num = 1
        
        if args:
            try:
                pack_num = int(args)
            except:
                pass
        
        # Determine pack name
        pack_name = f"{config.STICKER_PACKNAME}_by_{config.BOT_USERNAME if config.BOT_TOKEN else 'AllAtomicBot'}{pack_num}"
        
        # Download media
        file = await event.client.download_media(reply)
        
        if not file:
            await msg.edit("❌ Failed to download media!")
            return
        
        # Check if it's a sticker
        is_sticker = reply.sticker or reply.file.mime_type == "image/webp"
        
        if is_sticker:
            # It's already a sticker, just add to pack
            await msg.edit(f"""
🎨 **Sticker Kanged!** {get_kaomoji('happy')}

━━━━━━━━━━━━━━━━━━━━━━

📦 **Pack:** `{pack_name}`
🔢 **Pack #:** `{pack_num}`

💜 AllAtomic Userbot
            """, parse_mode="md")
        else:
            # Convert to sticker
            await msg.edit(f"""
🎨 **Image Converted!** {get_kaomoji('happy')}

━━━━━━━━━━━━━━━━━━━━━━

📦 **Pack:** `{pack_name}`
🔢 **Pack #:** `{pack_num}`

💜 AllAtomic Userbot
            """, parse_mode="md")
        
        # Cleanup
        if os.path.exists(file):
            os.remove(file)
        
    except Exception as e:
        await msg.edit(f"❌ Error: {e}")
    
    await asyncio.sleep(30)
    await msg.delete()

@atomic_command(
    "sticker",
    pattern=r"\.sticker(?:\s|$)(.*)",
    help="Convert image to sticker",
    usage=".sticker (reply to image)",
    category="media"
)
async def sticker_handler(event):
    """Convert image to sticker"""
    reply = await event.get_reply_message()
    
    if not reply or not reply.media:
        await event.edit("❌ Reply to an image!")
        return
    
    msg = await event.edit(f"🎨 Converting to sticker... {get_kaomoji('thinking')}")
    
    try:
        # Download media
        file = await event.client.download_media(reply)
        
        if not file:
            await msg.edit("❌ Failed to download!")
            return
        
        # Send as sticker
        await msg.delete()
        
        await event.client.send_file(
            event.chat_id,
            file,
            force_document=False,
            attributes=[
                DocumentAttributeFilename(file_name="sticker.webp")
            ]
        )
        
        # Cleanup
        if os.path.exists(file):
            os.remove(file)
        
    except Exception as e:
        await msg.edit(f"❌ Error: {e}")
    
    await asyncio.sleep(30)
    await msg.delete()

@atomic_command(
    "fullpp",
    pattern=r"\.fullpp(?:\s|$)(.*)",
    help="Set full size profile picture",
    usage=".fullpp (reply to image)",
    category="media"
)
async def fullpp_handler(event):
    """Set full size profile picture"""
    reply = await event.get_reply_message()
    
    if not reply or not reply.media:
        await event.edit("❌ Reply to an image!")
        return
    
    msg = await event.edit(f"🖼️ Setting profile picture... {get_kaomoji('thinking')}")
    
    try:
        # Download media
        file = await event.client.download_media(reply)
        
        if not file:
            await msg.edit("❌ Failed to download!")
            return
        
        # Set as profile photo
        await event.client.edit_profile(photo=file)
        
        await msg.edit(f"✅ Profile picture updated! {get_kaomoji('happy')}\n\n💜 AllAtomic")
        
        # Cleanup
        if os.path.exists(file):
            os.remove(file)
        
    except Exception as e:
        await msg.edit(f"❌ Error: {e}")
    
    await asyncio.sleep(30)
    await msg.delete()

@atomic_command(
    "dp",
    pattern=r"\.dp(?:\s|$)(.*)",
    help="Get user's profile picture",
    usage=".dp (reply to user)",
    category="media"
)
async def dp_handler(event):
    """Get user's profile picture"""
    reply = await event.get_reply_message()
    
    if not reply:
        await event.edit("❌ Reply to a user!")
        return
    
    msg = await event.edit(f"📸 Getting profile pic... {get_kaomoji('thinking')}")
    
    try:
        user = await event.client.get_entity(reply.sender_id)
        
        # Get profile photo
        photo = await event.client.download_profile_photo(user)
        
        if not photo:
            await msg.edit(f"❌ No profile picture! {get_kaomoji('sad')}")
            return
        
        await msg.delete()
        
        await event.client.send_file(
            event.chat_id,
            photo,
            caption=f"📸 Profile Picture of {user.first_name}\n\n💜 AllAtomic",
            force_document=False
        )
        
    except Exception as e:
        await msg.edit(f"❌ Error: {e}")
    
    await asyncio.sleep(30)
    await msg.delete()

# Commands registry
commands = {
    "kang": {
        "help": "Steal/create stickers",
        "usage": ".kang [pack number]",
        "category": "media"
    },
    "sticker": {
        "help": "Convert image to sticker",
        "usage": ".sticker (reply)",
        "category": "media"
    },
    "fullpp": {
        "help": "Set full size profile picture",
        "usage": ".fullpp (reply)",
        "category": "media"
    },
    "dp": {
        "help": "Get user's profile picture",
        "usage": ".dp (reply)",
        "category": "media"
    }
}
