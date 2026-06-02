# ⚛️ AllAtomic Userbot

<div align="center">

![AllAtomic Banner](https://i.imgur.com/placeholder-shadow.gif)

**「 I Am The Atom That Rules All 」**

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/new)
[![Deploy to Heroku](https://www.herokucdn.com/deploy-button.svg)](https://heroku.com/deploy?template=https://github.com/corruptcrew/AllAtomic)

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)
![Telethon](https://img.shields.io/badge/Telethon-1.34-purple?style=for-the-badge)
![Commands](https://img.shields.io/badge/Commands-200+-green?style=for-the-badge)
![Plugins](https://img.shields.io/badge/Plugins-50+-brightgreen?style=for-the-badge)

📢 **[@ComputeCode](https://t.me/ComputeCode)** | 👨‍💻 **[@GhostMarshal](https://t.me/GhostMarshal)**

</div>

---

<div align="center">

![Shadow Anime](https://i.imgur.com/placeholder-shadow2.gif)

*「 Power without control is meaningless. Control without power is useless. I have both. 」**

</div>

---

## 🌑 What is AllAtomic?

> *"In the shadows, I command forces unseen. AllAtomic is my creation - the ultimate Telegram userbot that bends the digital world to my will."*

AllAtomic is a **Telegram userbot** built with **Telethon** that automates everything - from group management to media downloads, AI chat to anime commands. With **200+ commands** and **50+ plugins**, it's the most powerful userbot you'll ever deploy.

---

## ⚡ Quick Deploy

<div align="center">

### 🚂 Deploy to Railway (Recommended)

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/new)

**✨ Free $5 credit | No card needed | 1-click deploy**

---

### 🛒 Deploy to Heroku

[![Deploy to Heroku](https://www.herokucdn.com/deploy-button.svg)](https://heroku.com/deploy?template=https://github.com/corruptcrew/AllAtomic)

**🎁 Free tier | Auto PostgreSQL | Easy scaling**

</div>

---

## 📋 Setup Guide

### Step 1: Get Telegram API Keys

1. Visit **https://my.telegram.org**
2. Login with your phone number
3. Click **"API development tools"**
4. Create a new application
5. Copy **API_ID** and **API_HASH**

<div align="center">
⚔️ 「 These keys are your gateway to power 」
</div>

---

### Step 2: Generate Session String

**Option A - Local (Recommended):**
```bash
git clone https://github.com/corruptcrew/AllAtomic
cd AllAtomic
pip install telethon
python3 generate_string_session.py
```

**Option B - Railway Shell:**
1. Deploy to Railway first
2. Open **Shell** from Railway dashboard
3. Run: `python3 generate_string_session.py`
4. Copy the session string to environment variables

<div align="center">
⚔️ 「 The session string is your soul - keep it secret 」
</div>

---

### Step 3: Environment Variables

**Required:**
```bash
API_ID=12345678
API_HASH=your_api_hash_here
SESSION_STRING=1BVtsOKbx...
OWNER_ID=your_telegram_id
DATABASE_URL=postgresql://...
```

**Optional:**
```bash
HANDLER=.
OPENAI_API_KEY=sk-...
HEROKU_API_KEY=
HEROKU_APP_NAME=
LOGGER_ID=
```

> Get your **OWNER_ID** from [@userinfobot](https://t.me/userinfobot) on Telegram.

---

## 🎯 Commands

<div align="center">

### ⚛️ Core Commands

| Command | Description |
|---------|-------------|
| `.alive` | Check bot status |
| `.ping` | Response time |
| `.help` | Show all commands |
| `.status` | Bot statistics |
| `.restart` | Restart bot |
| `.eval` | Evaluate Python |
| `.exec` | Execute Python |
| `.term` | Terminal command |
| `.sudo` | Run as sudo |
| `.heroku` | Heroku manager |

---

### 👥 Group Management

| Command | Description |
|---------|-------------|
| `.ban` | Ban user |
| `.kick` | Kick user |
| `.mute` | Mute user |
| `.unmute` | Unmute user |
| `.purge` | Delete messages |
| `.zombies clean` | Remove deleted accounts |
| `.lock` | Lock group |
| `.unlock` | Unlock group |
| `.pin` | Pin message |
| `.unpin` | Unpin all |
| `.setwelcome` | Set welcome message |
| `.setgoodbye` | Set goodbye message |

---

### 💬 PM Management

| Command | Description |
|---------|-------------|
| `.approve` | Approve user for PM |
| `.disapprove` | Remove approval |
| `.block` | Block user |
| `.unblock` | Unblock user |
| `.arc` | Archive chat |

---

### 🎬 Media Downloads

| Command | Description |
|---------|-------------|
| `.yt` | YouTube video |
| `.song` | YouTube audio |
| `.insta` | Instagram post |
| `.tiktok` | TikTok video |
| `.twitter` | Twitter video |
| `.fb` | Facebook video |
| `.media` | Universal downloader |

---

### 🎙️ Voice Chat

| Command | Description |
|---------|-------------|
| `.vcstart` | Start voice chat |
| `.vcend` | End voice chat |
| `.play` | Play music in VC |
| `.np` | Now playing |
| `.lastfm` | Last.fm stats |

---

### 🌸 Anime & Fun

| Command | Description |
|---------|-------------|
| `.waifu` | Random anime girl |
| `.neko` | Random neko |
| `.anime` | Search anime info |
| `.manga` | Search manga info |
| `.meme` | Reddit meme |
| `.joke` | Random joke |
| `.fact` | Random fact |
| `.quote` | Inspiring quote |

---

### 🔧 Utilities

| Command | Description |
|---------|-------------|
| `.weather` | Weather forecast |
| `.paste` | Paste to bin |
| `.git` | GitHub repo info |
| `.qr` | Generate QR code |
| `.tr` | Translate text |
| `.remind` | Set reminder |
| `.direct` | Direct download link |
| `.font` | Font styles |

---

### 🤖 AI Features

| Command | Description |
|---------|-------------|
| `.chat` | Chat with AI |
| `.ask` | Ask AI anything |
| `.summarize` | Summarize text |

</div>

> **「 Type `.help` after deploy for the full command list 」**

---

## 🗂️ File Structure

```
AllAtomic/
├── app/
│   ├── main.py           # Entry point
│   ├── config.py         # Configuration
│   ├── client.py         # Telethon client
│   ├── database.py       # Database models
│   └── utils/
│       └── helpers.py    # Helper functions
├── plugins/
│   ├── core/             # Core commands
│   ├── group/            # Group management
│   ├── pm/               # PM permit
│   ├── media/            # Downloads & VC
│   ├── anime/            # Anime commands
│   ├── ai/               # AI features
│   ├── utility/          # Utilities
│   └── fun/              # Fun commands
├── assets/               # Images, GIFs
├── requirements.txt      # Dependencies
├── Dockerfile           # Docker config
├── app.json             # Heroku config
├── railway.json         # Railway config
└── README.md            # This file
```

---

## 🐳 Docker Deploy

```bash
# Build image
docker build -t allatomic .

# Run container
docker run -d --env-file .env allatomic

# Or with Docker Compose
docker-compose up -d

# View logs
docker logs -f allatomic
```

---

## 🛠️ Local Installation

```bash
# Clone repository
git clone https://github.com/corruptcrew/AllAtomic
cd AllAtomic

# Install dependencies
pip install -r requirements.txt

# Configure
cp .env.example .env
nano .env  # Edit with your credentials

# Generate session
python3 generate_string_session.py

# Run bot
python3 app/main.py
```

---

## 🔧 Troubleshooting

<div align="center">

| Problem | Solution |
|---------|----------|
| **Bot won't start** | Check logs, verify API credentials |
| **Session expired** | Regenerate session string |
| **Database error** | Ensure PostgreSQL is connected |
| **Missing modules** | `pip install -r requirements.txt` |
| **Command not working** | Check if plugin is loaded |

</div>

> **「 Every problem has a solution. Every error has a fix. 」**

---

## 📊 Features

- ✅ **200+ Commands** - Complete automation
- ✅ **50+ Plugins** - Modular architecture
- ✅ **Group Management** - Full admin control
- ✅ **Media Downloads** - YT, Insta, TikTok, Twitter, FB
- ✅ **Voice Chat** - VC management with music
- ✅ **AI Integration** - Chat, summarize, ask
- ✅ **Anime Commands** - Waifu, neko, manga search
- ✅ **PM Permit** - Auto-approve/block users
- ✅ **Notes & Filters** - Save and auto-respond
- ✅ **Welcome Messages** - Custom greetings
- ✅ **Broadcast** - Send to all groups
- ✅ **Heroku Manager** - Full Heroku control
- ✅ **Deploy Anywhere** - Railway, Heroku, Render, VPS, Docker

---

## ⚠️ Disclaimer

> *"With great power comes great responsibility."*

This is a **userbot**, not a bot. It uses your **personal Telegram account**.

- Use responsibly
- Don't spam or abuse
- Telegram may ban accounts for misuse
- For educational purposes only
- Developers not responsible for bans

---

## 📜 License

MIT License - See [LICENSE](LICENSE) file

---

<div align="center">

![Shadow Divider](https://i.imgur.com/placeholder-divider.gif)

## 👑 Credits

**⚛️ Developer:** [@GhostMarshal](https://t.me/GhostMarshal)  
**📢 Channel:** [@ComputeCode](https://t.me/ComputeCode)  
**🔗 GitHub:** [corruptcrew/AllAtomic](https://github.com/corruptcrew/AllAtomic)

---

![Shadow Anime 2](https://i.imgur.com/placeholder-shadow3.gif)

**「 I Am Atomic. And I Rule The Shadows. 」**

<div align="center">

⚛️ **AllAtomic v1.0** | Made with 💜 by @GhostMarshal

[![GitHub stars](https://img.shields.io/github/stars/corruptcrew/AllAtomic?style=social)](https://github.com/corruptcrew/AllAtomic/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/corruptcrew/AllAtomic?style=social)](https://github.com/corruptcrew/AllAtomic/network/members)

</div>

</div>
