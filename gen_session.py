#!/usr/bin/env python3
"""
🔐 Session Generator - AllAtomic
"""

from telethon.sync import TelegramClient
from telethon.sessions import StringSession

API_ID = 38568281
API_HASH = "5dec3f281b9576f65824326f7cd984ed"

print("🔐 AllAtomic Session Generator")
print("="*50)

phone = input("📱 Enter phone number: ")

with TelegramClient(StringSession(), API_ID, API_HASH) as client:
    client.send_code_request(phone)
    print("Code sent!")
    code = input("🔢 Enter verification code from Telegram: ")
    client.sign_in(phone=phone, code=code)
    session = client.session.save()
    
    print()
    print("="*50)
    print("✅ SESSION STRING GENERATED!")
    print("="*50)
    print(f"\n{session}\n")
    print("="*50)
