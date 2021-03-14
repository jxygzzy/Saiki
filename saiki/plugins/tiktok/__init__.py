import json

from nonebot import on_command
from nonebot.adapters.cqhttp import MessageSegment
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event

from .data_source import get_resou

tiktok = on_command(cmd="抖音", aliases={"抖音", "tiktok"}, rule=to_me(), priority=5)


@tiktok.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    res = await get_resou()
    data = []
    for item in res:
        data.append({
            "title": f"{item['hot']}",
            "value": item['name']
        })

    tiktokJson = {
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
                    "appName": "抖音热搜榜",
                    "appType": "",
                    "appid": "",
                    "iconUrl": "https://ss3.bdstatic.com/yrwDcj7w0QhBkMak8IuT_XF5ehU5bvGh7c50/logopic/3219d0d1c4e4ce833636bb4feddbbe08_fullsize.jpg"
                },
                "data": data,
                "title": "",
                "emphasis_keyword": ""
            }
        },
        "text": "",
        "sourceAd": ""
    }
    await tiktok.finish(message=MessageSegment.json(data=json.dumps(tiktokJson)))
