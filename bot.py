#!/usr/bin/env python3
"""
AllAtomic Bot - HellBot Style Inline Menu Handler
Handles inline button callbacks for help menu
"""

import asyncio
from telethon import TelegramClient, events
from telethon.tl.custom import InlineButton
from app.bot_helper import (
    BOT_TOKEN, 
    HELP_CATEGORIES, 
    build_help_keyboard, 
    build_category_keyboard,
    build_main_menu_keyboard
)
from app.utils import get_kaomoji

# Bot configuration
API_ID = 20828230
API_HASH = 'a8c7e9f5d3b1a2c4e6f8a0b2d4e6f8a0'

# Create bot client
bot = TelegramClient('allatomic_helper_bot', API_ID, API_HASH)

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
║                                               ║
║  {kaomoji}                                    ║
║                                               ║
║  **Dev:** @GhostMarshal                       ║
║  **Channel:** @ComputeCode                    ║
║                                               ║
╚═══════════════════════════════════════════════╝

**📂 Select a category:**
"""

async def start_handler(event):
    """Handle /start command"""
    await event.respond(
        f"""
╔═══════════════════════════════════════════════╗
║      ⚛️  **AllAtomic Userbot**  ⚛️             ║
╠═══════════════════════════════════════════════╣
║                                               ║
║  💜 Welcome to AllAtomic!                     ║
║                                               ║
║  **Dev:** @GhostMarshal                       ║
║  **Channel:** @ComputeCode                    ║
║                                               ║
║  {get_kaomoji('happy')}                                    ║
║                                               ║
╚═══════════════════════════════════════════════╝

**Use the buttons below to navigate!**
""",
        parse_mode="md",
        buttons=build_main_menu_keyboard()
    )

async def help_callback_handler(event):
    """Handle help menu callbacks"""
    data = event.data.decode('utf-8')
    
    if data == 'help_main':
        await event.edit(
            HELP_MAIN_TEXT.format(kaomoji=get_kaomoji('happy')),
            parse_mode="md",
            buttons=build_help_keyboard()
        )
    
    elif data.startswith('help_'):
        category = data.replace('help_', '')
        
        if category in HELP_CATEGORIES:
            cat_info = HELP_CATEGORIES[category]
            commands_list = "\n".join([
                f"║  • `{cmd}` - {desc}" 
                for cmd, desc in cat_info["commands"]
            ])
            
            emoji = cat_info["name"].split()[0]
            
            await event.edit(
                HELP_CATEGORY_TEXT.format(
                    category_emoji=emoji,
                    category_name=cat_info["name"].split(' ', 1)[1] if ' ' in cat_info["name"] else cat_info["name"],
                    description=cat_info["description"],
                    commands_list=commands_list
                ),
                parse_mode="md",
                buttons=build_category_keyboard()
            )
    
    elif data == 'help_all':
        all_commands = []
        for cat_info in HELP_CATEGORIES.values():
            for cmd, desc in cat_info["commands"]:
                all_commands.append(f"`{cmd}`")
        
        cmds_text = "  " + "  ".join(all_commands)
        
        await event.edit(
            f"""
╔═══════════════════════════════════════════════╗
║      📜  **All Commands ({len(all_commands)})**  📜     ║
╠═══════════════════════════════════════════════╣
║                                               ║
{cmds_text}
║                                               ║
╚═══════════════════════════════════════════════╝
""",
            parse_mode="md",
            buttons=build_category_keyboard()
        )
    
    elif data == 'help_refresh':
        await event.edit(
            HELP_MAIN_TEXT.format(kaomoji=get_kaomoji('happy')),
            parse_mode="md",
            buttons=build_help_keyboard()
        )
    
    elif data == 'help_close':
        await event.delete()

async def menu_callback_handler(event):
    """Handle main menu callbacks"""
    data = event.data.decode('utf-8')
    
    if data == 'menu_help':
        await event.edit(
            HELP_MAIN_TEXT.format(kaomoji=get_kaomoji('happy')),
            parse_mode="md",
            buttons=build_help_keyboard()
        )
    
    elif data == 'menu_cmds':
        all_commands = []
        for cat_info in HELP_CATEGORIES.values():
            for cmd, desc in cat_info["commands"]:
                all_commands.append(f"`{cmd}` - {desc}")
        
        cmds_text = "\n".join(all_commands[:20])  # Show first 20
        await event.edit(
            f"""
╔═══════════════════════════════════════════════╗
║      📜  **All Commands**  📜                  ║
╠═══════════════════════════════════════════════╣
║                                               ║
{cmds_text}
║                                               ║
║  ...and more! Use .cmds for full list         ║
║                                               ║
╚═══════════════════════════════════════════════╝
""",
            parse_mode="md",
            buttons=build_main_menu_keyboard()
        )
    
    elif data == 'menu_about':
        await event.edit(
            f"""
╔═══════════════════════════════════════════════╗
║      ⚛️  **About AllAtomic**  ⚛️               ║
╠═══════════════════════════════════════════════╣
║                                               ║
║  **Version:** 1.0.0                           ║
║  **Theme:** Purple Anime 💜                   ║
║  **Style:** HellBot Inspired                  ║
║                                               ║
║  **Dev:** @GhostMarshal                       ║
║  **Channel:** @ComputeCode                    ║
║                                               ║
║  {get_kaomoji('happy')}                                    ║
║                                               ║
╚═══════════════════════════════════════════════╝
""",
            parse_mode="md",
            buttons=build_main_menu_keyboard()
        )
    
    elif data == 'menu_repo':
        await event.respond(
            "🔗 **Repository:**\nhttps://github.com/corruptcrew/AllAtomic",
            parse_mode="md",
            link_preview=True
        )

async def main():
    """Main function"""
    await bot.start(bot_token=BOT_TOKEN)
    
    # Register handlers
    bot.add_event_handler(start_handler, events.NewMessage(pattern='/start'))
    bot.add_event_handler(help_callback_handler, events.CallbackQuery(data=lambda d: d.decode().startswith('help_')))
    bot.add_event_handler(menu_callback_handler, events.CallbackQuery(data=lambda d: d.decode().startswith('menu_')))
    
    print("✅ AllAtomic Helper Bot started!")
    print("💜 HellBot-style inline menu ready!")
    
    await bot.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())
