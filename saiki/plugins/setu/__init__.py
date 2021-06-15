import json

from nonebot import on_command
from nonebot.adapters.cqhttp import MessageSegment, Message
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from .data_source import get_setu

setu = on_command("色图", aliases={"涩图", "色图"}, rule=to_me(), priority=5)


@setu.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    data = await get_setu()
    await bot.send(event=event, message=Message("找到色图了！但是发给主人了~"))
    await bot.call_api("send_private_msg", user_id=1924451951, message=MessageSegment.image(file=data['url']))
