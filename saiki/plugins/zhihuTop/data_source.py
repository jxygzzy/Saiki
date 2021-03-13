import httpx

UserAgent = "box-s-ville.Saiki"


async def get_zhTop_data() -> str:
    url = 'https://tenapi.cn/zhihuresou/'
    async with httpx.AsyncClient(headers={'User-Agent': UserAgent}) as client:
        resp = await client.get(url)
        data = resp.json()
        result = data['list']
    return result
