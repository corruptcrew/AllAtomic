"""
🎉 Fun & Entertainment for AllAtomic Userbot
Memes, Jokes, TTS, and more
"""

import asyncio
import aiohttp
import random
from telethon import events

from plugins import atomic_command
from app.utils import get_kaomoji

# Plugin metadata
__plugin__ = {
    "name": "Fun & Entertainment",
    "description": "Memes, jokes, TTS (inspired by top userbots)",
    "category": "fun"
}

@atomic_command(
    "meme",
    pattern=r"\.meme",
    help="Get random meme",
    usage=".meme",
    category="fun"
)
async def meme_handler(event):
    """Get random meme from Reddit"""
    msg = await event.edit(f"🎭 Getting meme... {get_kaomoji('thinking')}")
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://www.reddit.com/r/memes/random/.json") as resp:
                if resp.status == 200:
                    data = await resp.json()
                    post = data[0]['data']['children'][0]['data']
                    
                    title = post['title']
                    url = post['url']
                    author = post['author']
                    ups = post['ups']
                    
                    if url.endswith(('.jpg', '.png', '.gif')):
                        await msg.delete()
                        await event.client.send_file(
                            event.chat_id,
                            url,
                            caption=f"""
🎭 **Random Meme** {get_kaomoji('happy')}

📌 **Title:** {title[:100]}
👤 **Author:** u/{author}
⬆️ **Upvotes:** {ups}

💜 **AllAtomic Userbot**
📢 **Channel:** @ComputeCode
                            """,
                            parse_mode="md"
                        )
                    else:
                        await msg.edit(f"""
🎭 **Random Meme** {get_kaomoji('happy')}

📌 **Title:** {title[:200]}
👤 **Author:** u/{author}
⬆️ **Upvotes:** {ups}

🔗 [View Meme]({url})

💜 **AllAtomic Userbot**
📢 **Channel:** @ComputeCode
                        """, parse_mode="md", link_preview=True)
                    return
        
        await msg.edit("❌ Failed to get meme!")
        
    except Exception as e:
        await msg.edit(f"❌ Error: {e}")
    
    await asyncio.sleep(60)
    await msg.delete()

@atomic_command(
    "joke",
    pattern=r"\.joke",
    help="Get random joke",
    usage=".joke",
    category="fun"
)
async def joke_handler(event):
    """Get random joke"""
    msg = await event.edit(f"😂 Getting joke... {get_kaomoji('thinking')}")
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://v2.jokeapi.dev/joke/Any") as resp:
                if resp.status == 200:
                    data = await resp.json()
                    
                    if data['type'] == 'single':
                        joke = data['joke']
                    else:
                        joke = f"{data['setup']}\n\n{data['delivery']}"
                    
                    await msg.edit(f"""
😂 **Random Joke** {get_kaomoji('happy')}

━━━━━━━━━━━━━━━━━━━━━━

{joke}

━━━━━━━━━━━━━━━━━━━━━━

💜 **AllAtomic Userbot**
📢 **Channel:** @ComputeCode
🔗 **Repo:** github.com/GhostMarshal/AllAtomic
                    """, parse_mode="md")
                    return
        
        await msg.edit("❌ Failed to get joke!")
        
    except Exception as e:
        await msg.edit(f"❌ Error: {e}")
    
    await asyncio.sleep(60)
    await msg.delete()

@atomic_command(
    "tts",
    pattern=r"\.tts(?:\s|$)(.*)",
    help="Text to speech",
    usage=".tts <text>",
    category="fun"
)
async def tts_handler(event):
    """Text to speech"""
    text = event.pattern_match.group(1)
    
    if not text:
        reply = await event.get_reply_message()
        if reply and reply.text:
            text = reply.text
        else:
            await event.edit("❌ Provide text!")
            return
    
    msg = await event.edit(f"🔊 Converting to speech... {get_kaomoji('thinking')}")
    
    try:
        # Use Google TTS
        from gtts import gTTS
        
        tts = gTTS(text=text, lang='en')
        tts.save(f"tts_{event.id}.mp3")
        
        await msg.delete()
        
        await event.client.send_file(
            event.chat_id,
            f"tts_{event.id}.mp3",
            caption=f"🔊 TTS by AllAtomic\n\n💜 @ComputeCode",
            voice_note=True
        )
        
        # Cleanup
        import os
        os.remove(f"tts_{event.id}.mp3")
        
    except ImportError:
        await msg.edit("❌ Install gtts: `pip install gtts`")
    except Exception as e:
        await msg.edit(f"❌ Error: {e}")
    
    await asyncio.sleep(60)
    await msg.delete()

@atomic_command(
    "fact",
    pattern=r"\.fact",
    help="Get random fact",
    usage=".fact",
    category="fun"
)
async def fact_handler(event):
    """Get random fact"""
    msg = await event.edit(f"🧠 Getting fact... {get_kaomoji('thinking')}")
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://uselessfacts.jsph.pl/random.json?language=en") as resp:
                if resp.status == 200:
                    data = await resp.json()
                    fact = data['text']
                    
                    await msg.edit(f"""
🧠 **Random Fact** {get_kaomoji('happy')}

━━━━━━━━━━━━━━━━━━━━━━

{fact}

━━━━━━━━━━━━━━━━━━━━━━

💜 **AllAtomic Userbot**
📢 **Channel:** @ComputeCode
                    """, parse_mode="md")
                    return
        
        await msg.edit("❌ Failed to get fact!")
        
    except Exception as e:
        await msg.edit(f"❌ Error: {e}")
    
    await asyncio.sleep(60)
    await msg.delete()

@atomic_command(
    "quote",
    pattern=r"\.quote",
    help="Get inspiring quote",
    usage=".quote",
    category="fun"
)
async def quote_handler(event):
    """Get inspiring quote"""
    msg = await event.edit(f"💭 Getting quote... {get_kaomoji('thinking')}")
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.quotable.io/random") as resp:
                if resp.status == 200:
                    data = await resp.json()
                    content = data['content']
                    author = data['author']
                    
                    await msg.edit(f"""
💭 **Inspiring Quote** {get_kaomoji('happy')}

━━━━━━━━━━━━━━━━━━━━━━

"{content}"

— *{author}*

━━━━━━━━━━━━━━━━━━━━━━

💜 **AllAtomic Userbot**
📢 **Channel:** @ComputeCode
                    """, parse_mode="md")
                    return
        
        await msg.edit("❌ Failed to get quote!")
        
    except Exception as e:
        await msg.edit(f"❌ Error: {e}")
    
    await asyncio.sleep(60)
    await msg.delete()

@atomic_command(
    "roll",
    pattern=r"\.roll(?:\s|$)(.*)",
    help="Roll dice",
    usage=".roll [sides]",
    category="fun"
)
async def roll_handler(event):
    """Roll dice"""
    args = event.pattern_match.group(1)
    
    try:
        sides = int(args) if args else 6
        
        if sides < 2 or sides > 100:
            sides = 6
        
        result = random.randint(1, sides)
        
        await event.edit(f"""
🎲 **Dice Roll** {get_kaomoji('happy')}

━━━━━━━━━━━━━━━━━━━━━━

**Result:** `{result}` / {sides}

💜 **AllAtomic Userbot**
📢 **Channel:** @ComputeCode
        """, parse_mode="md")
        
    except:
        await event.edit("❌ Invalid number!")
    
    await asyncio.sleep(30)
    await event.delete()

@atomic_command(
    "coin",
    pattern=r"\.coin",
    help="Flip a coin",
    usage=".coin",
    category="fun"
)
async def coin_handler(event):
    """Flip a coin"""
    result = random.choice(["Heads", "Tails"])
    
    await event.edit(f"""
🪙 **Coin Flip** {get_kaomoji('happy')}

━━━━━━━━━━━━━━━━━━━━━━

**Result:** `{result}`

💜 **AllAtomic Userbot**
📢 **Channel:** @ComputeCode
    """, parse_mode="md")
    
    await asyncio.sleep(30)
    await event.delete()

# Commands registry
commands = {
    "meme": {
        "help": "Get random meme",
        "usage": ".meme",
        "category": "fun"
    },
    "joke": {
        "help": "Get random joke",
        "usage": ".joke",
        "category": "fun"
    },
    "tts": {
        "help": "Text to speech",
        "usage": ".tts <text>",
        "category": "fun"
    },
    "fact": {
        "help": "Get random fact",
        "usage": ".fact",
        "category": "fun"
    },
    "quote": {
        "help": "Get inspiring quote",
        "usage": ".quote",
        "category": "fun"
    },
    "roll": {
        "help": "Roll dice",
        "usage": ".roll [sides]",
        "category": "fun"
    },
    "coin": {
        "help": "Flip a coin",
        "usage": ".coin",
        "category": "fun"
    }
}
