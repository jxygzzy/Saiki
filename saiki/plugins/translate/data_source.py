import httpx

UserAgent = "box-s-ville.Saiki"


async def translate(keyword: str) -> str:
    async with httpx.AsyncClient(headers={'User-Agent': UserAgent}) as client:
        url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
        key = {
            'type': "AUTO",
            'i': keyword,
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "ue": "UTF-8",
            "action": "FY_BY_CLICKBUTTON",
            "typoResult": "true"
        }
        resp = await client.post(url, data=key)
        data = resp.json()
        return data['translateResult'][0][0]['tgt']
