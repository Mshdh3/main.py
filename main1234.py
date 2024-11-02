import telebot
import random
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
bot = telebot.TeleBot("7758313114:AAG2LUCY7yqdGAM2R0Dp5KGPBfJqFbr_QJw")

events = [
  "15.05.2024-Международный день биологического разнообразия",
  "05.06.2024-Всемирный день окружающей среды",
  "16.09.2024-Международный день охраны озонового слоя",
  "04.10.202-Всемирный день животных",
  "04.10.2024-Всемирный день животных",
  "2024-11-14 - День рециклинга",
  "2024-12-05 - Международный день добровольцев",
]

@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id, "Привет! Я могу рассказать тебе о предстоящих экологических мероприятиях.")

@bot.message_handler(commands=['events'])
def show_events(message):
  bot.send_message(message.chat.id, random.choice(events))

bot.polling()
