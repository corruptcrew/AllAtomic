"""
Bot Helper for Inline Keyboards
HellBot-style menu system
"""

from telethon import TelegramClient
from telethon.tl.custom import InlineButton
from telethon.events import NewMessage

# Bot configuration
BOT_TOKEN = "8367355512:AAELD9UvH1E8IoTWp8EZd2eFzAo3mpZdlpc"

# Create bot client
bot_client = TelegramClient('allatomic_bot', 20828230, 'a8c7e9f5d3b1a2c4e6f8a0b2d4e6f8a0')

async def start_bot():
    """Start the bot client"""
    await bot_client.start(bot_token=BOT_TOKEN)
    return bot_client

def build_help_keyboard():
    """Build HellBot-style inline keyboard for help menu"""
    buttons = [
        [
            InlineButton('⚙️ Core', data=b'help_core'),
            InlineButton('👥 Admin', data=b'help_admin'),
        ],
        [
            InlineButton('🎮 Fun', data=b'help_fun'),
            InlineButton('🔧 Utility', data=b'help_utility'),
        ],
        [
            InlineButton('📷 Media', data=b'help_media'),
            InlineButton('🎭 Stickers', data=b'help_stickers'),
        ],
        [
            InlineButton('🌸 Anime', data=b'help_anime'),
            InlineButton('🤖 AI', data=b'help_ai'),
        ],
        [
            InlineButton('📢 Group', data=b'help_group'),
            InlineButton('⚡ Advanced', data=b'help_advanced'),
        ],
        [
            InlineButton('📩 PM Permit', data=b'help_pm'),
            InlineButton('🎵 Voice', data=b'help_voice'),
        ],
        [
            InlineButton('🔗 Direct', data=b'help_direct'),
            InlineButton('📜 All Commands', data=b'help_all'),
        ],
        [
            InlineButton('🔄 Refresh', data=b'help_refresh'),
            InlineButton('❌ Close', data=b'help_close'),
        ],
    ]
    return buttons

def build_category_keyboard(category, back_data=b'help_main'):
    """Build keyboard for specific category"""
    buttons = [
        [
            InlineButton('◀️ Back', data=back_data),
            InlineButton('🔄 Refresh', data=b'help_refresh'),
        ],
        [
            InlineButton('❌ Close', data=b'help_close'),
        ],
    ]
    return buttons

def build_main_menu_keyboard():
    """Build main menu keyboard (after /start)"""
    buttons = [
        [
            InlineButton('⚛️ Help', data=b'menu_help'),
            InlineButton('📜 Commands', data=b'menu_cmds'),
        ],
        [
            InlineButton('👤 About', data=b'menu_about'),
            InlineButton('🔗 Repo', data=b'menu_repo'),
        ],
    ]
    return buttons

# Command categories with descriptions
HELP_CATEGORIES = {
    'core': {
        'name': '⚙️ Core Commands',
        'description': 'Essential bot commands',
        'commands': [
            ('.alive', 'Check if bot is online'),
            ('.status', 'Quick bot status'),
            ('.ping', 'Check bot latency'),
            ('.help', 'Show help menu'),
            ('.cmds', 'List all commands'),
            ('.repo', 'Bot repository link'),
            ('.support', 'Support group link'),
        ]
    },
    'admin': {
        'name': '👥 Admin Commands',
        'description': 'Group administration tools',
        'commands': [
            ('.ban', 'Ban a user'),
            ('.kick', 'Kick a user'),
            ('.mute', 'Mute a user'),
            ('.unmute', 'Unmute a user'),
            ('.purge', 'Delete messages'),
            ('.pin', 'Pin a message'),
            ('.unpin', 'Unpin a message'),
            ('.lock', 'Lock chat permissions'),
            ('.unlock', 'Unlock chat permissions'),
            ('.zombies', 'Remove deleted accounts'),
        ]
    },
    'fun': {
        'name': '🎮 Fun Commands',
        'description': 'Entertainment and games',
        'commands': [
            ('.meme', 'Get random meme'),
            ('.joke', 'Get random joke'),
            ('.tts', 'Text to speech'),
            ('.fact', 'Random fact'),
            ('.quote', 'Generate quote'),
            ('.roll', 'Roll dice'),
            ('.coin', 'Flip coin'),
        ]
    },
    'utility': {
        'name': '🔧 Utility Commands',
        'description': 'Useful tools',
        'commands': [
            ('.tr', 'Translate text'),
            ('.weather', 'Get weather info'),
            ('.readmore', 'Add read more'),
            ('.glitch', 'Glitch text effect'),
            ('.font', 'Change font style'),
            ('.paste', 'Paste to nekobin'),
            ('.gitinfo', 'GitHub user info'),
            ('.qr', 'Generate QR code'),
            ('.remind', 'Set reminder'),
        ]
    },
    'media': {
        'name': '📷 Media Commands',
        'description': 'Download from social media',
        'commands': [
            ('.song', 'Download YouTube song'),
            ('.video', 'Download YouTube video'),
            ('.insta', 'Download Instagram media'),
            ('.tiktok', 'Download TikTok video'),
            ('.twitter', 'Download Twitter video'),
            ('.facebook', 'Download Facebook video'),
            ('.media', 'General media downloader'),
            ('.yt', 'YouTube search'),
        ]
    },
    'stickers': {
        'name': '🎭 Sticker Commands',
        'description': 'Sticker and profile tools',
        'commands': [
            ('.kang', 'Steal/create sticker'),
            ('.sticker', 'Convert to sticker'),
            ('.fullpp', 'Get full profile pic'),
            ('.dp', 'Set display picture'),
        ]
    },
    'anime': {
        'name': '🌸 Anime Commands',
        'description': 'Anime-related commands',
        'commands': [
            ('.waifu', 'Get random waifu'),
            ('.neko', 'Get random neko'),
            ('.waifupic', 'Waifu image'),
            ('.anime', 'Search anime'),
            ('.manga', 'Search manga'),
        ]
    },
    'ai': {
        'name': '🤖 AI Commands',
        'description': 'AI-powered features',
        'commands': [
            ('.chat', 'AI chatbot'),
            ('.ask', 'Ask AI question'),
            ('.summarize', 'Summarize text'),
        ]
    },
    'group': {
        'name': '📢 Group Commands',
        'description': 'Notes and filters',
        'commands': [
            ('.save', 'Save a note'),
            ('.get', 'Get saved note'),
            ('.notes', 'List all notes'),
            ('.clear', 'Delete note'),
            ('.filter', 'Add filter'),
            ('.filters', 'List filters'),
            ('.stop', 'Remove filter'),
        ]
    },
    'advanced': {
        'name': '⚡ Advanced Commands',
        'description': 'Power user features',
        'commands': [
            ('.eval', 'Execute Python code'),
            ('.exec', 'Execute shell command'),
            ('.term', 'Terminal access'),
            ('.sudo', 'Sudo commands'),
            ('.heroku', 'Heroku management'),
            ('.gcast', 'Global broadcast'),
        ]
    },
    'pm': {
        'name': '📩 PM Permit Commands',
        'description': 'PM security features',
        'commands': [
            ('.pmpermit', 'PM permit settings'),
            ('.approve', 'Approve user'),
            ('.disapprove', 'Disapprove user'),
            ('.block', 'Block user'),
            ('.unblock', 'Unblock user'),
            ('.logger', 'Message logger'),
        ]
    },
    'voice': {
        'name': '🎵 Voice Chat Commands',
        'description': 'Voice chat features',
        'commands': [
            ('.vcstart', 'Start voice chat'),
            ('.vcend', 'End voice chat'),
            ('.nowplaying', 'Show current song'),
            ('.lastfm', 'Last.fm integration'),
            ('.play', 'Play song in VC'),
        ]
    },
    'direct': {
        'name': '🔗 Direct Link Commands',
        'description': 'Direct download links',
        'commands': [
            ('.direct', 'Generate direct link'),
            ('.source', 'Get message source'),
        ]
    },
}

__all__ = [
    'BOT_TOKEN',
    'bot_client',
    'start_bot',
    'build_help_keyboard',
    'build_category_keyboard',
    'build_main_menu_keyboard',
    'HELP_CATEGORIES',
]
