"""
Telethon Client Setup for AllAtomic Userbot
Handles Telegram connection and event management
"""

import asyncio
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.errors import SessionPasswordNeededError
from .config import Config
from .logger import logger

class AtomicClient:
    """Telethon client wrapper with atomic operations"""
    
    def __init__(self, config: Config):
        self.config = config
        self.session = StringSession(config.SESSION_STRING)
        
        # Initialize client
        self.client = TelegramClient(
            self.session,
            config.APP_ID,
            config.API_HASH,
            device_model="AllAtomic Userbot",
            app_version="1.0.0",
            lang_code="en",
            system_lang_code="en-US",
            auto_reconnect=True,
            connection_retries=5,
            retry_delay=2
        )
        
        # Event handlers registry
        self.handlers = {}
        
        # Bot info
        self.me = None
        self.is_bot = False
        
    async def start(self):
        """Start the client"""
        logger.info("🔌 Connecting to Telegram...")
        
        await self.client.start(bot_token=self.config.BOT_TOKEN or None)
        
        # Get bot/user info
        self.me = await self.client.get_me()
        self.is_bot = self.me.bot
        
        logger.info(f"✓ Logged in as: {self.me.first_name} (@{self.me.username or 'NoUsername'})")
        logger.info(f"  ID: {self.me.id} | Bot: {self.is_bot}")
        
        return self
    
    async def stop(self):
        """Stop the client"""
        logger.info("👋 Shutting down AllAtomic...")
        await self.client.disconnect()
        logger.info("✓ Disconnected")
    
    def on_event(self, pattern=None, **kwargs):
        """
        Decorator for registering event handlers
        
        Usage:
            @client.on_event(pattern=r"\.alive")
            async def alive_handler(event):
                await event.reply("Alive!")
        """
        def decorator(func):
            # Register handler
            handler = events.NewMessage(pattern=pattern, **kwargs)
            self.client.add_event_handler(func, handler)
            
            # Store in registry
            handler_name = func.__name__
            self.handlers[handler_name] = {
                "function": func,
                "pattern": pattern,
                "kwargs": kwargs
            }
            
            logger.debug(f"✓ Registered handler: {handler_name}")
            return func
        
        return decorator
    
    def register_handler(self, name: str, func, pattern=None, **kwargs):
        """Register a handler programmatically"""
        handler = events.NewMessage(pattern=pattern, **kwargs)
        self.client.add_event_handler(func, handler)
        
        self.handlers[name] = {
            "function": func,
            "pattern": pattern,
            "kwargs": kwargs
        }
        
        logger.debug(f"✓ Registered handler: {name}")
    
    async def send_message(self, entity, message, **kwargs):
        """Send message with error handling"""
        try:
            return await self.client.send_message(entity, message, **kwargs)
        except Exception as e:
            logger.error(f"❌ Send message failed: {e}")
            return None
    
    async def edit_message(self, message, new_text, **kwargs):
        """Edit message with error handling"""
        try:
            return await message.edit(new_text, **kwargs)
        except Exception as e:
            logger.error(f"❌ Edit message failed: {e}")
            return None
    
    async def delete_message(self, message):
        """Delete message with error handling"""
        try:
            return await message.delete()
        except Exception as e:
            logger.error(f"❌ Delete message failed: {e}")
            return None
    
    async def get_entity(self, entity):
        """Get entity with error handling"""
        try:
            return await self.client.get_entity(entity)
        except Exception as e:
            logger.error(f"❌ Get entity failed: {e}")
            return None
    
    async def download_media(self, message, path=None):
        """Download media from message"""
        try:
            if not message.media:
                return None
            
            path = path or f"downloads/{message.id}"
            return await self.client.download_media(message, path)
        except Exception as e:
            logger.error(f"❌ Download media failed: {e}")
            return None
    
    async def send_file(self, entity, file, **kwargs):
        """Send file with error handling"""
        try:
            return await self.client.send_file(entity, file, **kwargs)
        except Exception as e:
            logger.error(f"❌ Send file failed: {e}")
            return None
    
    def add_handler(self, func, event=events.NewMessage, **kwargs):
        """Add event handler directly"""
        self.client.add_event_handler(func, event(**kwargs))
    
    def run_until_disconnected(self):
        """Run client until disconnected"""
        return self.client.run_until_disconnected()
    
    @property
    def full_name(self):
        """Get full name"""
        if self.me:
            full = self.me.first_name or ""
            if self.me.last_name:
                full += f" {self.me.last_name}"
            return full
        return "Unknown"
    
    @property
    def username(self):
        """Get username"""
        return self.me.username if self.me else None
    
    @property
    def user_id(self):
        """Get user ID"""
        return self.me.id if self.me else 0
    
    def __repr__(self):
        return f"<AtomicClient [{self.full_name}]>"
