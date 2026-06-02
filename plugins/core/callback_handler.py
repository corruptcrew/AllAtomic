"""
⚛️  Callback Query Handler for AllAtomic Userbot
HellBot-style inline button callback processor
"""

import asyncio
from telethon import events
from telethon.tl.custom import Button
from plugins import register_handler
from app.utils import get_kaomoji
from app.logger import logger

# Plugin metadata
__plugin__ = {
    "name": "Callback Handler",
    "description": "Handle inline button callbacks for help menu",
    "category": "core"
}

# Command categories (same as help.py)
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

def build_main_keyboard():
    """Build main help keyboard"""
    return [
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

def build_back_keyboard():
    """Build back button keyboard"""
    return [
        [
            Button.inline('◀️ Back', data=b'help_main'),
            Button.inline('🔄 Refresh', data=b'help_refresh'),
        ],
        [
            Button.inline('❌ Close', data=b'help_close'),
        ],
    ]

@register_handler(events.CallbackQuery, data=lambda d: d.startswith(b'help_'))
async def help_callback_handler(event):
    """Handle help menu callback queries - HellBot style"""
    try:
        data = event.data.decode('utf-8')
        action = data.replace('help_', '')
        
        logger.info(f"🔘 Callback received: {action}")
        
        if action == 'main':
            # Show main menu
            await event.edit(
                HELP_MAIN_TEXT.format(kaomoji=get_kaomoji("happy")),
                parse_mode="md",
                buttons=build_main_keyboard()
            )
        
        elif action == 'close':
            # Close the menu
            await event.delete()
        
        elif action == 'refresh':
            # Refresh current view - re-send main menu
            await event.edit(
                HELP_MAIN_TEXT.format(kaomoji=get_kaomoji("happy")),
                parse_mode="md",
                buttons=build_main_keyboard()
            )
        
        elif action == 'all':
            # Show all commands
            all_commands = []
            for cat_info in HELP_CATEGORIES.values():
                for cmd in cat_info["commands"]:
                    all_commands.append(f"`.{cmd}`")
            
            cmds_text = "  " + "  ".join(all_commands)
            
            await event.edit(
                ALL_COMMANDS_TEXT.format(
                    total=len(all_commands),
                    all_commands=cmds_text
                ),
                parse_mode="md",
                buttons=build_back_keyboard()
            )
        
        elif action in HELP_CATEGORIES:
            # Show category help
            cat_info = HELP_CATEGORIES[action]
            commands_list = "\n".join([f"║  • `.{cmd}`" for cmd in cat_info["commands"]])
            
            emoji = cat_info["emoji"]
            name = cat_info["name"].split(' ', 1)[1] if ' ' in cat_info["name"] else cat_info["name"]
            
            await event.edit(
                HELP_CATEGORY_TEXT.format(
                    category_emoji=emoji,
                    category_name=name,
                    commands_list=commands_list
                ),
                parse_mode="md",
                buttons=build_back_keyboard()
            )
        
        # Answer callback query to remove loading state
        await event.answer()
        
    except Exception as e:
        logger.error(f"❌ Callback error: {e}")
        await event.answer(f"❌ Error: {e}", alert=True)

# Commands registry (empty - this is a handler plugin)
commands = {}
