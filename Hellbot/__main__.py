from pyrogram import idle

from AllAtomic import __version__
from AllAtomic.core import (
    Config,
    ForcesubSetup,
    GachaBotsSetup,
    TemplateSetup,
    UserSetup,
    db,
    AllAtomic,
)
from AllAtomic.functions.tools import initialize_git
from AllAtomic.functions.utility import BList, Flood, TGraph


async def main():
    await AllAtomic.startup()
    await db.connect()
    await UserSetup()
    await ForcesubSetup()
    await GachaBotsSetup()
    await TemplateSetup()
    await Flood.updateFromDB()
    await BList.updateBlacklists()
    await TGraph.setup()
    await initialize_git(Config.PLUGINS_REPO)
    await AllAtomic.start_message(__version__)
    await idle()


if __name__ == "__main__":
    AllAtomic.run(main())
