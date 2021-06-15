import random

from nonebot import on_command
from nonebot.adapters.cqhttp import Message
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from .data_source import get_ans

wallpaper = on_command("", rule=to_me(), priority=1)


@wallpaper.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    question = str(event.get_message()).strip()
    ans = await get_ans(question)
    if ans['code'] == 200:
        await bot.send(event=event, message=Message(ans['newslist'][0]['reply']))
    else:
        expr_tuling = [
            '系统出错了哦~联系主人修复吧！',
            '我的脑子好像不够用了~',
            '服务器被偷了~Saiki不能理解你在说什么啦~'
        ]
        await bot.send(event=event, message=Message(random.choice(expr_tuling)))
