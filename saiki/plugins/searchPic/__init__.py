import json

from nonebot import on_command
from nonebot.adapters.cqhttp import MessageSegment, Message
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from .data_source import search_pic

searchPic = on_command("搜图", rule=to_me(), priority=5)


@searchPic.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip() # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
    if args:
        state["keywords"] = args  # 如果用户发送了参数则直接赋值


@searchPic.got("keywords", prompt="请输入关键字")
async def handle_search(bot: Bot, event: Event, state: T_State):
    keywords = state["keywords"]
    data = await search_pic(keywords)
    if data == "404":
        await bot.send(event=event,message="没有符合条件的图")
    else:
        ImgCq = [
            {
                "type": "image",
                "data": {
                    "file": data['url'],
                    "type": "flash"
                }
            }
        ]
        await bot.send(event=event,message=Message("找到图了！但是发给主人了~"))
        await bot.call_api("send_private_msg", user_id=1924451951, message=ImgCq)
