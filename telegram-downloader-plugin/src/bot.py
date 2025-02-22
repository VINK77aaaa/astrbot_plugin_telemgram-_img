# filepath: /telegram-downloader-plugin/telegram-downloader-plugin/src/bot.py

import os
import asyncio
from dotenv import load_dotenv
from telethon import TelegramClient, events
from utils.downloader import download_file
from config import API_ID, API_HASH, SESSION_NAME

load_dotenv()

client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond('欢迎使用 Telegram 下载器插件！发送 /download 来开始下载媒体。')

@client.on(events.NewMessage(pattern='/download'))
async def download(event):
    await event.respond('请发送您想要下载的媒体消息的链接。')

@client.on(events.NewMessage)
async def handle_message(event):
    if event.message.media:
        await download_file(event.message)
        await event.respond('下载完成！')

async def main():
    await client.start()
    print("Bot is running...")
    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())