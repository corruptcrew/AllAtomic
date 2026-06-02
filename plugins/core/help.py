"""
⚛️  Help Command for AllAtomic Userbot
Triggers @AllAtomicBot for inline menu display
"""

import asyncio
from telethon.tl.custom import Button
from plugins import atomic_command
from app.utils import get_kaomoji, THEME

# Plugin metadata
__plugin__ = {
    "name": "Help",
    "description": "Show help menu - uses @AllAtomicBot for inline buttons",
    "category": "core"
}

# Bot username for inline menu
BOT_USERNAME = "@AllAtomicBot"

# Help menu text
HELP_MENU_TEXT = """
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

**🤖 For inline button menu, use:**
👉 `{bot}` in any chat!

**Or click the button below:**
"""

@atomic_command(
    "help",
    pattern=r"\.help",
    help="Show help menu with @AllAtomicBot inline buttons",
    usage=".help",
    category="core"
)
async def help_handler(event):
    """Show help menu with button to open @AllAtomicBot"""
    try:
        # Get total stats
        total_commands = 84
        num_plugins = 20
        
        # Build message
        msg = HELP_MENU_TEXT.format(
            total=total_commands,
            plugins=num_plugins,
            bot=BOT_USERNAME
        )
        
        # Build inline buttons - link to bot
        buttons = [
            [
                Button.url(
                    '📂 Open Help Menu',
                    f'https://t.me/{BOT_USERNAME}?start=help'
                )
            ],
            [
                Button.url('👥 Support', 'https://t.me/ComputeCode'),
                Button.url('📦 GitHub', 'https://github.com/corruptcrew/AllAtomic'),
            ],
        ]
        
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
    """List all commands with bot reference"""
    try:
        msg = f"""
╔═══════════════════════════════════════════════╗
║      📜  All Commands (84)  📜                 ║
╠═══════════════════════════════════════════════╣
║                                               ║
║  **For categorized menu use:**                ║
║  👉 {BOT_USERNAME}                            ║
║                                               ║
║  **Quick commands:**                          ║
║  `.alive` `.ping` `.help` `.status`           ║
║  `.repo` `.support` `.gcast` `.sudo`          ║
║                                               ║
╚═══════════════════════════════════════════════╝
"""
        
        buttons = [
            [
                Button.url(
                    '📂 Browse Commands',
                    f'https://t.me/{BOT_USERNAME}?start=cmds'
                )
            ],
        ]
        
        await event.respond(msg, parse_mode="md", buttons=buttons)
        
    except Exception as e:
        await event.respond(f"❌ Error: {e}")

# Commands registry
commands = {
    "help": {
        "help": "Show help menu with @AllAtomicBot",
        "usage": ".help",
        "category": "core"
    },
    "cmds": {
        "help": "List all commands",
        "usage": ".cmds",
        "category": "core"
    }
}
