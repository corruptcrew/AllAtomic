"""
⚛️  Help Command for AllAtomic Userbot
HellBot-style inline menu system
"""

import asyncio
from telethon.tl.custom import Button
from plugins import atomic_command
from app.utils import get_kaomoji, THEME

# Plugin metadata
__plugin__ = {
    "name": "Help",
    "description": "Show all available commands with inline buttons",
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

**📂 Select a category below:**
"""

ALL_COMMANDS_TEXT = """
╔═══════════════════════════════════════════════╗
║      📜  All Commands ({total})  📜             ║
╠═══════════════════════════════════════════════╣
║                                               ║
║  {all_commands}                               ║
║                                               ║
╚═══════════════════════════════════════════════╝

**💡 Tip:** Use buttons below for categories!
"""

@atomic_command(
    "help",
    pattern=r"\.help",
    help="Show help menu with inline buttons",
    usage=".help [category]",
    category="core"
)
async def help_handler(event):
    """Show help menu with inline buttons"""
    try:
        # Get total stats
        total_commands = sum(len(cat["commands"]) for cat in HELP_CATEGORIES.values())
        num_plugins = len(HELP_CATEGORIES)
        
        # Get category if specified
        category = None
        if len(event.text.split()) > 1:
            category = event.text.split()[1].lower()
        
        if category and category in HELP_CATEGORIES:
            # Show specific category
            cat = HELP_CATEGORIES[category]
            cmds_list = '\n'.join([f"║  • `.{cmd}`" for cmd in cat['commands']])
            
            msg = f"""
╔═══════════════════════════════════════════════╗
║      {cat['name']}      ║
╠═══════════════════════════════════════════════╣
║                                               ║
{cmds_list}
║                                               ║
╚═══════════════════════════════════════════════╝

**💡 Usage:** `.{cat['commands'][0]}`
"""
        else:
            # Show main help menu
            msg = HELP_MENU_TEXT.format(
                total=total_commands,
                plugins=num_plugins
            )
        
        # Build inline buttons
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
        
        # Send message with inline buttons
        await event.respond(msg, parse_mode="md", buttons=buttons)
        
    except Exception as e:
        await event.respond(f"❌ Error: {e}")

# Commands registry
commands = {
    "help": {
        "help": "Show help menu with inline buttons",
        "usage": ".help [category]",
        "category": "core"
    }
}
