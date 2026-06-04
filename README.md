# AllAtomic - Telegram Userbot (✿◠‿◠)

<div align="center">

![AllAtomic](https://te.legra.ph/file/9a8cff9a8cff9a8cff.jpg)

**Your Ultimate Telegram Userbot**

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**Dev:** [@GhostMarshal](https://t.me/GhostMarshal)  
**Channel:** [@ComputeCode](https://t.me/ComputeCode)  
**GitHub:** [corruptcrew/AllAtomic](https://github.com/corruptcrew/AllAtomic)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

</div>

<div align="center">

![Purple Theme](https://img.shields.io/badge/Theme-Purple-%239A8CFF)
![Version](https://img.shields.io/badge/Version-2.0.0-blue)
![License](https://img.shields.io/badge/License-GPL--3.0-green)

</div>

---

## (૨๑•̀ㅁ•́ฅा) Features

### Core Features
- ✨ **Multi-session Support** - Run multiple accounts
- 🚀 **Auto Plugin Discovery** - Load plugins automatically
- 💾 **MongoDB Database** - Persistent storage
- 🎨 **Purple Anime Theme** - Beautiful kaomoji and colors
- 🔧 **Inline Menu Support** - Bot commands with inline buttons
- 📦 **80+ Commands** - Across 13 categories

### Command Categories
1. **Core** - Start, help, stats, ping, credits
2. **Admin** - Ban, kick, mute, promote, gban
3. **Fun** - Meme, joke, dice, rps, waifu
4. **Utilities** - Time, date, paste, notes
5. **Media** - Photo, video, audio, stickers
6. **Anime** - Anime info, manga, characters, waifu images
7. **AI** - Chat with AI, image generation, translate
8. **Tools** - Wiki, weather, trivia, facts
9. **Group** - Welcome, goodbye, purge, tag
10. **User** - Forward, reply, clean, clear
11. **Search** - Reverse image, OCR, lyrics
12. **Broadcast** - Send to all users
13. **Other** - Afk, uptime, id

---

## (◕‿◕) Installation

### Method 1: Heroku (Recommended)

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/corruptcrew/AllAtomic)

1. Click the button above
2. Fill in your environment variables
3. Deploy!

### Method 2: VPS/Dedicated Server

```bash
# Clone repository
git clone https://github.com/corruptcrew/AllAtomic.git
cd AllAtomic

# Install dependencies
pip install -r requirements.txt

# Copy environment file
cp .env.example .env

# Edit .env with your credentials
nano .env

# Run the bot
python -m AllAtomic
```

### Method 3: Docker

```bash
# Build image
docker build -t allatomic .

# Run container
docker run -d --name allatomic -v $(pwd)/.env:/app/.env allatomic
```

---

## (🔥) Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `API_ID` | Telegram API ID | ✅ |
| `API_HASH` | Telegram API Hash | ✅ |
| `STRING_SESSION` | Pyrogram session string | ✅ |
| `BOT_TOKEN` | Bot token (for inline) | ⚠️ |
| `MONGO_URL` | MongoDB connection URL | ⚠️ |
| `OWNER_ID` | Your user ID | ⚠️ |
| `SUDO_USERS` | Sudo user IDs | ⚠️ |

### Get String Session

1. Visit [replit](https://replit.com/@GhostMarshal/StringSession-Generator)
2. Run the generator
3. Copy your session string

---

## (✨) Commands

### Core Commands
```
/start - Start the bot
/help - Show help
/stats - Show bot stats
/ping - Check latency
/source - Get source code
/credits - Show credits
```

### Admin Commands
```
/admins - List admins
/addadmin - Add admin
/rmadmin - Remove admin
/ban - Ban user
/unban - Unban user
/kick - Kick user
/gban - Global ban
/ungban - Remove gban
```

### Fun Commands
```
/meme - Get random meme
/joke - Get random joke
/quote - Get random quote
/roll - Roll dice
/flip - Coin flip
/rps - Rock Paper Scissors
/waifu - Get waifu image
/neko - Get neko image
```

### Anime Commands
```
/anime <name> - Get anime info
/manga <name> - Get manga info
/character <name> - Get character info
/waifu - Get waifu
/neko - Get neko
/megumin - Get Megumin
/shinobu - Get Shinobu
/kitsune - Get Kitsune
```

### AI Commands
```
/ai <message> - Chat with AI
/dall <prompt> - Generate image
/translate - Translate text
/wiki <topic> - Wikipedia
/weather <city> - Weather info
```

### Utility Commands
```
/time - Show time
/date - Show date
/id - Show IDs
/paste - Paste text
/note - Manage notes
/afk - Set AFK status
```

---

## (💜) Screenshots

<div align="center">

| Main Menu | Commands List | Anime Waifu |
|-----------|---------------|-------------|
| 🌸 | 🎨 | 🌺 |
| 🌼 | 🍥 | 🌸 |

</div>

---

## (🔥) Deployment Options

### Heroku
- Easy one-click deploy
- Free tier available
- Automatic updates

### VPS
- Full control
- Better performance
- Custom configuration

### Replit
- Cloud-based
- Easy to use
- Always online

### Docker
- Containerized
- Platform independent
- Easy scaling

---

## (✨) Plugins

AllAtomic supports auto-loading plugins from the `plugins/user/` directory.

### Create a Plugin

```python
from pyrogram import filters
from AllAtomic import log, clients, config

async def load(bot):
    @bot.on_message(filters.command("hello"))
    async def hello(client, message):
        await message.reply("Hello! (✿◠‿◠)")
```

---

## (💜) Credits

- **Developer:** [@GhostMarshal](https://t.me/GhostMarshal)
- **Channel:** [@ComputeCode](https://t.me/ComputeCode)
- **Theme:** Purple Anime (#9A8CFF)
- **Framework:** Pyrogram v2.x
- **Database:** MongoDB
- **License:** GPL-3.0

---

## (🔥) Support

- **Channel:** [@ComputeCode](https://t.me/ComputeCode)
- **GitHub:** [corruptcrew/AllAtomic](https://github.com/corruptcrew/AllAtomic)
- **Issues:** [Report bugs](https://github.com/corruptcrew/AllAtomic/issues)

---

## (✨) License

This project is licensed under the GPL-3.0 License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**Made with ❤️ and kaomoji**  
(૨๑•̀ㅁ•́ฅा) (✿◠‿◠) (◕‿◕)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**AllAtomic v2.0.0** | **Dev: @GhostMarshal** | **Channel: @ComputeCode**

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

</div>
