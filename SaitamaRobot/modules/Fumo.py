import html
import random
import time

from telegram import ParseMode, Update, ChatPermissions
from telegram.ext import CallbackContext, run_async
from telegram.error import BadRequest

import SaitamaRobot.modules.fumostrings as fumostrings
from SaitamaRobot import dispatcher
from SaitamaRobot.modules.disable import DisableAbleCommandHandler
from SaitamaRobot.modules.helper_funcs.chat_status import (is_user_admin)
from SaitamaRobot.modules.helper_funcs.extraction import extract_user



@run_async
def fumo(update: Update, context: CallbackContext):
    bot = context.bot
    args = context.args
    message = update.effective_message

    reply_to = message.reply_to_message if message.reply_to_message else message

    curr_user = html.escape(message.from_user.first_name)
    user_id = extract_user(message, args)

    if user_id:
        fumo_user = bot.get_chat(user_id)
        user1 = curr_user
        user2 = html.escape(fumo_user.first_name)

    else:
        user1 = bot.first_name
        user2 = curr_user

    fumo_type = random.choice(("Text", "Gif"))
    if fumo_type == "Gif":
        try:
            temp = random.choice(fumostrings.FUMO_GIFS)
            reply_to.reply_animation(temp)

help = """
 • /fumo*:* Use this to get Fumo Gifs!
"""


FUMO_HANDLER = DisableAbleCommandHandler("fumo", fumo)



dispatcher.add_handler(FUMO_HANDLER)

mod_name = "Fumo"

command_list = [
       "fumo"
]
handlers = [
       FUMO_HANDLER
]

#All Credits to UNKNOWN
