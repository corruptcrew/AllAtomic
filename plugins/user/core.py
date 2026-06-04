"""
AllAtomic - Core Commands Plugin
Dev: @GhostMarshal | Channel: @ComputeCode
(૨๑•̀ㅁ•́ฅา) Purple Anime Theme (#9A8CFF)
"""

from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from AllAtomic import log, clients, config, db
from AllAtomic.functions.utils import get_time


async def load(bot):
    """Load plugin (◕‿◕)"""
    
    # Start command
    @bot.on_message(filters.command("start"))
    async def start(client, message):
        user = message.from_user
        reply = f"""
{config.symbols.LINE}
{config.symbols.SPARKLE} **Welcome, {user.mention}!**
{config.CUTE} **I'm AllAtomic** - Your ultimate Telegram userbot!
{config.WINK} **Version:** {config.VERSION}
{config.symbols.ARROW} **Commands:** /help
{config.symbols.LINE}
{config.symbols.CUTE} Dev: @GhostMarshal
{config.symbols.WINK} Channel: @ComputeCode
"""
        buttons = [
            [
                InlineKeyboardButton("⚡️ Add Me", url=f"t.me/{client.me.username}?startgroup=true"),
                InlineKeyboardButton("📢 Channel", url=config.UPDATE_CHANNEL),
            ],
            [
                InlineKeyboardButton("💻 GitHub", url=config.GIT_REPO),
                InlineKeyboardButton("👤 Dev", url="@GhostMarshal"),
            ],
        ]
        await message.reply(reply, reply_markup=InlineKeyboardMarkup(buttons))
    
    # Help command
    @bot.on_message(filters.command("help"))
    async def help(client, message):
        help_text = f"""
{config.LINE}
{config.SPARKLE} **AllAtomic Commands** {config.WINK}
{config.LINE}

{config.FIRE} **CORE**
/start - Start the bot
/help - Show this help
/stats - Show bot stats
/ping - Check latency

{config.THUNDER} **ADMIN**
/admins - List admins
/addadmin - Add admin
/rmadmin - Remove admin
/gban - Global ban
/ungban - Remove gban

{config.CUTE} **FUN**
/meme - Get random meme
/joke - Get random joke
/quote - Get random quote
/roll - Roll dice
/flip - Coin flip

{config.WINK} **UTILITIES**
/invite - Get invite link
/clean - Clean chats
/clear - Clear messages
/note - Manage notes

{config.STAR} **MEDIA**
/lyrics - Get song lyrics
/rimage - Reverse image search
/ocr - Extract text from image

{config.HEART} **ANIME**
/anime - Get anime info
/manga - Get manga info
/waifu - Get waifu image

{config.LOVE} **AI**
/ai - Chat with AI
/dall - Generate image with AI

{config.WAVE} **OTHER**
/afk - Set AFK status
/source - Get source code
/credits - Show credits
"""
        await message.reply(help_text)
    
    # Stats command
    @bot.on_message(filters.command("stats"))
    async def stats(client, message):
        try:
            users = await db.get_all_users()
            user_count = len(users)
            
            stats_text = f"""
{config.LINE}
{config.SPARKLE} **AllAtomic Stats** {config.WINK}
{config.LINE}

{config.CUTE} **Users:** {user_count}
{config.WINK} **Version:** {config.VERSION}
{config.STAR} **Uptime:** {get_time()}
{config.FIRE} **Status:** Online
{config.THUNDER} **Plugins:** Auto-loaded

{config.WAVE} Dev: @GhostMarshal
{config.HEART} Channel: @ComputeCode
{config.symbols.ARROW} GitHub: {config.GIT_REPO}
"""
            await message.reply(stats_text)
        except Exception as e:
            log.error(f"Stats error: {e}")
            await message.reply("Error fetching stats!")
    
    # Ping command
    @bot.on_message(filters.command("ping"))
    async def ping(client, message):
        start_time = message.date
        reply = await message.reply("Pinging...")
        end_time = reply.date
        latency = (end_time - start_time).total_seconds() * 1000
        
        ping_text = f"""
{config.SPARKLE} **Ping!** {config.WINK}
{config.LINE}
{config.CUTE} Latency: **{latency:.2f}ms**
{config.WINK} Status: **Online**
{config.LINE}
"""
        await reply.edit(ping_text)
    
    # Source command
    @bot.on_message(filters.command("source"))
    async def source(client, message):
        source_text = f"""
{config.LINE}
{config.SPARKLE} **Source Code** {config.WINK}
{config.LINE}
{config.FIRE} **GitHub:** {config.GIT_REPO}
{config.THUNDER} **Dev:** @GhostMarshal
{config.CUTE} **Channel:** @ComputeCode
{config.LINE}
"""
        await message.reply(source_text)
    
    # Credits command
    @bot.on_message(filters.command("credits"))
    async def credits(client, message):
        credits_text = f"""
{config.LINE}
{config.SPARKLE} **Credits** {config.WINK}
{config.LINE}
{config.CUTE} **Developer:** @GhostMarshal
{config.WINK} **Channel:** @ComputeCode
{config.STAR} **Theme:** Purple Anime (#9A8CFF)
{config.FIRE} **Framework:** Pyrogram v2.x
{config.THUNDER} **Database:** MongoDB
{config.HEART} **License:** GPL-3.0
{config.symbols.ARROW} **GitHub:** {config.GIT_REPO}
{config.LINE}
{config.symbols.HAPPY} Made with ❤️ and kaomoji
{config.LINE}
"""
        await message.reply(credits_text)
