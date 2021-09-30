import os
import telebot
from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from SDSongBot.plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from SDSongBot import bot


@bot.message_handler(commands=["help"])
def send_message(message):
  bot.send_message(message.chat.id, "**Command avalable..!**/n/n☉ /so song name "



bot.polling()
