"""
🔘 Callback Handler for AllAtomic Userbot
Handles inline button callbacks (HellBot-style help menu)
"""

from telethon import events
from telethon.tl.custom import Button
from plugins import register_handler
from app.utils import get_kaomoji

# Plugin metadata
__plugin__ = {
    "name": "Callback Handler",
    "description": "Handles inline button callbacks for help menu",
    "category": "core"
}

# Help categories (must match help.py)
HELP_CATEGORIES = {
    "Core": {"emoji": "⚙️", "commands": ["alive", "ping", "help", "cmds", "settings", "repo", "support"]},
    "Admin": {"emoji": "👥", "commands": ["ban", "kick", "mute", "unmute", "pin", "unpin", "del", "purge"]},
    "Fun": {"emoji": "🎮", "commands": ["joke", "meme", "quote", "love", "rate", "emoji"]},
    "Utility": {"emoji": "🔧", "commands": ["weather", "time", "date", "info", "userid", "chatid"]},
    "Media": {"emoji": "📷", "commands": ["dl", "upload", "tts", "sticker", "kang"]},
    "Stickers": {"emoji": "🎭", "commands": ["kang", "sticker", "fullpp", "dp", "emoji"]},
    "Anime": {"emoji": "🌸", "commands": ["waifu", "neko", "waifupic", "anime", "manga"]},
    "AI": {"emoji": "🤖", "commands": ["ai", "chat", "ask", "gpt"]},
    "Group": {"emoji": "📢", "commands": ["welcome", "goodbye", "notes", "gcast", "gdel"]},
    "Advanced": {"emoji": "⚡", "commands": ["eval", "exec", "term", "sudo", "heroku"]},
    "PM Permit": {"emoji": "📩", "commands": ["pmpermit", "approve", "disapprove", "block", "unblock"]},
    "Voice": {"emoji": "🎵", "commands": ["play", "pause", "resume", "stop", "skip", "queue"]},
    "Direct": {"emoji": "🔗", "commands": ["direct", "source", "github", "link"]}
}

# Main help menu text
HELP_MAIN_TEXT = """
╔═══════════════════════════════════════════════╗
║      ⚛️  AllAtomic Help Menu  ⚛️               ║
╠═══════════════════════════════════════════════╣
║                                               ║
║  💜 **Total Commands:** 84                    ║
║  📦 **Plugins:** 20                           ║
║  🌸 **Theme:** Purple Anime                   ║
║                                               ║
║  **Prefix:** `.` (dot)                        ║
║  **Example:** `.alive`, `.help`               ║
║                                               ║
║  (૮๑•̀ㅁ•́ฅა)                                   ║
║                                               ║
║  **Dev:** @GhostMarshal                       ║
║  **Channel:** @ComputeCode                    ║
║                                               ║
╚═══════════════════════════════════════════════╝

**📂 Select a category below:**
"""


def build_category_buttons():
    """Build inline keyboard buttons for all categories"""
    buttons = []
    category_items = list(HELP_CATEGORIES.items())
    
    # Create rows of 2 buttons each
    for i in range(0, len(category_items), 2):
        row = []
        cat1_name, cat1_data = category_items[i]
        row.append(Button.inline(f"{cat1_data['emoji']} {cat1_name}", data=f"help_cat_{cat1_name}"))
        
        if i + 1 < len(category_items):
            cat2_name, cat2_data = category_items[i + 1]
            row.append(Button.inline(f"{cat2_data['emoji']} {cat2_name}", data=f"help_cat_{cat2_name}"))
        buttons.append(row)
    
    # Add navigation buttons
    buttons.append([
        Button.url("👥 Support", "https://t.me/ComputeCode"),
        Button.url("📦 GitHub", "https://github.com/corruptcrew/AllAtomic"),
    ])
    
    return buttons


def build_back_buttons():
    """Build back/close buttons"""
    return [
        [Button.inline("◀️ Back", data="help_back")],
        [Button.inline("❌ Close", data="help_close")],
    ]


@register_handler(events.CallbackQuery)
async def help_callback_handler(event):
    """Handle help menu callback queries (HellBot style)"""
    try:
        # Handle callback data - event.data is already bytes
        data = event.data
        if isinstance(data, bytes):
            data = data.decode('utf-8')
        
        # Handle main help menu back button
        if data == "help_back":
            await event.edit(HELP_MAIN_TEXT, buttons=build_category_buttons())
            await event.answer()
        
        # Handle close button
        elif data == "help_close":
            await event.delete()
            await event.answer("Help menu closed", alert=True)
        
        # Handle category selection
        elif data.startswith("help_cat_"):
            category_name = data.replace("help_cat_", "")
            cat_data = HELP_CATEGORIES.get(category_name)
            
            if cat_data and isinstance(cat_data, dict):
                emoji = cat_data.get("emoji", "📦")
                commands = cat_data.get("commands", [])
                
                # Format commands list
                cmd_list = "\n".join([f"║  •  `.{cmd}`" for cmd in commands])
                
                # Build category message
                msg = f"""
╔═══════════════════════════════════════════════╗
║  {emoji}  {category_name} Commands  {emoji}            ║
╠═══════════════════════════════════════════════╣
║                                               ║
{cmd_list}
║                                               ║
╚═══════════════════════════════════════════════╝

**📂 Select another category:**
"""
                # Build buttons with back button
                buttons = build_back_buttons()
                
                await event.edit(msg, parse_mode="md", buttons=buttons)
                await event.answer(f"{category_name} commands", alert=False)
            else:
                await event.answer("Category not found", alert=True)
        
    except Exception as e:
        await event.answer(f"Error: {str(e)}", alert=True)


# Commands registry
commands = {}
