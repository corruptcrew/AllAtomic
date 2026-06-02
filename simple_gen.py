#!/usr/bin/env python3
"""
🔐 Simple Session Generator - AllAtomic
Run: python3 simple_gen.py
"""

from telethon.sync import TelegramClient
from telethon.sessions import StringSession

# Your API credentials
API_ID = 38568281
API_HASH = "5dec3f281b9576f65824326f7cd984ed"

print("""
╔══════════════════════════════════════════════════╗
║     🔐 AllAtomic Session Generator               ║
╚══════════════════════════════════════════════════╝
""")

phone = input("📱 Enter phone number (+31613044783): ")

with TelegramClient(StringSession(), API_ID, API_HASH) as client:
    print("\n📱 Code sent to your Telegram app!")
    code = input("🔢 Enter verification code: ")
    
    try:
        client.sign_in(phone=phone, code=code)
        session = client.session.save()
        
        print("\n" + "="*50)
        print("✅ SESSION STRING GENERATED!")
        print("="*50)
        print(f"\n🔑 {session}\n")
        print("="*50)
        print("\n⚠️  Save this in .env as SESSION_STRING")
        print("💜 AllAtomic - @GhostMarshal | @ComputeCode")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("   Make sure the code is correct!")
