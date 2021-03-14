import json

from nonebot import on_command
from nonebot.adapters.cqhttp import MessageSegment
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event

from .data_source import get_resou

weibo = on_command(cmd="微博", rule=to_me(), priority=5)


@weibo.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    res = await get_resou()
    data = []
    for item in res:
        data.append({
            "title": f"{item['hot']}",
            "value": item['name']
        })

    weboJson = {
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
                    "appName": "微博热搜榜",
                    "appType": "",
                    "appid": "",
                    "iconUrl": "https://dss2.bdstatic.com/6Ot1bjeh1BF3odCf/it/u=2407332688,3354286168&fm=74&app=80&f=JPEG&size=f121,121?sec=1880279984&t=ad575eb2a5d213df9dca94b866172e8e"
                },
                "data": data,
                "title": "",
                "emphasis_keyword": ""
            }
        },
        "text": "",
        "sourceAd": ""
    }
    await weibo.finish(message=MessageSegment.json(data=json.dumps(weboJson)))
