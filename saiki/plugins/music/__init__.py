import json

from nonebot.adapters.cqhttp import MessageSegment

from .data_source import dataGet, dataProcess
from nonebot.permission import Permission
from nonebot.adapters import Bot, Event
from nonebot.typing import T_State
from nonebot import on_command

dataget = dataGet()

songpicker = on_command(
    cmd="点歌", aliases={"来首歌", "我想听"}, permission=Permission(), priority=5)


@songpicker.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()
    if args.isdigit():
        if "songName" in state:
            state["songNum"] = int(args)
    elif args:
        state["songName"] = args


@songpicker.got("songName", prompt="歌名是？")
async def handle_songName(bot: Bot, event: Event, state: T_State):
    songName = state["songName"]
    songIdList = await dataget.songIds(songName=songName)
    if not songIdList:
        await songpicker.reject("没有找到这首歌，请发送其它歌名！")
    songInfoList = list()
    for songId in songIdList:
        songInfoDict = await dataget.songInfo(songId)
        songInfoList.append(songInfoDict)
    songInfoMessage = await dataProcess.mergeSongInfo(songInfoList)
    songInfoMessageJson = {
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
                    "appName": f"{songName}结果如下,请输入欲点播歌曲的序号：",
                    "appType": "",
                    "appid": "",
                    "iconUrl": "https://bizaladdin-image.baidu.com/0/pic/67edf360ac5f88826e3d757a5e407579.jpg"
                },
                "data": songInfoMessage,
                "title": "",
                "button": [
                    {
                        "name": "【回复序号可重选】",
                        "action": ""
                    }
                ],
                "emphasis_keyword": ""
            }
        },
        "text": "",
        "sourceAd": ""
    }
    await songpicker.send(message=MessageSegment.json(data=json.dumps(songInfoMessageJson)))
    state["songIdList"] = songIdList


@songpicker.got("songNum")
async def handle_songNum(bot: Bot, event: Event, state: T_State):
    songIdList = state["songIdList"]
    songNum = state["songNum"]

    # 处理重选
    if not songNum.isdigit():
        await songpicker.finish()
    else:
        songNum = int(songNum)

    if songNum >= len(songIdList):
        await songpicker.reject("数字序号错误，请重选")

    selectedSongId = songIdList[int(songNum)]

    songContent = [
        {
            "type": "music",
            "data": {
                "type": 163,
                "id": selectedSongId
            }
        }
    ]
    await songpicker.send(songContent)

    songCommentsDict = await dataget.songComments(songId=selectedSongId)
    songCommentsMessage = await dataProcess.mergeSongComments(songCommentsDict)
    commentContent = [
        {
            "type": "text",
            "data": {
                "text": "下面为您播送热评：\n"
            }
        },
        {
            "type": "text",
            "data": {
                "text": songCommentsMessage
            }
        },
        {
            "type": "text",
            "data": {
                "text": "\n【回复序号可重选】"
            }
        }
    ]

    await songpicker.send(commentContent)

    # 重选功能
    await songpicker.reject()
