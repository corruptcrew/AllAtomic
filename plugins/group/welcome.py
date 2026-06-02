"""
👋 Welcome & Goodbye Messages
Automated welcome and goodbye for groups
"""

import asyncio
from telethon import events
from telethon.tl.types import ChatAdminAddedInviteBy, ChannelParticipantsAdmins

from plugins import atomic_command
from app.utils import get_kaomoji

# Plugin metadata
__plugin__ = {
    "name": "Welcome System",
    "description": "Automated welcome and goodbye messages",
    "category": "group"
}

# Store welcome messages per chat
welcome_messages = {}
goodbye_messages = {}
welcome_enabled = {}

@atomic_command(
    "setwelcome",
    pattern=r"\.setwelcome(?:\s|$)(.*)",
    help="Set custom welcome message",
    usage=".setwelcome <message>",
    category="group"
)
async def set_welcome_handler(event):
    """Set custom welcome message"""
    if not event.is_group:
        await event.edit("❌ This command only works in groups!")
        return
    
    if not await event.client.is_admin(event.chat_id, event.sender_id):
        await event.edit("❌ You need to be an admin!")
        return
    
    message = event.pattern_match.group(1)
    
    if not message:
        await event.edit("""
📝 **Set Welcome Message**

━━━━━━━━━━━━━━━━━━━━━━

**Usage:** `.setwelcome <message>`

**Available Variables:**
- `{first}` - User's first name
- `{last}` - User's last name
- `{fullname}` - User's full name
- `{username}` - User's username
- `{mention}` - Mention user
- `{group}` - Group name
- `{count}` - Member count

**Example:**
`.setwelcome Welcome {first} to {group}!`

💜 AllAtomic Userbot
        """, parse_mode="md")
        return
    
    welcome_messages[event.chat_id] = message
    
    await event.edit(f"""
✅ **Welcome Message Set!** {get_kaomoji('happy')}

━━━━━━━━━━━━━━━━━━━━━━

📝 **Message:** `{message[:100]}...`

💜 AllAtomic Userbot
    """, parse_mode="md")

@atomic_command(
    "setgoodbye",
    pattern=r"\.setgoodbye(?:\s|$)(.*)",
    help="Set custom goodbye message",
    usage=".setgoodbye <message>",
    category="group"
)
async def set_goodbye_handler(event):
    """Set custom goodbye message"""
    if not event.is_group:
        await event.edit("❌ This command only works in groups!")
        return
    
    if not await event.client.is_admin(event.chat_id, event.sender_id):
        await event.edit("❌ You need to be an admin!")
        return
    
    message = event.pattern_match.group(1)
    
    if not message:
        await event.edit("""
📝 **Set Goodbye Message**

━━━━━━━━━━━━━━━━━━━━━━

**Usage:** `.setgoodbye <message>`

**Available Variables:**
- `{first}` - User's first name
- `{last}` - User's last name
- `{fullname}` - User's full name
- `{username}` - User's username
- `{group}` - Group name

**Example:**
`.setgoodbye Goodbye {first}!`

💜 AllAtomic Userbot
        """, parse_mode="md")
        return
    
    goodbye_messages[event.chat_id] = message
    
    await event.edit(f"""
✅ **Goodbye Message Set!** {get_kaomoji('happy')}

━━━━━━━━━━━━━━━━━━━━━━

📝 **Message:** `{message[:100]}...`

💜 AllAtomic Userbot
    """, parse_mode="md")

@atomic_command(
    "welcome",
    pattern=r"\.welcome(?:\s|$)(.*)",
    help="Enable/disable welcome messages",
    usage=".welcome [on|off|get]",
    category="group"
)
async def welcome_handler(event):
    """Toggle welcome messages"""
    if not event.is_group:
        await event.edit("❌ This command only works in groups!")
        return
    
    if not await event.client.is_admin(event.chat_id, event.sender_id):
        await event.edit("❌ You need to be an admin!")
        return
    
    action = event.pattern_match.group(1).lower() if event.pattern_match.group(1) else "get"
    
    if action == "on":
        welcome_enabled[event.chat_id] = True
        await event.edit(f"""
✅ **Welcome Messages Enabled!** {get_kaomoji('happy')}

💜 AllAtomic Userbot
        """, parse_mode="md")
    elif action == "off":
        welcome_enabled[event.chat_id] = False
        await event.edit(f"""
❌ **Welcome Messages Disabled!** {get_kaomoji('sad')}

💜 AllAtomic Userbot
        """, parse_mode="md")
    else:
        status = "✅ Enabled" if welcome_enabled.get(event.chat_id, False) else "❌ Disabled"
        message = welcome_messages.get(event.chat_id, "No custom message set")
        
        await event.edit(f"""
👋 **Welcome Settings** {get_kaomoji('thinking')}

━━━━━━━━━━━━━━━━━━━━━━

📊 **Status:** {status}
📝 **Message:** `{message[:50]}...`

💜 AllAtomic Userbot
        """, parse_mode="md")

@atomic_command(
    "goodbye",
    pattern=r"\.goodbye(?:\s|$)(.*)",
    help="Enable/disable goodbye messages",
    usage=".goodbye [on|off|get]",
    category="group"
)
async def goodbye_handler(event):
    """Toggle goodbye messages"""
    if not event.is_group:
        await event.edit("❌ This command only works in groups!")
        return
    
    if not await event.client.is_admin(event.chat_id, event.sender_id):
        await event.edit("❌ You need to be an admin!")
        return
    
    action = event.pattern_match.group(1).lower() if event.pattern_match.group(1) else "get"
    
    if action == "on":
        await event.edit(f"""
✅ **Goodbye Messages Enabled!** {get_kaomoji('happy')}

💜 AllAtomic Userbot
        """, parse_mode="md")
    elif action == "off":
        await event.edit(f"""
❌ **Goodbye Messages Disabled!** {get_kaomoji('sad')}

💜 AllAtomic Userbot
        """, parse_mode="md")
    else:
        message = goodbye_messages.get(event.chat_id, "No custom message set")
        
        await event.edit(f"""
👋 **Goodbye Settings** {get_kaomoji('thinking')}

━━━━━━━━━━━━━━━━━━━━━━

📝 **Message:** `{message[:50]}...`

💜 AllAtomic Userbot
        """, parse_mode="md")

@atomic_command(
    "testwelcome",
    pattern=r"\.testwelcome",
    help="Test welcome message",
    usage=".testwelcome",
    category="group"
)
async def test_welcome_handler(event):
    """Test welcome message"""
    if not event.is_group:
        await event.edit("❌ This command only works in groups!")
        return
    
    message = welcome_messages.get(event.chat_id, "Welcome {first} to {group}!")
    
    # Replace variables
    user = await event.client.get_entity(event.sender_id)
    chat = await event.client.get_entity(event.chat_id)
    
    message = message.replace("{first}", user.first_name or "User")
    message = message.replace("{last}", user.last_name or "")
    message = message.replace("{fullname}", f"{user.first_name or ''} {user.last_name or ''}".strip())
    message = message.replace("{username}", f"@{user.username}" if user.username else "N/A")
    message = message.replace("{mention}", f"[{user.first_name}](tg://user?id={user.id})")
    message = message.replace("{group}", chat.title or "Group")
    
    await event.edit(message, parse_mode="md")

@atomic_command(
    "delwelcome",
    pattern=r"\.delwelcome",
    help="Delete custom welcome message",
    usage=".delwelcome",
    category="group"
)
async def del_welcome_handler(event):
    """Delete welcome message"""
    if not event.is_group:
        await event.edit("❌ This command only works in groups!")
        return
    
    if not await event.client.is_admin(event.chat_id, event.sender_id):
        await event.edit("❌ You need to be an admin!")
        return
    
    if event.chat_id in welcome_messages:
        del welcome_messages[event.chat_id]
        await event.edit(f"""
🗑️ **Welcome Message Deleted!** {get_kaomoji('happy')}

💜 AllAtomic Userbot
        """, parse_mode="md")
    else:
        await event.edit("❌ No custom welcome message set!")

@atomic_command(
    "delgoodbye",
    pattern=r"\.delgoodbye",
    help="Delete custom goodbye message",
    usage=".delgoodbye",
    category="group"
)
async def del_goodbye_handler(event):
    """Delete goodbye message"""
    if not event.is_group:
        await event.edit("❌ This command only works in groups!")
        return
    
    if not await event.client.is_admin(event.chat_id, event.sender_id):
        await event.edit("❌ You need to be an admin!")
        return
    
    if event.chat_id in goodbye_messages:
        del goodbye_messages[event.chat_id]
        await event.edit(f"""
🗑️ **Goodbye Message Deleted!** {get_kaomoji('happy')}

💜 AllAtomic Userbot
        """, parse_mode="md")
    else:
        await event.edit("❌ No custom goodbye message set!")

# Commands registry
commands = {
    "setwelcome": {"help": "Set welcome message", "usage": ".setwelcome <msg>", "category": "group"},
    "setgoodbye": {"help": "Set goodbye message", "usage": ".setgoodbye <msg>", "category": "group"},
    "welcome": {"help": "Toggle welcome", "usage": ".welcome [on|off]", "category": "group"},
    "goodbye": {"help": "Toggle goodbye", "usage": ".goodbye [on|off]", "category": "group"},
    "testwelcome": {"help": "Test welcome", "usage": ".testwelcome", "category": "group"},
    "delwelcome": {"help": "Delete welcome", "usage": ".delwelcome", "category": "group"},
    "delgoodbye": {"help": "Delete goodbye", "usage": ".delgoodbye", "category": "group"}
}
