"""
⚛️  HellBot-Style Help Menu for AllAtomic Userbot
Replicates HellBot's inline keyboard help system with categories
"""

import asyncio
from telethon.tl.custom import Button
from telethon.tl.types import InlineKeyboardMarkup, InlineKeyboardButton
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


def build_inline_keyboard():
    """Build inline keyboard using Telethon's InlineKeyboardMarkup"""
    keyboard = []
    category_items = list(HELP_CATEGORIES.items())
    
    # Create rows of 2 buttons each (HellBot style)
    for i in range(0, len(category_items), 2):
        row = []
        cat1_name, cat1_data = category_items[i]
        emoji = cat1_data.get("emoji", "📦") if isinstance(cat1_data, dict) else "📦"
        row.append(InlineKeyboardButton(
            text=f"{emoji} {cat1_name}",
            callback_data=f"help_cat_{cat1_name}"
        ))
        
        if i + 1 < len(category_items):
            cat2_name, cat2_data = category_items[i + 1]
            emoji = cat2_data.get("emoji", "📦") if isinstance(cat2_data, dict) else "📦"
            row.append(InlineKeyboardButton(
                text=f"{emoji} {cat2_name}",
                callback_data=f"help_cat_{cat2_name}"
            ))
        
        keyboard.append(row)
    
    # Add navigation buttons
    keyboard.append([
        InlineKeyboardButton(text="👥 Support", url="https://t.me/ComputeCode"),
        InlineKeyboardButton(text="📦 GitHub", url="https://github.com/corruptcrew/AllAtomic"),
    ])
    
    return InlineKeyboardMarkup(keyboard)


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
        # Get total stats - safely handle REGISTERED_PLUGINS
        if REGISTERED_PLUGINS and isinstance(REGISTERED_PLUGINS, list):
            # Count commands safely
            total_commands = len(REGISTERED_PLUGINS)
            # Count unique categories safely
            categories = set()
            for cmd in REGISTERED_PLUGINS:
                if isinstance(cmd, dict):
                    categories.add(cmd.get("category", "core"))
                else:
                    categories.add("core")
            num_plugins = len(categories) or 20
        else:
            total_commands = 84
            num_plugins = 20
        
        # Build message
        msg = HELP_TEXT.format(
            total=total_commands,
            plugins=num_plugins
        )
        
        # Build inline keyboard
        keyboard = build_inline_keyboard()
        
        # Send message with inline keyboard using reply_markup
        await event.respond(msg, parse_mode="md", reply_markup=keyboard)
        
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
        
        keyboard = build_inline_keyboard()
        
        await event.respond(msg, parse_mode="md", reply_markup=keyboard)
        
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
