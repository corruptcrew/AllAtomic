"""
🔥 Admin & Group Management Plugin
Complete admin tools for group management
"""

import asyncio
from telethon import events, functions, types
from telethon.tl.types import ChannelParticipantsAdmins, ChatBannedRights

from plugins import atomic_command
from app.utils import get_kaomoji

# Plugin metadata
__plugin__ = {
    "name": "Admin Tools",
    "description": "Complete group administration",
    "category": "group"
}

@atomic_command(
    "ban",
    pattern=r"\.ban(?:\s|$)(.*)",
    help="Ban a user from the group",
    usage=".ban [reason] (reply to user)",
    category="group"
)
async def ban_handler(event):
    """Ban a user from the group"""
    if not event.is_group:
        await event.edit("❌ This command only works in groups!")
        return
    
    if not await event.client.is_admin(event.chat_id, event.sender_id):
        await event.edit("❌ You need to be an admin!")
        return
    
    reply = await event.get_reply_message()
    reason = event.pattern_match.group(1)
    
    if not reply:
        await event.edit("❌ Reply to a user to ban!")
        return
    
    user = await event.client.get_entity(reply.sender_id)
    
    try:
        await event.client.edit_permissions(
            event.chat_id,
            user.id,
            view_messages=False
        )
        
        await event.edit(f"""
🔨 **User Banned!** {get_kaomoji('happy')}

━━━━━━━━━━━━━━━━━━━━━━

👤 **User:** {user.first_name}
🆔 **ID:** `{user.id}`
📝 **Reason:** {reason or 'No reason provided'}

💜 AllAtomic Userbot
        """, parse_mode="md")
        
    except Exception as e:
        await event.edit(f"❌ Error: {e}")
    
    await asyncio.sleep(30)
    await event.delete()

@atomic_command(
    "kick",
    pattern=r"\.kick(?:\s|$)(.*)",
    help="Kick a user from the group",
    usage=".kick [reason] (reply to user)",
    category="group"
)
async def kick_handler(event):
    """Kick a user from the group"""
    if not event.is_group:
        await event.edit("❌ This command only works in groups!")
        return
    
    if not await event.client.is_admin(event.chat_id, event.sender_id):
        await event.edit("❌ You need to be an admin!")
        return
    
    reply = await event.get_reply_message()
    reason = event.pattern_match.group(1)
    
    if not reply:
        await event.edit("❌ Reply to a user to kick!")
        return
    
    user = await event.client.get_entity(reply.sender_id)
    
    try:
        await event.client.kick_participant(event.chat_id, user.id)
        
        await event.edit(f"""
👢 **User Kicked!** {get_kaomoji('happy')}

━━━━━━━━━━━━━━━━━━━━━━

👤 **User:** {user.first_name}
🆔 **ID:** `{user.id}`
📝 **Reason:** {reason or 'No reason provided'}

💜 AllAtomic Userbot
        """, parse_mode="md")
        
    except Exception as e:
        await event.edit(f"❌ Error: {e}")
    
    await asyncio.sleep(30)
    await event.delete()

@atomic_command(
    "mute",
    pattern=r"\.mute(?:\s|$)(.*)",
    help="Mute a user in the group",
    usage=".mute [reason] (reply to user)",
    category="group"
)
async def mute_handler(event):
    """Mute a user in the group"""
    if not event.is_group:
        await event.edit("❌ This command only works in groups!")
        return
    
    if not await event.client.is_admin(event.chat_id, event.sender_id):
        await event.edit("❌ You need to be an admin!")
        return
    
    reply = await event.get_reply_message()
    reason = event.pattern_match.group(1)
    
    if not reply:
        await event.edit("❌ Reply to a user to mute!")
        return
    
    user = await event.client.get_entity(reply.sender_id)
    
    try:
        await event.client.edit_permissions(
            event.chat_id,
            user.id,
            send_messages=False
        )
        
        await event.edit(f"""
🔇 **User Muted!** {get_kaomoji('happy')}

━━━━━━━━━━━━━━━━━━━━━━

👤 **User:** {user.first_name}
🆔 **ID:** `{user.id}`
📝 **Reason:** {reason or 'No reason provided'}

💜 AllAtomic Userbot
        """, parse_mode="md")
        
    except Exception as e:
        await event.edit(f"❌ Error: {e}")
    
    await asyncio.sleep(30)
    await event.delete()

@atomic_command(
    "unmute",
    pattern=r"\.unmute(?:\s|$)(.*)",
    help="Unmute a user in the group",
    usage=".unmute (reply to user)",
    category="group"
)
async def unmute_handler(event):
    """Unmute a user in the group"""
    if not event.is_group:
        await event.edit("❌ This command only works in groups!")
        return
    
    if not await event.client.is_admin(event.chat_id, event.sender_id):
        await event.edit("❌ You need to be an admin!")
        return
    
    reply = await event.get_reply_message()
    
    if not reply:
        await event.edit("❌ Reply to a user to unmute!")
        return
    
    user = await event.client.get_entity(reply.sender_id)
    
    try:
        await event.client.edit_permissions(
            event.chat_id,
            user.id,
            send_messages=True
        )
        
        await event.edit(f"""
🔊 **User Unmuted!** {get_kaomoji('happy')}

━━━━━━━━━━━━━━━━━━━━━━

👤 **User:** {user.first_name}
🆔 **ID:** `{user.id}`

💜 AllAtomic Userbot
        """, parse_mode="md")
        
    except Exception as e:
        await event.edit(f"❌ Error: {e}")
    
    await asyncio.sleep(30)
    await event.delete()

@atomic_command(
    "purge",
    pattern=r"\.purge$",
    help="Purge messages (reply to start point)",
    usage=".purge (reply to message)",
    category="group"
)
async def purge_handler(event):
    """Purge messages"""
    if not event.is_group:
        await event.edit("❌ This command only works in groups!")
        return
    
    if not await event.client.is_admin(event.chat_id, event.sender_id):
        await event.edit("❌ You need to be an admin!")
        return
    
    reply = await event.get_reply_message()
    
    if not reply:
        await event.edit("❌ Reply to the message you want to start purging from!")
        return
    
    msg = await event.edit("🗑️ Purging messages...")
    
    try:
        # Get message IDs to delete
        message_ids = []
        async for message in event.client.iter_messages(
            event.chat_id,
            min_id=reply.id - 1,
            max_id=event.id
        ):
            if message.sender_id == event.sender_id or message.sender_id == reply.sender_id:
                message_ids.append(message.id)
        
        # Delete in batches
        deleted = 0
        for i in range(0, len(message_ids), 100):
            batch = message_ids[i:i+100]
            await event.client.delete_messages(event.chat_id, batch)
            deleted += len(batch)
        
        await msg.edit(f"""
🗑️ **Purge Complete!** {get_kaomoji('happy')}

━━━━━━━━━━━━━━━━━━━━━━

📊 **Deleted:** `{deleted}` messages

💜 AllAtomic Userbot
        """, parse_mode="md")
        
    except Exception as e:
        await msg.edit(f"❌ Error: {e}")
    
    await asyncio.sleep(30)
    await msg.delete()

@atomic_command(
    "zombies",
    pattern=r"\.zombies(?:\s|$)(.*)",
    help="Remove deleted accounts from group",
    usage=".zombies [clean to actually remove]",
    category="group"
)
async def zombies_handler(event):
    """Remove deleted accounts"""
    if not event.is_group:
        await event.edit("❌ This command only works in groups!")
        return
    
    if not await event.client.is_admin(event.chat_id, event.sender_id):
        await event.edit("❌ You need to be an admin!")
        return
    
    msg = await event.edit("🔍 Searching for deleted accounts...")
    
    try:
        deleted_users = []
        async for user in event.client.iter_participants(event.chat_id):
            if user.deleted:
                deleted_users.append(user.id)
        
        count = len(deleted_users)
        
        if count == 0:
            await msg.edit(f"✅ No deleted accounts found! {get_kaomoji('happy')}")
            return
        
        if event.pattern_match.group(1) and event.pattern_match.group(1).lower() == "clean":
            # Actually remove them
            removed = 0
            for user_id in deleted_users:
                try:
                    await event.client.kick_participant(event.chat_id, user_id)
                    removed += 1
                except:
                    pass
            
            await msg.edit(f"""
🧹 **Zombies Cleaned!** {get_kaomoji('happy')}

━━━━━━━━━━━━━━━━━━━━━━

📊 **Removed:** `{removed}` deleted accounts

💜 AllAtomic Userbot
            """, parse_mode="md")
        else:
            await msg.edit(f"""
🧟 **Zombies Found!** {get_kaomoji('thinking')}

━━━━━━━━━━━━━━━━━━━━━━

📊 **Count:** `{count}` deleted accounts

Use `.zombies clean` to remove them

💜 AllAtomic Userbot
            """, parse_mode="md")
        
    except Exception as e:
        await msg.edit(f"❌ Error: {e}")
    
    await asyncio.sleep(30)
    await msg.delete()

@atomic_command(
    "lock",
    pattern=r"\.lock(?:\s|$)(.*)",
    help="Lock group (messages, media, etc.)",
    usage=".lock [messages|media|stickers|polls|info|invite|pin|manage_topics]",
    category="group"
)
async def lock_handler(event):
    """Lock group permissions"""
    if not event.is_group:
        await event.edit("❌ This command only works in groups!")
        return
    
    if not await event.client.is_admin(event.chat_id, event.sender_id):
        await event.edit("❌ You need to be an admin!")
        return
    
    lock_type = event.pattern_match.group(1).lower() if event.pattern_match.group(1) else "messages"
    
    try:
        rights = ChatBannedRights(
            until_date=None,
            send_messages=lock_type in ["messages", "all"],
            send_media=lock_type in ["media", "all"],
            send_stickers=lock_type in ["stickers", "all"],
            send_polls=lock_type in ["polls", "all"],
            change_info=lock_type in ["info", "all"],
            invite_users=lock_type in ["invite", "all"],
            pin_messages=lock_type in ["pin", "all"]
        )
        
        await event.client.edit_permissions(event.chat_id, rights=rights)
        
        await event.edit(f"""
🔒 **Group Locked!** {get_kaomoji('happy')}

━━━━━━━━━━━━━━━━━━━━━━

📝 **Type:** `{lock_type}`

💜 AllAtomic Userbot
        """, parse_mode="md")
        
    except Exception as e:
        await event.edit(f"❌ Error: {e}")
    
    await asyncio.sleep(30)
    await event.delete()

@atomic_command(
    "unlock",
    pattern=r"\.unlock(?:\s|$)(.*)",
    help="Unlock group",
    usage=".unlock [messages|media|stickers|polls|info|invite|pin|manage_topics|all]",
    category="group"
)
async def unlock_handler(event):
    """Unlock group permissions"""
    if not event.is_group:
        await event.edit("❌ This command only works in groups!")
        return
    
    if not await event.client.is_admin(event.chat_id, event.sender_id):
        await event.edit("❌ You need to be an admin!")
        return
    
    lock_type = event.pattern_match.group(1).lower() if event.pattern_match.group(1) else "all"
    
    try:
        rights = ChatBannedRights(
            until_date=None,
            send_messages=False,
            send_media=False,
            send_stickers=False,
            send_polls=False,
            change_info=False,
            invite_users=False,
            pin_messages=False
        )
        
        await event.client.edit_permissions(event.chat_id, rights=rights)
        
        await event.edit(f"""
🔓 **Group Unlocked!** {get_kaomoji('happy')}

━━━━━━━━━━━━━━━━━━━━━━

💜 AllAtomic Userbot
        """, parse_mode="md")
        
    except Exception as e:
        await event.edit(f"❌ Error: {e}")
    
    await asyncio.sleep(30)
    await event.delete()

@atomic_command(
    "pin",
    pattern=r"\.pin(?:\s|$)(.*)",
    help="Pin a message",
    usage=".pin [notify|loud] (reply to message)",
    category="group"
)
async def pin_handler(event):
    """Pin a message"""
    if not event.is_group:
        await event.edit("❌ This command only works in groups!")
        return
    
    if not await event.client.is_admin(event.chat_id, event.sender_id):
        await event.edit("❌ You need to be an admin!")
        return
    
    reply = await event.get_reply_message()
    
    if not reply:
        await event.edit("❌ Reply to a message to pin!")
        return
    
    notify = "notify" in event.pattern_match.group(1).lower() if event.pattern_match.group(1) else False
    
    try:
        await event.client.pin_message(event.chat_id, reply.id, notify=notify)
        
        await event.edit(f"""
📌 **Message Pinned!** {get_kaomoji('happy')}

💜 AllAtomic Userbot
        """, parse_mode="md")
        
    except Exception as e:
        await event.edit(f"❌ Error: {e}")
    
    await asyncio.sleep(30)
    await event.delete()

@atomic_command(
    "unpin",
    pattern=r"\.unpin",
    help="Unpin all messages",
    usage=".unpin",
    category="group"
)
async def unpin_handler(event):
    """Unpin all messages"""
    if not event.is_group:
        await event.edit("❌ This command only works in groups!")
        return
    
    if not await event.client.is_admin(event.chat_id, event.sender_id):
        await event.edit("❌ You need to be an admin!")
        return
    
    try:
        await event.client.unpin_message(event.chat_id)
        
        await event.edit(f"""
📍 **All Messages Unpinned!** {get_kaomoji('happy')}

💜 AllAtomic Userbot
        """, parse_mode="md")
        
    except Exception as e:
        await event.edit(f"❌ Error: {e}")
    
    await asyncio.sleep(30)
    await event.delete()

# Commands registry
commands = {
    "ban": {"help": "Ban a user", "usage": ".ban [reason]", "category": "group"},
    "kick": {"help": "Kick a user", "usage": ".kick [reason]", "category": "group"},
    "mute": {"help": "Mute a user", "usage": ".mute [reason]", "category": "group"},
    "unmute": {"help": "Unmute a user", "usage": ".unmute", "category": "group"},
    "purge": {"help": "Purge messages", "usage": ".purge", "category": "group"},
    "zombies": {"help": "Remove deleted accounts", "usage": ".zombies [clean]", "category": "group"},
    "lock": {"help": "Lock group", "usage": ".lock [type]", "category": "group"},
    "unlock": {"help": "Unlock group", "usage": ".unlock [type]", "category": "group"},
    "pin": {"help": "Pin a message", "usage": ".pin", "category": "group"},
    "unpin": {"help": "Unpin all", "usage": ".unpin", "category": "group"}
}
