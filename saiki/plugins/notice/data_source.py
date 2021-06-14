import httpx

UserAgent = "box-s-ville.Saiki"


async def get_nickname(qq) -> str:
    url = f'https://api.muxiaoguo.cn/api/QqInfo?qq={qq}'
    async with httpx.AsyncClient(headers={'User-Agent': UserAgent}) as client:
        resp = await client.get(url)
        code = resp.json()
        result = code['data']['name']
    return result
