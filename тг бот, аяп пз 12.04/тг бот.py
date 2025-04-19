import random

import telebot
bot = telebot.TeleBot('7645898014:AAEMA3iuP8-H1grX3_tPUP4JYz9fjssu098')

from telebot import types

import requests

import matplotlib.pyplot as plt
import numpy as np
import io

def wheath(city):
    city1 = city.text
    try:
        url = 'https://api.openweathermap.org/data/2.5/weather?q=' + city1 + '&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'
        weather_data = requests.get(url).json()
        temperature = round(weather_data['main']['temp'])
        temperature_feels = round(weather_data['main']['feels_like'])
        bot.send_message(city.chat.id, f'Сейчас в городе {city1}, {str(temperature)} °C')
        bot.send_message(city.chat.id, f'Ощущается как {str(temperature_feels)} °C')
        keyboard(city)
    except:
        bot.send_message(city.chat.id, 'ПИШИТЕ ПРАВЛИЬНО!!!!!!!')
        msg = bot.send_message(city.chat.id, 'напишите название города')
        bot.register_next_step_handler(msg, wheath)

def keyboard(msg):
    keyboard = types.InlineKeyboardMarkup()  # наша клавиатура
    key_wheather = types.InlineKeyboardButton(text='погода', callback_data='wheather')  # кнопка «wheather»
    keyboard.add(key_wheather)  # добавляем кнопку в клавиатуру
    key_sticker = types.InlineKeyboardButton(text='стикер', callback_data='sticker')
    keyboard.add(key_sticker)
    key_graph = types.InlineKeyboardButton(text='график', callback_data='graph')
    keyboard.add(key_graph)
    key_finish = types.InlineKeyboardButton(text='завершить работу', callback_data='finish')
    keyboard.add(key_finish)
    bot.send_message(msg.chat.id, 'выберите нужную кнопку', reply_markup=keyboard)



def sticker(n):
    try:
        n1 = int(n.text)
        if n1 < 1 or n1 > 30:
            bot.send_message(n.chat.id, 'Пожалуйста, введите число от 1 до 30')
            return

        for i in range(n1):
            sticker_id = random.choice(sticker_list['stick'])
            bot.send_sticker(n.chat.id, sticker_id)

        keyboard(n)
    except ValueError:
        bot.send_message(n.chat.id, 'Пожалуйста, введите корректное число')
        msg = bot.send_message(n.chat.id, 'напишите кол-во стикеров которое хотите получить (от 1 до 30)')
        bot.register_next_step_handler(msg, sticker)

def getting_numbers(message):
    try:
        numbers = list(map(float, message.text.split()))
        if len(numbers) != 3:
            raise ValueError
        user_data[message.chat.id] = numbers
        graph(message.chat.id)
    except:
        bot.send_message(message.chat.id, "ВВОДИТЕ ПРАВИЛЬНО, пожалйсту :), через пробел например: 4 -16 0")
        msg = bot.send_message(message.chat.id, "Попробуйте еще раз. Введите 3 числа через пробел:")
        bot.register_next_step_handler(msg, getting_numbers)

def graph(chat_id):
    try:
        k = user_data[chat_id]
        k1, k2, k3 = k[0], k[1], k[2]

        x = np.linspace(-150, 150, 300)
        y = k1 * x ** 2 + k2 * x + k3

        plt.figure(figsize=(10, 5))
        plt.plot(x, y, color='blue')
        plt.title(f'График: y = {k1}x² + {k2}x + {k3}')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid(True)

        img = io.BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)

        bot.send_photo(chat_id, img)
        plt.close()

        class TempMessage:                  #костыль для вызова клавиатуры иначе реализовать ее вызов после этой ф-ции не удалось (:
            def __init__(self, chat_id):
                self.chat = type('Chat', (), {'id': chat_id})

        keyboard(TempMessage(chat_id))
    except Exception as e:
        bot.send_message(chat_id, f"Ошибка при построении графика: {str(e)}, для решения обратитесь к автору бота указав на код ошибки")

user_data = {}

sticker_list = {
    'stick': [
        'CAACAgIAAxkBAAIBjWf9iyRZzyMSNCr7EkrCLk-cu0UDAAIVWQACSSdpSL8SJQ0c01KENgQ',
        'CAACAgIAAxkBAAIBj2f9i0hRsrwD9AOBTA2c0YlFrsnLAAK-XgACLxRhSMBBRpm1AAHlPzYE',
        'CAACAgIAAxkBAAIBk2f9i3fsqZHT7TSQBjH2A5aY1TQ2AAJiYAACsUFpSPB4XrMwSCB1NgQ',
        'CAACAgIAAxkBAAIBlWf9i4BNKpVxdl3L2yGSMnm6ZAVuAAJ-VgAC8NxgSMtxOZeyz2dHNgQ',
        'CAACAgIAAxkBAAIBl2f9i4dP7htWLU9lOdzlm3gfEft1AAKaXQACsAJhSILyyC9CKUfuNgQ',
        'CAACAgIAAxkBAAIBmWf9i5LN6uQgeQz-vqu8AhQdEnzhAALPWwACTLRhSB-tRVkmQlX_NgQ',
        'CAACAgIAAxkBAAIBm2f9i5pO6P4QDudQ39zepS-Z1XhvAAKxYAACEuNhSPj4pYJtqz9dNgQ',
        'CAACAgIAAxkBAAIBnWf9jK89It7vzPaNi4wkL54g3VR8AAJrWwACqH5hSDu7PlGWgbw7NgQ',
        'CAACAgIAAxkBAAIBoWf9jMUIMnvI6i3_b_wVEtsdCpDOAAJ1YAAC6Sf4SIO12Wu8t5LpNgQ',
        'CAACAgIAAxkBAAIBp2f9jOFfeETp6EXmo8XztA6Yom07AAKzbQACybBhSKqVole1eRSaNgQ',
        'CAACAgIAAxkBAAIBqWf9jO33H7aDwflmFUbRFhR0U28fAAJxXAACEt75SSvthXlIwj1INgQ',
        'CAACAgIAAxkBAAIBq2f9jPYacx2JtOiySDT9ddzp9CgKAAI5WQACv0j5SYVNfQSA1tWwNgQ',
        'CAACAgIAAxkBAAIBrWf9jP_cqK6At_oBgq-SLw_OQzfLAAKMYAAC38_5STAkcfWUgVSzNgQ',
        'CAACAgIAAxkBAAIBr2f9jQ5uRMUm6L7O_LzXI6m-OiT6AAIDZgACff-ASEjpE1-U_qE5NgQ',
        'CAACAgIAAxkBAAIBsWf9jRc5XI6BPQq5K5sPwYFvg9BNAAJLXQACtaaZSUL7M-CQQ0q_NgQ',
        'CAACAgIAAxkBAAIBs2f9jSCCGXJqklkalemtPsdm-nMSAAKjaQAC856ZSaKAjaemUAawNgQ',
        'CAACAgIAAxkBAAIBtWf9jS3mZFrZFRtCocSYbl5udBv3AALXVwACHnuJSMRYCB1F2QKPNgQ',
        'CAACAgIAAxkBAAIBwWf9jUJRP2EsVGxg4sFUfN5lScFuAALCZAACoEI5Sc8JaxQ_OT20NgQ',
        'CAACAgIAAxkBAAIBw2f9jU3PgyPuHSyjS39J5uP5CqgpAAKubwACwmgxSVHiIyNmAAE6uTYE',
        'CAACAgIAAxkBAAIBxWf9jVWDp_CAneQGDsEdSVuOmmy4AALdXQACuWc5SYTI1jHzvjf9NgQ',
        'CAACAgIAAxkBAAIBx2f9jV8MMOiXf-cZixOJ6ycmlR5KAAL1ZgACrWY4Sd2W-U1fsG1nNgQ',
        'CAACAgIAAxkBAAIByWf9jWvpWvjbBqtQPCAfy6ZFz41UAAKGXQACdl85SZjTrqm5dLCVNgQ',
        'CAACAgIAAxkBAAIBy2f9jXkT0U7XnJzVY1UtZa9R3E9NAAKMZAACsd85SeFysc7KHrtaNgQ',
        'CAACAgIAAxkBAAIBzWf9jYSdxWb57XnwyHmkmknz2GLUAALjbAACYMwwSYmsbibWy9tbNgQ',
        'CAACAgIAAxkBAAIBz2f9jYzoqyV-PzDbemaaripFLHCHAAJreAACqHYwSf3Kfpk2P5a6NgQ',
        'CAACAgIAAxkBAAIB92f9jnsKlV4PP5JKS6YkxGj43srJAALhVQACsCq4SoJA_2mfcoZkNgQ',
        'CAACAgIAAxkBAAIB82f9jkssx_DsePgvfKWTQ_yolblrAALaXgACe-NoSrFDlx2JFWHhNgQ',
        'CAACAgIAAxkBAAIB62f9jjUjEZbxWqMtbXqouwfGsj3TAAK8YgACFmXISlCbihextuJGNgQ',
        'CAACAgIAAxkBAAIB52f9jeVRftut_-PGFJ2puwzdeyarAAIJAANuu201zS95agN--ZE2BA',
        'CAACAgIAAxkBAAIB5Wf9jctE8m0MqH4P1jmskeAy46EJAAKPHAACJXmoSf3kLULbL1gvNgQ',
        'CAACAgIAAxkBAAIB42f9jcTxLRMUWKVGY7CETNmzPrhhAALdGAACCQ94SQfGPAOx5BlvNgQ',
        'CAACAgIAAxkBAAIB4Wf9jbnPvwg9WgWOc6OlTyZrTrWGAAKzOQACzUwBSe-wwKfZ0HOYNgQ'
    ]
}


@bot.message_handler(content_types=['text', 'text', 'text'])
def get_text_messages(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "напишите привет для дальнейшего взаимодействия :)")
    elif message.text == 'привет' or message.text == 'Привет':
        bot.send_message(message.from_user.id, "привет, преподаватель, я бот по выполнению заданий Гембицкого Глеба М14О-102БВ-24 :) "
                                               "я умею выводить погоду, показывать стикер, строить графики для этого нажмите соответсвующую кнопку")
        keyboard(message)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "напишите 'привет'")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "wheather":
        msg = bot.send_message(call.message.chat.id, 'напишите название города')
        bot.register_next_step_handler(msg, wheath)
    elif call.data == 'sticker':
        n = bot.send_message(call.message.chat.id, 'напишите кол-во стикеров которое хотите получить ( от 1 до 30)')
        bot.register_next_step_handler(n, sticker)
    elif call.data == 'graph':
        message = bot.send_message(call.message.chat.id, 'через пробел напишите коэфициент к1, к2, к3 при параболе')
        bot.register_next_step_handler(message, getting_numbers)
    elif call.data == 'finish':
        bot.send_message(call.message.chat.id, "спасибо за использование, хорошего дня :) для повторной работы напишите: /start")
    else:
        msg = bot.send_message(call.message.chat.id, 'ошибка')
        keyboard(msg)

bot.polling(none_stop=True, interval=0)