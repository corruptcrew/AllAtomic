"""
⚛️  Help Menu for AllAtomic Userbot
Shows text-based help + directs to @AllAtomicBot for inline menu
"""

from plugins import atomic_command, REGISTERED_PLUGINS

# Plugin metadata
__plugin__ = {
    "name": "Help",
    "description": "Show help menu - use @AllAtomicBot for inline buttons",
    "category": "core"
}

# Bot username for inline menu
BOT_USERNAME = "@AllAtomicBot"

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

**🤖 For INLINE BUTTON menu, use:**
👉 `{bot}` in any chat!

**📂 Command Categories:**
"""


def build_category_list():
    """Build text-based category list"""
    result = ""
    for category, commands in HELP_CATEGORIES.items():
        emoji = {
            "Core": "⚙️", "Admin": "👥", "Fun": "🎮", "Utility": "🔧",
            "Media": "📷", "Stickers": "🎭", "Anime": "🌸", "AI": "🤖",
            "Group": "📢", "Advanced": "⚡", "PM Permit": "📩",
            "Voice": "🎵", "Direct": "🔗"
        }.get(category, "📦")
        result += f"\n{emoji} **{category}:** `.{commands[0]}`, `.{commands[1]}`...\n"
    return result


@atomic_command(
    "help",
    pattern=r"\.help",
    help="Show help menu with category list",
    usage=".help",
    category="core"
)
async def help_handler(event):
    """Show help menu with category list"""
    try:
        # Get total stats
        total_commands = 84
        num_plugins = 20
        
        # Build message
        msg = HELP_TEXT.format(
            total=total_commands,
            plugins=num_plugins,
            bot=BOT_USERNAME
        )
        msg += build_category_list()
        msg += f"\n**💡 Tip:** Search `{BOT_USERNAME}` and send `/start` for clickable buttons!"
        
        # Send message (no buttons - userbots can't send inline keyboards)
        await event.respond(msg, parse_mode="md")
        
    except Exception as e:
        await event.respond(f"❌ Error: {e}")


@atomic_command(
    "cmds",
    pattern=r"\.cmds",
    help="List all commands by category",
    usage=".cmds",
    category="core"
)
async def cmds_handler(event):
    """List all commands by category"""
    try:
        msg = """
╔═══════════════════════════════════════════════╗
║      📜  All Commands  📜                      ║
╠═══════════════════════════════════════════════╣
║                                               ║
║  **For INLINE BUTTON menu use:**              ║
║  👉 @AllAtomicBot                             ║
║                                               ║
"""
        msg += build_category_list()
        msg += "\n**💡 Search @AllAtomicBot for clickable menu!**"
        
        await event.respond(msg, parse_mode="md")
        
    except Exception as e:
        await event.respond(f"❌ Error: {e}")


# Commands registry
commands = {
    "help": {
        "help": "Show help menu with category list",
        "usage": ".help",
        "category": "core"
    },
    "cmds": {
        "help": "List all commands by category",
        "usage": ".cmds",
        "category": "core"
    }
}
