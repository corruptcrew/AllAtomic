#!/usr/bin/env python3
"""Pyrogram session generator"""
from pyrogram import Client

API_ID = 38568281
API_HASH = "5dec3f281b9576f65824326f7cd984ed"
PHONE = "+31613044783"

print("🔐 Pyrogram Session Generator")
print("="*50)

with Client("allatomic", api_id=API_ID, api_hash=API_HASH) as app:
    session = app.export_session_string()
    print(f"\n✅ SESSION: {session}\n")
    print("="*50)
