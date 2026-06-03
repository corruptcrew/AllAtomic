"""
⚛️  HellBot-Style Help Menu for AllAtomic Userbot
Uses BOT_TOKEN to send inline keyboard messages (HellBot method)
"""

import asyncio
from telethon import TelegramClient
from telethon.tl.custom import Button
from telethon.tl.types import InlineKeyboardMarkup
from plugins import atomic_command, REGISTERED_PLUGINS
from app.config import Config
from app.logger import log

# Plugin metadata
__plugin__ = {
    "name": "Help",
    "description": "HellBot-style help menu with inline category buttons",
    "category": "core"
}

# Bot username for inline menu
BOT_USERNAME = "@AllAtomicBot"

# Help categories (HellBot style)
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

**📂 Select a category below:**
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
            f"⚙️ {cat1_name}",
            data=f"help_cat_{cat1_name}"
        ))
        
        if i + 1 < len(category_items):
            cat2_name, cat2_data = category_items[i + 1]
            row.append(Button.inline(
                f"📦 {cat2_name}",
                data=f"help_cat_{cat2_name}"
            ))
        
        buttons.append(row)
    
    # Add navigation buttons
    buttons.append([
        Button.url("👥 Support", "https://t.me/ComputeCode"),
        Button.url("📦 GitHub", "https://github.com/corruptcrew/AllAtomic"),
    ])
    
    return buttons


async def send_help_with_bot(event, config):
    """Send help message using bot client (HellBot method)"""
    try:
        # Get bot token from config
        bot_token = config.BOT_TOKEN
        
        if not bot_token:
            # Fallback: send text-only message
            await event.respond("❌ BOT_TOKEN not configured. Please add BOT_TOKEN to .env file.")
            return
        
        # Create bot client using the same API credentials
        bot_client = TelegramClient(
            'allatomic_help_bot',
            config.APP_ID,
            config.API_HASH,
            session='allatomic_help_bot.session'
        )
        
        # Start bot client
        await bot_client.start(bot_token=bot_token)
        
        # Build message
        total_commands = 84
        num_plugins = 20
        
        msg = HELP_TEXT.format(
            total=total_commands,
            plugins=num_plugins
        )
        
        # Build inline keyboard
        buttons = build_category_buttons()
        
        # Send message with inline keyboard (via bot, not userbot!)
        sent_msg = await bot_client.send_message(
            event.chat_id,
            msg,
            buttons=buttons,
            parse_mode='md'
        )
        
        # Log the action
        log.info(f"Help message sent via bot to chat {event.chat_id}")
        
        # Close bot client
        await bot_client.disconnect()
        
    except Exception as e:
        log.error(f"Error sending help via bot: {e}")
        # Fallback: send text-only message
        await event.respond(f"❌ Error: {e}")


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
        from app.client import client
        
        # Get config
        config = client.config
        
        # Send help using bot client (HellBot method)
        await send_help_with_bot(event, config)
        
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
        from app.client import client
        config = client.config
        
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
        
        # Send using bot client
        await send_help_with_bot(event, config)
        
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
