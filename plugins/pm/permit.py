"""
💬 PM Permit for AllAtomic Userbot
Auto-approve/block unknown users in PM
"""

import asyncio
from telethon import events

from plugins import atomic_command
from app.utils import get_kaomoji, mention_html

# Plugin metadata
__plugin__ = {
    "name": "PM Permit",
    "description": "PM permit system",
    "category": "pm"
}

# PM permit message
PM_MESSAGE = """
⚠️ **PM Permit Active** ⚠️

━━━━━━━━━━━━━━━━━━━━━━

Hello! My master is currently busy.
Please wait for approval before messaging.

{kaomoji}

💜 AllAtomic Userbot
"""

# Track pending users
pending_users = set()

@atomic_command(
    "approve",
    pattern=r"\.approve(?:\s|$)(.*)",
    help="Approve a user for PM",
    usage=".approve",
    category="pm"
)
async def approve_handler(event):
    """Approve a user for PM"""
    from app import db, config
    
    if not event.is_private:
        await event.edit("❌ This command only works in PM!")
        return
    
    # Get user from reply or args
    reply = await event.get_reply_message()
    user = reply.sender if reply else None
    
    if not user:
        # Use current chat
        user = await event.get_chat()
    
    # Check if already approved
    if db.is_approved(user.id, event.chat_id):
        await event.edit("✅ User is already approved!")
        return
    
    # Approve user
    db.approve_user(user.id, event.chat_id, config.OWNER_ID, "Manual approval")
    pending_users.discard(user.id)
    
    approved_msg = f"""
✅ **User Approved!** {get_kaomoji('happy')}

━━━━━━━━━━━━━━━━━━━━━━

👤 **User:** {mention_html(user.id, user.first_name)}
🆔 **ID:** `{user.id}`

💜 Approved by AllAtomic
    """
    
    await event.edit(approved_msg, parse_mode="md")

@atomic_command(
    "disapprove",
    pattern=r"\.disapprove(?:\s|$)(.*)",
    help="Disapprove a user",
    usage=".disapprove",
    category="pm"
)
async def disapprove_handler(event):
    """Disapprove a user"""
    from app import db
    
    if not event.is_private:
        await event.edit("❌ This command only works in PM!")
        return
    
    user = await event.get_chat()
    
    # Disapprove user
    db.disapprove_user(user.id, event.chat_id)
    
    disapproved_msg = f"""
❌ **User Disapproved!** {get_kaomoji('angry')}

━━━━━━━━━━━━━━━━━━━━━━

👤 **User:** {mention_html(user.id, user.first_name)}
🆔 **ID:** `{user.id}`

💜 AllAtomic Userbot
    """
    
    await event.edit(disapproved_msg, parse_mode="md")

@atomic_command(
    "block",
    pattern=r"\.block(?:\s|$)(.*)",
    help="Block a user",
    usage=".block",
    category="pm"
)
async def block_handler(event):
    """Block a user"""
    from app import db
    
    if not event.is_private:
        await event.edit("❌ This command only works in PM!")
        return
    
    user = await event.get_chat()
    
    try:
        await event.client.block(user.id)
        db.disapprove_user(user.id, event.chat_id)
        
        blocked_msg = f"""
🚫 **User Blocked!** {get_kaomoji('angry')}

━━━━━━━━━━━━━━━━━━━━━━

👤 **User:** {mention_html(user.id, user.first_name)}
🆔 **ID:** `{user.id}`

💜 AllAtomic Userbot
        """
        
        await event.edit(blocked_msg, parse_mode="md")
        
    except Exception as e:
        await event.edit(f"❌ Error: {e}")

@atomic_command(
    "unblock",
    pattern=r"\.unblock(?:\s|$)(.*)",
    help="Unblock a user",
    usage=".unblock",
    category="pm"
)
async def unblock_handler(event):
    """Unblock a user"""
    if not event.is_private:
        await event.edit("❌ This command only works in PM!")
        return
    
    user = await event.get_chat()
    
    try:
        await event.client.unblock(user.id)
        
        unblocked_msg = f"""
✅ **User Unblocked!** {get_kaomoji('happy')}

━━━━━━━━━━━━━━━━━━━━━━

👤 **User:** {mention_html(user.id, user.first_name)}
🆔 **ID:** `{user.id}`

💜 AllAtomic Userbot
        """
        
        await event.edit(unblocked_msg, parse_mode="md")
        
    except Exception as e:
        await event.edit(f"❌ Error: {e}")

@atomic_command(
    "arc",
    pattern=r"\.arc(?:\s|$)(.*)",
    help="Archive a chat",
    usage=".arc",
    category="pm"
)
async def archive_handler(event):
    """Archive a chat"""
    try:
        await event.client.edit_folder(event.chat_id, folder=1)
        await event.edit(f"📁 Chat archived! {get_kaomoji('happy')}")
    except Exception as e:
        await event.edit(f"❌ Error: {e}")
    
    await asyncio.sleep(10)
    await event.delete()

# PM permit listener
async def pm_permit_listener(client, config, db):
    """Listen for new PM messages and apply permit"""
    
    @client.client.on(events.NewMessage(incoming=True, private=True))
    async def handler(event):
        if event.is_private and not event.out:
            user = await event.get_chat()
            
            # Skip if user is approved or owner
            if db.is_approved(user.id, event.chat_id):
                return
            
            if user.id == config.OWNER_ID:
                return
            
            # Check if already warned
            if user.id in pending_users:
                return
            
            pending_users.add(user.id)
            
            # Send PM permit message
            try:
                await event.reply(PM_MESSAGE.format(kaomoji=get_kaomoji('shy')))
            except:
                pass

# Commands registry
commands = {
    "approve": {
        "help": "Approve a user for PM",
        "usage": ".approve",
        "category": "pm"
    },
    "disapprove": {
        "help": "Disapprove a user",
        "usage": ".disapprove",
        "category": "pm"
    },
    "block": {
        "help": "Block a user",
        "usage": ".block",
        "category": "pm"
    },
    "unblock": {
        "help": "Unblock a user",
        "usage": ".unblock",
        "category": "pm"
    },
    "arc": {
        "help": "Archive a chat",
        "usage": ".arc",
        "category": "pm"
    }
}
