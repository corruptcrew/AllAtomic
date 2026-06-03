from pyrogram.enums import ChatType

from Hellbot.core.clients import AllAtomic
from Hellbot.core.config import Config, Symbols
from Hellbot.core.database import db
from Hellbot.plugins.decorator import custom_handler, on_message
from Hellbot.plugins.help import HelpMenu

handler = Config.HANDLERS[0]
bot = AllAtomic.bot

bot_only = [ChatType.BOT]
group_n_channel = [ChatType.GROUP, ChatType.SUPERGROUP, ChatType.CHANNEL]
group_only = [ChatType.GROUP, ChatType.SUPERGROUP]
private_n_bot = [ChatType.PRIVATE, ChatType.BOT]
private_only = [ChatType.PRIVATE]
