"""
AllAtomic - Media Commands Plugin
Dev: @GhostMarshal | Channel: @ComputeCode
(૨๑•̀ㅁ•́ฅา) Purple Anime Theme (#9A8CFF)
"""

import asyncio
import os
from pyrogram import filters
from AllAtomic import log, clients, config
from AllAtomic.functions.utils import is_admin as utils_is_admin


async def load(bot):
    """Load plugin (✿◠‿◠)"""
    
    # Lyrics command
    @bot.on_message(filters.command("lyrics"))
    async def lyrics(client, message):
        if len(message.command) < 2:
            await message.reply("Usage: /lyrics <song name>")
            return
        
        try:
            song = " ".join(message.command[1:])
            # Placeholder - would need lyrics API
            await message.reply(f"{config.SPARKLE} **Lyrics for:** {song} {config.WINK}\n{config.CUTE} (Lyrics API integration needed)")
        except Exception as e:
            log.error(f"Lyrics error: {e}")
            await message.reply("Error fetching lyrics!")
    
    # Rimage command (reverse image search)
    @bot.on_message(filters.command("rimage") & filters.reply)
    async def rimage(client, message):
        if not message.reply_message.photo:
            await message.reply("Reply to an image!")
            return
        
        try:
            download = await message.reply_message.download()
            # Placeholder - would need reverse image search API
            await message.reply(f"{config.SPARKLE} **Reverse Image Search** {config.WINK}\n{config.CUTE} (Image search API integration needed)")
            if os.path.exists(download):
                os.remove(download)
        except Exception as e:
            log.error(f"Rimage error: {e}")
            await message.reply("Error processing image!")
    
    # OCR command
    @bot.on_message(filters.command("ocr") & filters.reply)
    async def ocr(client, message):
        if not message.reply_message.photo:
            await message.reply("Reply to an image!")
            return
        
        try:
            download = await message.reply_message.download()
            # Placeholder - would need OCR library
            await message.reply(f"{config.SPARKLE} **OCR** {config.WINK}\n{config.CUTE} (OCR library integration needed)")
            if os.path.exists(download):
                os.remove(download)
        except Exception as e:
            log.error(f"OCR error: {e}")
            await message.reply("Error processing image!")
    
    # Sticker command
    @bot.on_message(filters.command("sticker"))
    async def sticker(client, message):
        if not message.reply_message.sticker:
            await message.reply("Reply to a sticker!")
            return
        
        try:
            sticker = message.reply_message.sticker
            await message.reply_photo(
                photo=sticker.file_id,
                caption=f"{config.SPARKLE} **Sticker** {config.WINK}"
            )
        except Exception as e:
            log.error(f"Sticker error: {e}")
            await message.reply("Error processing sticker!")
    
    # Gif command
    @bot.on_message(filters.command("gif"))
    async def gif(client, message):
        if not message.reply_message:
            await message.reply("Reply to a GIF!")
            return
        
        if not message.reply_message.video:
            await message.reply("Reply to a video!")
            return
        
        try:
            await message.reply_video(
                video=message.reply_message.video.file_id,
                caption=f"{config.SPARKLE} **GIF** {config.WINK}"
            )
        except Exception as e:
            log.error(f"GIF error: {e}")
            await message.reply("Error processing GIF!")
    
    # Photo command
    @bot.on_message(filters.command("photo") & filters.reply)
    async def photo(client, message):
        if not message.reply_message.photo:
            await message.reply("Reply to a photo!")
            return
        
        try:
            await message.reply_photo(
                photo=message.reply_message.photo.file_id,
                caption=message.reply_message.caption
            )
        except Exception as e:
            log.error(f"Photo error: {e}")
            await message.reply("Error processing photo!")
    
    # Video command
    @bot.on_message(filters.command("video") & filters.reply)
    async def video(client, message):
        if not message.reply_message.video:
            await message.reply("Reply to a video!")
            return
        
        try:
            await message.reply_video(
                video=message.reply_message.video.file_id,
                caption=message.reply_message.caption
            )
        except Exception as e:
            log.error(f"Video error: {e}")
            await message.reply("Error processing video!")
    
    # Audio command
    @bot.on_message(filters.command("audio") & filters.reply)
    async def audio(client, message):
        if not message.reply_message.audio:
            await message.reply("Reply to an audio!")
            return
        
        try:
            await message.reply_audio(
                audio=message.reply_message.audio.file_id,
                caption=message.reply_message.caption
            )
        except Exception as e:
            log.error(f"Audio error: {e}")
            await message.reply("Error processing audio!")
    
    # Voice command
    @bot.on_message(filters.command("voice") & filters.reply)
    async def voice(client, message):
        if not message.reply_message.voice:
            await message.reply("Reply to a voice message!")
            return
        
        try:
            await message.reply_voice(
                voice=message.reply_message.voice.file_id,
                caption=message.reply_message.caption
            )
        except Exception as e:
            log.error(f"Voice error: {e}")
            await message.reply("Error processing voice!")
    
    # Document command
    @bot.on_message(filters.command("document") & filters.reply)
    async def document(client, message):
        if not message.reply_message.document:
            await message.reply("Reply to a document!")
            return
        
        try:
            await message.reply_document(
                document=message.reply_message.document.file_id,
                caption=message.reply_message.caption
            )
        except Exception as e:
            log.error(f"Document error: {e}")
            await message.reply("Error processing document!")
    
    # Forward all command
    @bot.on_message(filters.command("fwdall") & filters.group)
    async def fwdall(client, message):
        if not await utils_is_admin(message.from_user.id):
            await message.reply("You're not an admin!")
            return
        
        if len(message.command) < 2:
            await message.reply("Usage: /fwdall <chat_id>")
            return
        
        try:
            chat_id = int(message.command[1])
            
            for msg_id in range(message.id - 10, message.id + 1):
                try:
                    await client.forward_messages(chat_id, message.chat.id, msg_id)
                except:
                    pass
            
            await message.reply(f"{config.SPARKLE} **Forwarded** {config.WINK}")
        except Exception as e:
            log.error(f"Fwdall error: {e}")
            await message.reply("Error forwarding!")
    
    # Download command
    @bot.on_message(filters.command("download") & filters.reply)
    async def download(client, message):
        if not message.reply_message:
            await message.reply("Reply to media!")
            return
        
        try:
            path = await message.reply_message.download()
            await message.reply(f"{config.SPARKLE} **Downloaded!** {config.WINK}\n{config.LINE}\n{path}\n{config.LINE}")
        except Exception as e:
            log.error(f"Download error: {e}")
            await message.reply("Error downloading!")
    
    # Upload command
    @bot.on_message(filters.command("upload"))
    async def upload(client, message):
        if len(message.command) < 2:
            await message.reply("Usage: /upload <file_path>")
            return
        
        try:
            file_path = message.command[1]
            
            if not os.path.exists(file_path):
                await message.reply("File not found!")
                return
            
            file_type = os.path.splitext(file_path)[1].lower()
            
            if file_type in [".jpg", ".jpeg", ".png", ".webp"]:
                await message.reply_photo(photo=file_path)
            elif file_type in [".mp4", ".mkv"]:
                await message.reply_video(video=file_path)
            elif file_type in [".mp3", ".wav"]:
                await message.reply_audio(audio=file_path)
            else:
                await message.reply_document(document=file_path)
            
            await message.reply(f"{config.SPARKLE} **Uploaded!** {config.WINK}")
        except Exception as e:
            log.error(f"Upload error: {e}")
            await message.reply("Error uploading!")
    
    # Telegram command
    @bot.on_message(filters.command("telegram") & filters.reply)
    async def telegram(client, message):
        if not message.reply_message:
            await message.reply("Reply to message!")
            return
        
        try:
            await message.reply_message.forward(message.chat.id)
            await message.reply(f"{config.SPARKLE} **Forwarded!** {config.WINK}")
        except Exception as e:
            log.error(f"Telegram error: {e}")
            await message.reply("Error forwarding!")
    
    # Save command
    @bot.on_message(filters.command("save") & filters.reply)
    async def save(client, message):
        if not message.reply_message:
            await message.reply("Reply to media!")
            return
        
        try:
            path = await message.reply_message.download()
            await message.reply(f"{config.SPARKLE} **Saved!** {config.WINK}\n{config.LINE}\n{path}\n{config.LINE}")
        except Exception as e:
            log.error(f"Save error: {e}")
            await message.reply("Error saving!")
    
    # Delete media command
    @bot.on_message(filters.command("delmedia") & filters.group)
    async def delmedia(client, message):
        if not await utils_is_admin(message.from_user.id):
            await message.reply("You're not an admin!")
            return
        
        if not message.reply_message:
            await message.reply("Reply to media!")
            return
        
        try:
            await message.reply_message.delete()
            await message.delete()
            await message.reply(f"{config.SPARKLE} **Deleted!** {config.WINK}")
        except Exception as e:
            log.error(f"Delmedia error: {e}")
            await message.reply("Error deleting!")
    
    # Media info command
    @bot.on_message(filters.command("mediainfo") & filters.reply)
    async def mediainfo(client, message):
        if not message.reply_message:
            await message.reply("Reply to media!")
            return
        
        try:
            media = message.reply_message
            
            info = f"{config.SPARKLE} **Media Info** {config.WINK}\n{config.LINE}\n"
            
            if media.photo:
                info += f"{config.CUTE} **Type:** Photo\n"
            elif media.video:
                info += f"{config.CUTE} **Type:** Video\n"
            elif media.audio:
                info += f"{config.CUTE} **Type:** Audio\n"
            elif media.sticker:
                info += f"{config.CUTE} **Type:** Sticker\n"
            
            info += f"{config.WINK} **Size:** {media.file_size}\n"
            info += f"{config.STAR} **ID:** {media.id}\n"
            
            await message.reply(info)
        except Exception as e:
            log.error(f"Mediainfo error: {e}")
            await message.reply("Error getting media info!")
