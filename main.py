import telebot
from telebot import types
token='5433848790:AAFn8ftN6HsGygDsrqiNWWMv2Wy1H-7s9js'
bot=telebot.TeleBot(token)
item2=types.KeyboardButton("Что делаешь?")
item3=types.KeyboardButton("ты конч???")
item4=types.KeyboardButton("ок")
photo1 = open('123.jpeg', 'rb')
photo2 = open('pivo1.jpg', 'rb')
photo3 = open('pivo2.jpg', 'rb')
photo4 = open('aga.jpg', 'rb')
photo5 = open('794.jpg', 'rb')
markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup4 = types.ReplyKeyboardMarkup(resize_keyboard=True)
offmarkup = types.ReplyKeyboardMarkup(resize_keyboard=False)
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Привет')
@bot.message_handler(commands=['button'])
def button_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Как дела?")
    markup.add(item1)
    bot.send_message(message.chat.id,'Выберите что вам надо',reply_markup=markup)
@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text == "Как дела?":
        bot.send_photo(message.chat.id, photo1)
        markup2.add(item2)
        bot.send_message(message.chat.id, 'аче', reply_markup=markup2)
    elif message.text == "Что делаешь?":
        bot.send_photo(message.chat.id, photo2)
        bot.send_photo(message.chat.id, photo3)
        markup3.add(item3)
        bot.send_message(message.chat.id, '???', reply_markup=markup3)
    elif message.text == 'ты конч???':
        bot.send_photo(message.chat.id, photo4)
        markup4.add(item4)
        bot.send_message(message.chat.id, ')0)', reply_markup=markup4)
    elif message.text == 'ок':
        bot.send_photo(message.chat.id, photo5)
bot.infinity_polling()