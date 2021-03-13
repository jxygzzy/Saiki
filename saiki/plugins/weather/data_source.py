import httpx

UserAgent = "box-s-ville.Saiki"


async def get_weather(city: str) -> []:
    url = f"https://api.muxiaoguo.cn/api/tianqi?city={city}&type=1"
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        code = resp.json()
        return code
        # if code['msg'] == "success":
        #     data = code['data']
        #     msg = data['cityname'] + "\n气温：" + data['temp'] + "℃ " + data['weather'] + '\nPM2.5：' + data[
        #         'pm25'] + "μg/m3\n最后更新时间：" + data['time']
        #     return data
        # else:
        #     msg = code['msg']
        #     return msg
