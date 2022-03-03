import json, requests

class WeatherInfo:
    
    def __init__(self,dist="香港天文台",rainfall_dist="油尖旺") -> None:
        self.dist = dist
        self.rainfall_dist = rainfall_dist
    
    def rhrread_process(self,verbose): # 本港地區天氣報告
        rhrread_url = 'https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread&lang=tc'
        rhrread_data = json.loads(requests.get(rhrread_url).text)

        for n_0 in range(len(rhrread_data["temperature"]["data"])):
            if rhrread_data["temperature"]["data"][n_0]["place"] ==self.dist:
                break
        if n_0 >= len(rhrread_data["temperature"]["data"])-1:
            if verbose: print("[ERROR] district not!")
            n_0 = 1

        for n_1 in range(len(rhrread_data["rainfall"]["data"])):
            if rhrread_data["rainfall"]["data"][n_1]["place"] ==self.rainfall_dist:
                break
        if n_1 >= len(rhrread_data["rainfall"]["data"]):
            n_1 = 1

        data = {
            "district":rhrread_data["temperature"]["data"][n_0]["place"],
            "temperature":rhrread_data["temperature"]["data"][n_0]["value"],
            "humanity":rhrread_data["humidity"]["data"][0]["value"],
            "rainfall":rhrread_data["rainfall"]["data"][n_1]["max"],
            "place_humidity":rhrread_data["humidity"]["data"][0]["place"],
            "place_rainfall":rhrread_data["rainfall"]["data"][n_1]["place"],
            "icon":rhrread_data["icon"][0],
            "update_time":rhrread_data["temperature"]["recordTime"]
            }
        if (verbose):
            self.verbose(data,"rhr")
        return data

    def fnd_process(self,verbose,days=2): # 九天天氣預報   
        fnd_url = 'https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=fnd&lang=tc'
        fnd_data = json.loads(requests.get(fnd_url).text)
        data=[]
        
        for i in range (days):
            data.append(
                    {"forecastDate":fnd_data["weatherForecast"][i]["forecastDate"],
                    "week":fnd_data["weatherForecast"][i]["week"],
                    "temperatureMin":fnd_data["weatherForecast"][i]["forecastMintemp"]["value"],
                    "temperatureMax":fnd_data["weatherForecast"][i]["forecastMaxtemp"]["value"],
                    "humanityMin":fnd_data["weatherForecast"][i]["forecastMinrh"]["value"],
                    "humanityMax":fnd_data["weatherForecast"][i]["forecastMaxrh"]["value"],
                    "wind":fnd_data["weatherForecast"][i]["forecastWind"],
                    "forecast":fnd_data["weatherForecast"][i]["forecastWeather"],
                    "psr":fnd_data["weatherForecast"][i]["PSR"],
                    "icon":fnd_data["weatherForecast"][i]["ForecastIcon"]}
            )
        data.append(fnd_data["generalSituation"])
        data.append(fnd_data["updateTime"])
        
        if (verbose):
            self.verbose(data,"fnd",days=days)
        
        return data
    
    def verbose(self,data,type,days=2):

        translation ={}

        if (type == "rhr"):
            for key in data:
                print("{:<16s}: {:<10s}".format(key, str(data[key])))
        elif (type == "fnd"):
            for i in range(days):
                for key in data:
                    print("{:<16s}: {:<10s}".format(key, str(data[key])))