import telebot
from config import TOKEN
from get_new_word import random_word
from data_of_words import word_dict
from telebot import types
from audio_generator import voice_message

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button = types.KeyboardButton(text='Получить слово')
    markup.add(button)
    bot.send_message(message.chat.id, 'Hi', reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == 'Получить слово':
        send_word(message)


def send_word(message):
    result = random_word(word_dict)
    english_word = next(iter(result))
    bot.send_message(message.chat.id, f"{english_word} : {result[english_word]['word_translation']}\n "
                                      f"{result[english_word]['english_sentence']}\n"
                                      f"{result[english_word]['sentence_translation']}")
    bot.send_voice(message.chat.id, voice_message)


bot.polling()
