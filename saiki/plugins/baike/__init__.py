from nonebot import on_command
from nonebot.adapters.cqhttp import MessageSegment
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from .data_source import fetch_wikipedia

baike = on_command("百科", rule=to_me(), priority=5)


@baike.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip().split()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
    if args:
        state["words"] = args[0]  # 如果用户发送了参数则直接赋值


@baike.got("words", prompt="你想查询什么词条呢？")
async def handle_city(bot: Bot, event: Event, state: T_State):
    words = state["words"]
    data = await fetch_wikipedia(words)
    if data['content'] == '':
        msg = '==未找到该词条=='
        await bot.send(event=event, message=msg)
    else:
        msg = data['content']

        await bot.send(event=event, message=msg + MessageSegment.image(file=data['ImgUrl']))
