"""
AllAtomic - Logging Setup
Dev: @GhostMarshal | Channel: @ComputeCode
(૨๑•̀ㅁ•́ฅა) Purple Anime Theme (#9A8CFF)
"""

import logging
import sys
from datetime import datetime
from pathlib import Path
from .config import symbols


class ColoredFormatter(logging.Formatter):
    """Custom formatter with purple anime theme colors (✿◠‿◠)"""
    
    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    BOLD = "\033[1m"
    RESET = "\033[0m"
    
    FORMATS = {
        logging.DEBUG: f"{CYAN}[DEBUG]{RESET} %(asctime)s | %(name)s | %(message)s",
        logging.INFO: f"{GREEN}[INFO]{RESET} %(asctime)s | %(name)s | %(message)s",
        logging.WARNING: f"{YELLOW}[WARN]{RESET} %(asctime)s | %(name)s | %(message)s",
        logging.ERROR: f"{RED}[ERROR]{RESET} %(asctime)s | %(name)s | %(message)s",
        logging.CRITICAL: f"{RED}{BOLD}[CRITICAL]{RESET} %(asctime)s | %(name)s | %(message)s",
    }
    
    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno, self.FORMATS[logging.INFO])
        formatter = logging.Formatter(log_fmt, datefmt="%H:%M:%S")
        return formatter.format(record)


def setup_logger(name: str = "AllAtomic", log_file: str = "allatomic.log") -> logging.Logger:
    """
    Setup logger with colored output and file logging (◕‿◕)
    
    Args:
        name: Logger name
        log_file: Log file path
    
    Returns:
        Configured logger instance
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    # Create logs directory
    log_path = Path(log_file)
    log_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Console handler with colors
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(ColoredFormatter())
    
    # File handler
    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(
        logging.Formatter(
            "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
    )
    
    # Add handlers
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    
    # Prevent duplicate logs
    logger.propagate = False
    
    return logger


def log_startup(logger: logging.Logger, version: str):
    """Log startup message with theme (૨๑•̀ㅁ•́ฅა)"""
    startup_msg = f"""
{symbols.LINE}
{symbols.PURPLE}  AllAtomic v{version} Starting...{symbols.RESET}
{symbols.CUTE} Dev: @GhostMarshal
{symbols.WINK} Channel: @ComputeCode
{symbols.SPARKLE} Theme: Purple Anime (#9A8CFF)
{symbols.LINE}
"""
    logger.info(startup_msg)


# Default logger instance
log = setup_logger()
