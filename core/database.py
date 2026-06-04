"""
AllAtomic - MongoDB Database Layer
Dev: @GhostMarshal | Channel: @ComputeCode
(૨๑•̀ㅁ•́ฅა) Purple Anime Theme (#9A8CFF)
"""

import asyncio
from datetime import datetime
from typing import Optional, List, Dict, Any
from motor.motor_asyncio import AsyncIOMotorClient
from .config import config, log


class Database:
    """MongoDB database handler for AllAtomic (✿◠‿◠)"""
    
    def __init__(self):
        self.client: Optional[AsyncIOMotorClient] = None
        self.db = None
        self.connected = False
    
    async def connect(self):
        """Connect to MongoDB (◕‿◕)"""
        if self.connected:
            log.info("Database already connected")
            return
        
        try:
            self.client = AsyncIOMotorClient(config.MONGO_URL)
            self.db = self.client[config.DB_NAME]
            
            # Test connection
            await self.client.admin.command("ping")
            self.connected = True
            log.info("Successfully connected to MongoDB")
            
        except Exception as e:
            log.error(f"Failed to connect to MongoDB: {e}")
            raise
    
    async def disconnect(self):
        """Disconnect from MongoDB"""
        if self.client and self.connected:
            self.client.close()
            self.connected = False
            log.info("Disconnected from MongoDB")
    
    async def add_admin(self, user_id: int, name: str = None) -> bool:
        """Add user to admin list"""
        if not self.connected:
            await self.connect()
        
        try:
            users = self.db.users
            await users.update_one(
                {"user_id": user_id},
                {"$set": {"is_admin": True, "name": name or f"User {user_id}"}},
                upsert=True
            )
            return True
        except Exception as e:
            log.error(f"Failed to add admin: {e}")
            return False
    
    async def remove_admin(self, user_id: int) -> bool:
        """Remove user from admin list"""
        if not self.connected:
            await self.connect()
        
        try:
            users = self.db.users
            await users.update_one(
                {"user_id": user_id},
                {"$set": {"is_admin": False}}
            )
            return True
        except Exception as e:
            log.error(f"Failed to remove admin: {e}")
            return False
    
    async def is_admin(self, user_id: int) -> bool:
        """Check if user is admin"""
        if not self.connected:
            await self.connect()
        
        try:
            users = self.db.users
            user = await users.find_one({"user_id": user_id})
            return user.get("is_admin", False)
        except Exception as e:
            log.error(f"Failed to check admin status: {e}")
            return False
    
    async def add_user(self, user_id: int, username: str = None, name: str = None) -> bool:
        """Add user to database"""
        if not self.connected:
            await self.connect()
        
        try:
            users = self.db.users
            await users.update_one(
                {"user_id": user_id},
                {
                    "$set": {
                        "username": username,
                        "name": name,
                        "added_at": datetime.utcnow()
                    }
                },
                upsert=True
            )
            return True
        except Exception as e:
            log.error(f"Failed to add user: {e}")
            return False
    
    async def get_user(self, user_id: int) -> Optional[Dict]:
        """Get user data"""
        if not self.connected:
            await self.connect()
        
        try:
            users = self.db.users
            return await users.find_one({"user_id": user_id})
        except Exception as e:
            log.error(f"Failed to get user: {e}")
            return None
    
    async def get_all_users(self) -> List[Dict]:
        """Get all users"""
        if not self.connected:
            await self.connect()
        
        try:
            users = self.db.users
            return await users.find({}).to_list(length=None)
        except Exception as e:
            log.error(f"Failed to get all users: {e}")
            return []
    
    async def add_blacklist(self, keyword: str) -> bool:
        """Add keyword to blacklist"""
        if not self.connected:
            await self.connect()
        
        try:
            blacklist = self.db.blacklist
            await blacklist.update_one(
                {"keyword": keyword.lower()},
                {"$set": {"added_at": datetime.utcnow()}},
                upsert=True
            )
            return True
        except Exception as e:
            log.error(f"Failed to add blacklist: {e}")
            return False
    
    async def remove_blacklist(self, keyword: str) -> bool:
        """Remove keyword from blacklist"""
        if not self.connected:
            await self.connect()
        
        try:
            blacklist = self.db.blacklist
            await blacklist.delete_one({"keyword": keyword.lower()})
            return True
        except Exception as e:
            log.error(f"Failed to remove blacklist: {e}")
            return False
    
    async def is_blacklisted(self, text: str) -> bool:
        """Check if text contains blacklisted keywords"""
        if not self.connected:
            await self.connect()
        
        try:
            blacklist = self.db.blacklist
            keywords = await blacklist.find({}).to_list(length=None)
            for kw in keywords:
                if kw["keyword"].lower() in text.lower():
                    return True
            return False
        except Exception as e:
            log.error(f"Failed to check blacklist: {e}")
            return False
    
    async def add_gban(self, user_id: int, reason: str = None) -> bool:
        """Add user to global ban list"""
        if not self.connected:
            await self.connect()
        
        try:
            gban = self.db.gban
            await gban.update_one(
                {"user_id": user_id},
                {
                    "$set": {
                        "reason": reason or "No reason provided",
                        "gban_at": datetime.utcnow()
                    }
                },
                upsert=True
            )
            return True
        except Exception as e:
            log.error(f"Failed to add gban: {e}")
            return False
    
    async def remove_gban(self, user_id: int) -> bool:
        """Remove user from global ban list"""
        if not self.connected:
            await self.connect()
        
        try:
            gban = self.db.gban
            await gban.delete_one({"user_id": user_id})
            return True
        except Exception as e:
            log.error(f"Failed to remove gban: {e}")
            return False
    
    async def is_gbanned(self, user_id: int) -> bool:
        """Check if user is gbanned"""
        if not self.connected:
            await self.connect()
        
        try:
            gban = self.db.gban
            user = await gban.find_one({"user_id": user_id})
            return user is not None
        except Exception as e:
            log.error(f"Failed to check gban status: {e}")
            return False
    
    async def add_afk(self, user_id: int, reason: str = None) -> bool:
        """Add user to AFK list"""
        if not self.connected:
            await self.connect()
        
        try:
            afk = self.db.afk
            await afk.update_one(
                {"user_id": user_id},
                {
                    "$set": {
                        "reason": reason or "No reason",
                        "afk_at": datetime.utcnow()
                    }
                },
                upsert=True
            )
            return True
        except Exception as e:
            log.error(f"Failed to add AFK: {e}")
            return False
    
    async def remove_afk(self, user_id: int) -> bool:
        """Remove user from AFK list"""
        if not self.connected:
            await self.connect()
        
        try:
            afk = self.db.afk
            await afk.delete_one({"user_id": user_id})
            return True
        except Exception as e:
            log.error(f"Failed to remove AFK: {e}")
            return False
    
    async def is_afk(self, user_id: int) -> bool:
        """Check if user is AFK"""
        if not self.connected:
            await self.connect()
        
        try:
            afk = self.db.afk
            user = await afk.find_one({"user_id": user_id})
            return user is not None
        except Exception as e:
            log.error(f"Failed to check AFK status: {e}")
            return False
    
    async def get_afk_reason(self, user_id: int) -> Optional[str]:
        """Get AFK reason for user"""
        if not self.connected:
            await self.connect()
        
        try:
            afk = self.db.afk
            user = await afk.find_one({"user_id": user_id})
            return user.get("reason") if user else None
        except Exception as e:
            log.error(f"Failed to get AFK reason: {e}")
            return None
    
    async def add_paste(self, data: str, language: str = "py") -> str:
        """Save paste to database"""
        if not self.connected:
            await self.connect()
        
        try:
            import uuid
            paste_id = str(uuid.uuid4())[:8]
            pastes = self.db.pastes
            
            await pastes.update_one(
                {"id": paste_id},
                {
                    "$set": {
                        "data": data,
                        "language": language,
                        "created_at": datetime.utcnow()
                    }
                },
                upsert=True
            )
            return paste_id
        except Exception as e:
            log.error(f"Failed to save paste: {e}")
            return None
    
    async def get_paste(self, paste_id: str) -> Optional[str]:
        """Get paste data"""
        if not self.connected:
            await self.connect()
        
        try:
            pastes = self.db.pastes
            paste = await pastes.find_one({"id": paste_id})
            return paste.get("data") if paste else None
        except Exception as e:
            log.error(f"Failed to get paste: {e}")
            return None
    
    async def add_note(self, chat_id: int, keyword: str, content: str) -> bool:
        """Add note to database"""
        if not self.connected:
            await self.connect()
        
        try:
            notes = self.db.notes
            await notes.update_one(
                {"chat_id": chat_id, "keyword": keyword.lower()},
                {
                    "$set": {
                        "content": content,
                        "updated_at": datetime.utcnow()
                    }
                },
                upsert=True
            )
            return True
        except Exception as e:
            log.error(f"Failed to add note: {e}")
            return False
    
    async def get_note(self, chat_id: int, keyword: str) -> Optional[str]:
        """Get note from database"""
        if not self.connected:
            await self.connect()
        
        try:
            notes = self.db.notes
            note = await notes.find_one({
                "chat_id": chat_id,
                "keyword": keyword.lower()
            })
            return note.get("content") if note else None
        except Exception as e:
            log.error(f"Failed to get note: {e}")
            return None
    
    async def delete_note(self, chat_id: int, keyword: str) -> bool:
        """Delete note from database"""
        if not self.connected:
            await self.connect()
        
        try:
            notes = self.db.notes
            await notes.delete_one({
                "chat_id": chat_id,
                "keyword": keyword.lower()
            })
            return True
        except Exception as e:
            log.error(f"Failed to delete note: {e}")
            return False
    
    async def get_all_notes(self, chat_id: int) -> List[Dict]:
        """Get all notes for a chat"""
        if not self.connected:
            await self.connect()
        
        try:
            notes = self.db.notes
            return await notes.find({"chat_id": chat_id}).to_list(length=None)
        except Exception as e:
            log.error(f"Failed to get all notes: {e}")
            return []
    
    async def add_welcome(self, chat_id: int, enabled: bool, message: str = None) -> bool:
        """Add/update welcome message"""
        if not self.connected:
            await self.connect()
        
        try:
            settings = self.db.settings
            await settings.update_one(
                {"chat_id": chat_id, "type": "welcome"},
                {
                    "$set": {
                        "enabled": enabled,
                        "message": message,
                        "updated_at": datetime.utcnow()
                    }
                },
                upsert=True
            )
            return True
        except Exception as e:
            log.error(f"Failed to add welcome: {e}")
            return False
    
    async def get_welcome(self, chat_id: int) -> Optional[Dict]:
        """Get welcome settings"""
        if not self.connected:
            await self.connect()
        
        try:
            settings = self.db.settings
            return await settings.find_one({
                "chat_id": chat_id,
                "type": "welcome"
            })
        except Exception as e:
            log.error(f"Failed to get welcome: {e}")
            return None


# Database instance
db = Database()
