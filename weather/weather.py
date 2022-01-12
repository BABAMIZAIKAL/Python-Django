import requests

class Weather:
    def max_temp():
        data = requests.post("https://tues2022.proxy.beeceptor.com/my/api/test").json()["data"]
        return max([i["temperature"] for i in data])
    def min_temp():
        data = requests.post("https://tues2022.proxy.beeceptor.com/my/api/test").json()["data"]
        return min([i["temperature"] for i in data])
    def avg_temp():
        data = requests.post("https://tues2022.proxy.beeceptor.com/my/api/test").json()["data"]
        return sum([i["temperature"] for i in data])/len(data)