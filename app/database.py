"""
Database Module for AllAtomic Userbot
SQLAlchemy ORM with PostgreSQL
"""

from sqlalchemy import create_engine, Column, String, BigInteger, Boolean, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import logging

logger = logging.getLogger("AllAtomic.DB")

Base = declarative_base()

# ───────────────────────────────────────────────────────
# Database Models
# ───────────────────────────────────────────────────────

class UserSetting(Base):
    """User settings stored in database"""
    __tablename__ = "user_settings"
    
    id = Column(BigInteger, primary_key=True)
    key = Column(String(50), nullable=False)
    value = Column(Text, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f"<UserSetting {self.key}={self.value}>"

class PluginSetting(Base):
    """Plugin-specific settings"""
    __tablename__ = "plugin_settings"
    
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    plugin_name = Column(String(50), nullable=False)
    chat_id = Column(BigInteger, nullable=False)
    key = Column(String(50), nullable=False)
    value = Column(Text, nullable=False)
    
    def __repr__(self):
        return f"<PluginSetting {self.plugin_name}.{self.key}>"

class ApprovedUser(Base):
    """Users approved for PM"""
    __tablename__ = "approved_users"
    
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, nullable=False)
    chat_id = Column(BigInteger, nullable=False)
    approved_by = Column(BigInteger, nullable=False)
    approved_at = Column(DateTime, default=datetime.utcnow)
    reason = Column(String(200), default="No reason provided")
    
    def __repr__(self):
        return f"<ApprovedUser {self.user_id}>"

class BlacklistedUser(Base):
    """Blacklisted users (gban)"""
    __tablename__ = "blacklisted_users"
    
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, nullable=False, unique=True)
    reason = Column(Text, default="No reason provided")
    added_by = Column(BigInteger, nullable=False)
    added_at = Column(DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f"<BlacklistedUser {self.user_id}>"

class Note(Base):
    """Saved notes"""
    __tablename__ = "notes"
    
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    chat_id = Column(BigInteger, nullable=False)
    name = Column(String(50), nullable=False)
    content = Column(Text, nullable=False)
    created_by = Column(BigInteger, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f"<Note {self.name}>"

class Filter(Base):
    """Chat filters"""
    __tablename__ = "filters"
    
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    chat_id = Column(BigInteger, nullable=False)
    trigger = Column(String(100), nullable=False)
    response = Column(Text, nullable=False)
    created_by = Column(BigInteger, nullable=False)
    
    def __repr__(self):
        return f"<Filter {self.trigger}>"

# ───────────────────────────────────────────────────────
# Database Manager
# ───────────────────────────────────────────────────────

class Database:
    """Database manager for AllAtomic"""
    
    def __init__(self, db_url: str):
        self.engine = create_engine(db_url, echo=False)
        self.SessionLocal = sessionmaker(bind=self.engine)
        
        # Create tables
        Base.metadata.create_all(self.engine)
        logger.info("✓ Database tables created")
    
    def get_session(self):
        """Get database session"""
        return self.SessionLocal()
    
    # ───────────────────────────────────────────────────
    # User Settings
    # ───────────────────────────────────────────────────
    
    def set_user_setting(self, user_id: int, key: str, value: str):
        """Set user setting"""
        session = self.get_session()
        try:
            setting = session.query(UserSetting).filter_by(
                id=user_id, key=key
            ).first()
            
            if setting:
                setting.value = value
            else:
                setting = UserSetting(id=user_id, key=key, value=value)
                session.add(setting)
            
            session.commit()
            return True
        except Exception as e:
            logger.error(f"DB Error (set_user_setting): {e}")
            session.rollback()
            return False
        finally:
            session.close()
    
    def get_user_setting(self, user_id: int, key: str, default=None):
        """Get user setting"""
        session = self.get_session()
        try:
            setting = session.query(UserSetting).filter_by(
                id=user_id, key=key
            ).first()
            return setting.value if setting else default
        except Exception as e:
            logger.error(f"DB Error (get_user_setting): {e}")
            return default
        finally:
            session.close()
    
    # ───────────────────────────────────────────────────
    # Approved Users
    # ───────────────────────────────────────────────────
    
    def is_approved(self, user_id: int, chat_id: int) -> bool:
        """Check if user is approved"""
        session = self.get_session()
        try:
            approved = session.query(ApprovedUser).filter_by(
                user_id=user_id, chat_id=chat_id
            ).first()
            return approved is not None
        except Exception as e:
            logger.error(f"DB Error (is_approved): {e}")
            return False
        finally:
            session.close()
    
    def approve_user(self, user_id: int, chat_id: int, approved_by: int, reason: str = ""):
        """Approve a user"""
        session = self.get_session()
        try:
            existing = session.query(ApprovedUser).filter_by(
                user_id=user_id, chat_id=chat_id
            ).first()
            
            if not existing:
                approved = ApprovedUser(
                    user_id=user_id,
                    chat_id=chat_id,
                    approved_by=approved_by,
                    reason=reason
                )
                session.add(approved)
                session.commit()
                return True
            return False
        except Exception as e:
            logger.error(f"DB Error (approve_user): {e}")
            session.rollback()
            return False
        finally:
            session.close()
    
    def disapprove_user(self, user_id: int, chat_id: int):
        """Disapprove a user"""
        session = self.get_session()
        try:
            session.query(ApprovedUser).filter_by(
                user_id=user_id, chat_id=chat_id
            ).delete()
            session.commit()
            return True
        except Exception as e:
            logger.error(f"DB Error (disapprove_user): {e}")
            session.rollback()
            return False
        finally:
            session.close()
    
    # ───────────────────────────────────────────────────
    # Blacklist (GBan)
    # ───────────────────────────────────────────────────
    
    def is_blacklisted(self, user_id: int) -> bool:
        """Check if user is blacklisted"""
        session = self.get_session()
        try:
            blacklisted = session.query(BlacklistedUser).filter_by(
                user_id=user_id
            ).first()
            return blacklisted is not None
        except Exception as e:
            logger.error(f"DB Error (is_blacklisted): {e}")
            return False
        finally:
            session.close()
    
    def blacklist_user(self, user_id: int, added_by: int, reason: str = ""):
        """Blacklist a user (GBan)"""
        session = self.get_session()
        try:
            existing = session.query(BlacklistedUser).filter_by(
                user_id=user_id
            ).first()
            
            if existing:
                existing.reason = reason
            else:
                blacklisted = BlacklistedUser(
                    user_id=user_id,
                    reason=reason,
                    added_by=added_by
                )
                session.add(blacklisted)
            
            session.commit()
            return True
        except Exception as e:
            logger.error(f"DB Error (blacklist_user): {e}")
            session.rollback()
            return False
        finally:
            session.close()
    
    def unblacklist_user(self, user_id: int):
        """Unblacklist a user"""
        session = self.get_session()
        try:
            session.query(BlacklistedUser).filter_by(
                user_id=user_id
            ).delete()
            session.commit()
            return True
        except Exception as e:
            logger.error(f"DB Error (unblacklist_user): {e}")
            session.rollback()
            return False
        finally:
            session.close()
    
    def get_blacklist_count(self) -> int:
        """Get total blacklisted users count"""
        session = self.get_session()
        try:
            return session.query(BlacklistedUser).count()
        except Exception as e:
            logger.error(f"DB Error (get_blacklist_count): {e}")
            return 0
        finally:
            session.close()
    
    def __repr__(self):
        return "<AllAtomic Database>"
