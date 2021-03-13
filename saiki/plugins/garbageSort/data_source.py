import httpx


async def get_garbageSort_data(keyword: str) -> str:
    async with httpx.AsyncClient() as client:
        url = f'https://api.muxiaoguo.cn/api/lajifl?m={keyword}'
        resp = await client.get(url)
        data = resp.json()
        result = data['data']
        msg = result['Name'] + '属于' + result['Type'] + '\n' + result['Description']['Concept'] + '\n' + result[
            'Type'] + '包含：' + result['Description']['Including'] + '\n' + '处理方法：' + result['Description'][
                  'Release_requirement']
    return result
