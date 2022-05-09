from config import open_weather_token
import datetime
from pprint import pprint
import requests


def get_weather(city, open_weather_token):
    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Морось \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B"
    }
    try:
        r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric'
           )
        data = r.json()
#       pprint(data)

        city = data["name"]
        cur_weather = data["main"]["temp"]

        weather_type = data["weather"][0]["main"]
        if weather_type in code_to_smile:
            wt = code_to_smile[weather_type]
        else:
            wt = "Что за погода?!"

        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]

        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
            data["sys"]["sunrise"])

        print(f"★★★★ {datetime.datetime.now().strftime('%d-%m-%Y %H:%M')} ★★★★\n"
              f"Погода в городе: {city}\nТемпература: {cur_weather}C° {wt}\n"
              f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind} м/с\n"
              f"Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\n"
              f"Продолжительность дня: {length_of_the_day}\n"
              f"Хорошего дня!"
              )

    except Exception as ex:
        print(ex)
        print('Check the name of the city')


def main():
    city = input('Enter the city name:  ')
    get_weather(city, open_weather_token)


if __name__ == '__main__':
    main()
