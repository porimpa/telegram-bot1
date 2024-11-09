import telebot
import random
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")

@bot.message_handler(commands=['math']) # /math 2+2
def calculator(message):
    key = telebot.util.extract_arguments(message.text)
    bot.send_message(message.chat.id, eval(str(key)))

@bot.message_handler(commands=['random_fact'])
def random_facts(message):
    facts = [
        'А вы знали,что небо голубое',
        'амамамамамамамамама',
        'Трава на самом деле зелёная'
        'эмэмэмэмэмэ'
    ]
    bot.send_message(message.chat.id, str(random.choice(facts)))

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()