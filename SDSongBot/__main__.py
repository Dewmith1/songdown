#MIT License

#Copyright (c) 2021 slgeekshow

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from SDSongBot import SDSongBot as app
from SDSongBot import LOGGER
from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from pyrogram.errors import UserNotParticipant, ChatAdminRequired, UsernameNotOccupied #fsub
from SDSongBot.plugins import
from pyrogram import idle, filters
from config import BOT_USERNAME

JOIN_ASAP = " **You cant use me untill subscribe our updates channel** ☹️\n\n So Please join our updates channel by the following button and hit on the ` /start ` button again 😊"

FSUBB = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton(text="Join our update Channel 🗣", url=f"https://t.me/cgs_officials") 
        ]]      
    )

text = """
Hello [{}](tg://user?id={}) 👋
I am song download bot you can download song @cgssongdownloadbot
command check on click help menu button

powered by @cgs_officials
"""

@app.on_message(filters.command("start"))
async def start(client, message): #fsub start
    try:
        await message._client.get_chat_member(int("-1001179611522"), message.from_user.id)
    except UserNotParticipant:
        await message.reply_text(
        text=JOIN_ASAP, disable_web_page_preview=True, reply_markup=FSUBB
    )
        return   #fsub end
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        button = [
    [
        InlineKeyboardButton(text="help menu❓",  callback_data="help"),
        ],
    [
        InlineKeyboardButton(text="Updates Channel✨", url="https://t.me/cgs_officials"),
        InlineKeyboardButton(
            text=" Support Group✨", url="https://t.me/cgs_official"
        ),
    ],
    [
        InlineKeyboardButton(text="Add Me To Your Group 🎉", url="http://t.me/{BOT_USERNAME}?startgroup=new"),
    ],
]
        
    else:
        button = None
    await message.reply_photo(
                    photo="https://telegra.ph/file/96b4bfc266dfc5a136260.jpg",
                    reply_markup=InlineKeyboardMarkup(button),
                    caption=text.format(name, user_id))



app.start()
LOGGER.info("""
cgs bot online ✔️
""")
idle()
