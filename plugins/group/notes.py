"""
📝 Notes & Filters for AllAtomic Userbot
Save and retrieve notes, auto-filters
"""

import asyncio
from telethon import events

from plugins import atomic_command
from app.utils import get_kaomoji

# Plugin metadata
__plugin__ = {
    "name": "Notes & Filters",
    "description": "Save notes and auto-filters",
    "category": "group"
}

@atomic_command(
    "save",
    pattern=r"\.save(?:\s|$)(.*)",
    help="Save a note",
    usage=".save <name> (reply to content)",
    category="group"
)
async def save_handler(event):
    """Save a note"""
    from app import db
    
    name = event.pattern_match.group(1)
    
    if not name:
        await event.edit("❌ Please provide a note name!")
        return
    
    reply = await event.get_reply_message()
    
    if not reply:
        await event.edit("❌ Reply to the message you want to save!")
        return
    
    try:
        # Save to database
        db.save_note(event.chat_id, name, reply.text, event.sender_id)
        
        await event.edit(f"""
📝 **Note Saved!** {get_kaomoji('happy')}

━━━━━━━━━━━━━━━━━━━━━━

📌 **Name:** `{name}`
💬 **Chat:** `{event.chat_id}`

💜 AllAtomic Userbot
        """, parse_mode="md")
        
    except Exception as e:
        await event.edit(f"❌ Error: {e}")
    
    await asyncio.sleep(30)
    await event.delete()

@atomic_command(
    "get",
    pattern=r"\.get(?:\s|$)(.*)",
    help="Get a saved note",
    usage=".get <name>",
    category="group"
)
async def get_handler(event):
    """Get a saved note"""
    from app import db
    
    name = event.pattern_match.group(1)
    
    if not name:
        await event.edit("❌ Please provide a note name!")
        return
    
    try:
        # Get from database
        note = db.get_note(event.chat_id, name)
        
        if note:
            await event.edit(f"""
📝 **Note: {name}** {get_kaomoji('happy')}

━━━━━━━━━━━━━━━━━━━━━━

{note.content}

━━━━━━━━━━━━━━━━━━━━━━

💜 AllAtomic Userbot
            """, parse_mode="md")
        else:
            await event.edit(f"❌ Note `{name}` not found! {get_kaomoji('sad')}")
        
    except Exception as e:
        await event.edit(f"❌ Error: {e}")
    
    await asyncio.sleep(60)
    await event.delete()

@atomic_command(
    "notes",
    pattern=r"\.notes",
    help="List all saved notes",
    usage=".notes",
    category="group"
)
async def notes_handler(event):
    """List all saved notes"""
    from app import db
    
    try:
        # Get all notes for chat
        notes = db.get_all_notes(event.chat_id)
        
        if not notes:
            await event.edit(f"📝 No notes saved! {get_kaomoji('sad')}")
            return
        
        notes_list = "\n".join([f"• `{note.name}`" for note in notes[:20]])
        
        if len(notes) > 20:
            notes_list += f"\n... and {len(notes) - 20} more"
        
        notes_msg = f"""
📝 **Saved Notes** {get_kaomoji('happy')}

━━━━━━━━━━━━━━━━━━━━━━

{notes_list}

━━━━━━━━━━━━━━━━━━━━━━

💜 AllAtomic Userbot
        """
        
        await event.edit(notes_msg, parse_mode="md")
        
    except Exception as e:
        await event.edit(f"❌ Error: {e}")
    
    await asyncio.sleep(60)
    await event.delete()

@atomic_command(
    "clear",
    pattern=r"\.clear(?:\s|$)(.*)",
    help="Delete a note",
    usage=".clear <name>",
    category="group"
)
async def clear_handler(event):
    """Delete a note"""
    from app import db
    
    name = event.pattern_match.group(1)
    
    if not name:
        await event.edit("❌ Please provide a note name!")
        return
    
    try:
        # Delete from database
        db.delete_note(event.chat_id, name)
        
        await event.edit(f"""
🗑️ **Note Deleted!** {get_kaomoji('happy')}

━━━━━━━━━━━━━━━━━━━━━━

📌 **Name:** `{name}`

💜 AllAtomic Userbot
        """, parse_mode="md")
        
    except Exception as e:
        await event.edit(f"❌ Error: {e}")
    
    await asyncio.sleep(30)
    await event.delete()

@atomic_command(
    "filter",
    pattern=r"\.filter(?:\s|$)(.*)",
    help="Add a filter",
    usage=".filter <trigger> (reply to response)",
    category="group"
)
async def filter_handler(event):
    """Add a filter"""
    from app import db
    
    trigger = event.pattern_match.group(1)
    
    if not trigger:
        await event.edit("❌ Please provide a trigger word!")
        return
    
    reply = await event.get_reply_message()
    
    if not reply:
        await event.edit("❌ Reply to the response message!")
        return
    
    try:
        # Save filter
        db.add_filter(event.chat_id, trigger, reply.text, event.sender_id)
        
        await event.edit(f"""
✅ **Filter Added!** {get_kaomoji('happy')}

━━━━━━━━━━━━━━━━━━━━━━

🔤 **Trigger:** `{trigger}`
💬 **Response:** `{reply.text[:50]}...`

💜 AllAtomic Userbot
        """, parse_mode="md")
        
    except Exception as e:
        await event.edit(f"❌ Error: {e}")
    
    await asyncio.sleep(30)
    await event.delete()

@atomic_command(
    "filters",
    pattern=r"\.filters",
    help="List all filters",
    usage=".filters",
    category="group"
)
async def filters_handler(event):
    """List all filters"""
    from app import db
    
    try:
        filters = db.get_all_filters(event.chat_id)
        
        if not filters:
            await event.edit(f"🔤 No filters set! {get_kaomoji('sad')}")
            return
        
        filters_list = "\n".join([f"• `{f.trigger}`" for f in filters[:20]])
        
        if len(filters) > 20:
            filters_list += f"\n... and {len(filters) - 20} more"
        
        filters_msg = f"""
🔤 **Active Filters** {get_kaomoji('happy')}

━━━━━━━━━━━━━━━━━━━━━━

{filters_list}

━━━━━━━━━━━━━━━━━━━━━━

💜 AllAtomic Userbot
        """
        
        await event.edit(filters_msg, parse_mode="md")
        
    except Exception as e:
        await event.edit(f"❌ Error: {e}")
    
    await asyncio.sleep(60)
    await event.delete()

@atomic_command(
    "stop",
    pattern=r"\.stop(?:\s|$)(.*)",
    help="Delete a filter",
    usage=".stop <trigger>",
    category="group"
)
async def stop_handler(event):
    """Delete a filter"""
    from app import db
    
    trigger = event.pattern_match.group(1)
    
    if not trigger:
        await event.edit("❌ Please provide a trigger word!")
        return
    
    try:
        db.delete_filter(event.chat_id, trigger)
        
        await event.edit(f"""
🗑️ **Filter Deleted!** {get_kaomoji('happy')}

━━━━━━━━━━━━━━━━━━━━━━

🔤 **Trigger:** `{trigger}`

💜 AllAtomic Userbot
        """, parse_mode="md")
        
    except Exception as e:
        await event.edit(f"❌ Error: {e}")
    
    await asyncio.sleep(30)
    await event.delete()

# Commands registry
commands = {
    "save": {
        "help": "Save a note",
        "usage": ".save <name>",
        "category": "group"
    },
    "get": {
        "help": "Get a saved note",
        "usage": ".get <name>",
        "category": "group"
    },
    "notes": {
        "help": "List all notes",
        "usage": ".notes",
        "category": "group"
    },
    "clear": {
        "help": "Delete a note",
        "usage": ".clear <name>",
        "category": "group"
    },
    "filter": {
        "help": "Add a filter",
        "usage": ".filter <trigger>",
        "category": "group"
    },
    "filters": {
        "help": "List all filters",
        "usage": ".filters",
        "category": "group"
    },
    "stop": {
        "help": "Delete a filter",
        "usage": ".stop <trigger>",
        "category": "group"
    }
}
