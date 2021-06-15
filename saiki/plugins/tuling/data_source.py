import httpx
from config import taixingApiKey
UserAgent = "box-s-ville.Saiki"


async def get_ans(qustion: str) -> []:
    url = f'http://api.tianapi.com/txapi/robot/index?key={taixingApiKey}&question={qustion}'
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        code = resp.json()
        # print(code)
        return code