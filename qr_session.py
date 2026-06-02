#!/usr/bin/env python3
"""
🔐 QR Session Generator - AllAtomic
Based on: github.com/SkillichSE/TG-session-QR

QR code login - no SMS needed!
"""

import asyncio
from telethon.sync import TelegramClient
from telethon.sessions import StringSession

API_ID = 38568281
API_HASH = "5dec3f281b9576f65824326f7cd984ed"

print("""
╔═══════════════════════════════════════════════════════╗
║     🔐 QR Session Generator - AllAtomic               ║
║                                                       ║
║   Scan QR with Telegram - No SMS needed!              ║
║   Dev: @GhostMarshal | Channel: @ComputeCode          ║
╚═══════════════════════════════════════════════════════╝
""")

async def generate_qr_session():
    """Generate session using QR code login"""
    
    async with TelegramClient(StringSession(), API_ID, API_HASH) as client:
        print("\n📱 Generating QR code...")
        
        # Get QR login token
        qr_login = await client.qr_login()
        
        print("\n" + "="*60)
        print("📲 SCAN THIS QR CODE WITH TELEGRAM")
        print("="*60)
        print("\nOn your phone:")
        print("  1. Open Telegram")
        print("  2. Settings → Devices")
        print("  3. Link Desktop Device")
        print("  4. Scan the QR code below\n")
        
        # Display QR code in terminal
        qr_code = qr_login.token
        print(f"QR Token: {qr_code[:50]}...")
        print("\n⏳ Waiting for scan (60 seconds)...")
        
        try:
            # Wait for QR scan
            await qr_login.wait(60)
            
            # Get session string
            session = client.session.save()
            
            print("\n" + "="*60)
            print("✅ SESSION STRING GENERATED!")
            print("="*60)
            print(f"\n🔑 {session}\n")
            print("="*60)
            print("\n💜 AllAtomic - @GhostMarshal | @ComputeCode")
            
        except asyncio.TimeoutError:
            print("\n❌ QR code expired. Please run the script again.")
        except Exception as e:
            print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    try:
        asyncio.run(generate_qr_session())
    except KeyboardInterrupt:
        print("\n\n❌ Cancelled by user.")
    except Exception as e:
        print(f"\n❌ Error: {e}")
