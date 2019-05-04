import pyowm
import telebot
owm = pyowm.OWM('9f0709c0198162d061b9875696ffe616', language = 'ru')
bot = telebot.TeleBot("874128141:AAHMGCy1ubTLy7YIiUeHK3zU-7gibWJl1rA")
@bot.message_handler(content_types=['text'])
def send_echo(message):
    observation = owm.weather_at_place(message.text)
    w = observation.get_weather()
    temp = w.get_temperature('celsius')["temp"]
    answer = 'В городе ' + message.text + ' сейчас ' + w.get_detailed_status() + '\n'
    answer += 'Темература сейчас в районе ' + str(temp) + '\n\n'
    if temp < 10:
        answer += "Ппц как холодно. Одень шапку."
    elif temp < 20:
        answer += "Прохладно."
    else:
        answer += "Нормуль. Скоро лето..."
    bot.send_message(message.chat.id, answer)

bot.polling(none_stop = True)
