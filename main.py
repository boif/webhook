import os
import telebot
from flask import Flask, request

TOKEN = '5440159287:AAGTNsmaZC-Y2sMGy-0rnt7gyAFS-MtQFyQ'
APP_URL = f'https://boif-webhook.herokuapp.com/{TOKEN}'
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)

@bot.message_handler(commands = ['stert'])
def start(message):
    bot.reply_to(message, 'Hello, ' + message.from_user.first_name)

@bot.message_handler(func = lambda message: True, content_types = ['text'])
def echo(message):
    bot.reply_to(message, message.text)

@server.route('/' + TOKEN, methods = ['POST'])
def get_messsage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([updates])
    return '!', 200

@server.route('/')
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url = APP_URL)
    return '!', 200

if __name__ == '__main__':
    server.run(host = '0.0.0.0', port = int(os.environ.get('PORT', 5000)))


