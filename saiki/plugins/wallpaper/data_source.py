import httpx

UserAgent = "box-s-ville.Saiki"


async def get_wallpaper():
    url = "https://api.muxiaoguo.cn/api/sjbz?method=pc&type=sina"
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        code = resp.json()
        data = code['data']
        imgurl = data['imgurl']
        return imgurl
        # resp = await client.get(imgurl)
        # content = resp.content
        # return content
