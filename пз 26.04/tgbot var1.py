import telebot
bot = telebot.TeleBot('7645898014:AAEMA3iuP8-H1grX3_tPUP4JYz9fjssu098')

from telebot import types

import datetime

import random

def keyboard(msg):
    keyboard = types.InlineKeyboardMarkup()  # наша клавиатура
    key_time = types.InlineKeyboardButton(text='время', callback_data='time')
    keyboard.add(key_time)  # добавляем кнопку в клавиатуру
    key_rn = types.InlineKeyboardButton(text='число', callback_data='rn')
    keyboard.add(key_rn)
    key_Id = types.InlineKeyboardButton(text='айди пользователя', callback_data='Id')
    keyboard.add(key_Id)
    key_finish = types.InlineKeyboardButton(text='завершить работу', callback_data='finish')
    keyboard.add(key_finish)
    bot.send_message(msg.chat.id, 'выберите нужную кнопку', reply_markup=keyboard)

def time(msg):
    now = datetime.datetime.now()
    bot.send_message(msg.chat.id, f"Текущее время по Москве: {now}")
    keyboard(msg)

user_data = {}


@bot.message_handler(content_types=['text', 'text', 'text'])
def get_text_messages(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "напишите привет для дальнейшего взаимодействия :)")
    elif message.text == 'привет' or message.text == 'Привет':
        bot.send_message(message.from_user.id, "привет, преподаватель, я бот по выполнению заданий Гембицкого Глеба М14О-102БВ-24 :) "
                                               "я умею выводить текущее время, выводить рандомное число, показывать ай ди пользователя для этого нажмите соответсвующую кнопку")
        keyboard(message)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "напишите 'привет'")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "time":
            time(call.message)
    elif call.data == 'rn':
        bot.send_message(call.message.chat.id, f"Ваше число: {random.randint(1, 105403)}")
        keyboard(call.message)
    elif call.data == 'Id':
        bot.send_message(call.message.chat.id, f"Ваш ID: {call.from_user.id}")
        keyboard(call.message)
    elif call.data == 'finish':
        bot.send_message(call.message.chat.id, "спасибо за использование, хорошего дня :) для повторной работы напишите: /start")
    else:
        msg = bot.send_message(call.message.chat.id, 'ошибка')
        keyboard(msg)

bot.polling(none_stop=True, interval=0)