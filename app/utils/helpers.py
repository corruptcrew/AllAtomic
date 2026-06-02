"""
Utility Functions for AllAtomic Userbot
Helper functions, formatters, and animations
"""

import time
import random
from datetime import datetime
from typing import Optional

# ───────────────────────────────────────────────────────
# Kaomoji Collection (Purple Anime Theme)
# ───────────────────────────────────────────────────────

KAOMOJI = {
    "happy": ["૮๑•̀ㅁ•́ฅა", "(◕‿◕)", "(✿◠‿◠)", "୧(◕‿◕)୨", "(｡◕‿◕｡)"],
    "sad": ["(｡•́︿•̀｡)", "(╥_╥)", "(T_T)", "(；´д；)ゞ", "(｡•́︿•̀｡)"],
    "angry": ["(＃`Д´)", "(｀Д´)", "(▼ヘ▼#)", "(╬ Ò﹏Ó)", "(ノಠ益ಠ)ノ"],
    "love": ["(♡μ_μ)", "(｡♡‿♡｡)", "(ღ˘⌣˘ღ)", "(´｡• ᵕ •｡`)", "(*♡∀♡)"],
    "cool": ["(•_•)", "(⌐■_■)", "(☞ﾟヮﾟ)☞", "└(￣^￣ )┐", "(☞ ͡° ͜ʖ ͡°)☞"],
    "wink": ["(￣▽￣)~*", "(^_-)", "(´▽`ʃ♡ƪ)", "(✿´‿`)", "(◕‿◕✿)"],
    "shy": ["(⁄ ⁄•⁄ω⁄•⁄ ⁄)", "(*/ω＼*)", "(✿◡‿◡)", "(๑•́ ₃ •̀๑)", "(⁄ ⁄>⁄ ▽ ⁄<⁄ ⁄)"],
    "excited": ["o(>ω<)o", "＼(≧▽≦)／", "(ﾉ´ヮ´) ﾉ*:･ﾟ", "ヽ (゜∀゜) メ(゜∀゜) メ(゜∀゜) ノ", "٩(◕‿◕｡)۶"],
    "thinking": ["(・_・;)", "(￣～￣;)", "(´･_･`)", "(⊙_⊙)?", "(・∀・)"],
    "sleep": ["(￣o￣) zzZZ", "(∪.∪ )...zzz", "(＿ ＿*) Z z z", "(¦3[▓▓]", "(*´ρ`)"]
}

def get_kaomoji(emotion: str = "happy") -> str:
    """Get random kaomoji for emotion"""
    return random.choice(KAOMOJI.get(emotion, KAOMOJI["happy"]))

# ───────────────────────────────────────────────────────
# Time Formatting
# ───────────────────────────────────────────────────────

def get_readable_time(seconds: int) -> str:
    """Convert seconds to readable time"""
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    
    if days:
        return f"{days}d {hours}h {minutes}m {seconds}s"
    elif hours:
        return f"{hours}h {minutes}m {seconds}s"
    elif minutes:
        return f"{minutes}m {seconds}s"
    else:
        return f"{seconds}s"

def get_time() -> str:
    """Get current time in HH:MM format"""
    return datetime.now().strftime("%H:%M")

def get_date() -> str:
    """Get current date in DD/MM/YYYY format"""
    return datetime.now().strftime("%d/%m/%Y")

def get_datetime() -> str:
    """Get current datetime"""
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

# ───────────────────────────────────────────────────────
# Text Formatting
# ───────────────────────────────────────────────────────

def truncate_text(text: str, max_length: int = 50) -> str:
    """Truncate text with ellipsis"""
    if len(text) <= max_length:
        return text
    return text[:max_length - 3] + "..."

def mention_html(user_id: int, name: str) -> str:
    """Create HTML mention"""
    return f'<a href="tg://user?id={user_id}">{name}</a>'

def escape_markdown(text: str) -> str:
    """Escape markdown special characters"""
    special_chars = ["_", "*", "[", "]", "(", ")", "~", "`", ">", "#", "+", "-", "=", "|", "{", "}", ".", "!"]
    for char in special_chars:
        text = text.replace(char, f"\\{char}")
    return text

def code_block(code: str, lang: str = "") -> str:
    """Create code block"""
    return f"```{lang}\n{code}\n```"

def inline_mention(user_id: int) -> str:
    """Create inline mention"""
    return f"[user](tg://user?id={user_id})"

# ───────────────────────────────────────────────────────
# Progress Bar
# ───────────────────────────────────────────────────────

def progress_bar(current: int, total: int, width: int = 10) -> str:
    """Create progress bar"""
    percentage = current / total
    filled = int(width * percentage)
    empty = width - filled
    
    bar = "█" * filled + "░" * empty
    percent = f"{percentage * 100:.1f}%"
    
    return f"[{bar}] {percent}"

# ───────────────────────────────────────────────────────
# Animation Frames
# ───────────────────────────────────────────────────────

LOADING_FRAMES = [
    "⚛️  Loading",
    "⚛️  Loading.",
    "⚛️  Loading..",
    "⚛️  Loading...",
]

PURPLE_HEARTS = ["💜", "💙", "🩷", "💖", "✨", "🌸"]

def get_loading_frame(index: int) -> str:
    """Get loading animation frame"""
    return LOADING_FRAMES[index % len(LOADING_FRAMES)]

def get_random_heart() -> str:
    """Get random purple heart emoji"""
    return random.choice(PURPLE_HEARTS)

# ───────────────────────────────────────────────────────
# Command Parser
# ───────────────────────────────────────────────────────

def parse_command(text: str, handler: str = ".") -> tuple:
    """
    Parse command from message
    
    Returns: (command, args)
    Example: ".hello @user" -> ("hello", "@user")
    """
    if not text.startswith(handler):
        return None, None
    
    text = text[len(handler):]
    parts = text.split(" ", 1)
    
    command = parts[0].split("@")[0]  # Remove bot username if present
    args = parts[1] if len(parts) > 1 else ""
    
    return command, args.strip()

def get_args(message, handler: str = ".") -> str:
    """Get command arguments"""
    if not message.text:
        return ""
    
    _, args = parse_command(message.text, handler)
    return args or ""

# ───────────────────────────────────────────────────────
# Decorator Helper
# ───────────────────────────────────────────────────────

def atomic_command(command: str, group: int = 0, **kwargs):
    """
    Decorator for atomic commands
    
    Usage:
        @atomic_command("ping")
        async def ping_cmd(event):
            await event.reply("Pong!")
    """
    def decorator(func):
        func.__atomic_command__ = command
        func.__atomic_group__ = group
        func.__atomic_kwargs__ = kwargs
        return func
    return decorator

# ───────────────────────────────────────────────────────
# Misc Utilities
# ───────────────────────────────────────────────────────

def human_readable_size(size_bytes: int) -> str:
    """Convert bytes to human readable size"""
    if size_bytes == 0:
        return "0B"
    
    size_units = ["B", "KB", "MB", "GB", "TB"]
    unit_index = 0
    
    while size_bytes >= 1024 and unit_index < len(size_units) - 1:
        size_bytes /= 1024
        unit_index += 1
    
    return f"{size_bytes:.2f} {size_units[unit_index]}"

def extract_user_id(text: str) -> Optional[int]:
    """Extract user ID from text/mention"""
    if not text:
        return None
    
    # From mention: @username or tg://user?id=123
    if text.startswith("@"):
        # Username - would need API call to resolve
        return None
    elif "tg://user?id=" in text:
        try:
            return int(text.split("id=")[1].split("&")[0])
        except:
            return None
    else:
        # Try to parse as ID
        try:
            return int(text)
        except:
            return None

def is_admin(chat_id: int, user_id: int, admins_list: list) -> bool:
    """Check if user is admin"""
    return user_id in admins_list or user_id == chat_id

# ═══════════════════════════════════════════════════════
# Purple Theme Constants
# ═══════════════════════════════════════════════════════

THEME = {
    "color": "#9A8CFF",
    "emoji": "💜",
    "heart": "🩷",
    "star": "⭐",
    "sparkle": "✨",
    "flower": "🌸",
    "atom": "⚛️",
    "purple_heart": "💜",
    "blue_heart": "💙",
    "pink_heart": "🩷",
}

def get_theme_emoji() -> str:
    """Get random theme emoji"""
    return random.choice(list(THEME.values())[1:])
