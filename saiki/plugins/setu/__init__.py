import json

from nonebot import on_command
from nonebot.adapters.cqhttp import MessageSegment
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from .data_source import get_setu

setu = on_command("色图", rule=to_me(), priority=5)


@setu.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    data = await get_setu()
    setuJson = {
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
                    "appName": f"标题:{data['title']}",
                    "appType": "",
                    "appid": "",
                    "iconUrl": "https://dss0.bdstatic.com/6Ox1bjeh1BF3odCf/it/u=1348432222,2058638649&fm=74&app=80&f=PNG&size=f121,121?sec=1880279984&t=8bef360aab47a34204c38aa496ccdb57"
                },
                "data": [
                    {
                        "title": "pid:",
                        "value": f"{str(data['pid'])}"
                    },
                    {
                        "title": "作者:",
                        "value": f"{data['author']}"
                    },
                    {
                        "title": "url:",
                        "value": f"{data['url']}"
                    },
                    {
                        "title": "标签:",
                        "value": f"{str(data['tags'])}"
                    }
                ],
                "title": "",
                "emphasis_keyword": ""
            }
        },
        "text": "",
        "sourceAd": ""
    }
    await bot.send(event=event, message=MessageSegment.json(data=json.dumps(setuJson)))
    ImgCq = [
        {
            "type": "image",
            "data": {
                "file": data['url'],
                "type": "flash"
            }
        }
    ]
    await bot.send(event=event, message=ImgCq)
