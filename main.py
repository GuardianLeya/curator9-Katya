import telebot
from telebot import types

bot = telebot.TeleBot('6461488113:AAHEZnJXTlZUJsIbMftqu7fCg8QxodaxBoI')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет,я Аркадий!'),


parse_mode = 'Markdown'


@bot.message_handler()
def get_user_text(message):
    if message.text == "Как дела?":
        bot.send_message(message.chat.id, "Всё отлично,хорошего тебе дня!", parse_mode='html')


@bot.message_handler(commands=['help'])
def website(message):
    markup = types.ReplyKeyboardMarkup()
    website = types.KeyboardButton('Идеи фильмов на НГ')
    bot.send_message(message.chat.id, "Гарри Поттер, Ёлки, Один дома, Гринч", reply_markup=markup)
    start = types.KeyboardButton('Новогодняя еда')
    bot.send_message(message.chat.id, "Имбирный пряник, Оливье , Бутерброд с красной икрой", reply_markup=markup)


bot.infinity_polling(none_stop=True)


