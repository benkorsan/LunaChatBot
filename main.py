import re
import os
from pyrogram import filters, Client 
from pyrogram.types import Message
import requests


is_config = os.path.exists("config.py")

if is_config:
    from config import *
else:
    from sample_config import *

neko = Client(name="aichan", api_hash=API_HASH, api_id=API_ID,
              bot_token=TOKEN)

bot_id = int(bot_token.split(":")[0])

@neko.on_message(filters.text, group=100)
async def ai(_, message: Message):
    if message.reply_to_message and message.reply_to_message.from_user.id == BOT_ID:
        ai_gen = requests.get(f"https://apikatsu.otakatsu.studio/api/chatbot/Iseria?message={message.text}", timeout=5).json()["response"]
        print(ai_gen)
        await neko.send_message(chat_id=message.chat.id ,text=ai_gen , reply_to_message_id=message.id)

    

@neko.on_message(filters.command(commands=["missharley_bot"] , prefixes="@"))
async def username(_, message: Message):
    fixed_text = message.text.replace("Selam", "")
    ai_gen = requests.get(f"https://apikatsu.otakatsu.studio/api/chatbot/Iseria?message={fixed_text}", timeout=5).json()["response"]
    print(ai_gen)
    await neko.send_message(chat_id=message.chat.id ,text=ai_gen, reply_to_message_id=message.id)

neko.run()
