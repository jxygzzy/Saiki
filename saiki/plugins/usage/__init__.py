from nonebot import on_command
from nonebot.adapters.cqhttp import MessageSegment, Message
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event

usage = on_command(cmd="功能", aliases={"帮助", "功能", "help"}, rule=to_me(), priority=5)


@usage.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    await bot.send(event=event, message=Message(
        "[CQ:image,file=https://gitee.com/jxygzzy/filebad/raw/master/svg/20210615-205222-0699.png]"))
