"""
🔥 Advanced Features for AllAtomic Userbot
Eval, Exec, Sudo, Heroku - Inspired by Dragon-Userbot & TechnoAyanBOT
"""

import asyncio
import os
from telethon import events

from plugins import atomic_command
from app.utils import get_kaomoji, code_block

# Plugin metadata
__plugin__ = {
    "name": "Advanced Features",
    "description": "Eval, Exec, Sudo, Heroku (Dragon-Userbot inspired)",
    "category": "core",
    "credit": "Inspired by Dragon-Userbot & TechnoAyanBOT"
}

@atomic_command(
    "eval",
    pattern=r"\.eval(?:\s|$)(.*)",
    help="Evaluate Python expression",
    usage=".eval <expression>",
    category="core"
)
async def eval_handler(event):
    """Evaluate Python expression"""
    from app import client
    
    expression = event.pattern_match.group(1)
    
    if not expression:
        await event.edit("❌ Please provide a Python expression!")
        return
    
    msg = await event.edit(f"🔍 Evaluating... {get_kaomoji('thinking')}")
    
    try:
        # Evaluate the expression
        result = eval(expression)
        
        output = f"""
🐍 **Eval Output** {get_kaomoji('happy')}

━━━━━━━━━━━━━━━━━━━━━━

**Input:**
{code_block('python', expression)}

**Output:**
{code_block('python', str(result))}

━━━━━━━━━━━━━━━━━━━━━━

💜 **AllAtomic Userbot**
📢 **Channel:** @ComputeCode
🔗 **Repo:** github.com/GhostMarshal/AllAtomic
        """
        
        await msg.edit(output, parse_mode="md")
        
    except Exception as e:
        await msg.edit(f"""
❌ **Eval Error** {get_kaomoji('sad')}

{code_block('python', str(e))}

💜 AllAtomic Userbot
        """, parse_mode="md")
    
    await asyncio.sleep(60)
    await msg.delete()

@atomic_command(
    "exec",
    pattern=r"\.exec(?:\s|$)(.*)",
    help="Execute Python code",
    usage=".exec <code>",
    category="core"
)
async def exec_handler(event):
    """Execute Python code"""
    from app import client
    
    code = event.pattern_match.group(1)
    
    if not code:
        await event.edit("❌ Please provide Python code!")
        return
    
    msg = await event.edit(f"⚙️ Executing... {get_kaomoji('thinking')}")
    
    try:
        # Create output buffer
        import io
        import sys
        
        old_stdout = sys.stdout
        redirected_output = io.StringIO()
        sys.stdout = redirected_output
        
        # Execute the code
        exec(code)
        
        # Restore stdout
        sys.stdout = old_stdout
        
        output = redirected_output.getvalue()
        
        result = f"""
⚙️ **Exec Output** {get_kaomoji('happy')}

━━━━━━━━━━━━━━━━━━━━━━

**Code:**
{code_block('python', code)}

**Output:**
{code_block('python', output or 'No output')}

━━━━━━━━━━━━━━━━━━━━━━

💜 **AllAtomic Userbot**
📢 **Channel:** @ComputeCode
🔗 **Repo:** github.com/GhostMarshal/AllAtomic
        """
        
        await msg.edit(result, parse_mode="md")
        
    except Exception as e:
        await msg.edit(f"""
❌ **Exec Error** {get_kaomoji('sad')}

{code_block('python', str(e))}

💜 AllAtomic Userbot
        """, parse_mode="md")
    
    await asyncio.sleep(60)
    await msg.delete()

@atomic_command(
    "sudo",
    pattern=r"\.sudo(?:\s|$)(.*)",
    help="Run command as sudo (admin)",
    usage=".sudo <command>",
    category="core"
)
async def sudo_handler(event):
    """Run command with sudo"""
    from app import config
    
    command = event.pattern_match.group(1)
    
    if not command:
        await event.edit("❌ Please provide a command!")
        return
    
    msg = await event.edit(f"🔐 Running as sudo... {get_kaomoji('thinking')}")
    
    try:
        # Execute shell command
        process = await asyncio.create_subprocess_shell(
            command,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        
        stdout, stderr = await process.communicate()
        
        output = stdout.decode().strip() or stderr.decode().strip() or "Command executed successfully"
        
        result = f"""
🔐 **Sudo Output** {get_kaomoji('happy')}

━━━━━━━━━━━━━━━━━━━━━━

**Command:**
{code_block('bash', command)}

**Output:**
{code_block('bash', output[:4000])}

━━━━━━━━━━━━━━━━━━━━━━

💜 **AllAtomic Userbot**
📢 **Channel:** @ComputeCode
🔗 **Repo:** github.com/GhostMarshal/AllAtomic
        """
        
        await msg.edit(result, parse_mode="md")
        
    except Exception as e:
        await msg.edit(f"""
❌ **Sudo Error** {get_kaomoji('sad')}

{code_block('bash', str(e))}

💜 AllAtomic Userbot
        """, parse_mode="md")
    
    await asyncio.sleep(60)
    await msg.delete()

@atomic_command(
    "heroku",
    pattern=r"\.heroku(?:\s|$)(.*)",
    help="Heroku management",
    usage=".heroku <command>",
    category="core"
)
async def heroku_handler(event):
    """Heroku management (TechnoAyanBOT inspired)"""
    from app import config
    
    args = event.pattern_match.group(1)
    
    msg = await event.edit(f"☁️ Heroku Manager... {get_kaomoji('thinking')}")
    
    try:
        if not args:
            await msg.edit(f"""
☁️ **Heroku Manager** {get_kaomoji('happy')}

━━━━━━━━━━━━━━━━━━━━━━

**Available Commands:**

• `.heroku logs` - Get app logs
• `.heroku restart` - Restart dyno
• `.heroku usage` - Check dyno hours
• `.heroku vars` - List config vars
• `.heroku setvar` - Set config var
• `.heroku getvar` - Get config var

━━━━━━━━━━━━━━━━━━━━━━

💜 **AllAtomic Userbot**
📢 **Channel:** @ComputeCode
🔗 **Repo:** github.com/GhostMarshal/AllAtomic

⚠️ Set HEROKU_API_KEY and HEROKU_APP_NAME in env
            """, parse_mode="md")
            return
        
        # Parse command
        cmd = args.split()[0].lower()
        
        if cmd == "logs":
            await msg.edit(f"""
📜 **Heroku Logs** {get_kaomoji('thinking')}

━━━━━━━━━━━━━━━━━━━━━━

⚠️ Configure HEROKU_API_KEY to fetch logs.

💜 AllAtomic Userbot
            """, parse_mode="md")
            
        elif cmd == "restart":
            await msg.edit(f"""
🔄 **Restarting Dyno...** {get_kaomoji('thinking')}

━━━━━━━━━━━━━━━━━━━━━━

⚠️ Configure HEROKU_API_KEY to restart.

💜 AllAtomic Userbot
            """, parse_mode="md")
            
        elif cmd == "usage":
            await msg.edit(f"""
⏱️ **Dyno Usage** {get_kaomoji('happy')}

━━━━━━━━━━━━━━━━━━━━━━

📊 **Quota:** Not configured
⏰ **Used:** 0 hours
⏱️ **Remaining:** 730 hours

💜 **AllAtomic Userbot**
📢 **Channel:** @ComputeCode
            """, parse_mode="md")
            
        elif cmd == "vars":
            await msg.edit(f"""
⚙️ **Config Vars** {get_kaomoji('happy')}

━━━━━━━━━━━━━━━━━━━━━━

API_ID: {'✅' if config.API_ID else '❌'}
API_HASH: {'✅' if config.API_HASH else '❌'}
DATABASE_URL: {'✅' if config.DATABASE_URL else '❌'}
HEROKU_API_KEY: {'✅' if config.HEROKU_API_KEY else '❌'}
HEROKU_APP_NAME: {'✅' if config.HEROKU_APP_NAME else '❌'}

💜 AllAtomic Userbot
            """, parse_mode="md")
        else:
            await msg.edit(f"❌ Unknown heroku command: `{cmd}`")
        
    except Exception as e:
        await msg.edit(f"❌ Error: {e}")
    
    await asyncio.sleep(60)
    await msg.delete()

@atomic_command(
    "gcast",
    pattern=r"\.gcast(?:\s|$)(.*)",
    help="Global broadcast to all groups",
    usage=".gcast <message>",
    category="core"
)
async def gcast_handler(event):
    """Global broadcast (Man-Userbot inspired)"""
    from app import client
    
    message = event.pattern_match.group(1)
    
    if not message:
        await event.edit("❌ Please provide a message to broadcast!")
        return
    
    msg = await event.edit(f"📢 Broadcasting... {get_kaomoji('thinking')}")
    
    try:
        # Get all dialogs (groups/channels)
        dialogs = await event.client.get_dialogs()
        groups = [d for d in dialogs if d.is_group or d.is_channel]
        
        success = 0
        failed = 0
        
        for group in groups[:50]:  # Limit to 50 to avoid rate limits
            try:
                await event.client.send_message(
                    group.id,
                    f"""
📢 **Broadcast** {get_kaomoji('happy')}

━━━━━━━━━━━━━━━━━━━━━━

{message}

━━━━━━━━━━━━━━━━━━━━━━

💜 **AllAtomic Userbot**
📢 **Channel:** @ComputeCode
🔗 **Repo:** github.com/GhostMarshal/AllAtomic
                    """,
                    parse_mode="md"
                )
                success += 1
            except:
                failed += 1
            
            await asyncio.sleep(1)  # Avoid rate limits
        
        await msg.edit(f"""
📢 **Broadcast Complete!** {get_kaomoji('happy')}

━━━━━━━━━━━━━━━━━━━━━━

✅ **Success:** `{success}` groups
❌ **Failed:** `{failed}` groups

💜 **AllAtomic Userbot**
📢 **Channel:** @ComputeCode
🔗 **Repo:** github.com/GhostMarshal/AllAtomic
        """, parse_mode="md")
        
    except Exception as e:
        await msg.edit(f"❌ Error: {e}")
    
    await asyncio.sleep(60)
    await msg.delete()

@atomic_command(
    "term",
    pattern=r"\.term(?:\s|$)(.*)",
    help="Run terminal command",
    usage=".term <command>",
    category="core"
)
async def term_handler(event):
    """Terminal command (Dragon-Userbot inspired)"""
    command = event.pattern_match.group(1)
    
    if not command:
        await event.edit("❌ Please provide a command!")
        return
    
    msg = await event.edit(f"💻 Running... {get_kaomoji('thinking')}")
    
    try:
        process = await asyncio.create_subprocess_shell(
            command,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        
        stdout, stderr = await process.communicate()
        
        output = stdout.decode().strip() or stderr.decode().strip() or "Command executed"
        
        # Split if too long
        if len(output) > 4000:
            output = output[:4000] + "... (truncated)"
        
        result = f"""
💻 **Terminal Output** {get_kaomoji('happy')}

━━━━━━━━━━━━━━━━━━━━━━

**Command:**
{code_block('bash', command)}

**Output:**
{code_block('bash', output)}

━━━━━━━━━━━━━━━━━━━━━━

💜 **AllAtomic Userbot**
📢 **Channel:** @ComputeCode
🔗 **Repo:** github.com/GhostMarshal/AllAtomic
        """
        
        await msg.edit(result, parse_mode="md")
        
    except Exception as e:
        await msg.edit(f"❌ Error: {e}")
    
    await asyncio.sleep(60)
    await msg.delete()

# Commands registry
commands = {
    "eval": {
        "help": "Evaluate Python expression",
        "usage": ".eval <expr>",
        "category": "core"
    },
    "exec": {
        "help": "Execute Python code",
        "usage": ".exec <code>",
        "category": "core"
    },
    "sudo": {
        "help": "Run command as sudo",
        "usage": ".sudo <cmd>",
        "category": "core"
    },
    "heroku": {
        "help": "Heroku management",
        "usage": ".heroku <cmd>",
        "category": "core"
    },
    "gcast": {
        "help": "Global broadcast",
        "usage": ".gcast <msg>",
        "category": "core"
    },
    "term": {
        "help": "Run terminal command",
        "usage": ".term <cmd>",
        "category": "core"
    }
}
