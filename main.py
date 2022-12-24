import requests

s_city = "Moscow,RU"  # почему в методичке city?
appid = "33f736c1e13c19fbf15e3fd8640584fd"
# s_city = None
res = requests.get("http://api.openweathermap.org/data/2.5/weather", params={'q': s_city, 'units': 'metric', 'lang':
    'ru', 'APPID': appid})
data = res.json()
# print("Город:", s_city)
# print("Погодные условия:", data['weather'][0]['description'])  # что значит "0"?
# print("Температура:", data['main']['temp'])
# print("Минимальная температура:", data['main']['temp_min'])
# print("Максимальная температура", data['main']['temp_max'])
# # домашнее задание
# print(f"видимость: {data['visibility']}")
# print(f"скорость ветра: {data['wind']['speed']}")

# прогноз погоды на неделю

res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                   params={'q': s_city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("Прогноз погоды на неделю:")
# for i in data['list']:
#     print("Дата <", i['dt_txt'], "> \r\nТемпература <", '{0:+3.0f }'.format(i['main']['temp']),
#           "> \r\n Погодные условия <", i['weather'][0]['description'], ">")
# print("____________________________")
# + дз
for i in data['list']:
    print("\nДата <", i['dt_txt'], "> \r\nТемпература <", i['main']["temp"],
          "> \r\n Погодные условия <", i['weather'][0]['description'], ">", f"видимость: < {i['visibility']} >",
          f"скорость ветра: {i['wind']['speed']}")
print("____________________________")
