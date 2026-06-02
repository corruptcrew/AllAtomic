"""
⚛️  Help Command for AllAtomic Userbot
HellBot-style inline menu system
"""

import asyncio
from plugins import atomic_command
from app.utils import get_kaomoji, THEME
from app.bot_helper import HELP_CATEGORIES, build_help_keyboard, build_category_keyboard

# Plugin metadata
__plugin__ = {
    "name": "Help",
    "description": "Show all available commands with HellBot-style menu",
    "category": "core"
}

HELP_MAIN_TEXT = """
╔═══════════════════════════════════════════════╗
║      ⚛️  **AllAtomic Help Menu**  ⚛️           ║
╠═══════════════════════════════════════════════╣
║                                               ║
║  💜 **Total Commands:** `83`                  ║
║  📦 **Plugins:** `19`                         ║
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

**📂 Select a category below:**
"""

HELP_CATEGORY_TEXT = """
╔═══════════════════════════════════════════════╗
║      {category_emoji}  **{category_name}**  {category_emoji}       ║
╠═══════════════════════════════════════════════╣
║  📝 {description}                             ║
╠═══════════════════════════════════════════════╣
║                                               ║
{commands_list}
║                                               ║
╚═══════════════════════════════════════════════╝

**💡 Usage:** `.{command}` [arguments]
"""

ALL_COMMANDS_TEXT = """
╔═══════════════════════════════════════════════╗
║      📜  **All Commands ({total})**  📜          ║
╠═══════════════════════════════════════════════╣
║                                               ║
{all_commands}
║                                               ║
╚═══════════════════════════════════════════════╝

**💡 Tip:** Use the buttons below for categorized help!
"""

ABOUT_TEXT = """
╔═══════════════════════════════════════════════╗
║      ⚛️  **About AllAtomic**  ⚛️               ║
╠═══════════════════════════════════════════════╣
║                                               ║
║  **Name:** AllAtomic Userbot                  ║
║  **Version:** 1.0.0                           ║
║  **Theme:** Purple Anime 💜                   ║
║                                               ║
║  **Base:** Telethon (Python 3.12)             ║
║  **Style:** HellBot Inspired                  ║
║                                               ║
║  ────────────────────────────────────────     ║
║                                               ║
║  **Developer:** @GhostMarshal                 ║
║  **Channel:** @ComputeCode                    ║
║  **Support:** @ComputeCode                    ║
║                                               ║
║  **Repository:**                              ║
║  github.com/corruptcrew/AllAtomic             ║
║                                               ║
║  {kaomoji}                                    ║
║                                               ║
╚═══════════════════════════════════════════════╝
"""

@atomic_command(
    "help",
    pattern=r"\.help(?:\s|$)(.*)",
    help="Show help menu with inline buttons",
    usage=".help",
    category="core"
)
async def help_handler(event):
    """Help command handler with inline keyboard"""
    try:
        kaomoji = get_kaomoji("happy")
        
        help_msg = HELP_MAIN_TEXT.format(kaomoji=kaomoji)
        
        # Send with inline keyboard
        await event.respond(
            help_msg,
            parse_mode="md",
            buttons=build_help_keyboard()
        )
        
        # Delete command message
        await asyncio.sleep(5)
        await event.delete()
        
    except Exception as e:
        await event.respond(f"❌ Error: {e}")
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
    try:
        all_commands = []
        for cat_info in HELP_CATEGORIES.values():
            for cmd, desc in cat_info["commands"]:
                all_commands.append(f"`{cmd}` - {desc}")
        
        cmds_text = "\n".join(all_commands)
        
        msg = ALL_COMMANDS_TEXT.format(
            total=len(all_commands),
            all_commands=cmds_text
        )
        
        await event.respond(msg, parse_mode="md")
        await asyncio.sleep(10)
        await event.delete()
        
    except Exception as e:
        await event.respond(f"❌ Error: {e}")
        await asyncio.sleep(5)
        await event.delete()

# Commands registry
commands = {
    "help": {
        "help": "Show help menu with inline buttons",
        "usage": ".help",
        "category": "core"
    },
    "cmds": {
        "help": "List all commands",
        "usage": ".cmds",
        "category": "core"
    }
}
