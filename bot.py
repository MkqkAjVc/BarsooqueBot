import os
import telebot

token = os.environ['BOT_TOKEN']

bot = telebot.TeleBot(token)

@bot.message_handler()
def handle_message(m):
	bot.send_message(m.chat.id, "Хуй")

bot.polling(none_stop=1, interval=0, timeout=100000)
