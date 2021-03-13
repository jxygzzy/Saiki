import json

from nonebot import on_command
from nonebot.adapters.cqhttp import MessageSegment
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from .data_source import get_weather

weather = on_command("天气", rule=to_me(), priority=5)


@weather.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip().split()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
    if args:
        state["city"] = args[0]  # 如果用户发送了参数则直接赋值


@weather.got("city", prompt="你想查询哪个城市的天气呢？")
async def handle_city(bot: Bot, event: Event, state: T_State):
    city = state["city"]
    code = await get_weather(city)
    if code['msg'] == "success":
        data = code['data']
        weatherJson = {
            "app": "com.tencent.miniapp",
            "desc": "",
            "view": "notification",
            "ver": "0.0.0.1",
            "prompt": "",
            "appID": "",
            "sourceName": "",
            "actionData": "",
            "actionData_A": "",
            "sourceUrl": "",
            "meta": {
                "notification": {
                    "appInfo": {
                        "appName": f"{data['cityname']}天气",
                        "appType": "",
                        "appid": "",
                        "iconUrl": "https://www.easyicon.net//api/resizeApi.php?id=1142180&size=128"
                    },
                    "data": [
                        {
                            "title": "气温:",
                            "value": f"{data['temp']}℃ {data['weather']}"
                        },
                        {
                            "title": "PM2.5:",
                            "value": f"{data['pm25']}μg/m3"
                        }
                    ],
                    "title": "",
                    "button": [
                        {
                            "name": f"最后更新时间:{data['time']}",
                            "action": ""
                        }
                    ],
                    "emphasis_keyword": ""
                }
            },
            "text": "",
            "sourceAd": ""
        }
        await weather.finish(message=MessageSegment.json(data=json.dumps(weatherJson)))
    else:
        msg = code['msg']
        await weather.finish(message=msg)
