"""
AllAtomic - Admin Commands Plugin
Dev: @GhostMarshal | Channel: @ComputeCode
(૨๑•̀ㅁ•́ฅा) Purple Anime Theme (#9A8CFF)
"""

from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from AllAtomic import log, clients, config, db
from AllAtomic.functions.utils import is_admin as utils_is_admin


async def load(bot):
    """Load plugin (✿◠‿◠)"""
    
    # Admins list
    @bot.on_message(filters.command("admins") & filters.group)
    async def admins(client, message):
        try:
            chat = message.chat
            admins = await client.get_chat_administrators(chat.id)
            
            if not admins:
                await message.reply("No admins found!")
                return
            
            text = f"{config.LINE}\n{config.SPARKLE} **Admins** {config.WINK}\n{config.LINE}\n"
            for admin in admins:
                status = "👑" if admin.is_custom_title else "🔨"
                name = admin.user.first_name or "Deleted"
                username = f"@{admin.user.username}" if admin.user.username else ""
                text += f"{status} {name} {username}\n"
            
            await message.reply(text)
        except Exception as e:
            log.error(f"Admins error: {e}")
            await message.reply("Error fetching admins!")
    
    # Add admin
    @bot.on_message(filters.command("addadmin") & filters.group)
    async def add_admin(client, message):
        if not await utils_is_admin(message.from_user.id):
            await message.reply("You're not an admin!")
            return
        
        if len(message.command) < 2:
            await message.reply("Usage: /addadmin <user_id or reply>")
            return
        
        try:
            user = message.reply_message.from_user if message.reply_message else await client.get_users(message.command[1])
            
            await db.add_admin(user.id, user.first_name)
            await client.promote_chat_member(
                message.chat.id,
                user.id,
                can_change_info=True,
                can_delete_messages=True
            )
            
            await message.reply(f"{config.CUTE} Added **{user.mention}** as admin! {config.WINK}")
        except Exception as e:
            log.error(f"Add admin error: {e}")
            await message.reply("Error adding admin!")
    
    # Remove admin
    @bot.on_message(filters.command("rmadmin") & filters.group)
    async def rm_admin(client, message):
        if not await utils_is_admin(message.from_user.id):
            await message.reply("You're not an admin!")
            return
        
        if not message.reply_message:
            await message.reply("Reply to user's message!")
            return
        
        try:
            user = message.reply_message.from_user
            
            await db.remove_admin(user.id)
            await client.promote_chat_member(
                message.chat.id,
                user.id,
                can_change_info=False,
                can_delete_messages=False,
                can_restrict_members=False,
                can_invite_users=False
            )
            
            await message.reply(f"{config.CUTE} Removed **{user.mention}** from admin! {config.WINK}")
        except Exception as e:
            log.error(f"Remove admin error: {e}")
            await message.reply("Error removing admin!")
    
    # Ban user
    @bot.on_message(filters.command("ban") & filters.group)
    async def ban_user(client, message):
        if not await utils_is_admin(message.from_user.id):
            await message.reply("You're not an admin!")
            return
        
        if not message.reply_message:
            await message.reply("Reply to user's message!")
            return
        
        try:
            user = message.reply_message.from_user
            reason = " ".join(message.command[1:]) if len(message.command) > 1 else "No reason"
            
            await client.ban_chat_member(message.chat.id, user.id)
            
            await message.reply(f"{config.CUTE} Banned **{user.mention}**! {config.WINK}\n{config.THUNDER} Reason: {reason}")
        except Exception as e:
            log.error(f"Ban error: {e}")
            await message.reply("Error banning user!")
    
    # Unban user
    @bot.on_message(filters.command("unban") & filters.group)
    async def unban_user(client, message):
        if not await utils_is_admin(message.from_user.id):
            await message.reply("You're not an admin!")
            return
        
        if len(message.command) < 2:
            await message.reply("Usage: /unban <user_id>")
            return
        
        try:
            user_id = int(message.command[1])
            
            await client.unban_chat_member(message.chat.id, user_id)
            
            await message.reply(f"{config.CUTE} Unbanned user! {config.WINK}")
        except Exception as e:
            log.error(f"Unban error: {e}")
            await message.reply("Error unbanning user!")
    
    # Kick user
    @bot.on_message(filters.command("kick") & filters.group)
    async def kick_user(client, message):
        if not await utils_is_admin(message.from_user.id):
            await message.reply("You're not an admin!")
            return
        
        if not message.reply_message:
            await message.reply("Reply to user's message!")
            return
        
        try:
            user = message.reply_message.from_user
            
            await client.ban_chat_member(message.chat.id, user.id, date=int(message.date.timestamp()) + 60)
            
            await message.reply(f"{config.CUTE} Kicked **{user.mention}**! {config.WINK}")
        except Exception as e:
            log.error(f"Kick error: {e}")
            await message.reply("Error kicking user!")
    
    # Purge messages
    @bot.on_message(filters.command("purge") & filters.group)
    async def purge(client, message):
        if not await utils_is_admin(message.from_user.id):
            await message.reply("You're not an admin!")
            return
        
        if not message.reply_message:
            await message.reply("Reply to message to start purge!")
            return
        
        try:
            start_id = message.reply_message.id
            end_id = message.id
            
            await client.delete_messages(message.chat.id, range(start_id, end_id + 1))
            
            await message.reply(f"{config.CUTE} Purged messages! {config.WINK}")
        except Exception as e:
            log.error(f"Purge error: {e}")
            await message.reply("Error purging messages!")
    
    # Pin message
    @bot.on_message(filters.command("pin") & filters.group)
    async def pin_message(client, message):
        if not await utils_is_admin(message.from_user.id):
            await message.reply("You're not an admin!")
            return
        
        try:
            msg_id = message.reply_message.id if message.reply_message else message.id
            
            await message.chat.pin_message(
                message_id=msg_id,
                disable_notification=True
            )
            
            await message.reply(f"{config.CUTE} Pinned message! {config.WINK}")
        except Exception as e:
            log.error(f"Pin error: {e}")
            await message.reply("Error pinning message!")
    
    # Unpin message
    @bot.on_message(filters.command("unpin") & filters.group)
    async def unpin_message(client, message):
        if not await utils_is_admin(message.from_user.id):
            await message.reply("You're not an admin!")
            return
        
        try:
            await message.chat.unpin_message()
            await message.reply(f"{config.CUTE} Unpinned message! {config.WINK}")
        except Exception as e:
            log.error(f"Unpin error: {e}")
            await message.reply("Error unpinning message!")
    
    # Promote user
    @bot.on_message(filters.command("promote") & filters.group)
    async def promote_user(client, message):
        if not await utils_is_admin(message.from_user.id):
            await message.reply("You're not an admin!")
            return
        
        if not message.reply_message:
            await message.reply("Reply to user's message!")
            return
        
        try:
            user = message.reply_message.from_user
            
            await client.promote_chat_member(
                message.chat.id,
                user.id,
                can_change_info=True,
                can_delete_messages=True,
                can_restrict_members=True
            )
            
            await message.reply(f"{config.CUTE} Promoted **{user.mention}**! {config.WINK}")
        except Exception as e:
            log.error(f"Promote error: {e}")
            await message.reply("Error promoting user!")
    
    # Demote user
    @bot.on_message(filters.command("demote") & filters.group)
    async def demote_user(client, message):
        if not await utils_is_admin(message.from_user.id):
            await message.reply("You're not an admin!")
            return
        
        if not message.reply_message:
            await message.reply("Reply to user's message!")
            return
        
        try:
            user = message.reply_message.from_user
            
            await client.promote_chat_member(
                message.chat.id,
                user.id,
                can_change_info=False,
                can_delete_messages=False,
                can_restrict_members=False,
                can_invite_users=False
            )
            
            await message.reply(f"{config.CUTE} Demoted **{user.mention}**! {config.WINK}")
        except Exception as e:
            log.error(f"Demote error: {e}")
            await message.reply("Error demoting user!")
    
    # Gban
    @bot.on_message(filters.command("gban"))
    async def gban(client, message):
        if not await utils_is_admin(message.from_user.id):
            await message.reply("You're not an admin!")
            return
        
        if not message.reply_message:
            await message.reply("Reply to user's message!")
            return
        
        try:
            user = message.reply_message.from_user
            reason = " ".join(message.command[1:]) if len(message.command) > 1 else "No reason"
            
            await db.add_gban(user.id, reason)
            
            # Try to ban in all chats
            try:
                await client.ban_chat_member(user.id, user.id)
            except:
                pass
            
            await message.reply(f"{config.CUTE} **Global Banned** {user.mention}! {config.THUNDER}\n{config.REASON}: {reason}")
        except Exception as e:
            log.error(f"Gban error: {e}")
            await message.reply("Error gbaning user!")
    
    # Ungban
    @bot.on_message(filters.command("ungban"))
    async def ungban(client, message):
        if not await utils_is_admin(message.from_user.id):
            await message.reply("You're not an admin!")
            return
        
        if len(message.command) < 2:
            await message.reply("Usage: /ungban <user_id>")
            return
        
        try:
            user_id = int(message.command[1])
            await db.remove_gban(user_id)
            await message.reply(f"{config.CUTE} **Ungbanned** user! {config.WINK}")
        except Exception as e:
            log.error(f"Ungban error: {e}")
            await message.reply("Error ungbaning user!")
    
    # Blacklist
    @bot.on_message(filters.command("blacklist") & filters.group)
    async def blacklist(client, message):
        if not await utils_is_admin(message.from_user.id):
            await message.reply("You're not an admin!")
            return
        
        if len(message.command) < 2:
            await message.reply("Usage: /blacklist <keyword>")
            return
        
        try:
            keyword = " ".join(message.command[1:])
            await db.add_blacklist(keyword)
            await message.reply(f"{config.CUTE} Added **{keyword}** to blacklist! {config.WINK}")
        except Exception as e:
            log.error(f"Blacklist error: {e}")
            await message.reply("Error adding to blacklist!")
    
    # Unblacklist
    @bot.on_message(filters.command("unblacklist") & filters.group)
    async def unblacklist(client, message):
        if not await utils_is_admin(message.from_user.id):
            await message.reply("You're not an admin!")
            return
        
        if len(message.command) < 2:
            await message.reply("Usage: /unblacklist <keyword>")
            return
        
        try:
            keyword = " ".join(message.command[1:])
            await db.remove_blacklist(keyword)
            await message.reply(f"{config.CUTE} Removed **{keyword}** from blacklist! {config.WINK}")
        except Exception as e:
            log.error(f"Unblacklist error: {e}")
            await message.reply("Error removing from blacklist!")
