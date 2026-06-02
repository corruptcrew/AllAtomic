"""
Logger for AllAtomic Userbot
Purple-themed logging with emojis
"""

import logging
import sys
from datetime import datetime

class AtomicFormatter(logging.Formatter):
    """Custom formatter with purple theme"""
    
    grey = "\x1b[38;21m"
    purple = "\x1b[38;5;141m"
    pink = "\x1b[38;5;213m"
    red = "\x1b[38;5;196m"
    bold_red = "\x1b[38;5;196;1m"
    reset = "\x1b[0m"
    
    format_str = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    
    FORMATS = {
        logging.DEBUG: grey + format_str + reset,
        logging.INFO: purple + format_str + reset,
        logging.WARNING: "\x1b[38;5;226m" + format_str + reset,
        logging.ERROR: red + format_str + reset,
        logging.CRITICAL: bold_red + format_str + reset
    }
    
    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, datefmt="%H:%M:%S")
        return formatter.format(record)

def setup_logger(name: str = "AllAtomic") -> logging.Logger:
    """Setup logger with purple theme"""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(AtomicFormatter())
    
    # File handler
    file_handler = logging.FileHandler("allatomic.log")
    file_handler.setLevel(logging.DEBUG)
    file_formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    file_handler.setFormatter(file_formatter)
    
    # Add handlers
    if not logger.handlers:
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)
    
    return logger

# Default logger
logger = setup_logger()

def log_startup():
    """Log startup message"""
    logger.info("╔═══════════════════════════════════════════════════════╗")
    logger.info("║           ⚛️  AllAtomic Userbot Starting              ║")
    logger.info("║                                                       ║")
    logger.info("║  Dev: @GhostMarshal                                   ║")
    logger.info("║  Channel: @ComputeCode                                ║")
    logger.info("║  Theme: Purple Anime 💜                               ║")
    logger.info("╚═══════════════════════════════════════════════════════╝")

def log_shutdown():
    """Log shutdown message"""
    logger.info("👋 AllAtomic shutting down...")
    logger.info("💜 Thank you for using AllAtomic!")
