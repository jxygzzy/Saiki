import httpx
import os

UserAgent = "box-s-ville.Saiki"
Referer = 'safe.soyiji.com'
headers = {
    'UserAgent': UserAgent,
    'Referer': Referer
}


async def get_news():
    url = "http://api.soyiji.com//news_jpg"
    async with httpx.AsyncClient(headers=headers) as client:
        resp = await client.get(url)
        code = resp.json()
        news_url = code['news_url']
        resp = await client.get(news_url)
        img = resp.read()
        path = os.path.split(os.path.realpath(__file__))[0]
        with open(path+"/dailyNews.jpg", 'wb') as f:
            f.write(img)
