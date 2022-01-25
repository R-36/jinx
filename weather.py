from pyowm import OWM
from pyowm.utils import config, timestamps
from pyowm.utils.config import get_default_config


def get_weather(place):
    config_dict = get_default_config()
    config_dict['language'] = 'ru'
    country = 'Россия'

    owm = OWM('600df091dda31313b2bda71b7f3a2bff')
    mgr = owm.weather_manager()
    observation = mgr.weather_at_places(place, 'accurate')
    print(observation)
    w = observation[0].weather
    status = w.detailed_status
    w.wind()
    humidity = w.humidity
    temp = w.temperature('celsius')['temp']

    return ("В городе " + str(place) +
            " сейчас " + str(status) +
            " Температура " + str(round(temp)) + " градусов по цельсию" +
            " Влажность сотставляет " + str(humidity) + "%" +
            " Скорость ветра " + str(w.wind()['speed']) + " метров в секунду")
