"""
AllAtomic - Inline Menu Plugin
Dev: @GhostMarshal | Channel: @ComputeCode
(૨๑•̀ㅁ•́ฅा) Purple Anime Theme (#9A8CFF)
"""

from pyrogram import filters
from pyrogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent
from AllAtomic import log, config


async def load(bot):
    """Load plugin (✿◠‿◠)"""
    
    # Start inline query
    @bot.on_inline_query()
    async def inline_query(client, inline_query: InlineQuery):
        results = []
        
        # Welcome result
        results.append(
            InlineQueryResultArticle(
                id="welcome",
                title="AllAtomic",
                description="Your ultimate Telegram userbot",
                input_message_content=InputTextMessageContent(
                    message_text=f"{config.SPARKLE} **AllAtomic Inline Menu** {config.WINK}\n{config.CUTE} Use the buttons below!"
                ),
                thumb_url="https://te.legra.ph/file/9a8cff9a8cff9a8cff.jpg"
            )
        )
        
        # Core commands
        results.append(
            InlineQueryResultArticle(
                id="help",
                title="Help",
                description="View all commands",
                input_message_content=InputTextMessageContent(
                    message_text=f"{config.SPARKLE} **Help Commands** {config.WINK}\n{config.LINE}\n{config.CUTE} /start - Start the bot\n{config.WINK} /help - Show help\n{config.STAR} /stats - Show stats\n{config.FIRE} /ping - Check latency"
                ),
                thumb_url=config.THEME_COLOR
            )
        )
        
        # Fun commands
        results.append(
            InlineQueryResultArticle(
                id="fun",
                title="Fun",
                description="Have fun!",
                input_message_content=InputTextMessageContent(
                    message_text=f"{config.SPARKLE} **Fun Commands** {config.WINK}\n{config.LINE}\n{config.CUTE} /meme - Get random meme\n{config.WINK} /joke - Get random joke\n{config.STAR} /quote - Get random quote\n{config.FIRE} /roll - Roll dice"
                ),
                thumb_url=config.THEME_COLOR
            )
        )
        
        # Anime commands
        results.append(
            InlineQueryResultArticle(
                id="anime",
                title="Anime",
                description="Anime commands",
                input_message_content=InputTextMessageContent(
                    message_text=f"{config.SPARKLE} **Anime Commands** {config.WINK}\n{config.LINE}\n{config.CUTE} /anime <name> - Get anime info\n{config.WINK} /waifu - Get waifu\n{config.STAR} /neko - Get neko\n{config.FIRE} /megumin - Get Megumin"
                ),
                thumb_url=config.THEME_COLOR
            )
        )
        
        # AI commands
        results.append(
            InlineQueryResultArticle(
                id="ai",
                title="AI",
                description="AI commands",
                input_message_content=InputTextMessageContent(
                    message_text=f"{config.SPARKLE} **AI Commands** {config.WINK}\n{config.LINE}\n{config.CUTE} /ai <message> - Chat with AI\n{config.WINK} /dall <prompt> - Generate image\n{config.STAR} /translate - Translate text\n{config.FIRE} /wiki <topic> - Wikipedia"
                ),
                thumb_url=config.THEME_COLOR
            )
        )
        
        # Utility commands
        results.append(
            InlineQueryResultArticle(
                id="utils",
                title="Utilities",
                description="Utility commands",
                input_message_content=InputTextMessageContent(
                    message_text=f"{config.SPARKLE} **Utility Commands** {config.WINK}\n{config.LINE}\n{config.CUTE} /time - Show time\n{config.WINK} /date - Show date\n{config.STAR} /id - Show IDs\n{config.FIRE} /paste - Paste text"
                ),
                thumb_url=config.THEME_COLOR
            )
        )
        
        await inline_query.answer(results, cache_time=300)
    
    # Callback query handler
    @bot.on_callback_query()
    async def callback_query(client, callback_query):
        data = callback_query.data
        
        if data == "help":
            await callback_query.answer("Help menu shown!", show_alert=True)
        elif data == "fun":
            await callback_query.answer("Fun commands!", show_alert=True)
        elif data == "anime":
            await callback_query.answer("Anime commands!", show_alert=True)
        elif data == "ai":
            await callback_query.answer("AI commands!", show_alert=True)
        elif data == "utils":
            await callback_query.answer("Utility commands!", show_alert=True)
        elif data == "settings":
            await callback_query.answer("Settings menu!", show_alert=True)
        elif data == "about":
            await callback_query.answer(
                f"AllAtomic v{config.VERSION}\nDev: @GhostMarshal\nChannel: @ComputeCode",
                show_alert=True
            )
        elif data == "github":
            await callback_query.answer(f"GitHub: {config.GIT_REPO}", show_alert=True)
        elif data == "channel":
            await callback_query.answer(f"Channel: {config.UPDATE_CHANNEL}", show_alert=True)
        elif data == "back":
            await callback_query.edit_message_text(
                f"{config.SPARKLE} **AllAtomic** {config.WINK}\n{config.CUTE} Use the buttons below!"
            )
