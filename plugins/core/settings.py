"""
⚙️ Settings & Configuration Plugin
Manage bot settings, variables, and preferences
"""

import asyncio
from telethon import events

from plugins import atomic_command
from app.utils import get_kaomoji

# Plugin metadata
__plugin__ = {
    "name": "Settings",
    "description": "Bot settings and configuration",
    "category": "core"
}

# In-memory settings storage
bot_settings = {
    "pm_permit": True,
    "antispam": True,
    "logger": True,
    "auto_read": False,
    "online_status": True
}

@atomic_command(
    "settings",
    pattern=r"\.settings(?:\s|$)(.*)",
    help="View bot settings",
    usage=".settings",
    category="core"
)
async def settings_handler(event):
    """View all bot settings"""
    settings_msg = f"""
⚙️ **AllAtomic Settings** {get_kaomoji('happy')}

━━━━━━━━━━━━━━━━━━━━━━

🔒 **PM Permit:** {'✅ Enabled' if bot_settings.get('pm_permit') else '❌ Disabled'}
🛡️ **AntiSpam:** {'✅ Enabled' if bot_settings.get('antispam') else '❌ Disabled'}
📝 **Logger:** {'✅ Enabled' if bot_settings.get('logger') else '❌ Disabled'}
👁️ **Auto Read:** {'✅ Enabled' if bot_settings.get('auto_read') else '❌ Disabled'}
🟢 **Online:** {'✅ Enabled' if bot_settings.get('online_status') else '❌ Disabled'}

━━━━━━━━━━━━━━━━━━━━━━

Use `.set <key> <value>` to change settings

💜 AllAtomic Userbot
    """
    
    await event.edit(settings_msg, parse_mode="md")

@atomic_command(
    "set",
    pattern=r"\.set(?:\s|$)(.*)",
    help="Set a bot variable",
    usage=".set <key> <value>",
    category="core"
)
async def set_handler(event):
    """Set a bot variable"""
    args = event.pattern_match.group(1)
    
    if not args:
        await event.edit("""
⚙️ **Set Variable**

━━━━━━━━━━━━━━━━━━━━━━

**Usage:** `.set <key> <value>`

**Available Keys:**
- `pm_permit` (on/off)
- `antispam` (on/off)
- `logger` (on/off)
- `auto_read` (on/off)
- `online_status` (on/off)

**Example:**
`.set pm_permit off`

💜 AllAtomic Userbot
        """, parse_mode="md")
        return
    
    try:
        key, value = args.split(" ", 1)
        key = key.lower()
        value = value.lower()
        
        if key in bot_settings:
            bot_settings[key] = value in ["on", "true", "yes", "1"]
            
            await event.edit(f"""
✅ **Setting Updated!** {get_kaomoji('happy')}

━━━━━━━━━━━━━━━━━━━━━━

🔑 **Key:** `{key}`
💎 **Value:** `{bot_settings[key]}`

💜 AllAtomic Userbot
            """, parse_mode="md")
        else:
            await event.edit(f"❌ Unknown setting: `{key}`")
    
    except ValueError:
        await event.edit("❌ Format: `.set <key> <value>`")
    
    await asyncio.sleep(30)
    await event.delete()

@atomic_command(
    "get",
    pattern=r"\.get(?:\s|$)(.*)",
    help="Get a bot variable",
    usage=".get <key>",
    category="core"
)
async def get_handler(event):
    """Get a bot variable"""
    key = event.pattern_match.group(1)
    
    if not key:
        await event.edit("❌ Provide a key: `.get <key>`")
        return
    
    key = key.lower()
    
    if key in bot_settings:
        await event.edit(f"""
🔑 **Variable: {key}** {get_kaomoji('happy')}

━━━━━━━━━━━━━━━━━━━━━━

💎 **Value:** `{bot_settings[key]}`

💜 AllAtomic Userbot
        """, parse_mode="md")
    else:
        await event.edit(f"❌ Unknown key: `{key}`")
    
    await asyncio.sleep(30)
    await event.delete()

@atomic_command(
    "reset",
    pattern=r"\.reset(?:\s|$)(.*)",
    help="Reset settings to default",
    usage=".reset [all|key]",
    category="core"
)
async def reset_handler(event):
    """Reset settings to default"""
    key = event.pattern_match.group(1)
    
    if not key:
        await event.edit("""
🔄 **Reset Settings**

━━━━━━━━━━━━━━━━━━━━━━

**Usage:** `.reset <key|all>`

**Example:**
`.reset pm_permit`
`.reset all`

💜 AllAtomic Userbot
        """, parse_mode="md")
        return
    
    if key.lower() == "all":
        bot_settings.update({
            "pm_permit": True,
            "antispam": True,
            "logger": True,
            "auto_read": False,
            "online_status": True
        })
        
        await event.edit(f"""
🔄 **All Settings Reset!** {get_kaomoji('happy')}

💜 AllAtomic Userbot
        """, parse_mode="md")
    elif key.lower() in bot_settings:
        defaults = {
            "pm_permit": True,
            "antispam": True,
            "logger": True,
            "auto_read": False,
            "online_status": True
        }
        bot_settings[key.lower()] = defaults[key.lower()]
        
        await event.edit(f"""
🔄 **Setting Reset!** {get_kaomoji('happy')}

🔑 **Key:** `{key}`
💎 **Value:** `{bot_settings[key.lower()]}`

💜 AllAtomic Userbot
        """, parse_mode="md")
    else:
        await event.edit(f"❌ Unknown key: `{key}`")
    
    await asyncio.sleep(30)
    await event.delete()

@atomic_command(
    "pmpermit",
    pattern=r"\.pmpermit(?:\s|$)(.*)",
    help="Toggle PM permit",
    usage=".pmpermit [on|off]",
    category="core"
)
async def pmpermit_handler(event):
    """Toggle PM permit"""
    action = event.pattern_match.group(1).lower() if event.pattern_match.group(1) else "get"
    
    if action == "on":
        bot_settings["pm_permit"] = True
        await event.edit(f"""
✅ **PM Permit Enabled!** {get_kaomoji('happy')}

💜 AllAtomic Userbot
        """, parse_mode="md")
    elif action == "off":
        bot_settings["pm_permit"] = False
        await event.edit(f"""
❌ **PM Permit Disabled!** {get_kaomoji('sad')}

💜 AllAtomic Userbot
        """, parse_mode="md")
    else:
        status = "✅ Enabled" if bot_settings.get("pm_permit") else "❌ Disabled"
        await event.edit(f"""
🔒 **PM Permit Status**

━━━━━━━━━━━━━━━━━━━━━━

📊 **Status:** {status}

Use `.pmpermit on` or `.pmpermit off`

💜 AllAtomic Userbot
        """, parse_mode="md")
    
    await asyncio.sleep(30)
    await event.delete()

@atomic_command(
    "antispam",
    pattern=r"\.antispam(?:\s|$)(.*)",
    help="Toggle anti-spam",
    usage=".antispam [on|off]",
    category="core"
)
async def antispam_handler(event):
    """Toggle anti-spam"""
    action = event.pattern_match.group(1).lower() if event.pattern_match.group(1) else "get"
    
    if action == "on":
        bot_settings["antispam"] = True
        await event.edit(f"""
🛡️ **AntiSpam Enabled!** {get_kaomoji('happy')}

💜 AllAtomic Userbot
        """, parse_mode="md")
    elif action == "off":
        bot_settings["antispam"] = False
        await event.edit(f"""
❌ **AntiSpam Disabled!** {get_kaomoji('sad')}

💜 AllAtomic Userbot
        """, parse_mode="md")
    else:
        status = "✅ Enabled" if bot_settings.get("antispam") else "❌ Disabled"
        await event.edit(f"""
🛡️ **AntiSpam Status**

━━━━━━━━━━━━━━━━━━━━━━

📊 **Status:** {status}

💜 AllAtomic Userbot
        """, parse_mode="md")
    
    await asyncio.sleep(30)
    await event.delete()

@atomic_command(
    "logger",
    pattern=r"\.logger(?:\s|$)(.*)",
    help="Toggle logger",
    usage=".logger [on|off]",
    category="core"
)
async def logger_handler(event):
    """Toggle logger"""
    action = event.pattern_match.group(1).lower() if event.pattern_match.group(1) else "get"
    
    if action == "on":
        bot_settings["logger"] = True
        await event.edit(f"""
📝 **Logger Enabled!** {get_kaomoji('happy')}

💜 AllAtomic Userbot
        """, parse_mode="md")
    elif action == "off":
        bot_settings["logger"] = False
        await event.edit(f"""
❌ **Logger Disabled!** {get_kaomoji('sad')}

💜 AllAtomic Userbot
        """, parse_mode="md")
    else:
        status = "✅ Enabled" if bot_settings.get("logger") else "❌ Disabled"
        await event.edit(f"""
📝 **Logger Status**

━━━━━━━━━━━━━━━━━━━━━━

📊 **Status:** {status}

💜 AllAtomic Userbot
        """, parse_mode="md")
    
    await asyncio.sleep(30)
    await event.delete()

# Commands registry
commands = {
    "settings": {"help": "View settings", "usage": ".settings", "category": "core"},
    "set": {"help": "Set variable", "usage": ".set <key> <value>", "category": "core"},
    "get": {"help": "Get variable", "usage": ".get <key>", "category": "core"},
    "reset": {"help": "Reset settings", "usage": ".reset [key]", "category": "core"},
    "pmpermit": {"help": "Toggle PM permit", "usage": ".pmpermit [on/off]", "category": "core"},
    "antispam": {"help": "Toggle anti-spam", "usage": ".antispam [on/off]", "category": "core"},
    "logger": {"help": "Toggle logger", "usage": ".logger [on/off]", "category": "core"}
}
