import httpx

UserAgent = "box-s-ville.Saiki"
apikey = '0961535560170e964e4689'


async def get_setu() -> []:
    url = f"https://api.lolicon.app/setu?apikey={apikey}&r18=2&size1200=true"
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        code = resp.json()
        data = code['data'][0]
        msg = "pid:" + str(data['pid']) + "\n" + "title:" + data['title'] + "\n" \
              + "author:" + data['author'] + "\n" + "url:" + data['url'] + "\n" + \
              "tags:" + str(data['tags'])
        res = [msg, data['url']]
        return data