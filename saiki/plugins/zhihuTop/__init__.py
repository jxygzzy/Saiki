import json

from nonebot import on_command
from nonebot.adapters.cqhttp import MessageSegment
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event

from .data_source import get_zhTop_data

zhihu = on_command("知乎", rule=to_me(), priority=5)


@zhihu.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    res = await get_zhTop_data()
    data = []
    for item in res:
        data.append({
            "title": item['name'],
            "value": item['query']
        })

    zhihuJson = {
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
                    "appName": "知乎热搜榜",
                    "appType": "",
                    "appid": "",
                    "iconUrl": "https://gss3.bdstatic.com/84oSdTum2Q5BphGlnYG/timg?wapp&quality=80&size=b150_150&subsize=20480&cut_x=0&cut_w=0&cut_y=0&cut_h=0&sec=1369815402&srctrace&di=80c98c17d6c06d4e2a92d94a5bad2123&wh_rate=null&src=http%3A%2F%2Fimgsrc.baidu.com%2Fforum%2Fpic%2Fitem%2F6709c93d70cf3bc71923c096d200baa1cd112aac.jpg"
                },
                "data": data,
                "title": "",
                "emphasis_keyword": ""
            }
        },
        "text": "",
        "sourceAd": ""
    }
    await zhihu.finish(message=MessageSegment.json(data=json.dumps(zhihuJson)))
