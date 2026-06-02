"""
⚛️  HellBot-Style Help Menu for AllAtomic Userbot
Replicates HellBot's inline keyboard help system with categories
"""

import asyncio
from telethon.tl.custom import Button
from plugins import atomic_command, REGISTERED_PLUGINS
from app.utils import get_kaomoji, THEME

# Plugin metadata
__plugin__ = {
    "name": "Help",
    "description": "HellBot-style help menu with inline category buttons",
    "category": "core"
}

# Bot username for inline mode
BOT_USERNAME = "@AllAtomicBot"

# Help categories (HellBot style)
HELP_CATEGORIES = {
    "Core": {
        "emoji": "⚙️",
        "commands": ["alive", "ping", "help", "cmds", "settings", "repo", "support"]
    },
    "Admin": {
        "emoji": "👥",
        "commands": ["ban", "kick", "mute", "unmute", "pin", "unpin", "del", "purge"]
    },
    "Fun": {
        "emoji": "🎮",
        "commands": ["joke", "meme", "quote", "love", "rate", "emoji"]
    },
    "Utility": {
        "emoji": "🔧",
        "commands": ["weather", "time", "date", "info", "userid", "chatid"]
    },
    "Media": {
        "emoji": "📷",
        "commands": ["dl", "upload", "tts", "sticker", "kang"]
    },
    "Stickers": {
        "emoji": "🎭",
        "commands": ["kang", "sticker", "fullpp", "dp", "emoji"]
    },
    "Anime": {
        "emoji": "🌸",
        "commands": ["waifu", "neko", "waifupic", "anime", "manga"]
    },
    "AI": {
        "emoji": "🤖",
        "commands": ["ai", "chat", "ask", "gpt"]
    },
    "Group": {
        "emoji": "📢",
        "commands": ["welcome", "goodbye", "notes", "gcast", "gdel"]
    },
    "Advanced": {
        "emoji": "⚡",
        "commands": ["eval", "exec", "term", "sudo", "heroku"]
    },
    "PM Permit": {
        "emoji": "📩",
        "commands": ["pmpermit", "approve", "disapprove", "block", "unblock"]
    },
    "Voice": {
        "emoji": "🎵",
        "commands": ["play", "pause", "resume", "stop", "skip", "queue"]
    },
    "Direct": {
        "emoji": "🔗",
        "commands": ["direct", "source", "github", "link"]
    }
}

# Main help menu text
HELP_TEXT = """
╔═══════════════════════════════════════════════╗
║      ⚛️  AllAtomic Help Menu  ⚛️               ║
╠═══════════════════════════════════════════════╣
║                                               ║
║  💜 **Total Commands:** `{total}`               ║
║  📦 **Plugins:** `{plugins}`                    ║
║  🌸 **Theme:** Purple Anime                   ║
║                                               ║
║  **Prefix:** `.` (dot)                        ║
║  **Example:** `.alive`, `.help`               ║
║                                               ║
║  (૮๑•̀ㅁ•́ฅა)                                   ║
║                                               ║
║  **Dev:** @GhostMarshal                       ║
║  **Channel:** @ComputeCode                    ║
║                                               ║
╚═══════════════════════════════════════════════╝

**📂 Select a category below:**
"""

# Category help text template
CATEGORY_HELP_TEXT = """
╔═══════════════════════════════════════════════╗
║  {emoji}  {category} Commands  {emoji}            ║
╠═══════════════════════════════════════════════╣
║                                               ║
{commands}
║                                               ║
╚═══════════════════════════════════════════════╝

**📂 Select another category:**
"""


def build_category_buttons():
    """Build inline keyboard buttons for all categories (HellBot style)"""
    buttons = []
    category_items = list(HELP_CATEGORIES.items())
    
    # Create rows of 2 buttons each (HellBot style)
    for i in range(0, len(category_items), 2):
        row = []
        cat1_name, cat1_data = category_items[i]
        row.append(Button.inline(
            f"{cat1_data['emoji']} {cat1_name}",
            data=f"help_cat_{cat1_name}"
        ))
        
        if i + 1 < len(category_items):
            cat2_name, cat2_data = category_items[i + 1]
            row.append(Button.inline(
                f"{cat2_data['emoji']} {cat2_name}",
                data=f"help_cat_{cat2_name}"
            ))
        
        buttons.append(row)
    
    # Add navigation buttons
    buttons.append([
        Button.url("👥 Support", "https://t.me/ComputeCode"),
        Button.url("📦 GitHub", "https://github.com/corruptcrew/AllAtomic"),
    ])
    
    return buttons


def build_category_view_buttons(category_name):
    """Build buttons for category view with back button"""
    buttons = []
    
    # Back button
    buttons.append([Button.inline("◀️ Back", data="help_back")])
    
    # Close button
    buttons.append([Button.inline("❌ Close", data="help_close")])
    
    return buttons


def format_category_commands(category_name):
    """Format commands list for a category"""
    cat_data = HELP_CATEGORIES.get(category_name, {})
    commands = cat_data.get("commands", [])
    
    # Format each command
    cmd_list = ""
    for cmd in commands:
        cmd_list += f"║  •  `.{cmd}`\n"
    
    return cmd_list


@atomic_command(
    "help",
    pattern=r"\.help",
    help="Show help menu with inline category buttons (HellBot style)",
    usage=".help",
    category="core"
)
async def help_handler(event):
    """Show HellBot-style help menu with inline category buttons"""
    try:
        # Get total stats
        total_commands = len(REGISTERED_PLUGINS) if REGISTERED_PLUGINS else 84
        num_plugins = len(set(cmd.get("category", "core") for cmd in (REGISTERED_PLUGINS or []))) or 20
        
        # Build message
        msg = HELP_TEXT.format(
            total=total_commands,
            plugins=num_plugins
        )
        
        # Build inline keyboard (HellBot style)
        buttons = build_category_buttons()
        
        # Send message with inline buttons
        await event.respond(msg, parse_mode="md", buttons=buttons)
        
    except Exception as e:
        await event.respond(f"❌ Error: {e}")


@atomic_command(
    "cmds",
    pattern=r"\.cmds",
    help="List all commands",
    usage=".cmds",
    category="core"
)
async def cmds_handler(event):
    """List all commands"""
    try:
        msg = """
╔═══════════════════════════════════════════════╗
║      📜  All Commands  📜                      ║
╠═══════════════════════════════════════════════╣
║                                               ║
║  **Use .help for categorized menu**           ║
║                                               ║
║  **Quick commands:**                          ║
║  `.alive` `.ping` `.help` `.settings`         ║
║  `.repo` `.support` `.gcast` `.sudo`          ║
║                                               ║
╚═══════════════════════════════════════════════╝
"""
        
        buttons = [
            [Button.inline("📂 Open Help Menu", data="help_back")],
        ]
        
        await event.respond(msg, parse_mode="md", buttons=buttons)
        
    except Exception as e:
        await event.respond(f"❌ Error: {e}")


# Commands registry
commands = {
    "help": {
        "help": "Show HellBot-style help menu with inline buttons",
        "usage": ".help",
        "category": "core"
    },
    "cmds": {
        "help": "List all commands",
        "usage": ".cmds",
        "category": "core"
    }
}
