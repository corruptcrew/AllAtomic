"""
AllAtomic - Utility Functions
Dev: @GhostMarshal | Channel: @ComputeCode
(૨๑•̀ㅁ•́ฅा) Purple Anime Theme (#9A8CFF)
"""

import time
from datetime import datetime
from AllAtomic.core.config import config
from AllAtomic.core.database import db


def get_time() -> str:
    """Get formatted uptime time (✿◠‿◠)"""
    start_time = getattr(get_time, "start_time", None)
    if not start_time:
        get_time.start_time = time.time()
        return "0s"
    
    uptime = time.time() - start_time
    
    if uptime < 60:
        return f"{uptime:.0f}s"
    elif uptime < 3600:
        return f"{uptime/60:.0f}m"
    elif uptime < 86400:
        return f"{uptime/3600:.0f}h"
    else:
        return f"{uptime/86400:.0f}d"


def is_admin(user_id: int) -> bool:
    """Check if user is admin (◕‿◕)"""
    if user_id in config.SUDO_USERS:
        return True
    if config.OWNER_ID and user_id == config.OWNER_ID:
        return True
    return False


def format_time(seconds: int) -> str:
    """Format seconds to human readable time"""
    if seconds < 60:
        return f"{seconds}s"
    elif seconds < 3600:
        return f"{seconds//60}m {seconds%60}s"
    elif seconds < 86400:
        return f"{seconds//3600}h {seconds%3600//60}m"
    else:
        return f"{seconds//86400}d {seconds%86400//3600}h"


def get_uptime() -> str:
    """Get uptime string"""
    from AllAtomic.core.initializer import get_uptime
    return get_uptime()


def parse_duration(duration: str) -> int:
    """Parse duration string to seconds"""
    units = {
        "s": 1,
        "m": 60,
        "h": 3600,
        "d": 86400,
    }
    
    total = 0
    for part in duration.split():
        if part[-1] in units:
            total += int(part[:-1]) * units[part[-1]]
    
    return total


def get_chat_type(chat_id: int) -> str:
    """Get chat type"""
    if chat_id < 0:
        return "supergroup"
    return "private"


def sanitize_text(text: str) -> str:
    """Sanitize text for safe processing"""
    # Remove special characters that could cause issues
    text = text.replace("\u200b", "").replace("\u200c", "").replace("\u200d", "")
    return text


def truncate_text(text: str, max_length: int = 4096) -> str:
    """Truncate text to max length"""
    if len(text) <= max_length:
        return text
    return text[:max_length] + "\n\n... (truncated)"


async def get_user_info(client, user_id: int) -> dict:
    """Get user information"""
    try:
        user = await client.get_users(user_id)
        return {
            "id": user.id,
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "is_bot": user.is_bot,
            "is_premium": user.is_premium,
            "language_code": user.language_code,
        }
    except Exception:
        return {}


async def get_chat_info(client, chat_id: int) -> dict:
    """Get chat information"""
    try:
        chat = await client.get_chat(chat_id)
        return {
            "id": chat.id,
            "title": chat.title,
            "username": chat.username,
            "type": chat.type,
            "description": chat.description,
            "member_count": chat.members_count,
        }
    except Exception:
        return {}


def generate_id() -> str:
    """Generate unique ID"""
    import uuid
    return str(uuid.uuid4())[:8]


def check_blacklist(text: str) -> bool:
    """Check if text contains blacklisted keywords"""
    import asyncio
    try:
        return asyncio.get_event_loop().run_until_complete(
            db.is_blacklisted(text)
        )
    except Exception:
        return False


def is_sudo(user_id: int) -> bool:
    """Check if user is sudo"""
    return user_id in config.SUDO_USERS


def is_owner(user_id: int) -> bool:
    """Check if user is owner"""
    return config.OWNER_ID and user_id == config.OWNER_ID


def get_theme_color() -> str:
    """Get theme color"""
    return config.THEME_COLOR


def get_version() -> str:
    """Get version string"""
    return config.VERSION
