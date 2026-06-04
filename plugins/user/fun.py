"""
AllAtomic - Fun Commands Plugin
Dev: @GhostMarshal | Channel: @ComputeCode
(૨๑•̀ㅁ•́ฅา) Purple Anime Theme (#9A8CFF)
"""

import random
from pyrogram import filters
from AllAtomic import log, clients, config


# Random quotes
QUOTES = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "Get busy living or get busy dying. - Stephen King",
    "You only live once, but if you do it right, once is enough. - Mae West",
    "The journey of a thousand miles begins with one step. - Lao Tzu",
    "That which does not kill us makes us stronger. - Friedrich Nietzsche",
    "Be the change that you wish to see in the world. - Mahatma Gandhi",
    "In the end, it's not the years in your life that count. It's the life in your years. - Abraham Lincoln",
    "Life is either a daring adventure or nothing at all. - Helen Keller",
    "Many of life's failures are people who did not realize how close they were to success. - Thomas Edison",
]

# Jokes
JOKES = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the scarecrow win an award? He was outstanding in his field!",
    "Why don't eggs tell jokes? They'd crack each other up!",
    "What do you call a fake noodle? An impasta!",
    "Why did the bicycle fall over? Because it was two-tired!",
    "What do you call a bear with no teeth? A gummy bear!",
    "Why don't skeletons fight each other? They don't have the guts!",
    "What do you call cheese that isn't yours? Nacho cheese!",
    "Why couldn't the leopard play hide and seek? Because he was always spotted!",
    "What do you call a fish wearing a bowtie? Sofishticated!",
]

# Waifu images (placeholder URLs)
WAFIU_URLS = [
    "https://waifu.pics/api/sfw/waifu",
    "https://api.waifu.pics/sfw/waifu",
]

# Meme subreddits
MEME_REDDITS = [
    "memes",
    "dankmemes",
    "me_irl",
    "wholesomememes",
    "comedyheaven",
]


async def load(bot):
    """Load plugin (✿◠‿◠)"""
    
    # Meme command
    @bot.on_message(filters.command("meme"))
    async def meme(client, message):
        try:
            import aiohttp
            
            subreddit = random.choice(MEME_REDDITS)
            async with aiohttp.ClientSession() as session:
                async with session.get(f"https://www.reddit.com/r/{subreddit}/hot.json?limit=1") as resp:
                    data = await resp.json()
                    post = data["data"]["children"][0]["data"]
                    image_url = post["url"]
                    
                    await message.reply_photo(
                        photo=image_url,
                        caption=f"{config.SPARKLE} **Meme** {config.WINK}\n{config.CUTE} r/{subreddit}"
                    )
        except Exception as e:
            log.error(f"Meme error: {e}")
            await message.reply("Error fetching meme!")
    
    # Joke command
    @bot.on_message(filters.command("joke"))
    async def joke(client, message):
        joke_text = random.choice(JOKES)
        await message.reply(f"{config.CUTE} **Joke** {config.WINK}\n{config.WINK}\n{joke_text}\n{config.LINE}")
    
    # Quote command
    @bot.on_message(filters.command("quote"))
    async def quote(client, message):
        quote_text = random.choice(QUOTES)
        await message.reply(f"{config.SPARKLE} **Quote** {config.WINK}\n{config.LINE}\n{quote_text}\n{config.LINE}")
    
    # Roll command
    @bot.on_message(filters.command("roll"))
    async def roll(client, message):
        dice = random.randint(1, 6)
        await message.reply(f"{config.CUTE} **Rolled:** {dice} {config.WINK}")
    
    # Flip command (coin flip)
    @bot.on_message(filters.command("flip"))
    async def flip(client, message):
        result = random.choice(["Heads", "Tails"])
        await message.reply(f"{config.SPARKLE} **Coin Flip:** {result} {config.WINK}")
    
    # Choose command
    @bot.on_message(filters.command("choose"))
    async def choose(client, message):
        if len(message.command) < 2:
            await message.reply("Usage: /choose option1, option2, option3...")
            return
        
        options = message.text.split("/choose", 1)[1].split(",")
        options = [opt.strip() for opt in options]
        
        choice = random.choice(options)
        await message.reply(f"{config.SPARKLE} **I choose:** {choice} {config.WINK}")
    
    # Dice command
    @bot.on_message(filters.command("dice"))
    async def dice(client, message):
        dice = random.randint(1, 6)
        await message.reply(f"{config.CUTE} 🎲 {dice} {config.WINK}")
    
    # Rock Paper Scissors
    @bot.on_message(filters.command("rps"))
    async def rps(client, message):
        choices = ["rock", "paper", "scissors"]
        user_choice = message.text.split()[1].lower() if len(message.text.split()) > 1 else None
        
        if not user_choice or user_choice not in choices:
            await message.reply("Usage: /rps rock|paper|scissors")
            return
        
        bot_choice = random.choice(choices)
        
        if user_choice == bot_choice:
            result = "It's a tie!"
        elif (user_choice == "rock" and bot_choice == "scissors") or \
             (user_choice == "paper" and bot_choice == "rock") or \
             (user_choice == "scissors" and bot_choice == "paper"):
            result = "You win!"
        else:
            result = "You lose!"
        
        await message.reply(f"{config.SPARKLE} **You:** {user_choice}\n{config.WINK} **Bot:** {bot_choice}\n{config.CUTE} {result}")
    
    # Pick command
    @bot.on_message(filters.command("pick"))
    async def pick(client, message):
        if len(message.command) < 2:
            await message.reply("Usage: /pick option1, option2, option3...")
            return
        
        options = message.text.split("/pick", 1)[1].split(",")
        options = [opt.strip() for opt in options]
        
        picked = random.choice(options)
        await message.reply(f"{config.SPARKLE} **I pick:** {picked} {config.WINK}")
    
    # Shout command
    @bot.on_message(filters.command("shout"))
    async def shout(client, message):
        if len(message.command) < 2:
            await message.reply("Usage: /shout <text>")
            return
        
        text = " ".join(message.command[1:])
        await message.reply(text.upper())
    
    # Whisper command
    @bot.on_message(filters.command("whisper"))
    async def whisper(client, message):
        if len(message.command) < 2:
            await message.reply("Usage: /whisper <text>")
            return
        
        text = " ".join(message.command[1:])
        await message.reply(text.lower())
    
    # Reverse command
    @bot.on_message(filters.command("reverse"))
    async def reverse(client, message):
        if len(message.command) < 2:
            await message.reply("Usage: /reverse <text>")
            return
        
        text = " ".join(message.command[1:])
        reversed_text = text[::-1]
        await message.reply(reversed_text)
    
    # Flip text command
    @bot.on_message(filters.command("flip"))
    async def flip_text(client, message):
        if len(message.command) < 2:
            await message.reply("Usage: /flip <text>")
            return
        
        text = " ".join(message.command[1:])
        flipped = text.translate(str.maketrans("abcdefghijklmnopqrstuvwxyz", "zyxwvutsrqponmlkjihgfedcba"))
        await message.reply(flipped)
    
    # Waifu command
    @bot.on_message(filters.command("waifu"))
    async def waifu(client, message):
        try:
            import aiohttp
            
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
            import aiohttp
            
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
    
    # Kitsune command
    @bot.on_message(filters.command("kitsune"))
    async def kitsune(client, message):
        try:
            import aiohttp
            
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
    
    # Shinobu command
    @bot.on_message(filters.command("shinobu"))
    async def shinobu(client, message):
        try:
            import aiohttp
            
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
            import aiohttp
            
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
