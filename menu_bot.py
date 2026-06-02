#!/usr/bin/env python3
"""
AllAtomic Bot - HellBot Style Inline Menu
Separate bot for inline keyboard help menu
"""

import asyncio
import logging
from telethon import TelegramClient, events
from telethon.tl.custom import Button

# Configuration - Using same API credentials as userbot
API_ID = 38568281
API_HASH = "5dec3f281b9576f65824326f7cd984ed"
BOT_TOKEN = "8367355512:AAHM0nZO3C32roFtmxOtzjJiW6fQcsx0LsQ"

# Setup logging
logging.basicConfig(
    format='[%(levelname)s] %(name)s: %(message)s',
    level=logging.INFO
)

# Create bot client
bot = TelegramClient('allatomic_menu_bot', API_ID, API_HASH)

# Help menu text
HELP_TEXT = """
╔═══════════════════════════════════════════════╗
║      ⚛️  **AllAtomic Help Menu**  ⚛️           ║
╠═══════════════════════════════════════════════╣
║                                               ║
║  💜 **Total Commands:** `84`                  ║
║  📦 **Plugins:** `20`                         ║
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

**📂 Select a category:**
"""

# Command categories
CATEGORIES = {
    'core': {
        'name': '⚙️ Core',
        'commands': ['alive', 'status', 'ping', 'help', 'cmds', 'repo', 'support']
    },
    'admin': {
        'name': '👥 Admin',
        'commands': ['ban', 'kick', 'mute', 'unmute', 'purge', 'pin', 'unpin', 'lock', 'unlock', 'zombies']
    },
    'fun': {
        'name': '🎮 Fun',
        'commands': ['meme', 'joke', 'tts', 'fact', 'quote', 'roll', 'coin']
    },
    'utility': {
        'name': '🔧 Utility',
        'commands': ['tr', 'weather', 'readmore', 'glitch', 'font', 'paste', 'gitinfo', 'qr', 'remind']
    },
    'media': {
        'name': '📷 Media',
        'commands': ['song', 'video', 'insta', 'tiktok', 'twitter', 'facebook', 'media', 'yt']
    },
    'stickers': {
        'name': '🎭 Stickers',
        'commands': ['kang', 'sticker', 'fullpp', 'dp']
    },
    'anime': {
        'name': '🌸 Anime',
        'commands': ['waifu', 'neko', 'waifupic', 'anime', 'manga']
    },
    'ai': {
        'name': '🤖 AI',
        'commands': ['chat', 'ask', 'summarize']
    },
    'group': {
        'name': '📢 Group',
        'commands': ['save', 'get', 'notes', 'clear', 'filter', 'filters', 'stop']
    },
    'advanced': {
        'name': '⚡ Advanced',
        'commands': ['eval', 'exec', 'term', 'sudo', 'heroku', 'gcast']
    },
    'pm': {
        'name': '📩 PM Permit',
        'commands': ['pmpermit', 'approve', 'disapprove', 'block', 'unblock', 'logger']
    },
    'voice': {
        'name': '🎵 Voice',
        'commands': ['vcstart', 'vcend', 'nowplaying', 'lastfm', 'play']
    },
    'direct': {
        'name': '🔗 Direct',
        'commands': ['direct', 'source']
    }
}

def main_menu_buttons():
    """Build main menu inline keyboard"""
    return [
        [Button.inline('⚙️ Core', b'help_core'), Button.inline('👥 Admin', b'help_admin')],
        [Button.inline('🎮 Fun', b'help_fun'), Button.inline('🔧 Utility', b'help_utility')],
        [Button.inline('📷 Media', b'help_media'), Button.inline('🎭 Stickers', b'help_stickers')],
        [Button.inline('🌸 Anime', b'help_anime'), Button.inline('🤖 AI', b'help_ai')],
        [Button.inline('📢 Group', b'help_group'), Button.inline('⚡ Advanced', b'help_advanced')],
        [Button.inline('📩 PM Permit', b'help_pm'), Button.inline('🎵 Voice', b'help_voice')],
        [Button.inline('🔗 Direct', b'help_direct'), Button.inline('📜 All Commands', b'help_all')],
        [Button.inline('🔄 Refresh', b'help_refresh'), Button.inline('❌ Close', b'help_close')],
    ]

def back_buttons():
    """Build back button keyboard"""
    return [
        [Button.inline('◀️ Back', b'help_main'), Button.inline('🔄 Refresh', b'help_refresh')],
        [Button.inline('❌ Close', b'help_close')],
    ]

@bot.on(events.NewMessage(pattern='/start'))
async def start_handler(event):
    """Handle /start command"""
    await event.respond(
        HELP_TEXT,
        parse_mode='md',
        buttons=main_menu_buttons()
    )

@bot.on(events.NewMessage(pattern='/help'))
async def help_handler(event):
    """Handle /help command"""
    await event.respond(
        HELP_TEXT,
        parse_mode='md',
        buttons=main_menu_buttons()
    )

@bot.on(events.CallbackQuery())
async def callback_handler(event):
    """Handle inline button callbacks"""
    data = event.data.decode('utf-8')
    
    if data == 'help_main':
        await event.edit(
            HELP_TEXT,
            parse_mode='md',
            buttons=main_menu_buttons()
        )
    
    elif data == 'help_close':
        await event.delete()
    
    elif data == 'help_refresh':
        await event.edit(
            HELP_TEXT,
            parse_mode='md',
            buttons=main_menu_buttons()
        )
    
    elif data == 'help_all':
        all_cmds = []
        for cat in CATEGORIES.values():
            all_cmds.extend(cat['commands'])
        
        cmds_text = '  ' + '  '.join([f'`.{cmd}`' for cmd in all_cmds])
        
        await event.edit(
            f"""
╔═══════════════════════════════════════════════╗
║      📜  **All Commands ({len(all_cmds)})**  📜     ║
╠═══════════════════════════════════════════════╣
║                                               ║
{cmds_text}
║                                               ║
╚═══════════════════════════════════════════════╝

**💡 Tip:** Use buttons below for categories!
""",
            parse_mode='md',
            buttons=back_buttons()
        )
    
    elif data.startswith('help_'):
        category = data.replace('help_', '')
        if category in CATEGORIES:
            cat = CATEGORIES[category]
            cmds_list = '\n'.join([f"║  • `.{cmd}`" for cmd in cat['commands']])
            
            await event.edit(
                f"""
╔═══════════════════════════════════════════════╗
║      {cat['name']}      ║
╠═══════════════════════════════════════════════╣
║                                               ║
{cmds_list}
║                                               ║
╚═══════════════════════════════════════════════╝

**💡 Usage:** `.{cat['commands'][0]}`
""",
                parse_mode='md',
                buttons=back_buttons()
            )
    
    await event.answer()

async def main():
    """Main function"""
    logging.info('⚛️  Starting AllAtomic Menu Bot...')
    await bot.start(bot_token=BOT_TOKEN)
    logging.info('✅ Bot started successfully!')
    logging.info('💜 Menu bot is ready!')
    logging.info('📱 Talk to @AllAtomicBot to use the menu')
    await bot.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())
