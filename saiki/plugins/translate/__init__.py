from nonebot import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from .data_source import translate

trans = on_command("翻译", rule=to_me(), priority=5)


@trans.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip().split()
    if args:
        state["word"] = args[0]


@trans.got("word", prompt="你想翻译什么句子呢？")
async def handle_city(bot: Bot, event: Event, state: T_State):
    word = state["word"]
    transTarget = await translate(keyword=word)
    await trans.finish(transTarget)
