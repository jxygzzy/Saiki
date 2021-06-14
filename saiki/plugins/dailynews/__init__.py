from nonebot import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp import MessageSegment
import os

from .data_source import get_news

wallpaper = on_command(cmd="新闻", aliases={"新闻", "每日新闻", "一觉醒来发生了什么"}, rule=to_me(), priority=5)


@wallpaper.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    path = os.path.split(os.path.realpath(__file__))[0]
    await get_news()
    await bot.send(event=event,
                   message=MessageSegment.image(
                       'file:///' + path + "/dailyNews.jpg"))
