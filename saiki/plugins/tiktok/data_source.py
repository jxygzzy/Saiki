import httpx

UserAgent = "box-s-ville.Saiki"


async def get_resou() -> str:
    url = 'https://tenapi.cn/douyinresou/'
    async with httpx.AsyncClient(headers={'User-Agent': UserAgent}) as client:
        resp = await client.get(url)
        data = resp.json()
        result = data['list']
    return result
