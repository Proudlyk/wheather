import requests

API_KEY = 'your API_KEY'
BASE_URL = 'http://api.openweathermap.org/data/2.5/'

def get_current_weather(city):
    url = f"{BASE_URL}weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        print(f"Город: {data['name']}")
        print(f"Температура: {main['temp']}°C")
        print(f"Погода: {weather['description']}")
        print(f"Влажность: {main['humidity']}%")
        print(f"Скорость ветра: {data['wind']['speed']} м/с")
    else:
        print("Ошибка:", response.status_code, response.json().get("message"))

def get_forecast(city):
    url = f"{BASE_URL}forecast?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print(f"Прогноз погоды для {data['city']['name']}:")
        for item in data['list']:
            dt_txt = item['dt_txt']
            main = item['main']
            weather = item['weather'][0]
            print(f"{dt_txt}: Температура: {main['temp']}°C, Погода: {weather['description']}")
    else:
        print("Ошибка:", response.status_code, response.json().get("message"))

def main():
    city = input("Введите название города: ")
    print("\nТекущая погода:")
    get_current_weather(city)
    print("\nПрогноз погоды:")
    get_forecast(city)

if __name__ == "__main__":
    main()