import requests
import matplotlib.pyplot as plt
import datetime

# Константы
API_KEY = 'your_api_key'  # Замените 'your_api_key' на ваш ключ API от OpenWeatherMap
BASE_URL = 'http://api.openweathermap.org/data/2.5/forecast'
CITY = 'Moscow'
UNITS = 'metric'

# Функция для получения данных о погоде
def get_weather_data(city, api_key, units='metric'):
    params = {
        'q': city,
        'appid': api_key,
        'units': units
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print("Ошибка получения данных:", response.status_code)
        return None

# Функция для обработки данных о погоде
def process_weather_data(data):
    dates = []
    temperatures = []
    for entry in data['list']:
        date = datetime.datetime.fromtimestamp(entry['dt'])
        temp = entry['main']['temp']
        dates.append(date)
        temperatures.append(temp)
    return dates, temperatures

# Функция для визуализации данных о погоде
def plot_weather_data(dates, temperatures):
    plt.figure(figsize=(10, 5))
    plt.plot(dates, temperatures, marker='o')
    plt.title('Temperature Forecast')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('weather_forecast.png')
    plt.show()

# Основная часть
def main():
    data = get_weather_data(CITY, API_KEY, UNITS)
    if data:
        dates, temperatures = process_weather_data(data)
        plot_weather_data(dates, temperatures)

if __name__ == "__main__":
    main()
