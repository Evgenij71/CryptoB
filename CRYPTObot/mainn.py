import telebot
from exe import APIException, perevod
from config import tok, k

bot = telebot.TeleBot(tok)

@bot.message_handler(commands=['start', 'help'])
def start(message: telebot.types.Message):
    text = "👋"
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['values'])
def v(message: telebot.types.Message):
    text = 'валюты:'
    for i in k.keys():
        text = '\n'.join((text, i))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def per(message: telebot.types.Message):
    val = message.text.split(' ')
    try:
        if len(val) != 3:
            raise APIException('неверное кол-во ключевых слов')

        answer = perevod.get_price(*val)
    except APIException as e:
        bot.reply_to(message, f"ошибка в команде:\n{e}")
    else:
        bot.reply_to(message, answer)


bot.polling()