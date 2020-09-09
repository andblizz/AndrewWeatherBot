import pyowm
#from pyowm.utils.config import get_default_config
import telebot

bot = telebot.TeleBot("1312275856:AAFujjUoQK0GPABJugyWkIWsoVmM9NUvdjM")
#config_dict = get_default_config()
#config_dict['language'] = 'ru'
owm = pyowm.OWM('94f30450475b423d8a8065fbe892c632')

mgr = owm.weather_manager()

@bot.message_handler(content_types=["text"])
def send_echo(message):
    observation = mgr.weather_at_place(message.text)
    w = observation.weather
    temp = w.temperature('celsius')["temp"]
    answer = "В городе " + message.text + " сейчас " + w.detailed_status + "\n"
    answer += "Температура сейчас в районе " + str(temp) + "\n"
    if temp < 10:
        answer += "Очень холодно, одевайся теплее"
    elif temp < 20:
        answer += "Прохладно, фи"
    else:
        answer += "Заебок"
    bot.send_message(message.chat.id, answer)

bot.polling(none_stop=True)
