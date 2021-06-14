from nonebot import on_command
from nonebot.adapters.cqhttp import MessageSegment, Message
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event

usage = on_command(cmd="功能", aliases={"帮助", "功能", "help"}, rule=to_me(), priority=5)


@usage.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    await bot.send(event=event, message=Message(
        "[CQ:share,url=https://gitee.com/jxygzzy/saiki-bot-function-description"
        ",title=Saiki-BOT-支持功能列表,content=QQ机器人Saiki的功能说明]"))
