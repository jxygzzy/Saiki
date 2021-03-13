import httpx

UserAgent = "box-s-ville.Saiki"


async def get_yiyan() -> str:
    url = f"https://api.muxiaoguo.cn/api/yiyan"
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        code = resp.json()
        data = code['data']
        msg=data['constant']+" --"+data['source']
        return msg