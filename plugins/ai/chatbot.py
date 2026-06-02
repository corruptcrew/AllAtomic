"""
🤖 AI Chatbot for AllAtomic Userbot
Chat with AI using OpenAI API
"""

import asyncio
import aiohttp
from telethon import events

from plugins import atomic_command
from app.utils import get_kaomoji

# Plugin metadata
__plugin__ = {
    "name": "AI Chatbot",
    "description": "Chat with AI",
    "category": "ai"
}

@atomic_command(
    "chat",
    pattern=r"\.chat(?:\s|$)(.*)",
    help="Chat with AI",
    usage=".chat <message>",
    category="ai"
)
async def chat_handler(event):
    """Chat with AI"""
    from app import config
    
    message = event.pattern_match.group(1)
    
    if not message:
        await event.edit("❌ Please provide a message to chat!\n\nUsage: `.chat <message>`")
        return
    
    if not config.AI_ENABLED:
        await event.edit("⚠️ AI features are disabled!\n\nEnable in `.env` with `AI_ENABLED=True`")
        return
    
    msg = await event.edit("🤖 Chatting with AI... {get_kaomoji('thinking')}")
    
    try:
        if not config.OPENAI_API:
            await msg.edit("❌ OpenAI API key not configured!\n\nGet from: https://platform.openai.com/api-keys")
            return
        
        # Use OpenAI API
        async with aiohttp.ClientSession() as session:
            async with session.post(
                "https://api.openai.com/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {config.OPENAI_API}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": "gpt-3.5-turbo",
                    "messages": [
                        {"role": "system", "content": "You are a helpful assistant for AllAtomic Userbot."},
                        {"role": "user", "content": message}
                    ],
                    "max_tokens": 500
                }
            ) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    response = data['choices'][0]['message']['content']
                    
                    chat_msg = f"""
🤖 **AI Response** {get_kaomoji('happy')}

━━━━━━━━━━━━━━━━━━━━━━

💬 **You:** `{message}`

🤖 **AI:** `{response}`

━━━━━━━━━━━━━━━━━━━━━━

💜 AllAtomic Userbot
                    """
                    
                    await msg.edit(chat_msg, parse_mode="md")
                else:
                    await msg.edit(f"❌ API Error: {resp.status}")
        
    except Exception as e:
        await msg.edit(f"❌ Error: {e}")
    
    await asyncio.sleep(60)
    await msg.delete()

@atomic_command(
    "ask",
    pattern=r"\.ask(?:\s|$)(.*)",
    help="Ask AI a question",
    usage=".ask <question>",
    category="ai"
)
async def ask_handler(event):
    """Ask AI a question"""
    from app import config
    
    question = event.pattern_match.group(1)
    
    if not question:
        await event.edit("❌ Please provide a question!\n\nUsage: `.ask <question>`")
        return
    
    if not config.AI_ENABLED:
        await event.edit("⚠️ AI features are disabled!")
        return
    
    msg = await event.edit("🤖 Asking AI... {get_kaomoji('thinking')}")
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(
                "https://api.openai.com/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {config.OPENAI_API}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": "gpt-3.5-turbo",
                    "messages": [
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": question}
                    ],
                    "max_tokens": 300
                }
            ) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    response = data['choices'][0]['message']['content']
                    
                    ask_msg = f"""
❓ **Question:** `{question}`

━━━━━━━━━━━━━━━━━━━━━━

🤖 **Answer:** `{response}`

━━━━━━━━━━━━━━━━━━━━━━

💜 AllAtomic Userbot
                    """
                    
                    await msg.edit(ask_msg, parse_mode="md")
                else:
                    await msg.edit(f"❌ Error: {resp.status}")
        
    except Exception as e:
        await msg.edit(f"❌ Error: {e}")
    
    await asyncio.sleep(60)
    await msg.delete()

@atomic_command(
    "summarize",
    pattern=r"\.summarize(?:\s|$)(.*)",
    help="Summarize text",
    usage=".summarize <text>",
    category="ai"
)
async def summarize_handler(event):
    """Summarize text"""
    from app import config
    
    text = event.pattern_match.group(1)
    
    if not text:
        # Try to get from reply
        reply = await event.get_reply_message()
        if reply and reply.text:
            text = reply.text
        else:
            await event.edit("❌ Please provide text to summarize!\n\nUsage: `.summarize <text>`")
            return
    
    if not config.AI_ENABLED:
        await event.edit("⚠️ AI features are disabled!")
        return
    
    msg = await event.edit("🤖 Summarizing... {get_kaomoji('thinking')}")
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(
                "https://api.openai.com/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {config.OPENAI_API}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": "gpt-3.5-turbo",
                    "messages": [
                        {"role": "system", "content": "Summarize this text concisely."},
                        {"role": "user", "content": f"Summarize: {text[:1500]}"}
                    ],
                    "max_tokens": 200
                }
            ) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    summary = data['choices'][0]['message']['content']
                    
                    summary_msg = f"""
📝 **Summary** {get_kaomoji('happy')}

━━━━━━━━━━━━━━━━━━━━━━

{summary}

━━━━━━━━━━━━━━━━━━━━━━

💜 AllAtomic Userbot
                    """
                    
                    await msg.edit(summary_msg, parse_mode="md")
                else:
                    await msg.edit(f"❌ Error: {resp.status}")
        
    except Exception as e:
        await msg.edit(f"❌ Error: {e}")
    
    await asyncio.sleep(60)
    await msg.delete()

# Commands registry
commands = {
    "chat": {
        "help": "Chat with AI",
        "usage": ".chat <message>",
        "category": "ai"
    },
    "ask": {
        "help": "Ask AI a question",
        "usage": ".ask <question>",
        "category": "ai"
    },
    "summarize": {
        "help": "Summarize text",
        "usage": ".summarize <text>",
        "category": "ai"
    }
}
