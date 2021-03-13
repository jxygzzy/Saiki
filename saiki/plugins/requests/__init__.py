# from nonebot import on_request
# from nonebot.notice_request import RequestSession
#
#
# @on_request('friend')
# async def _(session: RequestSession):
#     await session.bot.set_friend_add_request(flag=session.event.fla, approve=True, self_id=session.event.self_id,
#                                              remark=session.event.comment)
#
#
# @on_request('group')
# async def _(session: RequestSession):
#     await session.bot.set_group_add_request(flag=session.event.fla, approve=True, self_id=session.event.self_id,
#                                             remark=session.event.comment)
