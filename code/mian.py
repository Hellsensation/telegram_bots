import random

import telebot
from telebot import types
import os

bot = telebot.TeleBot("6156452605:AAHq6QLMjgj2J60EMTR0KKDgLd3IYBSiAyI")
DIR_SCARY = "/home/hellsensation/dev/python/telegram_bots/mood_bot/content/scary/"
DIR_FUNNY = "/home/hellsensation/dev/python/telegram_bots/mood_bot/content/funny/"
DIR_INTERESTING = "/home/hellsensation/dev/python/telegram_bots/mood_bot/content/interesting/"


@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton("Пришли интересную картинку")
    markup.row(btn1)
    btn2 = types.KeyboardButton("Пришли страшную картинку")
    btn3 = types.KeyboardButton("Пришли смешную картинку")
    markup.row(btn2, btn3)

    bot.send_message(message.chat.id, "HELLO!", reply_markup=markup)
    bot.register_next_step_handler(message, on_click)


def on_click(message):
    markup = types.ReplyKeyboardMarkup()
    if message.text == "Пришли интересную картинку":
        file = open(os.path.join(DIR_INTERESTING, random.choice(os.listdir(DIR_INTERESTING))), "rb")
        bot.send_photo(message.chat.id, file, reply_markup=markup)
    elif message.text == "Пришли страшную картинку":
        file = open(os.path.join(DIR_SCARY, random.choice(os.listdir(DIR_SCARY))), "rb")
        bot.send_photo(message.chat.id, file, reply_markup=markup)
    elif message.text == "Пришли смешную картинку":
        file = open(os.path.join(DIR_FUNNY, random.choice(os.listdir(DIR_FUNNY))), "rb")
        bot.send_photo(message.chat.id, file, reply_markup=markup)


bot.polling(none_stop=True)

