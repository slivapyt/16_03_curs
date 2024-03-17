from datetime import datetime
import os
import telebot
from main import get_currency_rate

API_TOKEN_OLEG = os.getenv('API_TOKEN_OLEG')

bot = telebot.TeleBot(API_TOKEN_OLEG)


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, "Введите названеие валюты (USD или EUR)")


@bot.message_handler(content_types=['text', 'photo', 'sticker'])
def handle_message(message):

    # Ответ на текстовое сообщение
    if message.text == ('USD'):
        currency = "USD"
        rate = get_currency_rate(currency)
        timestamp = datetime.now().strftime('%d.%m.%Y')
        bot.send_message(
            message.chat.id, f'На {timestamp} курс USD к рублю составляет {rate} рублей.')

    elif message.text == ('EUR'):
        currency = "EUR"
        rate = get_currency_rate(currency)
        timestamp = datetime.now().strftime('%d.%m.%Y')
        bot.send_message(
            message.chat.id, f'На {timestamp} курс EUR к рублю составляет {rate} рублей.')

    else:
        bot.send_message(message.chat.id, 'заебал')


bot.polling()
