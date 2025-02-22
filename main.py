import os
import random
from telethon import TelegramClient
from telethon.tl.types import InputMessagesFilterPhotos
from astrbot.api.all import *
from astrbot.api.message_components import *
from astrbot.api.star import Context, Star, register
from astrbot.api import logger

@register("telegram_img", "YourName", "Telegram频道图片下载插件", "1.0.0")
class TelegramImageDownloader(Star):
    def __init__(self, context: Context, config: dict):
        super().__init__(context)
        self.config = config
        # 从配置文件获取 Telegram API 信息
        self.api_id = int(config.get("api_id", ""))
        self.api_hash = config.get("api_hash", "")
        self.session_name = config.get("session_name", "tg_downloader")
        self.client = None

    async def init_client(self):
        if not self.client:
            self.client = TelegramClient(self.session_name, self.api_id, self.api_hash)
            await self.client.start()

    @command("tg随机图")
    async def random_image(self, event: AstrMessageEvent):
        '''从指定的Telegram频道随机下载一张图片'''
        if not self.api_id or not self.api_hash:
            yield event.plain_result("请先配置 Telegram API 信息")
            return

        await self.init_client()
        
        # 获取用户输入的频道名
        channel_name = event.message_str.strip()
        if not channel_name:
            yield event.plain_result("请输入Telegram频道名称")
            return

        try:
            # 获取频道实体
            channel = await self.client.get_entity(channel_name)
            
            # 获取最新消息ID
            latest_message = await self.client.get_messages(channel, limit=1)
            max_id = latest_message[0].id

            # 随机选择一个消息ID
            while True:
                random_id = random.randint(1, max_id)
                message = await self.client.get_messages(channel, ids=random_id)
                
                if message and message.photo:
                    # 下载图片
                    download_path = f"downloads/telegram_images/{channel_name}_{random_id}.jpg"
                    os.makedirs(os.path.dirname(download_path), exist_ok=True)
                    
                    await message.download_media(download_path)
                    
                    # 发送图片
                    yield event.chain_result([
                        Plain(f"已从频道 {channel_name} 获取随机图片\n"),
                        Image.fromPath(download_path)
                    ])
                    break

        except Exception as e:
            logger.error(f"下载图片失败: {str(e)}")
            yield event.plain_result(f"下载失败: {str(e)}")

    def __del__(self):
        if self.client:
            self.client.disconnect()
