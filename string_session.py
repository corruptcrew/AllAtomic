#!/usr/bin/env python3
"""
🔐 String Session Generator - AllAtomic
Generates Telethon session string for userbot deployment

Usage: python3 string_session.py
"""

import asyncio
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from telethon.errors import SessionPasswordNeededError

# Configuration
API_ID = 38568281
API_HASH = "5dec3f281b9576f65824326f7cd984ed"

print("""
╔═══════════════════════════════════════════════════════╗
║        🔐 AllAtomic String Session Generator          ║
║                                                       ║
║   Generate session string for Telegram userbot        ║
║                                                       ║
║   Dev: @GhostMarshal | Channel: @ComputeCode          ║
╚═══════════════════════════════════════════════════════╝
""")

async def generate_session():
    """Generate Telethon session string"""
    
    # Get phone number
    phone = input("\n📱 Enter phone number (e.g., +31613044783): ").strip()
    
    if not phone:
        print("❌ Phone number cannot be empty!")
        return
    
    async with TelegramClient(StringSession(), API_ID, API_HASH) as client:
        # Send code request
        print("\n📡 Sending verification code...")
        
        try:
            result = await client.send_code_request(phone)
        except Exception as e:
            print(f"❌ Failed to send code: {e}")
            return
        
        print("✅ Code sent to your Telegram app!")
        print("   Check your Telegram messages for the verification code.\n")
        
        # Get verification code
        code = input("🔢 Enter verification code: ").strip()
        
        if not code:
            print("❌ Code cannot be empty!")
            return
        
        # Sign in
        try:
            await client.sign_in(phone=phone, code=code)
        except SessionPasswordNeededError:
            # 2FA password required
            print("\n🔒 Two-factor authentication enabled!")
            password = input("🔑 Enter your 2FA password: ").strip()
            await client.sign_in(password=password)
        except Exception as e:
            print(f"❌ Sign in failed: {e}")
            return
        
        # Get session string
        session = await client.session.save()
        
        # Display result
        print("\n" + "="*60)
        print("✅ SESSION STRING GENERATED SUCCESSFULLY!")
        print("="*60)
        print(f"\n🔑 Your Session String:\n\n{session}\n")
        print("="*60)
        print("\n⚠️  IMPORTANT - SAVE THIS SECURELY:")
        print("   • Add to .env file as SESSION_STRING")
        print("   • Never share this string with anyone")
        print("   • Anyone with this can access your account")
        print("   • Store in a password manager")
        print("\n💜 AllAtomic Userbot - @GhostMarshal | @ComputeCode")
        print("="*60)

if __name__ == "__main__":
    try:
        asyncio.run(generate_session())
    except KeyboardInterrupt:
        print("\n\n❌ Session generation cancelled by user.")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\n💡 Make sure you have telethon installed:")
        print("   pip install telethon")
