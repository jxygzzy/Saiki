import random

from nonebot import on_notice
from nonebot.adapters.cqhttp import Bot, Event, GroupDecreaseNoticeEvent, GroupIncreaseNoticeEvent, \
    FriendAddNoticeEvent, PokeNotifyEvent, LuckyKingNotifyEvent, HonorNotifyEvent, Message
from nonebot.rule import to_me
from nonebot.typing import T_State

from .data_source import get_nickname

LuckyKing = on_notice()
"""群红包运气王提醒事件"""


@LuckyKing.handle()
async def handle_first_receive(bot: Bot, event: LuckyKingNotifyEvent, state: T_State):
    rely = f'[CQ:at,qq={event.target_id}]是运气王!\n\t来自{event.user_id}的红包'
    await bot.send(event=event, message=rely)


poke = on_notice(rule=to_me())
"""戳一戳提醒事件"""


@poke.handle()
async def handle_first_receive(bot: Bot, event: PokeNotifyEvent, state: T_State):
    expr_poke = [
        f'[CQ:poke,qq={event.get_user_id()}]',
        '那里不可以！(>﹏<)',
        '再戳就要坏了！',
        '我在！',
        '干嘛！'
    ]
    await bot.send(event=event, message=Message(random.choice(expr_poke)))


GroupDecrease = on_notice()
"""群成员减少事件"""


@GroupDecrease.handle()
async def handle_first_receive(bot: Bot, event: GroupDecreaseNoticeEvent, state: T_State):
    nick_name = await get_nickname(event.user_id)
    if event.user_id == event.operator_id:
        rely = f'【{nick_name}】主动离开了群聊\n[CQ:image,file=https://q4.qlogo.cn/headimg_dl?dst_uin={event.user_id}&spec=640]'
    else:
        rely = f'【{nick_name}】被踢出群聊\n[CQ:image,file=https://q4.qlogo.cn/headimg_dl?dst_uin={event.user_id}&spec=640]'
    await bot.send(event=event, message=rely)


GroupIncrease = on_notice()
"""群成员增加事件"""


@GroupIncrease.handle()
async def handle_first_receive(bot: Bot, event: GroupIncreaseNoticeEvent, state: T_State):
    groupIncrease = f'欢迎[CQ:at,qq={event.user_id}]进群[CQ:image,file=https://q4.qlogo.cn/headimg_dl?dst_uin={event.user_id}&spec=640]'
    await bot.send(event=event, message=Message(groupIncrease))


FriendAdd = on_notice()
"""好友添加事件"""


@FriendAdd.handle()
async def handle_first_receive(bot: Bot, event: FriendAddNoticeEvent, state: T_State):
    await bot.send(event=event, message=Message('你好!请回复【功能】查看可进行的操作'))


Honor = on_notice()
"""群荣誉变更提醒事件"""
"""
honor_type	talkative:龙王 performer:群聊之火 emotion:快乐源泉
"""


@Honor.handle()
async def handle_first_receive(bot: Bot, event: HonorNotifyEvent, state: T_State):
    if event.honor_type == 'talkative':
        nick_name = await get_nickname(event.user_id)
        expr_talkative = [
            f"恭喜{nick_name}成为今日龙王，赶紧给大家表演一个喷水吧。",
            f'{nick_name}成为今日龙王，大家赶紧欺负ta！'
        ]
        await bot.send(event=event, message=random.choice(expr_talkative))
