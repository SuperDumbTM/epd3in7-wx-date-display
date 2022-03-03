class WeatherInfo:
    
    def __init__(self) -> None:
        self.dist = "香港天文台"
        self.rain_dist = "油尖旺"

    @classmethod
    # with specified location
    def WeatherInfo(self,dist,rain_dist):
        self.dist = dist
        self.rain_dist = rain_dist
    
    def rhrread_process(): # 本港地區天氣報告
        rhrread_url = 'https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread&lang=tc'
        rhrread_data = json.loads(requests.get(rhrread_url).text)

        for n_0 in range(len(rhrread_data["temperature"]["data"])):
            if rhrread_data["temperature"]["data"][n_0]["place"] ==dist:
                break
        if n_0 >= len(rhrread_data["temperature"]["data"])-1:
            n_0 = 1

        for n_1 in range(len(rhrread_data["rainfall"]["data"])):
            if rhrread_data["rainfall"]["data"][n_1]["place"] ==rainfall_dist:
                break
        if n_1 >= len(rhrread_data["rainfall"]["data"]):
            n_1 = 1

        print('- 本港地區天氣報告 -')
        print('地區 :', rhrread_data["temperature"]["data"][n_0]["place"])
        print('氣溫 :', rhrread_data["temperature"]["data"][n_0]["value"],'°C')
        print('濕度 :', rhrread_data["humidity"]["data"][0]["value"],'%')
        # print('濕度資料位置 :', rhrread_data["humidity"]["data"][0]["place"])
        print('圖示 :',  + rhrread_data["icon"][0])

        print('雨量資料位置 :', rhrread_data["rainfall"]["data"][n_1]["place"])
        print('最高雨量紀錄 :', rhrread_data["rainfall"]["data"][n_1]["max"],'mm')

        print('更新時間 :', rhrread_data["temperature"]["recordTime"],'\n')