import os
import telebot


bot = telebot.TeleBot("API එක දාහන් උස්සන්නෙ නැතුව මගෙ ඒව")


@bot.message_handler(commands=["how"])
def send_message(message):
  bot.send_message(message.chat.id, "https://youtube.com/c/Uvindubro")



bot.polling()