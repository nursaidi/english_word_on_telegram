import telebot
from config import TOKEN
from get_new_word import random_word
from data_of_words import word_dict
from telebot import types
from telebot.util import quick_markup

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    button = types.InlineKeyboardButton(text='Получить слово', callback_data='send_word')
    markup = types.InlineKeyboardMarkup().add(button)
    bot.send_message(message.chat.id, 'Привет! Нажми кнопку:', reply_markup=markup)



@bot.message_handler(commands=['new_word'])
def send_word(message):
    result = random_word(word_dict)
    english_word = next(iter(result))
    bot.send_message(message.chat.id, f"{english_word} : {result[english_word]['word_translation']}\n "
                                      f"{result[english_word]['english_sentence']}\n"
                                      f"{result[english_word]['sentence_translation']}")


bot.polling()

# @bot.message_handler(commands=['new_word'])
# def send_word(message):
#     result = random_word(word_dict)
#     english_word = next(iter(result))
#     bot.send_message(message.chat.id, f"{english_word} : {result[english_word]['word_translation']}\n "
#                                       f"{result[english_word]['english_sentence']}\n"
#                                       f"{result[english_word]['sentence_translation']}")
