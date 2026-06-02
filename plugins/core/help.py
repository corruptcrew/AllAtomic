"""
⚛️  Help Command for AllAtomic Userbot
Shows available commands with purple anime theme
"""

import asyncio
from telethon import events

from plugins import atomic_command, get_all_commands, get_commands_by_category
from app.utils import get_kaomoji, THEME

# Plugin metadata
__plugin__ = {
    "name": "Help",
    "description": "Show available commands",
    "category": "core"
}

# Help menu template
HELP_HEADER = """
╔═══════════════════════════════════════════════╗
║     ⚛️  **AllAtomic Help Menu**  ⚛️           ║
╠═══════════════════════════════════════════════╣
║                                               ║
║  💜 Welcome to AllAtomic Userbot!             ║
║  🌸 Purple Anime Theme Edition                ║
║                                               ║
╚═══════════════════════════════════════════════╝

**Available Categories:**
"""

HELP_FOOTER = """
━━━━━━━━━━━━━━━━━━━━━━

💜 **Dev:** @GhostMarshal
📢 **Channel:** @ComputeCode
{kaomoji}

**Usage:** `.help <category>`
**Example:** `.help core`
"""

# Categories with emojis
CATEGORIES = {
    "core": "⚛️  Core",
    "group": "👥 Group",
    "pm": "💬 PM",
    "media": "🎬 Media",
    "ai": "🤖 AI",
    "anime": "🌸 Anime",
    "utility": "🔧 Utility"
}

@atomic_command(
    "help",
    pattern=r"\.help(?:\s|$)(.*)",
    help="Show help menu",
    usage=".help [category]",
    category="core"
)
async def help_handler(event):
    """Help command handler"""
    # Get category if specified
    category = event.pattern_match.group(1).strip().lower() if event.pattern_match.group(1) else None
    
    if category:
        # Show commands for specific category
        await show_category_help(event, category)
    else:
        # Show all categories
        await show_main_help(event)

async def show_main_help(event):
    """Show main help menu with categories"""
    all_commands = get_all_commands()
    
    # Group commands by category
    categories_dict = {}
    for cmd in all_commands:
        cat = cmd.get("category", "misc")
        if cat not in categories_dict:
            categories_dict[cat] = []
        categories_dict[cat].append(cmd)
    
    # Build help message
    help_msg = HELP_HEADER
    
    for cat_name, cat_display in CATEGORIES.items():
        if cat_name in categories_dict:
            cmd_count = len(categories_dict[cat_name])
            help_msg += f"\n{cat_display} — `{cmd_count}` commands"
    
    help_msg += HELP_FOOTER.format(kaomoji=get_kaomoji("happy"))
    
    await event.edit(help_msg, parse_mode="md", link_preview=False)

async def show_category_help(event, category: str):
    """Show help for specific category"""
    commands = get_commands_by_category(category)
    
    if not commands:
        # Try to find by partial match
        for cat in CATEGORIES.keys():
            if category in cat:
                commands = get_commands_by_category(cat)
                break
    
    if not commands:
        await event.edit(f"❌ No commands found for category: `{category}`")
        return
    
    category_name = CATEGORIES.get(category, category.title())
    
    help_msg = f"""
╔═══════════════════════════════════════════════╗
║  {category_name} Commands                     ║
╚═══════════════════════════════════════════════╝

"""
    
    for cmd in commands:
        cmd_name = cmd.get("name", "unknown")
        cmd_help = cmd.get("help", "No description")
        cmd_usage = cmd.get("usage", f".{cmd_name}")
        
        help_msg += f"⚡ **{cmd_usage}**\n"
        help_msg += f"   └─ {cmd_help}\n\n"
    
    help_msg += f"{'━' * 40}\n"
    help_msg += f"💜 Total: `{len(commands)}` commands\n"
    help_msg += f"{get_kaomoji('happy')}"
    
    await event.edit(help_msg, parse_mode="md", link_preview=False)

@atomic_command(
    "cmds",
    pattern=r"\.cmds",
    help="Quick command list",
    usage=".cmds",
    category="core"
)
async def cmds_handler(event):
    """Quick command list"""
    all_commands = get_all_commands()
    
    cmd_list = ", ".join([f".{cmd['name']}" for cmd in all_commands[:20]])
    
    if len(all_commands) > 20:
        cmd_list += f"... and {len(all_commands) - 20} more"
    
    cmds_msg = f"""
⚛️ **AllAtomic Commands** {get_kaomoji('cool')}

{cmd_list}

━━━━━━━━━━━━━━━━━━━━━━

💜 Use `.help` for details
📢 @ComputeCode
    """
    
    await event.edit(cmds_msg, parse_mode="md")
    await asyncio.sleep(60)
    await event.delete()

@atomic_command(
    "repo",
    pattern=r"\.repo",
    help="Get repository link",
    usage=".repo",
    category="core"
)
async def repo_handler(event):
    """Show repository link"""
    repo_msg = f"""
⚛️ **AllAtomic Repository** {get_kaomoji('excited')}

━━━━━━━━━━━━━━━━━━━━━━

📦 **Source:** [GitHub](https://github.com/GhostMarshal/AllAtomic)
💜 **Dev:** @GhostMarshal
📢 **Channel:** @ComputeCode

🌟 Star the repo if you like it!
{get_kaomoji('love')}
    """
    
    await event.edit(repo_msg, parse_mode="md", link_preview=False)

@atomic_command(
    "support",
    pattern=r"\.support",
    help="Get support group link",
    usage=".support",
    category="core"
)
async def support_handler(event):
    """Show support group link"""
    support_msg = f"""
💜 **AllAtomic Support** {get_kaomoji('happy')}

━━━━━━━━━━━━━━━━━━━━━━

📢 **Channel:** [@ComputeCode](https://t.me/ComputeCode)
💬 **Support:** [@ComputeCode](https://t.me/ComputeCode)
👤 **Dev:** [@GhostMarshal](https://t.me/GhostMarshal)

Join for updates and help!
⚛️
    """
    
    await event.edit(support_msg, parse_mode="md", link_preview=False)

# Commands registry
commands = {
    "help": {
        "help": "Show help menu",
        "usage": ".help [category]",
        "category": "core"
    },
    "cmds": {
        "help": "Quick command list",
        "usage": ".cmds",
        "category": "core"
    },
    "repo": {
        "help": "Get repository link",
        "usage": ".repo",
        "category": "core"
    },
    "support": {
        "help": "Get support group link",
        "usage": ".support",
        "category": "core"
    }
}
