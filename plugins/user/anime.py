"""
AllAtomic - Anime Commands Plugin
Dev: @GhostMarshal | Channel: @ComputeCode
(૨๑•̀ㅁ•́ฅा) Purple Anime Theme (#9A8CFF)
"""

import aiohttp
from pyrogram import filters
from AllAtomic import log, config


async def load(bot):
    """Load plugin (✿◠‿◠)"""
    
    # Anime command
    @bot.on_message(filters.command("anime"))
    async def anime(client, message):
        if len(message.command) < 2:
            await message.reply("Usage: /anime <anime name>")
            return
        
        try:
            anime_name = " ".join(message.command[1:])
            
            async with aiohttp.ClientSession() as session:
                async with session.get(
                    f"https://api.jikan.moe/v4/anime?q={anime_name}&limit=1"
                ) as resp:
                    data = await resp.json()
                    
                    if not data["data"]:
                        await message.reply("Anime not found!")
                        return
                    
                    anime = data["data"][0]
                    
                    title = anime.get("title", "Unknown")
                    synopsis = anime.get("synopsis", "No synopsis")[:500]
                    score = anime.get("score", "N/A")
                    episodes = anime.get("episodes", "Ongoing")
                    status = anime.get("status", "Unknown")
                    image = anime.get("images", {}).get("jpg", {}).get("image_url", "")
                    
                    text = f"""
{config.SPARKLE} **Anime** {config.WINK}
━━━━━━━━━━━━━━━━━━━
{config.CUTE} **Title:** {title}
{config.WINK} **Score:** {score}
{config.STAR} **Episodes:** {episodes}
{config.FIRE} **Status:** {status}
{config.symbols.DASH}
{config.symbols.ARROW} **Synopsis:**
{synopsis}
"""
                    if image:
                        await client.send_photo(
                            message.chat.id,
                            photo=image,
                            caption=text
                        )
                    else:
                        await message.reply(text)
        except Exception as e:
            log.error(f"Anime error: {e}")
            await message.reply("Error fetching anime!")
    
    # Manga command
    @bot.on_message(filters.command("manga"))
    async def manga(client, message):
        if len(message.command) < 2:
            await message.reply("Usage: /manga <manga name>")
            return
        
        try:
            manga_name = " ".join(message.command[1:])
            
            async with aiohttp.ClientSession() as session:
                async with session.get(
                    f"https://api.jikan.moe/v4/manga?q={manga_name}&limit=1"
                ) as resp:
                    data = await resp.json()
                    
                    if not data["data"]:
                        await message.reply("Manga not found!")
                        return
                    
                    manga = data["data"][0]
                    
                    title = manga.get("title", "Unknown")
                    synopsis = manga.get("synopsis", "No synopsis")[:500]
                    score = manga.get("score", "N/A")
                    chapters = manga.get("chapters", "Unknown")
                    volumes = manga.get("volumes", "Unknown")
                    status = manga.get("status", "Unknown")
                    image = manga.get("images", {}).get("jpg", {}).get("image_url", "")
                    
                    text = f"""
{config.SPARKLE} **Manga** {config.WINK}
━━━━━━━━━━━━━━━━━━━
{config.CUTE} **Title:** {title}
{config.WINK} **Score:** {score}
{config.STAR} **Chapters:** {chapters}
{config.FIRE} **Volumes:** {volumes}
{config.THUNDER} **Status:** {status}
{config.symbols.DASH}
{config.symbols.ARROW} **Synopsis:**
{synopsis}
"""
                    if image:
                        await client.send_photo(
                            message.chat.id,
                            photo=image,
                            caption=text
                        )
                    else:
                        await message.reply(text)
        except Exception as e:
            log.error(f"Manga error: {e}")
            await message.reply("Error fetching manga!")
    
    # Character command
    @bot.on_message(filters.command("character"))
    async def character(client, message):
        if len(message.command) < 2:
            await message.reply("Usage: /character <character name>")
            return
        
        try:
            char_name = " ".join(message.command[1:])
            
            async with aiohttp.ClientSession() as session:
                async with session.get(
                    f"https://api.jikan.moe/v4/characters?q={char_name}&limit=1"
                ) as resp:
                    data = await resp.json()
                    
                    if not data["data"]:
                        await message.reply("Character not found!")
                        return
                    
                    char = data["data"][0]
                    
                    name = char.get("name", "Unknown")
                    about = char.get("about", "No information")[:500]
                    image = char.get("images", {}).get("jpg", {}).get("image_url", "")
                    
                    text = f"""
{config.SPARKLE} **Character** {config.WINK}
━━━━━━━━━━━━━━━━━━━
{config.CUTE} **Name:** {name}
{config.symbols.DASH}
{config.symbols.ARROW} **About:**
{about}
"""
                    if image:
                        await client.send_photo(
                            message.chat.id,
                            photo=image,
                            caption=text
                        )
                    else:
                        await message.reply(text)
        except Exception as e:
            log.error(f"Character error: {e}")
            await message.reply("Error fetching character!")
    
    # Waifu command
    @bot.on_message(filters.command("waifu"))
    async def waifu(client, message):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get("https://api.waifu.pics/sfw/waifu") as resp:
                    data = await resp.json()
                    image_url = data["url"]
                    
                    await message.reply_photo(
                        photo=image_url,
                        caption=f"{config.SPARKLE} **Waifu** {config.WINK}\n{config.CUTE} Enjoy!"
                    )
        except Exception as e:
            log.error(f"Waifu error: {e}")
            await message.reply("Error fetching waifu!")
    
    # Neko command
    @bot.on_message(filters.command("neko"))
    async def neko(client, message):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get("https://api.waifu.pics/sfw/neko") as resp:
                    data = await resp.json()
                    image_url = data["url"]
                    
                    await message.reply_photo(
                        photo=image_url,
                        caption=f"{config.SPARKLE} **Neko** {config.WINK}\n{config.CUTE} Meow!"
                    )
        except Exception as e:
            log.error(f"Neko error: {e}")
            await message.reply("Error fetching neko!")
    
    # Shinobu command
    @bot.on_message(filters.command("shinobu"))
    async def shinobu(client, message):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get("https://api.waifu.pics/sfw/shinobu") as resp:
                    data = await resp.json()
                    image_url = data["url"]
                    
                    await message.reply_photo(
                        photo=image_url,
                        caption=f"{config.SPARKLE} **Shinobu** {config.WINK}\n{config.CUTE} Love you!"
                    )
        except Exception as e:
            log.error(f"Shinobu error: {e}")
            await message.reply("Error fetching shinobu!")
    
    # Megumin command
    @bot.on_message(filters.command("megumin"))
    async def megumin(client, message):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get("https://api.waifu.pics/sfw/megumin") as resp:
                    data = await resp.json()
                    image_url = data["url"]
                    
                    await message.reply_photo(
                        photo=image_url,
                        caption=f"{config.SPARKLE} **Megumin** {config.WINK}\n{config.CUTE} EXPLOSION!"
                    )
        except Exception as e:
            log.error(f"Megumin error: {e}")
            await message.reply("Error fetching Megumin!")
    
    # Kitsune command
    @bot.on_message(filters.command("kitsune"))
    async def kitsune(client, message):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get("https://api.waifu.pics/sfw/kitsune") as resp:
                    data = await resp.json()
                    image_url = data["url"]
                    
                    await message.reply_photo(
                        photo=image_url,
                        caption=f"{config.SPARKLE} **Kitsune** {config.WINK}\n{config.CUTE} Fox girl!"
                    )
        except Exception as e:
            log.error(f"Kitsune error: {e}")
            await message.reply("Error fetching kitsune!")
    
    # Bully command
    @bot.on_message(filters.command("bully"))
    async def bully(client, message):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get("https://api.waifu.pics/sfw/bully") as resp:
                    data = await resp.json()
                    image_url = data["url"]
                    
                    await message.reply_photo(
                        photo=image_url,
                        caption=f"{config.SPARKLE} **Bully** {config.WINK}\n{config.CUTE} (⁠≧⁠▽⁠≦⁠) "
                    )
        except Exception as e:
            log.error(f"Bully error: {e}")
            await message.reply("Error fetching image!")
    
    # Cuddle command
    @bot.on_message(filters.command("cuddle"))
    async def cuddle(client, message):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get("https://api.waifu.pics/sfw/cuddle") as resp:
                    data = await resp.json()
                    image_url = data["url"]
                    
                    await message.reply_photo(
                        photo=image_url,
                        caption=f"{config.SPARKLE} **Cuddle** {config.WINK}\n{config.CUTE} (⁠≧⁠◡⁠≦⁠) "
                    )
        except Exception as e:
            log.error(f"Cuddle error: {e}")
            await message.reply("Error fetching image!")
    
    # Cry command
    @bot.on_message(filters.command("cry"))
    async def cry(client, message):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get("https://api.waifu.pics/sfw/cry") as resp:
                    data = await resp.json()
                    image_url = data["url"]
                    
                    await message.reply_photo(
                        photo=image_url,
                        caption=f"{config.SPARKLE} **Cry** {config.WINK}\n{config.CUTE} (⁠╥⁠﹏⁠╥⁠) "
                    )
        except Exception as e:
            log.error(f"Cry error: {e}")
            await message.reply("Error fetching image!")
    
    # Hug command
    @bot.on_message(filters.command("hug"))
    async def hug(client, message):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get("https://api.waifu.pics/sfw/hug") as resp:
                    data = await resp.json()
                    image_url = data["url"]
                    
                    await message.reply_photo(
                        photo=image_url,
                        caption=f"{config.SPARKLE} **Hug** {config.WINK}\n{config.CUTE} (⁠づ⁠◡⁠﹏⁠◡⁠)⁠づ "
                    )
        except Exception as e:
            log.error(f"Hug error: {e}")
            await message.reply("Error fetching image!")
    
    # Kiss command
    @bot.on_message(filters.command("kiss"))
    async def kiss(client, message):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get("https://api.waifu.pics/sfw/kiss") as resp:
                    data = await resp.json()
                    image_url = data["url"]
                    
                    await message.reply_photo(
                        photo=image_url,
                        caption=f"{config.SPARKLE} **Kiss** {config.WINK}\n{config.CUTE} (⁠ﾉ⁠´⁠ヮ⁠`⁠) ⁠ﾉ⁠╭⁠══⁠╮ "
                    )
        except Exception as e:
            log.error(f"Kiss error: {e}")
            await message.reply("Error fetching image!")
    
    # slap command
    @bot.on_message(filters.command("slap"))
    async def slap(client, message):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get("https://api.waifu.pics/sfw/slap") as resp:
                    data = await resp.json()
                    image_url = data["url"]
                    
                    await message.reply_photo(
                        photo=image_url,
                        caption=f"{config.SPARKLE} **Slap** {config.WINK}\n{config.CUTE} (⁠ꏿ⁠﹏⁠ꏿ⁠) "
                    )
        except Exception as e:
            log.error(f"Slap error: {e}")
            await message.reply("Error fetching image!")
    
    # pat command
    @bot.on_message(filters.command("pat"))
    async def pat(client, message):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get("https://api.waifu.pics/sfw/pat") as resp:
                    data = await resp.json()
                    image_url = data["url"]
                    
                    await message.reply_photo(
                        photo=image_url,
                        caption=f"{config.SPARKLE} **Pat** {config.WINK}\n{config.CUTE} (⁠◡⁠‿⁠◡⁠✿⁠) "
                    )
        except Exception as e:
            log.error(f"Pat error: {e}")
            await message.reply("Error fetching image!")
    
    # smug command
    @bot.on_message(filters.command("smug"))
    async def smug(client, message):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get("https://api.waifu.pics/sfw/smug") as resp:
                    data = await resp.json()
                    image_url = data["url"]
                    
                    await message.reply_photo(
                        photo=image_url,
                        caption=f"{config.SPARKLE} **Smug** {config.WINK}\n{config.CUTE} (⁠￣⁠ー⁠￣⁠) "
                    )
        except Exception as e:
            log.error(f"Smug error: {e}")
            await message.reply("Error fetching image!")
    
    # blush command
    @bot.on_message(filters.command("blush"))
    async def blush(client, message):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get("https://api.waifu.pics/sfw/blush") as resp:
                    data = await resp.json()
                    image_url = data["url"]
                    
                    await message.reply_photo(
                        photo=image_url,
                        caption=f"{config.SPARKLE} **Blush** {config.WINK}\n{config.CUTE} (⁠≧⁠◡⁠≦⁠) "
                    )
        except Exception as e:
            log.error(f"Blush error: {e}")
            await message.reply("Error fetching image!")
    
    # smile command
    @bot.on_message(filters.command("smile"))
    async def smile(client, message):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get("https://api.waifu.pics/sfw/smile") as resp:
                    data = await resp.json()
                    image_url = data["url"]
                    
                    await message.reply_photo(
                        photo=image_url,
                        caption=f"{config.SPARKLE} **Smile** {config.WINK}\n{config.CUTE} (⁠◕⁠‿⁠◕⁠) "
                    )
        except Exception as e:
            log.error(f"Smile error: {e}")
            await message.reply("Error fetching image!")
