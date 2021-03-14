import json

from nonebot import on_command
from nonebot.adapters.cqhttp import MessageSegment
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from .data_source import search_pic

searchPic = on_command("搜图", rule=to_me(), priority=5)


@searchPic.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip().split()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
    if args:
        state["keywords"] = args[0]  # 如果用户发送了参数则直接赋值


@searchPic.got("keywords", prompt="请输入关键字")
async def handle_search(bot: Bot, event: Event, state: T_State):
    keywords = state["keywords"]
    data = await search_pic(keywords)
    if data == "404":
        await bot.send(event=event,message="没有符合条件的图")
    else:
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
        await bot.send(event=event, message=MessageSegment.image(file=data['url'],type_="flash"))
