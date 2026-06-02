#!/usr/bin/env python3
"""
🔐 Session Creator - from telegram-session-maker
https://github.com/py-hariom/telegram-session-maker
"""

import os
import logging
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.errors import SessionPasswordNeededError, RPCError, PhoneCodeInvalidError, PhoneCodeExpiredError

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

API_ID = 38568281
API_HASH = "5dec3f281b9576f65824326f7cd984ed"

print("""
╔═══════════════════════════════════════════════════════╗
║     🔐 Session String Generator (Telethon)            ║
║                                                       ║
║   Source: github.com/py-hariom/telegram-session-maker ║
║   AllAtomic Edition: @GhostMarshal | @ComputeCode     ║
╚═══════════════════════════════════════════════════════╝
""")

def create_session():
    """Create a Telegram session string."""
    try:
        session_name = input("Enter session name (e.g., allatomic): ").strip() or "allatomic"
        
        with TelegramClient(StringSession(), int(API_ID), API_HASH) as client:
            if client.is_user_authorized():
                print("✅ Already authorized!")
                return
            
            phone = input("\n📱 Please enter your phone (or bot token): ").strip()
            client.send_code_request(phone)
            
            code = input("🔢 Enter the code you received: ").strip()
            
            try:
                client.sign_in(phone, code)
            except SessionPasswordNeededError:
                password = input("🔑 Please enter your 2FA password: ").strip()
                client.sign_in(password=password)
            except (PhoneCodeInvalidError, PhoneCodeExpiredError):
                print("❌ The code you entered is invalid or has expired.")
                return
            except RPCError as e:
                print(f"❌ RPC Error: {e}")
                return
            
            session = client.session.save()
            
            print("\n" + "="*60)
            print("✅ SESSION STRING GENERATED!")
            print("="*60)
            print(f"\n🔑 {session}\n")
            print("="*60)
            print("\n💜 AllAtomic - @GhostMarshal | @ComputeCode")
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    create_session()
