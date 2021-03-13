import json
from xml.dom import minidom

from nonebot import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp import MessageSegment
from .data_source import get_wallpaper

wallpaper = on_command("壁纸", rule=to_me(), priority=5)


@wallpaper.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    url = await get_wallpaper()
    await bot.send(event=event, message=MessageSegment.image(file=url))

