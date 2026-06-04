"""
AllAtomic - Session Generator
Dev: @GhostMarshal | Channel: @ComputeCode
(૨๑•̀ㅁ•́ฅा) Purple Anime Theme (#9A8CFF)
"""

from pyrogram import Client
from AllAtomic.core.config import symbols


def main():
    """Generate session string (✿◠‿◠)"""
    
    print(f"""
{symbols.LINE}
{symbols.SPARKLE} AllAtomic Session Generator {symbols.WINK}
{symbols.LINE}
""")
    
    api_id = input(f"{symbols.CUTE} Enter API ID: {symbols.WINK} ")
    api_hash = input(f"{symbols.CUTE} Enter API Hash: {symbols.WINK} ")
    
    try:
        api_id = int(api_id)
    except ValueError:
        print("Invalid API ID!")
        return
    
    with Client(
        "allatomic",
        api_id=api_id,
        api_hash=api_hash
    ) as app:
        session = app.export_session_string()
        
        print(f"""
{symbols.LINE}
{symbols.SPARKLE} Session Generated! {symbols.WINK}
{symbols.LINE}
{symbols.CUTE} Your session string:
{symbols.WINK}
{session}
{symbols.LINE}
{symbols.CUTE} Save this string securely!
{symbols.WINK} Do not share it with anyone!
{symbols.LINE}
""")
        
        # Save to file
        with open("session.string", "w") as f:
            f.write(session)
        
        print(f"{symbols.SPARKLE} Session saved to session.string")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n{symbols.CUTE} Cancelled!")
