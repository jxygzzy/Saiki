from nonebot import on_request
from nonebot.adapters.cqhttp import Event, FriendRequestEvent, GroupRequestEvent
from nonebot.typing import T_State
from nonebot.adapters import Bot

friend_req = on_request()


@friend_req.handle()
async def friend_req(bot: Bot, event: FriendRequestEvent, state: T_State):
    await bot.call_api('set_friend_add_request', flag=event.flag, approve=True)


group_req = on_request()


@group_req.handle()
async def group_req(bot: Bot, event: GroupRequestEvent, state: T_State):
    await bot.call_api('set_group_add_request', flag=event.flag, approve=True)