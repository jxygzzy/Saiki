import httpx


async def fetch_wikipedia(word: str) -> str:
    url = f"https://api.muxiaoguo.cn/api/Baike?type=Baidu&word={word}"
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        resp.raise_for_status()
        result = resp.json()
        return result['data']
