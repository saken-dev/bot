import telebot
from telebot import types
import os

global state
state = {}
bot = telebot.TeleBot("908406004:AAGrLpVsntGdPAkCvQ6-j7g9LFyF_pcZXLA")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('Доступные товары')
    itembtn2 = types.KeyboardButton('Часто задаваемые вопросы')
    itembtn3 = types.KeyboardButton('Где мы находимся?')
    markup.add(itembtn1, itembtn2, itembtn3)
    bot.send_message(message.chat.id, "Добро пожаловать в магазин часов города Кокшетау\n\nДля управления ботом вы можете использовать кнопки.", reply_markup=markup)
    state [message.chat.id] = {"step": 0, "casio": 0, "band": 0, "money": 0}
    print(state)

@bot.message_handler(func=lambda message: message.text == 'Доступные товары')
def popupBalance(message):
    global state
    state[message.chat.id]["step"] = 1
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('Доступные товары')
    itembtn2 = types.KeyboardButton('Часто задаваемые вопросы')
    itembtn3 = types.KeyboardButton('Где мы находимся?')
    bot.send_message(message.chat.id, "В наличии \nЧасы 'Casio': " + str(state[message.chat.id]["casio"]) + "\nЧасы 'Mi Band 4': " + str(state[message.chat.id]["band"]), reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Часто задаваемые вопросы')
def gotoBut(message):
    global state
    state[message.chat.id]["step"] = 2
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('Оригинальные ли вы часы предоставляется?')
    itembtn2 = types.KeyboardButton('Что на счет доставки?')
    itembtn3 = types.KeyboardButton('Есть ли гарантия?')
    itembtn4 = types.KeyboardButton('Как с вами связаться?')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4)
    bot.send_message(message.chat.id, "Выберите интересующий вас вопрос.", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Где мы находимся?')
def gotoAdr(message):
    global state
    markup = types.ReplyKeyboardMarkup(row_width=2)
    state[message.chat.id]["step"] = 3
    bot.send_message(message.chat.id, "Микрорайон Сарыарка 7А, IT школа-лицей.", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'добтов band++')
def plusBand(message):
    global state
    markup = types.ReplyKeyboardMarkup(row_width=2)
    state[message.chat.id]["band"] += 1 
    state[message.chat.id]["step"] = 4
    bot.send_message(message.chat.id, "Товар добавлен Mi Band 4. Осталось: " + str(state[message.chat.id]["band"]), reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'мойдхд')
def plusBand(message):
    global state
    markup = types.ReplyKeyboardMarkup(row_width=2)
    state[message.chat.id]["step"] = 9
    bot.send_message(message.chat.id, "Доход за сегодня: "  + str(state[message.chat.id]["money"]), reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'удлтов band--')
def delBand(message):
    global state
    markup = types.ReplyKeyboardMarkup(row_width=2)
    state[message.chat.id]["band"] -= 1
    state[message.chat.id]["money"] +=16000
    state[message.chat.id]["step"] = 5
    bot.send_message(message.chat.id, "Товар удален Mi Band 4. Осталось: " + str(state[message.chat.id]["band"]), reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'добтов casio++')
def plusCasio(message):
    global state
    state[message.chat.id]["casio"] += 1 
    markup = types.ReplyKeyboardMarkup(row_width=2)
    state[message.chat.id]["step"] = 6
    bot.send_message(message.chat.id, "Товар удален Casio. Осталось: " + str(state[message.chat.id]["casio"]), reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'удлтов сasio--')
def delCasio(message):
    global state
    markup = types.ReplyKeyboardMarkup(row_width=2)
    state[message.chat.id]["casio"] -= 1 
    state[message.chat.id]["money"] +=320000
    state[message.chat.id]["step"] = 7
    bot.send_message(message.chat.id, "Товар удален Casio. Осталось: " + str(state[message.chat.id]["casio"]), reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    global state
    if state[message.chat.id]["step"] == 1:
        try:
            state[message.chat.id]["step"] = 0
            markup = types.ReplyKeyboardMarkup(row_width=2)
            itembtn1 = types.KeyboardButton('Доступные товары')
            itembtn2 = types.KeyboardButton('Часто задаваемые вопросы')
            itembtn3 = types.KeyboardButton('Где мы находимся?')
            markup.add(itembtn1, itembtn2, itembtn3)
        except ValueError:
            bot.send_message(message.chat.id, "Используйте кнопки")
    elif state[message.chat.id]["step"] == 2:
        useBut(message)
    elif state[message.chat.id]["step"] == 3:
        useAdr(message)
    else:
        bot.send_message(message.chat.id, "Извините, я вас не понимаю. Пожалуйста, воспользуйтесь кнопками.")
    print(state)

def useBut(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('Доступные товары')
    itembtn2 = types.KeyboardButton('Часто задаваемые вопросы')
    itembtn3 = types.KeyboardButton('Где мы находимся?')
    markup.add(itembtn1, itembtn2, itembtn3)
    if message.text == "Оригинальные ли вы часы предоставляется?":
        bot.send_message(message.chat.id, "-Да! Мы заказываем только у представителей компании.", reply_markup=markup)
    if message.text == "Что на счет доставки?":
        bot.send_message(message.chat.id, "-У нас нет доставки. Исключительно самовывоз.", reply_markup=markup)
    if message.text == "Есть ли гарантия?":
        bot.send_message(message.chat.id, "-Гарантия имеется, на 4 месяца.", reply_markup=markup)
    if message.text == "Как с вами связаться?":
        bot.send_message(message.chat.id, "-Телефон: 8(777)777-77-77.", reply_markup=markup)
    if state[message.chat.id]["step"] == 0:
        markup = types.ReplyKeyboardMarkup(row_width=2)
        itembtn1 = types.KeyboardButton('Доступные товары')
        itembtn2 = types.KeyboardButton('Часто задаваемые вопросы')
        itembtn3 = types.KeyboardButton('Где мы находимся?')
        markup.add(itembtn1, itembtn2, itembtn3)
        bot.send_message(message.chat.id, "Добро пожаловать в магазин часов города Кокшетау\n\nДля управления ботом вы можете использовать кнопки.", reply_markup=markup)

def useAdr(message):
    if state[message.chat.id]["step"] == 0:
        markup = types.ReplyKeyboardMarkup(row_width=2)
        itembtn1 = types.KeyboardButton('Доступные товары')
        itembtn2 = types.KeyboardButton('Часто задаваемые вопросы')
        itembtn3 = types.KeyboardButton('Где мы находимся?')
        markup.add(itembtn1, itembtn2, itembtn3)
        bot.send_message(message.chat.id, "Добро пожаловать в магазин часов города Кокшетау\n\nДля управления ботом вы можете использовать кнопки.", reply_markup=markup)
    else:
        markup = types.ReplyKeyboardMarkup(row_width=2)
        markup = types.ReplyKeyboardMarkup(row_width=2)
        itembtn1 = types.KeyboardButton('Доступные товары')
        itembtn2 = types.KeyboardButton('Часто задаваемые вопросы')
        itembtn3 = types.KeyboardButton('Где мы находимся?')
        markup.add(itembtn1, itembtn2, itembtn3)
        bot.send_message(message.chat.id, "Я вас не понимаю", reply_markup=markup)

bot.polling()