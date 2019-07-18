import telebot
import requests


token = '970097746:AAG79CRA1t3o6kCwamqWrlYrT4SKG55bFmk'
base_url = 'https://telegg.ru/orig/bot'

bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])  # Обработка /start
def handle_start(message):
    bot.send_message(message.from_user.id, 'Привет! \nЕсли хочешь посмотреть погоду в каком-то городе, напиши "погода" и название города ')


@bot.message_handler(content_types=["text"])
def handle_t(message):
    if message.text[:7] == "Погода " or message.text[:7] == "погода ":
            city = message.text[7:]
            r = requests.get('http://api.openweathermap.org/data/2.5/weather?&units=metric&q=%s&appid=0c9f3c052f1d81b7062750ff0926f345' % (city))
            data = r.json()
            temp = data["main"]["temp"]
            bot.send_message(message.chat.id, "Температура в {}: {} C".format(city, temp))


bot.polling(none_stop=True, interval=0)
