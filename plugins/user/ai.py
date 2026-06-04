"""
AllAtomic - AI Commands Plugin
Dev: @GhostMarshal | Channel: @ComputeCode
(૨๑•̀ㅁ•́ฅा) Purple Anime Theme (#9A8CFF)
"""

import aiohttp
from pyrogram import filters
from AllAtomic import log, config


async def load(bot):
    """Load plugin (✿◠‿◠)"""
    
    # AI chat command
    @bot.on_message(filters.command("ai"))
    async def ai(client, message):
        if len(message.command) < 2:
            await message.reply("Usage: /ai <message>")
            return
        
        try:
            user_message = " ".join(message.command[1:])
            
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    "https://api.openai.com/v1/chat/completions",
                    json={
                        "model": "gpt-3.5-turbo",
                        "messages": [
                            {"role": "system", "content": "You are AllAtomic, a helpful AI assistant created by @GhostMarshal. Keep responses concise and friendly."},
                            {"role": "user", "content": user_message}
                        ]
                    },
                    headers={
                        "Authorization": f"Bearer {config.OPENAI_API_KEY}",
                        "Content-Type": "application/json"
                    }
                ) as resp:
                    data = await resp.json()
                    
                    if "error" in data:
                        await message.reply(f"Error: {data['error']['message']}")
                        return
                    
                    response = data["choices"][0]["message"]["content"]
                    
                    await message.reply(
                        f"{config.SPARKLE} **AI Response** {config.WINK}\n{config.LINE}\n{response}\n{config.LINE}"
                    )
        except Exception as e:
            log.error(f"AI error: {e}")
            await message.reply("Error processing request!")
    
    # DALL-E image generation
    @bot.on_message(filters.command("dall"))
    async def dall(client, message):
        if len(message.command) < 2:
            await message.reply("Usage: /dall <prompt>")
            return
        
        try:
            prompt = " ".join(message.command[1:])
            
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    "https://api.openai.com/v1/images/generations",
                    json={
                        "model": "dall-e-3",
                        "prompt": prompt,
                        "n": 1,
                        "size": "1024x1024"
                    },
                    headers={
                        "Authorization": f"Bearer {config.OPENAI_API_KEY}",
                        "Content-Type": "application/json"
                    }
                ) as resp:
                    data = await resp.json()
                    
                    if "error" in data:
                        await message.reply(f"Error: {data['error']['message']}")
                        return
                    
                    image_url = data["data"][0]["url"]
                    
                    await message.reply_photo(
                        photo=image_url,
                        caption=f"{config.SPARKLE} **AI Image** {config.WINK}\n{config.CUTE} Prompt: {prompt}"
                    )
        except Exception as e:
            log.error(f"DALL-E error: {e}")
            await message.reply("Error generating image!")
    
    # Translate command
    @bot.on_message(filters.command("translate"))
    async def translate(client, message):
        if len(message.command) < 2:
            await message.reply("Usage: /translate <language> <text>")
            return
        
        try:
            target_lang = message.command[1]
            text = " ".join(message.command[2:])
            
            async with aiohttp.ClientSession() as session:
                async with session.get(
                    f"https://api.mymemory.translated.net/get?q={text}&langpair=en|{target_lang}"
                ) as resp:
                    data = await resp.json()
                    
                    if "responseData" in data:
                        translated = data["responseData"]["translatedText"]
                        await message.reply(
                            f"{config.SPARKLE} **Translated** {config.WINK}\n{config.LINE}\n{translated}\n{config.LINE}"
                        )
                    else:
                        await message.reply("Translation not found!")
        except Exception as e:
            log.error(f"Translate error: {e}")
            await message.reply("Error translating!")
    
    # Wiki command
    @bot.on_message(filters.command("wiki"))
    async def wiki(client, message):
        if len(message.command) < 2:
            await message.reply("Usage: /wiki <topic>")
            return
        
        try:
            topic = " ".join(message.command[1:])
            
            async with aiohttp.ClientSession() as session:
                async with session.get(
                    f"https://en.wikipedia.org/api/rest_v1/page/summary/{topic}"
                ) as resp:
                    data = await resp.json()
                    
                    if resp.status == 200:
                        title = data.get("title", "Unknown")
                        extract = data.get("extract", "No description")[:500]
                        image = data.get("thumbnail", {}).get("source", "")
                        
                        text = f"""
{config.SPARKLE} **Wikipedia** {config.WINK}
━━━━━━━━━━━━━━━━━━━
{config.CUTE} **Title:** {title}
{config.symbols.DASH}
{config.symbols.ARROW} **Summary:**
{extract}
"""
                        if image:
                            await client.send_photo(
                                message.chat.id,
                                photo=image,
                                caption=text
                            )
                        else:
                            await message.reply(text)
                    else:
                        await message.reply("Page not found!")
        except Exception as e:
            log.error(f"Wiki error: {e}")
            await message.reply("Error fetching Wikipedia!")
    
    # Weather command
    @bot.on_message(filters.command("weather"))
    async def weather(client, message):
        if len(message.command) < 2:
            await message.reply("Usage: /weather <city>")
            return
        
        try:
            city = " ".join(message.command[1:])
            
            async with aiohttp.ClientSession() as session:
                async with session.get(
                    f"http://wttr.in/{city}?format=%C+%t+%w"
                ) as resp:
                    weather_data = await resp.text()
                    
                    await message.reply(
                        f"{config.SPARKLE} **Weather** {config.WINK}\n{config.LINE}\n{weather_data} {config.CUTE}\n{config.LINE}"
                    )
        except Exception as e:
            log.error(f"Weather error: {e}")
            await message.reply("Error fetching weather!")
    
    # Trivia command
    @bot.on_message(filters.command("trivia"))
    async def trivia(client, message):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get("https://opentdb.com/api.php?amount=1&type=multiple") as resp:
                    data = await resp.json()
                    
                    if data["results"]:
                        question = data["results"][0]["question"]
                        answers = data["results"][0]["incorrect_answers"] + [data["results"][0]["correct_answer"]]
                        
                        import random
                        random.shuffle(answers)
                        
                        text = f"{config.SPARKLE} **Trivia** {config.WINK}\n{config.LINE}\n{question}\n{config.LINE}\n"
                        for i, answer in enumerate(answers, 1):
                            text += f"{i}. {answer}\n"
                        
                        await message.reply(text)
        except Exception as e:
            log.error(f"Trivia error: {e}")
            await message.reply("Error fetching trivia!")
    
    # Quote command
    @bot.on_message(filters.command("quote"))
    async def quote(client, message):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get("https://api.quotable.io/random") as resp:
                    data = await resp.json()
                    
                    quote = data["content"]
                    author = data["author"]
                    
                    await message.reply(
                        f"{config.SPARKLE} **Quote** {config.WINK}\n{config.LINE}\n\"{quote}\" - {author}\n{config.LINE}"
                    )
        except Exception as e:
            log.error(f"Quote error: {e}")
            await message.reply("Error fetching quote!")
    
    # Fact command
    @bot.on_message(filters.command("fact"))
    async def fact(client, message):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get("https://uselessfacts.jsph.pl/random.json?language=en") as resp:
                    data = await resp.json()
                    
                    await message.reply(
                        f"{config.SPARKLE} **Fact** {config.WINK}\n{config.LINE}\n{data['text']}\n{config.LINE}"
                    )
        except Exception as e:
            log.error(f"Fact error: {e}")
            await message.reply("Error fetching fact!")
    
    # Joke command
    @bot.on_message(filters.command("joke"))
    async def joke(client, message):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get("https://icanhazdadjoke.com/", headers={"Accept": "application/json"}) as resp:
                    data = await resp.json()
                    
                    await message.reply(
                        f"{config.SPARKLE} **Joke** {config.WINK}\n{config.LINE}\n{data['joke']}\n{config.LINE}"
                    )
        except Exception as e:
            log.error(f"Joke error: {e}")
            await message.reply("Error fetching joke!")
    
    # News command
    @bot.on_message(filters.command("news"))
    async def news(client, message):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(
                    "https://newsapi.org/v2/top-headlines?country=us&apiKey=" + config.NEWS_API_KEY
                ) as resp:
                    data = await resp.json()
                    
                    if data["articles"]:
                        article = data["articles"][0]
                        text = f"""
{config.SPARKLE} **News** {config.WINK}
━━━━━━━━━━━━━━━━━━━
{config.CUTE} **Title:** {article['title']}
{config.WINK} **Source:** {article['source']['name']}
{config.symbols.DASH}
{config.symbols.ARROW} **Description:**
{article['description']}
"""
                        await message.reply(text)
                    else:
                        await message.reply("No news found!")
        except Exception as e:
            log.error(f"News error: {e}")
            await message.reply("Error fetching news!")
    
    # Define command
    @bot.on_message(filters.command("define"))
    async def define(client, message):
        if len(message.command) < 2:
            await message.reply("Usage: /define <word>")
            return
        
        try:
            word = message.command[1]
            
            async with aiohttp.ClientSession() as session:
                async with session.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}") as resp:
                    data = await resp.json()
                    
                    if isinstance(data, list) and data:
                        word_data = data[0]
                        word = word_data["word"]
                        definition = word_data["meanings"][0]["definitions"][0]["definition"]
                        
                        await message.reply(
                            f"{config.SPARKLE} **Definition** {config.WINK}\n{config.LINE}\n{word}: {definition}\n{config.LINE}"
                        )
                    else:
                        await message.reply("Word not found!")
        except Exception as e:
            log.error(f"Define error: {e}")
            await message.reply("Error fetching definition!")
    
    # Currency command
    @bot.on_message(filters.command("currency"))
    async def currency(client, message):
        if len(message.command) < 3:
            await message.reply("Usage: /currency <from> <to>")
            return
        
        try:
            from_currency = message.command[1].upper()
            to_currency = message.command[2].upper()
            
            async with aiohttp.ClientSession() as session:
                async with session.get(
                    f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
                ) as resp:
                    data = await resp.json()
                    
                    rate = data["rates"].get(to_currency, "N/A")
                    
                    await message.reply(
                        f"{config.SPARKLE} **Currency** {config.WINK}\n{config.LINE}\n1 {from_currency} = {rate} {to_currency}\n{config.LINE}"
                    )
        except Exception as e:
            log.error(f"Currency error: {e}")
            await message.reply("Error fetching currency!")
    
    # Speedtest command
    @bot.on_message(filters.command("speedtest"))
    async def speedtest(client, message):
        try:
            import speedtest
            
            st = speedtest.Speedtest()
            st.get_best_server()
            download = st.download() / 1024 / 1024
            upload = st.upload / 1024 / 1024
            ping = st.results.ping
            
            await message.reply(
                f"{config.SPARKLE} **Speedtest** {config.WINK}\n{config.LINE}\n{config.CUTE} Download: {download:.2f} Mbps\n{config.WINK} Upload: {upload:.2f} Mbps\n{config.STAR} Ping: {ping:.2f} ms\n{config.LINE}"
            )
        except Exception as e:
            log.error(f"Speedtest error: {e}")
            await message.reply("Error running speedtest!")
