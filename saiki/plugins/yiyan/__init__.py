from nonebot import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event

from .data_source import get_yiyan

yiyan = on_command("一言", rule=to_me(), priority=5)


@yiyan.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    msg = await get_yiyan()
    await yiyan.finish(msg)
