#!/usr/bin/env python3
"""
AllAtomic Menu Bot - HellBot Style Inline Menu
Supports: Commands, Inline Mode, Group Chats
Use @AllAtomicBot in any chat for inline results
"""

import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes, InlineQueryHandler

# Configuration
BOT_TOKEN = "8367355512:AAHM0nZO3C32roFtmxOtzjJiW6fQcsx0LsQ"

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

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

def main_menu_keyboard():
    """Build main menu inline keyboard"""
    return [
        [InlineKeyboardButton('⚙️ Core', callback_data='help_core'), 
         InlineKeyboardButton('👥 Admin', callback_data='help_admin')],
        [InlineKeyboardButton('🎮 Fun', callback_data='help_fun'), 
         InlineKeyboardButton('🔧 Utility', callback_data='help_utility')],
        [InlineKeyboardButton('📷 Media', callback_data='help_media'), 
         InlineKeyboardButton('🎭 Stickers', callback_data='help_stickers')],
        [InlineKeyboardButton('🌸 Anime', callback_data='help_anime'), 
         InlineKeyboardButton('🤖 AI', callback_data='help_ai')],
        [InlineKeyboardButton('📢 Group', callback_data='help_group'), 
         InlineKeyboardButton('⚡ Advanced', callback_data='help_advanced')],
        [InlineKeyboardButton('📩 PM Permit', callback_data='help_pm'), 
         InlineKeyboardButton('🎵 Voice', callback_data='help_voice')],
        [InlineKeyboardButton('🔗 Direct', callback_data='help_direct'), 
         InlineKeyboardButton('📜 All Commands', callback_data='help_all')],
        [InlineKeyboardButton('🔄 Refresh', callback_data='help_refresh'), 
         InlineKeyboardButton('❌ Close', callback_data='help_close')],
    ]

def back_keyboard():
    """Build back button keyboard"""
    return [
        [InlineKeyboardButton('◀️ Back', callback_data='help_main'), 
         InlineKeyboardButton('🔄 Refresh', callback_data='help_refresh')],
        [InlineKeyboardButton('❌ Close', callback_data='help_close')],
    ]

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /start command"""
    await update.message.reply_text(
        HELP_TEXT,
        parse_mode='Markdown',
        reply_markup=InlineKeyboardMarkup(main_menu_keyboard())
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /help command"""
    await update.message.reply_text(
        HELP_TEXT,
        parse_mode='Markdown',
        reply_markup=InlineKeyboardMarkup(main_menu_keyboard())
    )

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle inline button callbacks"""
    query = update.callback_query
    await query.answer()
    
    data = query.data
    
    if data == 'help_main':
        await query.edit_message_text(
            HELP_TEXT,
            parse_mode='Markdown',
            reply_markup=InlineKeyboardMarkup(main_menu_keyboard())
        )
    
    elif data == 'help_close':
        await query.delete_message()
    
    elif data == 'help_refresh':
        await query.edit_message_text(
            HELP_TEXT,
            parse_mode='Markdown',
            reply_markup=InlineKeyboardMarkup(main_menu_keyboard())
        )
    
    elif data == 'help_all':
        all_cmds = []
        for cat in CATEGORIES.values():
            all_cmds.extend(cat['commands'])
        
        cmds_text = '  ' + '  '.join([f'`.{cmd}`' for cmd in all_cmds])
        
        await query.edit_message_text(
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
            parse_mode='Markdown',
            reply_markup=InlineKeyboardMarkup(back_keyboard())
        )
    
    elif data.startswith('help_'):
        category = data.replace('help_', '')
        if category in CATEGORIES:
            cat = CATEGORIES[category]
            cmds_list = '\n'.join([f"║  • `.{cmd}`" for cmd in cat['commands']])
            
            await query.edit_message_text(
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
                parse_mode='Markdown',
                reply_markup=InlineKeyboardMarkup(back_keyboard())
            )

async def inline_query(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle inline queries - type @AllAtomicBot in any chat"""
    query = update.inline_query
    results = []
    
    # Main help result
    results.append(
        InlineQueryResultArticle(
            id='help_main',
            title='📂 AllAtomic Help Menu',
            description='View all commands with inline buttons',
            input_message_content=InputTextMessageContent(
                HELP_TEXT,
                parse_mode='Markdown'
            ),
            reply_markup=InlineKeyboardMarkup(main_menu_keyboard())
        )
    )
    
    # Add category results
    for cat_id, cat in CATEGORIES.items():
        cmds_list = ', '.join([f'.{cmd}' for cmd in cat['commands'][:5]])
        if len(cat['commands']) > 5:
            cmds_list += '...'
        
        results.append(
            InlineQueryResultArticle(
                id=f'cat_{cat_id}',
                title=f'{cat["name"]} Commands',
                description=f'{len(cat["commands"])} commands: {cmds_list}',
                input_message_content=InputTextMessageContent(
                    f"""
╔═══════════════════════════════════════════════╗
║      {cat['name']}      ║
╠═══════════════════════════════════════════════╣
║                                               ║
{chr(10).join([f"║  • `.{cmd}`" for cmd in cat['commands']])}
║                                               ║
╚═══════════════════════════════════════════════╝

**💡 Usage:** `.{cat['commands'][0]}`
""",
                    parse_mode='Markdown'
                ),
                reply_markup=InlineKeyboardMarkup(back_keyboard())
            )
        )
    
    await update.inline_query.answer(results, cache_time=300)

async def post_init(application):
    """Called after bot initialization"""
    bot_info = await application.bot.get_me()
    logger.info(f'✅ Bot started: @{bot_info.username}')
    logger.info(f'💜 AllAtomic Menu Bot is ready!')
    logger.info(f'📱 Use @AllAtomicBot in any chat for inline menu!')

def main():
    """Main function"""
    logger.info('⚛️  Starting AllAtomic Menu Bot...')
    
    # Create application with inline mode enabled
    application = Application.builder().token(BOT_TOKEN).post_init(post_init).build()
    
    # Add handlers
    application.add_handler(CommandHandler('start', start_command))
    application.add_handler(CommandHandler('help', help_command))
    application.add_handler(CallbackQueryHandler(button_callback))
    application.add_handler(InlineQueryHandler(inline_query))
    
    # Start the bot
    logger.info('🚀 Bot is running! Type @AllAtomicBot in any chat.')
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
