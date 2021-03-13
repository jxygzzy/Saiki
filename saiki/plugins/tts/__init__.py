from nonebot import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event

tts = on_command(cmd="tts", aliases={"说", "say"}, rule=to_me(), priority=5)


@tts.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip().split()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
    if args:
        state["words"] = args[0]  # 如果用户发送了参数则直接赋值


@tts.got("words", prompt="说什么？")
async def handle_city(bot: Bot, event: Event, state: T_State):
    words = state["words"]
    msg = [
        {
            "type": "tts",
            "data": {
                "text": words
            }

        }
    ]
    await bot.send(event=event, message=msg)
