"""
⚛️  Help Command for AllAtomic Userbot
Shows all available commands with categories
"""

import asyncio
from plugins import atomic_command
from app.utils import get_kaomoji, THEME

# Plugin metadata
__plugin__ = {
    "name": "Help",
    "description": "Show all available commands",
    "category": "core"
}

# Command categories
COMMAND_CATEGORIES = {
    "core": {
        "name": "⚙️ Core",
        "emoji": "⚙️",
        "commands": ["alive", "status", "ping", "help", "cmds", "repo", "support"]
    },
    "admin": {
        "name": "👥 Admin",
        "emoji": "👥",
        "commands": ["ban", "kick", "mute", "unmute", "purge", "pin", "unpin", "lock", "unlock", "zombies"]
    },
    "fun": {
        "name": "🎮 Fun",
        "emoji": "🎮",
        "commands": ["meme", "joke", "tts", "fact", "quote", "roll", "coin"]
    },
    "utility": {
        "name": "🔧 Utility",
        "emoji": "🔧",
        "commands": ["tr", "weather", "readmore", "glitch", "font", "paste", "gitinfo", "qr", "remind"]
    },
    "media": {
        "name": "📷 Media",
        "emoji": "📷",
        "commands": ["song", "video", "insta", "tiktok", "twitter", "facebook", "media", "yt"]
    },
    "stickers": {
        "name": "🎭 Stickers",
        "emoji": "🎭",
        "commands": ["kang", "sticker", "fullpp", "dp"]
    },
    "anime": {
        "name": "🌸 Anime",
        "emoji": "🌸",
        "commands": ["waifu", "neko", "waifupic", "anime", "manga"]
    },
    "ai": {
        "name": "🤖 AI",
        "emoji": "🤖",
        "commands": ["chat", "ask", "summarize"]
    },
    "group": {
        "name": "📢 Group",
        "emoji": "📢",
        "commands": ["save", "get", "notes", "clear", "filter", "filters", "stop"]
    },
    "advanced": {
        "name": "⚡ Advanced",
        "emoji": "⚡",
        "commands": ["eval", "exec", "term", "sudo", "heroku", "gcast"]
    },
    "pm": {
        "name": "📩 PM Permit",
        "emoji": "📩",
        "commands": ["pmpermit", "approve", "disapprove", "block", "unblock", "logger"]
    },
    "voice": {
        "name": "🎵 Voice Chat",
        "emoji": "🎵",
        "commands": ["vcstart", "vcend", "nowplaying", "lastfm", "play"]
    },
    "direct": {
        "name": "🔗 Direct Links",
        "emoji": "🔗",
        "commands": ["direct", "source"]
    }
}

HELP_TEXT = """
╔═══════════════════════════════════════════════╗
║      ⚛️  **AllAtomic Help Menu**  ⚛️           ║
╠═══════════════════════════════════════════════╣
║                                               ║
║  💜 **Total Commands:** `{total}`             ║
║  📦 **Plugins:** `{plugins}`                  ║
║  🌸 **Theme:** Purple Anime                   ║
║                                               ║
║  **Prefix:** `.` (dot)                        ║
║  **Example:** `.alive`, `.help`               ║
║                                               ║
║  {kaomoji}                                    ║
║                                               ║
║  **Dev:** @GhostMarshal                       ║
║  **Channel:** @ComputeCode                    ║
║  **Repo:** github.com/corruptcrew/AllAtomic   ║
║                                               ║
╚═══════════════════════════════════════════════╝

**📂 Categories:**
{categories}

**💡 Tip:** Use `.help <category>` for specific commands!
"""

CATEGORY_HELP = """
╔═══════════════════════════════════════════════╗
║      📂  **{category_name}**  📂               ║
╠═══════════════════════════════════════════════╣
║                                               ║
{commands}
║                                               ║
╚═══════════════════════════════════════════════╝
"""

@atomic_command(
    "help",
    pattern=r"\.help(?:\s|$)(.*)",
    help="Show help menu",
    usage=".help [category]",
    category="core"
)
async def help_handler(event):
    """Help command handler"""
    from app import client
    
    # Get category if specified
    category = event.pattern_match.group(1).strip().lower() if event.pattern_match.group(1) else None
    
    if category and category in COMMAND_CATEGORIES:
        # Show specific category help
        cat_info = COMMAND_CATEGORIES[category]
        commands_list = "\n".join([f"║  • `.{cmd}`" for cmd in cat_info["commands"]])
        
        help_msg = CATEGORY_HELP.format(
            category_name=cat_info["name"],
            commands=commands_list
        )
        
        await event.respond(help_msg, parse_mode="md")
    else:
        # Show main help menu
        categories_text = ""
        for cat_key, cat_info in COMMAND_CATEGORIES.items():
            cmd_count = len(cat_info["commands"])
            categories_text += f"  {cat_info['emoji']} **{cat_info['name'][4:]}:** `{cmd_count}` commands\n"
        
        help_msg = HELP_TEXT.format(
            total=85,
            plugins=19,
            kaomoji=get_kaomoji("happy"),
            categories=categories_text
        )
        
        await event.respond(help_msg, parse_mode="md")
    
    # Delete command message
    await asyncio.sleep(5)
    await event.delete()

@atomic_command(
    "cmds",
    pattern=r"\.cmds",
    help="List all commands",
    usage=".cmds",
    category="core"
)
async def cmds_handler(event):
    """List all commands"""
    all_commands = []
    for cat_info in COMMAND_CATEGORIES.values():
        all_commands.extend(cat_info["commands"])
    
    cmds_text = "\n".join([f"`.{cmd}`" for cmd in sorted(all_commands)])
    
    msg = f"""
╔═══════════════════════════════════════════════╗
║      📜  **All Commands ({len(all_commands)})**  📜     ║
╠═══════════════════════════════════════════════╣
║                                               ║
{cmds_text}
║                                               ║
╚═══════════════════════════════════════════════╝

**💡 Tip:** Use `.help <category>` for categorized help!
"""
    
    await event.respond(msg, parse_mode="md")
    await asyncio.sleep(10)
    await event.delete()

# Commands registry
commands = {
    "help": {
        "help": "Show help menu with all commands",
        "usage": ".help [category]",
        "category": "core"
    },
    "cmds": {
        "help": "List all commands",
        "usage": ".cmds",
        "category": "core"
    }
}
