#!/usr/bin/env python3
"""Simple async session generator"""
import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

API_ID = 38568281
API_HASH = "5dec3f281b9576f65824326f7cd984ed"
PHONE = "+31613044783"

async def main():
    print("🔐 Connecting to Telegram...")
    async with TelegramClient(StringSession(), API_ID, API_HASH) as client:
        print("📡 Sending code...")
        await client.send_code_request(PHONE)
        print("✅ Code sent! Check Telegram.")
        code = input("🔢 Enter code: ")
        await client.sign_in(PHONE, code)
        session = client.session.save()
        print(f"\n✅ SESSION: {session}\n")

asyncio.run(main())
