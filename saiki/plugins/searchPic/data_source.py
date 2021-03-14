import httpx
from config import loliconApikey


async def search_pic(keywords: str) -> []:
    url = f"https://api.lolicon.app/setu?apikey={loliconApikey}&keyword={keywords}&size1200=true"
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        code = resp.json()
        if code['data'] == []:
            return "404"
        else:
            data = code['data'][0]
            # msg = "pid:" + str(data['pid']) + "\n" + "title:" + data['title'] + "\n" \
            #       + "author:" + data['author'] + "\n" + "url:" + data['url'] + "\n" + \
            #       "tags:" + str(data['tags'])
            # res = [msg, data['url']]
            return data
