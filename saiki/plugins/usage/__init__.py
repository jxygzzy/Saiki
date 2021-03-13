import json

import nonebot
from nonebot import on_command
from nonebot.adapters.cqhttp import MessageSegment
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event

usage = on_command("功能", rule=to_me(), priority=5)


@usage.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    contentJson = {
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
                    "appName": "功能列表",
                    "appType": "",
                    "appid": "",
                    "iconUrl": f"https://q4.qlogo.cn/headimg_dl?dst_uin={bot.self_id}&spec=640"
                },
                "data": [
                    {
                        "title": "",
                        "value": "百科 发送【百科 XXX】"
                    },
                    {
                        "title": "",
                        "value": "垃圾分类 发送【垃圾分类 XXX】"
                    },
                    {
                        "title": "",
                        "value": "笑话 发送【笑话】"
                    },
                    {
                        "title": "",
                        "value": "点歌 发送【点歌 XXX】"
                    },
                    {
                        "title": "",
                        "value": "彩虹屁 发送【彩虹屁】"
                    },
                    {
                        "title": "",
                        "value": "翻译 发送【翻译 XXX】"
                    },
                    {
                        "title": "",
                        "value": "壁纸 发送【壁纸】"
                    },
                    {
                        "title": "",
                        "value": "天气 发送【天气 XXX】"
                    },
                    {
                        "title": "",
                        "value": "一言 发送【一言】"
                    },
                    {
                        "title": "",
                        "value": "知乎热搜 发送【知乎】"
                    },
                    {
                        "title": "",
                        "value": "色图 发送【色图】注意使用场合"
                    },
                    {
                        "title": "",
                        "value": "复读 发送【说/say XXX】"
                    }
                ],
                "title": "",
                "button": [
                    {
                        "name": "在群聊中与bot交流请统一加上前缀",
                        "action": ""
                    },
                    {
                        "name": "目前设有如下前缀：saiki,Saiki,~",
                        "action": ""
                    }
                ],
                "emphasis_keyword": ""
            }
        },
        "text": "",
        "sourceAd": ""
    }
    face = MessageSegment.face(260)
    await bot.send(event=event,message=MessageSegment.json(json.dumps(contentJson)))
