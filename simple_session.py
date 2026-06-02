#!/usr/bin/env python3
"""
🔐 Simple Session Gen - AllAtomic
Minimal script with explicit connection settings
"""

import sys
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.errors import SessionPasswordNeededError

API_ID = 38568281
API_HASH = "5dec3f281b9576f65824326f7cd984ed"
PHONE = "+31613044783"

print("🔐 AllAtomic Session Generator")
print("="*50)
print(f"📱 Phone: {PHONE}")
print("="*50)

session = StringSession()
client = TelegramClient(session, API_ID, API_HASH)

print("\n📡 Connecting to Telegram...")
client.connect()

if not client.is_connected():
    print("❌ Failed to connect to Telegram servers")
    print("\n💡 This environment may block Telegram connections.")
    print("   Use @strgen_bot on Telegram instead:")
    print("   https://t.me/strgen_bot")
    sys.exit(1)

print("✅ Connected!")

if not client.is_user_authorized():
    print("\n📡 Sending code request...")
    try:
        client.send_code_request(PHONE)
        print("✅ Code sent! Check your Telegram app.")
        
        code = input("\n🔢 Enter verification code: ").strip()
        
        try:
            client.sign_in(PHONE, code)
        except SessionPasswordNeededError:
            print("\n🔒 2FA enabled!")
            password = input("🔑 Enter password: ").strip()
            client.sign_in(password=password)
            
    except Exception as e:
        print(f"❌ Error: {e}")
        client.disconnect()
        sys.exit(1)

# Get session string
session_string = client.session.save()
client.disconnect()

print("\n" + "="*50)
print("✅ SESSION GENERATED!")
print("="*50)
print(f"\n🔑 {session_string}\n")
print("="*50)
print("\n💜 AllAtomic - @GhostMarshal | @ComputeCode")
