"""
AllAtomic - Utility Commands Plugin
Dev: @GhostMarshal | Channel: @ComputeCode
(૨๑•̀ㅁ•́ฅา) Purple Anime Theme (#9A8CFF)
"""

import asyncio
from datetime import datetime
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from AllAtomic import log, clients, config, db
from AllAtomic.functions.utils import is_admin as utils_is_admin


async def load(bot):
    """Load plugin (✿◠‿◠)"""
    
    # Invite command
    @bot.on_message(filters.command("invite") & filters.group)
    async def invite(client, message):
        try:
            invite_link = await client.export_chat_invite_link(message.chat.id)
            await message.reply(f"{config.SPARKLE} **Invite Link** {config.WINK}\n{config.LINE}\n{invite_link}\n{config.LINE}")
        except Exception as e:
            log.error(f"Invite error: {e}")
            await message.reply("Error creating invite link!")
    
    # Clean command
    @bot.on_message(filters.command("clean") & filters.group)
    async def clean(client, message):
        if not await utils_is_admin(message.from_user.id):
            await message.reply("You're not an admin!")
            return
        
        try:
            deleted = await message.delete()
            await message.reply(f"{config.CUTE} Cleaned! {config.WINK}")
            await asyncio.sleep(1)
            await deleted.delete()
        except Exception as e:
            log.error(f"Clean error: {e}")
            await message.reply("Error cleaning!")
    
    # Clear command
    @bot.on_message(filters.command("clear") & filters.group)
    async def clear(client, message):
        if not await utils_is_admin(message.from_user.id):
            await message.reply("You're not an admin!")
            return
        
        if not message.reply_message:
            await message.reply("Reply to message to clear!")
            return
        
        try:
            start_id = message.reply_message.id
            end_id = message.id
            
            await client.delete_messages(message.chat.id, range(start_id, end_id + 1))
            
            await message.reply(f"{config.CUTE} Cleared messages! {config.WINK}")
        except Exception as e:
            log.error(f"Clear error: {e}")
            await message.reply("Error clearing messages!")
    
    # Forward command
    @bot.on_message(filters.command("forward"))
    async def forward(client, message):
        if not message.reply_message:
            await message.reply("Reply to message to forward!")
            return
        
        if len(message.command) < 2:
            await message.reply("Usage: /forward <chat_id>")
            return
        
        try:
            chat_id = int(message.command[1])
            await message.reply_message.forward(chat_id)
            await message.reply(f"{config.CUTE} Forwarded! {config.WINK}")
        except Exception as e:
            log.error(f"Forward error: {e}")
            await message.reply("Error forwarding!")
    
    # Reply command
    @bot.on_message(filters.command("reply"))
    async def reply(client, message):
        if not message.reply_message:
            await message.reply("Reply to message!")
            return
        
        if len(message.command) < 2:
            await message.reply("Usage: /reply <text>")
            return
        
        try:
            text = " ".join(message.command[1:])
            await message.reply_message.reply(text)
            await message.delete()
        except Exception as e:
            log.error(f"Reply error: {e}")
            await message.reply("Error replying!")
    
    # Note command (add)
    @bot.on_message(filters.command("note"))
    async def note(client, message):
        if len(message.command) < 3:
            await message.reply("Usage: /note <keyword> <content>")
            return
        
        try:
            keyword = message.command[1]
            content = " ".join(message.command[2:])
            await db.add_note(message.chat.id, keyword, content)
            await message.reply(f"{config.CUTE} Added note **{keyword}**! {config.WINK}")
        except Exception as e:
            log.error(f"Note error: {e}")
            await message.reply("Error adding note!")
    
    # Note command (get)
    @bot.on_message(filters.regex(r"^#[\w-]+"))
    async def get_note(client, message):
        keyword = message.text.split()[0].lstrip("#").lower()
        
        try:
            content = await db.get_note(message.chat.id, keyword)
            if content:
                await message.reply(content)
        except Exception as e:
            log.error(f"Get note error: {e}")
    
    # Note command (list)
    @bot.on_message(filters.command("notes") & filters.group)
    async def list_notes(client, message):
        try:
            notes = await db.get_all_notes(message.chat.id)
            
            if not notes:
                await message.reply("No notes found!")
                return
            
            text = f"{config.SPARKLE} **Notes** {config.WINK}\n{config.LINE}\n"
            for note in notes:
                text += f"#`{note['keyword']}`\n"
            
            await message.reply(text)
        except Exception as e:
            log.error(f"List notes error: {e}")
            await message.reply("Error listing notes!")
    
    # Note command (delete)
    @bot.on_message(filters.command("delnote") & filters.group)
    async def del_note(client, message):
        if len(message.command) < 2:
            await message.reply("Usage: /delnote <keyword>")
            return
        
        try:
            keyword = message.command[1]
            await db.delete_note(message.chat.id, keyword)
            await message.reply(f"{config.CUTE} Deleted note **{keyword}**! {config.WINK}")
        except Exception as e:
            log.error(f"Delete note error: {e}")
            await message.reply("Error deleting note!")
    
    # Welcome command
    @bot.on_message(filters.command("welcome") & filters.group)
    async def welcome(client, message):
        if not await utils_is_admin(message.from_user.id):
            await message.reply("You're not an admin!")
            return
        
        if len(message.command) < 2:
            await message.reply("Usage: /welcome enable|disable [message]")
            return
        
        try:
            action = message.command[1].lower()
            
            if action == "enable":
                msg = " ".join(message.command[2:]) if len(message.command) > 2 else None
                await db.add_welcome(message.chat.id, True, msg)
                await message.reply(f"{config.CUTE} Welcome enabled! {config.WINK}")
            elif action == "disable":
                await db.add_welcome(message.chat.id, False)
                await message.reply(f"{config.CUTE} Welcome disabled! {config.WINK}")
            else:
                await message.reply("Usage: /welcome enable|disable [message]")
        except Exception as e:
            log.error(f"Welcome error: {e}")
            await message.reply("Error setting welcome!")
    
    # Goodbye command
    @bot.on_message(filters.command("goodbye") & filters.group)
    async def goodbye(client, message):
        if not await utils_is_admin(message.from_user.id):
            await message.reply("You're not an admin!")
            return
        
        if len(message.command) < 2:
            await message.reply("Usage: /goodbye enable|disable [message]")
            return
        
        try:
            action = message.command[1].lower()
            
            if action == "enable":
                msg = " ".join(message.command[2:]) if len(message.command) > 2 else None
                await db.add_welcome(message.chat.id, True, msg, "goodbye")
                await message.reply(f"{config.CUTE} Goodbye enabled! {config.WINK}")
            elif action == "disable":
                await db.add_welcome(message.chat.id, False, None, "goodbye")
                await message.reply(f"{config.CUTE} Goodbye disabled! {config.WINK}")
            else:
                await message.reply("Usage: /goodbye enable|disable [message]")
        except Exception as e:
            log.error(f"Goodbye error: {e}")
            await message.reply("Error setting goodbye!")
    
    # Afk command
    @bot.on_message(filters.command("afk"))
    async def afk(client, message):
        try:
            reason = " ".join(message.command[1:]) if len(message.command) > 1 else "AFK"
            await db.add_afk(message.from_user.id, reason)
            await message.reply(f"{config.CUTE} You're now **AFK**! {config.WINK}\n{config.REASON}: {reason}")
        except Exception as e:
            log.error(f"Afk error: {e}")
            await message.reply("Error setting AFK!")
    
    # Remove afk
    @bot.on_message(filters.text & ~filters.command)
    async def remove_afk(client, message):
        try:
            if await db.is_afk(message.from_user.id):
                await db.remove_afk(message.from_user.id)
                await message.reply(f"{config.CUTE} Welcome back! {config.WINK}")
        except Exception as e:
            log.error(f"Remove AFK error: {e}")
    
    # Paste command
    @bot.on_message(filters.command("paste"))
    async def paste(client, message):
        if not message.reply_message:
            await message.reply("Reply to text to paste!")
            return
        
        try:
            text = message.reply_message.text or message.reply_message.caption
            if not text:
                await message.reply("No text to paste!")
                return
            
            paste_id = await db.add_paste(text)
            paste_url = f"https://paste.allatomic.dev/{paste_id}"
            
            await message.reply(f"{config.SPARKLE} **Pasted!** {config.WINK}\n{config.LINE}\n{paste_url}\n{config.LINE}")
        except Exception as e:
            log.error(f"Paste error: {e}")
            await message.reply("Error pasting!")
    
    # Get paste
    @bot.on_message(filters.regex(r"^https?://paste\.allatomic\.dev/[\w-]+$"))
    async def get_paste(client, message):
        paste_id = message.text.split("/")[-1]
        
        try:
            text = await db.get_paste(paste_id)
            if text:
                await message.reply(text)
        except Exception as e:
            log.error(f"Get paste error: {e}")
    
    # Time command
    @bot.on_message(filters.command("time"))
    async def time(client, message):
        now = datetime.utcnow()
        await message.reply(f"{config.SPARKLE} **Current Time** {config.WINK}\n{config.LINE}\n{now.strftime('%H:%M:%S UTC')}\n{config.LINE}")
    
    # Date command
    @bot.on_message(filters.command("date"))
    async def date(client, message):
        now = datetime.utcnow()
        await message.reply(f"{config.SPARKLE} **Current Date** {config.WINK}\n{config.LINE}\n{now.strftime('%Y-%m-%d')}\n{config.LINE}")
    
    # Uptime command
    @bot.on_message(filters.command("uptime"))
    async def uptime(client, message):
        from AllAtomic.core.initializer import get_uptime
        try:
            uptime_str = get_uptime()
            await message.reply(f"{config.SPARKLE} **Uptime** {config.WINK}\n{config.LINE}\n{uptime_str}\n{config.LINE}")
        except Exception as e:
            log.error(f"Uptime error: {e}")
            await message.reply("Error getting uptime!")
    
    # Id command
    @bot.on_message(filters.command("id"))
    async def id(client, message):
        user_id = message.from_user.id
        chat_id = message.chat.id
        
        await message.reply(f"{config.SPARKLE} **IDs** {config.WINK}\n{config.LINE}\n{config.CUTE} **Your ID:** {user_id}\n{config.WINK} **Chat ID:** {chat_id}\n{config.LINE}")
    
    # Tag command
    @bot.on_message(filters.command("tag") & filters.group)
    async def tag(client, message):
        if not await utils_is_admin(message.from_user.id):
            await message.reply("You're not an admin!")
            return
        
        if len(message.command) < 2:
            await message.reply("Usage: /tag @username")
            return
        
        try:
            username = message.command[1]
            await message.reply(f"{config.SPARKLE} **Tagged:** {username} {config.WINK}")
        except Exception as e:
            log.error(f"Tag error: {e}")
            await message.reply("Error tagging!")
    
    # Broadcast command
    @bot.on_message(filters.command("broadcast") & filters.user(config.OWNER_ID))
    async def broadcast(client, message):
        if not message.reply_message:
            await message.reply("Reply to message to broadcast!")
            return
        
        try:
            users = await db.get_all_users()
            count = 0
            
            for user in users:
                try:
                    await message.reply_message.forward(user["user_id"])
                    count += 1
                except:
                    pass
            
            await message.reply(f"{config.SPARKLE} **Broadcast Complete** {config.WINK}\n{config.LINE}\n{config.CUTE} **Sent to:** {count} users\n{config.LINE}")
        except Exception as e:
            log.error(f"Broadcast error: {e}")
            await message.reply("Error broadcasting!")
