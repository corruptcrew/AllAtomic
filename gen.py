#!/usr/bin/env python3
"""🔐 Session Generator"""
from telethon.sync import TelegramClient
from telethon.sessions import StringSession

print("🔐 AllAtomic Session Generator")
print("="*50)

with TelegramClient(StringSession(), 38568281, "5dec3f281b9576f65824326f7cd984ed") as client:
    print("📱 Sending code to +31613044783...")
    client.send_code_request('+31613044783')
    print("✅ Code sent! Check your Telegram app.")
    code = input("🔢 Enter code: ")
    client.sign_in(phone='+31613044783', code=code)
    session = client.session.save()
    print("\n" + "="*50)
    print("✅ SESSION STRING GENERATED!")
    print("="*50)
    print(f"\n{session}\n")
    print("="*50)
