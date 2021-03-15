import json

from nonebot import on_command
from nonebot.adapters.cqhttp import MessageSegment
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from .data_source import get_garbageSort_data

garbage = on_command("垃圾分类", rule=to_me(), priority=5)


@garbage.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()
    if args:
        state["garbage"] = args


@garbage.got("garbage", prompt="请问是什么物品呢？")
async def handle_city(bot: Bot, event: Event, state: T_State):
    keyword = state["garbage"]
    data = await get_garbageSort_data(keyword)
    garbageJson = {
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
                    "appName": f"物品:{data['Name']}",
                    "appType": "",
                    "appid": "",
                    "iconUrl": f"https://q4.qlogo.cn/headimg_dl?dst_uin={event.get_user_id()}&spec=640"
                },
                "data": [
                    {
                        "title": "分类:",
                        "value": f"{data['Type']}"
                    },
                    {
                        "title": "详细解释:",
                        "value": f"{data['Description']['Concept']}"
                    },
                    {
                        "title": f"{data['Type']}包含:",
                        "value": f"{data['Description']['Including']}"
                    },
                    {
                        "title": "处理方法:",
                        "value": f"{str(data['Description']['Release_requirement'])}"
                    }
                ],
                "title": "",
                "emphasis_keyword": ""
            }
        },
        "text": "",
        "sourceAd": ""
    }
    await bot.send(event=event,message=MessageSegment.json(data=json.dumps(garbageJson)))
