"""
⚛️  Help Command for AllAtomic Userbot
HellBot-style inline menu system using main bot
"""

import asyncio
from telethon.tl.custom import Button
from plugins import atomic_command
from app.utils import get_kaomoji, THEME

# Plugin metadata
__plugin__ = {
    "name": "Help",
    "description": "Show all available commands with HellBot-style menu",
    "category": "core"
}

# Command categories
HELP_CATEGORIES = {
    'core': {
        'name': '⚙️ Core',
        'emoji': '⚙️',
        'commands': ['alive', 'status', 'ping', 'help', 'cmds', 'repo', 'support']
    },
    'admin': {
        'name': '👥 Admin',
        'emoji': '👥',
        'commands': ['ban', 'kick', 'mute', 'unmute', 'purge', 'pin', 'unpin', 'lock', 'unlock', 'zombies']
    },
    'fun': {
        'name': '🎮 Fun',
        'emoji': '🎮',
        'commands': ['meme', 'joke', 'tts', 'fact', 'quote', 'roll', 'coin']
    },
    'utility': {
        'name': '🔧 Utility',
        'emoji': '🔧',
        'commands': ['tr', 'weather', 'readmore', 'glitch', 'font', 'paste', 'gitinfo', 'qr', 'remind']
    },
    'media': {
        'name': '📷 Media',
        'emoji': '📷',
        'commands': ['song', 'video', 'insta', 'tiktok', 'twitter', 'facebook', 'media', 'yt']
    },
    'stickers': {
        'name': '🎭 Stickers',
        'emoji': '🎭',
        'commands': ['kang', 'sticker', 'fullpp', 'dp']
    },
    'anime': {
        'name': '🌸 Anime',
        'emoji': '🌸',
        'commands': ['waifu', 'neko', 'waifupic', 'anime', 'manga']
    },
    'ai': {
        'name': '🤖 AI',
        'emoji': '🤖',
        'commands': ['chat', 'ask', 'summarize']
    },
    'group': {
        'name': '📢 Group',
        'emoji': '📢',
        'commands': ['save', 'get', 'notes', 'clear', 'filter', 'filters', 'stop']
    },
    'advanced': {
        'name': '⚡ Advanced',
        'emoji': '⚡',
        'commands': ['eval', 'exec', 'term', 'sudo', 'heroku', 'gcast']
    },
    'pm': {
        'name': '📩 PM Permit',
        'emoji': '📩',
        'commands': ['pmpermit', 'approve', 'disapprove', 'block', 'unblock', 'logger']
    },
    'voice': {
        'name': '🎵 Voice',
        'emoji': '🎵',
        'commands': ['vcstart', 'vcend', 'nowplaying', 'lastfm', 'play']
    },
    'direct': {
        'name': '🔗 Direct',
        'emoji': '🔗',
        'commands': ['direct', 'source']
    }
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
║                                               ║
╚═══════════════════════════════════════════════╝

**📂 Select a category below:**
"""

HELP_CATEGORY_TEXT = """
╔═══════════════════════════════════════════════╗
║      {category_emoji}  **{category_name}**  {category_emoji}       ║
╠═══════════════════════════════════════════════╣
║                                               ║
{commands_list}
║                                               ║
╚═══════════════════════════════════════════════╝

**💡 Usage:** `.{command}`
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

@atomic_command(
    "help",
    pattern=r"\.help(?:\s|$)(.*)",
    help="Show help menu with inline buttons",
    usage=".help [category]",
    category="core"
)
async def help_handler(event):
    """Help command handler with inline keyboard"""
    try:
        from app import client
        
        # Get category if specified
        category = event.pattern_match.group(1).strip().lower() if event.pattern_match.group(1) else None
        
        if category and category in HELP_CATEGORIES:
            # Show specific category
            cat_info = HELP_CATEGORIES[category]
            commands_list = "\n".join([f"║  • `.{cmd}`" for cmd in cat_info["commands"]])
            
            emoji = cat_info["emoji"]
            name = cat_info["name"].split(' ', 1)[1] if ' ' in cat_info["name"] else cat_info["name"]
            
            msg = HELP_CATEGORY_TEXT.format(
                category_emoji=emoji,
                category_name=name,
                commands_list=commands_list
            )
            
            buttons = [
                [
                    Button.inline('◀️ Back', data=b'help_main'),
                    Button.inline('🔄 Refresh', data=b'help_refresh'),
                ],
                [
                    Button.inline('❌ Close', data=b'help_close'),
                ],
            ]
            
            await event.respond(msg, parse_mode="md", buttons=buttons)
        else:
            # Show main help menu
            categories_text = ""
            for cat_key, cat_info in HELP_CATEGORIES.items():
                cmd_count = len(cat_info["commands"])
                categories_text += f"  {cat_info['emoji']} **{cat_info['name'][4:]}:** `{cmd_count}` commands\n"
            
            help_msg = HELP_MAIN_TEXT.format(kaomoji=get_kaomoji("happy"))
            
            buttons = [
                [
                    Button.inline('⚙️ Core', data=b'help_core'),
                    Button.inline('👥 Admin', data=b'help_admin'),
                ],
                [
                    Button.inline('🎮 Fun', data=b'help_fun'),
                    Button.inline('🔧 Utility', data=b'help_utility'),
                ],
                [
                    Button.inline('📷 Media', data=b'help_media'),
                    Button.inline('🎭 Stickers', data=b'help_stickers'),
                ],
                [
                    Button.inline('🌸 Anime', data=b'help_anime'),
                    Button.inline('🤖 AI', data=b'help_ai'),
                ],
                [
                    Button.inline('📢 Group', data=b'help_group'),
                    Button.inline('⚡ Advanced', data=b'help_advanced'),
                ],
                [
                    Button.inline('📩 PM Permit', data=b'help_pm'),
                    Button.inline('🎵 Voice', data=b'help_voice'),
                ],
                [
                    Button.inline('🔗 Direct', data=b'help_direct'),
                    Button.inline('📜 All Commands', data=b'help_all'),
                ],
                [
                    Button.inline('🔄 Refresh', data=b'help_refresh'),
                    Button.inline('❌ Close', data=b'help_close'),
                ],
            ]
            
            await event.respond(help_msg, parse_mode="md", buttons=buttons)
        
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
            for cmd in cat_info["commands"]:
                all_commands.append(f"`.{cmd}`")
        
        cmds_text = "  " + "  ".join(all_commands)
        
        msg = ALL_COMMANDS_TEXT.format(
            total=len(all_commands),
            all_commands=cmds_text
        )
        
        buttons = [
            [
                Button.inline('◀️ Back', data=b'help_main'),
                Button.inline('🔄 Refresh', data=b'help_refresh'),
            ],
            [
                Button.inline('❌ Close', data=b'help_close'),
            ],
        ]
        
        await event.respond(msg, parse_mode="md", buttons=buttons)
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
        "usage": ".help [category]",
        "category": "core"
    },
    "cmds": {
        "help": "List all commands",
        "usage": ".cmds",
        "category": "core"
    }
}
