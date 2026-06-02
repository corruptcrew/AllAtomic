"""
🔧 Weather Plugin for AllAtomic Userbot
Get weather information for any location
"""

import asyncio
import aiohttp
from telethon import events

from plugins import atomic_command
from app.utils import get_kaomoji

# Plugin metadata
__plugin__ = {
    "name": "Weather",
    "description": "Get weather information",
    "category": "utility"
}

@atomic_command(
    "weather",
    pattern=r"\.weather(?:\s|$)(.*)",
    help="Get weather information",
    usage=".weather <city>",
    category="utility"
)
async def weather_handler(event):
    """Get weather for a city"""
    from app import config
    
    city = event.pattern_match.group(1)
    
    if not city:
        await event.edit("❌ Please provide a city name!\n\nUsage: `.weather <city>`")
        return
    
    msg = await event.edit(f"🌤️  Getting weather for **{city}**... {get_kaomoji('thinking')}")
    
    try:
        api_key = config.WEATHER_API
        
        if not api_key:
            # Use free API without key
            async with aiohttp.ClientSession() as session:
                async with session.get(f"https://wttr.in/{city}?format=j1") as resp:
                    if resp.status == 200:
                        data = await resp.json()
                        
                        current = data.get("current_condition", [{}])[0]
                        weather_desc = current.get("weatherDesc", [{}])[0].get("value", "Unknown")
                        temp_c = current.get("temp_C", "Unknown")
                        temp_f = current.get("temp_F", "Unknown")
                        humidity = current.get("humidity", "Unknown")
                        wind_kph = current.get("windspeedKmph", "Unknown")
                        feels_like = current.get("FeelsLikeC", "Unknown")
                        
                        weather_msg = f"""
🌤️ **Weather in {city}** {get_kaomoji('happy')}

━━━━━━━━━━━━━━━━━━━━━━

🌡️ **Temperature:** `{temp_c}°C` / `{temp_f}°F`
🤔 **Feels Like:** `{feels_like}°C`
💧 **Humidity:** `{humidity}%`
💨 **Wind:** `{wind_kph} km/h`
🌫️ **Condition:** {weather_desc}

━━━━━━━━━━━━━━━━━━━━━━

💜 AllAtomic Userbot
                        """
                        
                        await msg.edit(weather_msg, parse_mode="md")
                        return
        
        # With API key (OpenWeatherMap)
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
            ) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    
                    weather_desc = data["weather"][0]["description"]
                    temp = data["main"]["temp"]
                    feels_like = data["main"]["feels_like"]
                    humidity = data["main"]["humidity"]
                    wind = data["wind"]["speed"]
                    country = data["sys"]["country"]
                    
                    weather_msg = f"""
🌤️ **Weather in {city}, {country}** {get_kaomoji('happy')}

━━━━━━━━━━━━━━━━━━━━━━

🌡️ **Temperature:** `{temp}°C`
🤔 **Feels Like:** `{feels_like}°C`
💧 **Humidity:** `{humidity}%`
💨 **Wind:** `{wind} m/s`
🌫️ **Condition:** {weather_desc}

━━━━━━━━━━━━━━━━━━━━━━

💜 AllAtomic Userbot
                    """
                    
                    await msg.edit(weather_msg, parse_mode="md")
                    return
                else:
                    await msg.edit(f"❌ City not found! {get_kaomoji('sad')}")
        
    except Exception as e:
        await msg.edit(f"❌ Error: {e}")
    
    await asyncio.sleep(60)
    await msg.delete()

# Commands registry
commands = {
    "weather": {
        "help": "Get weather information",
        "usage": ".weather <city>",
        "category": "utility"
    }
}
