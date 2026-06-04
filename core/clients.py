"""
AllAtomic - Pyrogram Client Setup
Dev: @GhostMarshal | Channel: @ComputeCode
(૨๑•̀ㅁ•́ฅา) Purple Anime Theme (#9A8CFF)
"""

import asyncio
from typing import Optional, List
from pyrogram import Client
from pyrogram.enums import ParseMode
from .config import config, log
from .database import db


class ClientManager:
    """Manages all Pyrogram clients (✿◠‿◠)"""
    
    def __init__(self):
        self.bot: Optional[Client] = None
        self.user: Optional[Client] = None
        self.clients: List[Client] = []
    
    async def start_bot(self):
        """Start bot client"""
        if not config.BOT_TOKEN:
            log.warning("Bot token not configured, skipping bot client")
            return
        
        try:
            self.bot = Client(
                "bot",
                api_id=config.API_ID,
                api_hash=config.API_HASH,
                bot_token=config.BOT_TOKEN,
                parse_mode=ParseMode.MARKDOWN,
                workers=100
            )
            await self.bot.start()
            bot_user = await self.bot.get_me()
            log.info(f"Bot started: @{bot_user.username}")
            self.clients.append(self.bot)
        except Exception as e:
            log.error(f"Failed to start bot: {e}")
            raise
    
    async def start_user(self):
        """Start user client with string session"""
        if not config.STRING_SESSION:
            log.warning("String session not configured, skipping user client")
            return
        
        try:
            self.user = Client(
                "user",
                api_id=config.API_ID,
                api_hash=config.API_HASH,
                session_string=config.STRING_SESSION,
                parse_mode=ParseMode.MARKDOWN,
                workers=100
            )
            await self.user.start()
            user = await self.user.get_me()
            log.info(f"User started: @{user.username} ({user.id})")
            self.clients.append(self.user)
            
            # Add user to database
            await db.add_user(user.id, user.username, user.first_name)
            
        except Exception as e:
            log.error(f"Failed to start user: {e}")
            raise
    
    async def start_all(self):
        """Start all clients"""
        await self.start_bot()
        await self.start_user()
        log.info(f"Started {len(self.clients)} client(s)")
    
    async def stop_all(self):
        """Stop all clients"""
        for client in self.clients:
            try:
                await client.stop()
            except Exception as e:
                log.error(f"Error stopping client: {e}")
        self.clients.clear()
        log.info("All clients stopped")
    
    async def restart_all(self):
        """Restart all clients"""
        await self.stop_all()
        await asyncio.sleep(1)
        await self.start_all()
    
    def get_client(self, identifier: str = None) -> Optional[Client]:
        """Get client by identifier"""
        if identifier == "bot":
            return self.bot
        elif identifier == "user":
            return self.user
        elif self.user:
            return self.user
        return self.bot


# Client manager instance
clients = ClientManager()


async def get_client(identifier: str = None) -> Optional[Client]:
    """Get client by identifier"""
    return clients.get_client(identifier)
