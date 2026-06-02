"""
Plugin System for AllAtomic Userbot
Auto-discovers and loads plugins from plugins/ directory
"""

import importlib
from pathlib import Path
from typing import List, Dict
from telethon import events

from app.logger import logger
from app.config import Config

# Plugin registry
REGISTERED_PLUGINS: Dict[str, dict] = {}

def atomic_command(command: str, pattern: str = None, group: int = 0, **kwargs):
    """Decorator for registering atomic commands"""
    def decorator(func):
        cmd_name = command
        cmd_pattern = pattern or f"\\.{command}"
        
        REGISTERED_PLUGINS[cmd_name] = {
            "function": func,
            "pattern": cmd_pattern,
            "group": group,
            "kwargs": kwargs,
            "help": kwargs.get("help", "No description"),
            "usage": kwargs.get("usage", f".{command}"),
            "category": kwargs.get("category", "misc")
        }
        
        logger.debug(f"✓ Registered command: {cmd_name} (total: {len(REGISTERED_PLUGINS)})")
        return func
    
    return decorator

def register_handler(event_type=events.NewMessage, **kwargs):
    """Decorator for registering custom event handlers"""
    def decorator(func):
        REGISTERED_PLUGINS[func.__name__] = {
            "function": func,
            "event_type": event_type,
            "kwargs": kwargs,
            "is_handler": True
        }
        return func
    return decorator

def register_command(cmd_info: dict, client):
    """Register a command with the client"""
    func = cmd_info["function"]
    pattern = cmd_info.get("pattern")
    group = cmd_info.get("group", 0)
    kwargs = cmd_info.get("kwargs", {})
    
    event = events.NewMessage(pattern=pattern, **kwargs)
    client.add_handler(func, event=event, group=group)

def load_all_plugins(client, config: Config) -> int:
    """Load all plugins from plugins/ directory"""
    plugins_dir = Path(__file__).parent.parent / "plugins"
    loaded_count = 0
    
    logger.info(f"🔍 Searching for plugins in: {plugins_dir}")
    
    if not plugins_dir.exists():
        logger.error(f"❌ Plugins directory not found: {plugins_dir}")
        return 0
    
    # Find all plugin modules
    plugin_files = []
    
    for category_dir in plugins_dir.iterdir():
        if not category_dir.is_dir():
            continue
        
        if category_dir.name.startswith("__"):
            continue
        
        for py_file in category_dir.glob("*.py"):
            if py_file.name.startswith("__"):
                continue
            
            module_path = f"plugins.{category_dir.name}.{py_file.stem}"
            plugin_files.append(module_path)
    
    logger.info(f"📁 Found {len(plugin_files)} plugin files to load")
    
    # Load each plugin and register commands
    for module_path in plugin_files:
        try:
            logger.debug(f"📦 Importing: {module_path}")
            module = importlib.import_module(module_path)
            
            # Check for __plugin__ attribute
            if hasattr(module, "__plugin__"):
                plugin_info = module.__plugin__
                logger.info(f"  📦 {plugin_info.get('name', module_path)}")
            
        except Exception as e:
            logger.error(f"❌ Error loading {module_path}: {e}")
    
    logger.info(f"📊 REGISTERED_PLUGINS after imports: {len(REGISTERED_PLUGINS)} commands")
    
    # Now register all commands from REGISTERED_PLUGINS with the client
    for cmd_name, cmd_info in REGISTERED_PLUGINS.items():
        if cmd_info and "function" in cmd_info:
            try:
                pattern = cmd_info.get("pattern", f"\\.{cmd_name}")
                group = cmd_info.get("group", 0)
                
                # Register command with client using the correct Telethon API
                client.add_handler(
                    cmd_info["function"],
                    events.NewMessage(pattern=pattern),
                    group=group
                )
                loaded_count += 1
                
            except Exception as e:
                logger.error(f"❌ Failed to register {cmd_name}: {e}")
    
    logger.info(f"💜 Total commands registered: {loaded_count}")
    return loaded_count

def get_plugin_info(plugin_name: str) -> dict:
    """Get info about a specific plugin"""
    return REGISTERED_PLUGINS.get(plugin_name, {})

def get_all_commands() -> List[dict]:
    """Get list of all registered commands"""
    commands = []
    for name, info in REGISTERED_PLUGINS.items():
        commands.append({
            "name": name,
            "help": info.get("help", "No description"),
            "usage": info.get("usage", f".{name}"),
            "category": info.get("category", "misc")
        })
    return commands

def get_commands_by_category(category: str) -> List[dict]:
    """Get commands filtered by category"""
    commands = get_all_commands()
    return [cmd for cmd in commands if cmd.get("category") == category]

__all__ = [
    "atomic_command",
    "register_handler",
    "load_all_plugins",
    "get_plugin_info",
    "get_all_commands",
    "get_commands_by_category",
    "REGISTERED_PLUGINS"
]
