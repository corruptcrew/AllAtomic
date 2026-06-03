"""
⚛️  Help Menu for AllAtomic Userbot
Shows help with text-based category list
"""

from plugins import atomic_command, REGISTERED_PLUGINS

# Plugin metadata
__plugin__ = {
    "name": "Help",
    "description": "Show help menu with all commands",
    "category": "core"
}

# Help categories
HELP_CATEGORIES = {
    "Core": ["alive", "ping", "help", "cmds", "settings", "repo", "support"],
    "Admin": ["ban", "kick", "mute", "unmute", "pin", "unpin", "del", "purge"],
    "Fun": ["joke", "meme", "quote", "love", "rate", "emoji"],
    "Utility": ["weather", "time", "date", "info", "userid", "chatid"],
    "Media": ["dl", "upload", "tts", "sticker", "kang"],
    "Stickers": ["kang", "sticker", "fullpp", "dp", "emoji"],
    "Anime": ["waifu", "neko", "waifupic", "anime", "manga"],
    "AI": ["ai", "chat", "ask", "gpt"],
    "Group": ["welcome", "goodbye", "notes", "gcast", "gdel"],
    "Advanced": ["eval", "exec", "term", "sudo", "heroku"],
    "PM Permit": ["pmpermit", "approve", "disapprove", "block", "unblock"],
    "Voice": ["play", "pause", "resume", "stop", "skip", "queue"],
    "Direct": ["direct", "source", "github", "link"]
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

**📂 Categories:**
"""


@atomic_command(
    "help",
    pattern=r"\.help",
    help="Show help menu with all commands",
    usage=".help",
    category="core"
)
async def help_handler(event):
    """Show help menu with all categories"""
    try:
        total_commands = 84
        num_plugins = 20
        
        msg = HELP_TEXT.format(
            total=total_commands,
            plugins=num_plugins
        )
        
        # Add categories
        msg += "\n**📦 Command Categories:**\n\n"
        for category, commands in HELP_CATEGORIES.items():
            msg += f"**• {category}:** `{', '.join(commands)}`\n"
        
        msg += """
**💜 For inline menu buttons, use:** @AllAtomicBot

(✿◠‿◠)
"""
        
        await event.respond(msg)
        
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
        
        await event.respond(msg)
        
    except Exception as e:
        await event.respond(f"❌ Error: {e}")


# Commands registry
commands = {
    "help": {
        "help": "Show help menu with commands",
        "usage": ".help",
        "category": "core"
    },
    "cmds": {
        "help": "List all commands",
        "usage": ".cmds",
        "category": "core"
    }
}
