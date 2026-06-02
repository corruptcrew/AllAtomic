"""
🔐 Session String Generator for AllAtomic Userbot
Run this to generate your session string
"""

from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import getpass
import os

# Import config
from app.config import Config

def generate_session():
    """Generate session string"""
    print("""
╔═══════════════════════════════════════════════════════╗
║     🔐 AllAtomic Session Generator                   ║
╚═══════════════════════════════════════════════════════╝

⚠️  This will generate your session string.
⚠️  Keep this string SECRET and secure!

""")
    
    # Get API credentials
    api_id = input("🔑 Enter API_ID: ").strip()
    api_hash = input("🔑 Enter API_HASH: ").strip()
    
    if not api_id or not api_hash:
        print("❌ API credentials cannot be empty!")
        return
    
    # Create client
    with TelegramClient(StringSession(), int(api_id), api_hash) as client:
        # Send verification code
        print("\n📱 A verification code will be sent to your Telegram app.")
        print("   Please enter it below.\n")
        
        # Attempt to sign in (will prompt for code)
        try:
            client.sign_in()
        except:
            # First attempt might not work, continue
            pass
        
        # Get phone number if needed
        phone = input("📞 Enter your phone number (with country code): ").strip()
        
        # Send code
        code = client.sign_in(phone)
        
        # Enter code
        if hasattr(code, 'phone_code_hash'):
            code_input = input("🔢 Enter the code you received: ").strip()
            try:
                client.sign_up(phone=phone, code=code_input)
            except:
                # Try alternative method
                client.send_code_request(phone)
                code_input = input("🔢 Enter the code you received: ").strip()
                client.sign_in(phone=phone, code=code_input)
        
        # Get session string
        session = client.session.save()
        
        print("\n" + "="*50)
        print("✅ Session string generated successfully!")
        print("="*50)
        print("\n🔑 Your session string:")
        print(f"\n{session}\n")
        print("="*50)
        print("\n⚠️  IMPORTANT:")
        print("   - Copy this string and save it securely")
        print("   - Paste it in your .env file as SESSION_STRING")
        print("   - NEVER share this string with anyone!")
        print("   - Anyone with this string can access your account!")
        print("\n💜 AllAtomic Userbot - @GhostMarshal")
        print("="*50)

if __name__ == "__main__":
    try:
        generate_session()
    except KeyboardInterrupt:
        print("\n\n❌ Session generation cancelled.")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("   Make sure you have telethon installed:")
        print("   pip install telethon")
