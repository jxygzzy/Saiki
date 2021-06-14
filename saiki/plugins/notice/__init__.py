from nonebot import on_notice
from nonebot.adapters.cqhttp import Bot, Event, GroupDecreaseNoticeEvent, GroupIncreaseNoticeEvent, \
    FriendAddNoticeEvent, PokeNotifyEvent, LuckyKingNotifyEvent, HonorNotifyEvent
from nonebot.rule import to_me
from nonebot.typing import T_State

from .data_source import get_nickname

LuckyKing = on_notice()
"""群红包运气王提醒事件"""


@LuckyKing.handle()
async def handle_first_receive(bot: Bot, event: LuckyKingNotifyEvent, state: T_State):
    rely = [
        {
            "type": "at",
            "data": {
                "qq": f"{event.target_id}"
            }
        },
        {
            "type": "text",
            "data": {
                "text": "是运气王"
            }
        },
        {
            "type": "image",
            "data": {
                "file": f"https://q4.qlogo.cn/headimg_dl?dst_uin={event.target_id}&spec=640"
            }
        },
        {
            "type": "text",
            "data": {
                "text": "红包来自"
            }
        },
        {
            {
                "type": "at",
                "data": {
                    "qq": f"{event.user_id}"
                }
            }
        }

    ]
    await bot.send(event=event, message=rely)


poke = on_notice(rule=to_me())
"""戳一戳提醒事件"""


@poke.handle()
async def handle_first_receive(bot: Bot, event: PokeNotifyEvent, state: T_State):
    rely = [{
        "type": "poke",
        "data": {
            "qq": event.get_user_id()
        }
    }]
    await bot.send(event=event, message=rely)


GroupDecrease = on_notice()
"""群成员减少事件"""


@GroupDecrease.handle()
async def handle_first_receive(bot: Bot, event: GroupDecreaseNoticeEvent, state: T_State):
    if event.user_id == event.operator_id:
        rely = [
            {
                "type": "text",
                "data": {
                    "text": f"【{get_nickname(event.user_id)}】主动离开了群聊\n"
                }
            },
            {
                "type": "image",
                "data": {
                    "file": f"https://q4.qlogo.cn/headimg_dl?dst_uin={event.user_id}&spec=640"
                }
            }
        ]
    else:
        rely = [
            {
                "type": "text",
                "data": {
                    "text": f"【{get_nickname(event.user_id)}】被踢出群聊\n"
                }
            },
            {
                "type": "image",
                "data": {
                    "file": f"https://q4.qlogo.cn/headimg_dl?dst_uin={event.user_id}&spec=640"
                }
            }
        ]
    await bot.send(event=event, message=rely)


GroupIncrease = on_notice()
"""群成员增加事件"""


@GroupIncrease.handle()
async def handle_first_receive(bot: Bot, event: GroupIncreaseNoticeEvent, state: T_State):
    rely = [
        {
            "type": "text",
            "data": {
                "text": "欢迎"
            }
        },
        {
            "type": "at",
            "data": {
                "qq": f"{event.user_id}"
            }
        },
        {
            "type": "text",
            "data": {
                "text": "进群"
            }
        },
        {
            "type": "image",
            "data": {
                "file": f"https://q4.qlogo.cn/headimg_dl?dst_uin={event.user_id}&spec=640"
            }
        }
    ]
    await bot.send(event=event, message=rely)


FriendAdd = on_notice()
"""好友添加事件"""


@FriendAdd.handle()
async def handle_first_receive(bot: Bot, event: FriendAddNoticeEvent, state: T_State):
    rely = [
        {
            "type": "text",
            "data": {
                "text": "你好!请回复【功能】查看可进行的操作"
            }
        }
    ]
    await bot.send(event=event, message=rely)


Honor = on_notice()
"""群荣誉变更提醒事件"""
"""
honor_type	talkative:龙王 performer:群聊之火 emotion:快乐源泉
"""


@Honor.handle()
async def handle_first_receive(bot: Bot, event: HonorNotifyEvent, state: T_State):
    if event.honor_type == 'talkative':
        rely = [
            {
                "type": "text",
                "data": {
                    "text": f"恭喜{get_nickname(event.user_id)}成为今日龙王，赶紧给大家表演一个喷水吧"
                }
            }
        ]
        await bot.send(event=event, message=rely)
