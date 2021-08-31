import html
import random
import time

from telegram import ParseMode, Update, ChatPermissions
from telegram.ext import CallbackContext, run_async
from telegram.error import BadRequest

import SaitamaRobot.modules._g_h_l_strings as _g_h_l_strings
from SaitamaRobot import dispatcher
from SaitamaRobot.modules.disable import DisableAbleCommandHandler
from SaitamaRobot.modules.helper_funcs.chat_status import (is_user_admin)
from SaitamaRobot.modules.helper_funcs.extraction import extract_user



@run_async
def Gay(update: Update, context: CallbackContext):
    bot = context.bot
    args = context.args
    message = update.effective_message

    reply_to = message.reply_to_message if message.reply_to_message else message

    curr_user = html.escape(message.from_user.first_name)
    user_id = extract_user(message, args)

    if user_id:
        gae_user = bot.get_chat(user_id)
        user1 = curr_user
        user2 = html.escape(gae_user.first_name)

    else:
        user1 = bot.first_name
        user2 = curr_user

    Gay_type = random.choice(("Gay"))

    if Gay_type == "Gay":

        temp = random.choice(_g_h_l_strings.Gay)
        reply = temp.format(user1=user1, user2=user2)
        reply_to.reply_text(reply, parse_mode=ParseMode.HTML)

    @run_async
    def Lesbian(update: Update, context: CallbackContext):
        bot = context.bot
        args = context.args
        message = update.effective_message

        reply_to = message.reply_to_message if message.reply_to_message else message

        curr_user = html.escape(message.from_user.first_name)
        user_id = extract_user(message, args)

    if user_id:
        lesbian_user = bot.get_chat(user_id)
        user1 = curr_user
        user2 = html.escape(lesbian_user.first_name)

    else:
        user1 = bot.first_name
        user2 = curr_user

    Lesbian_type = random.choice(("Lesbian"))

    if Lesbian_type == "Lesbian":

        temp = random.choice(_g_h_l_strings.Lesbian)
        reply = temp.format(user1=user1, user2=user2)
        reply_to.reply_text(reply, parse_mode=ParseMode.HTML)

    @run_async
    def Horny(update: Update, context: CallbackContext):
        bot = context.bot
        args = context.args
        message = update.effective_message

        reply_to = message.reply_to_message if message.reply_to_message else message

        curr_user = html.escape(message.from_user.first_name)
        user_id = extract_user(message, args)

    if user_id:
        gay_user = bot.get_chat(user_id)
        user1 = curr_user
        user2 = html.escape(gay_user.first_name)

    else:
        user1 = bot.first_name
        user2 = curr_user

    Horny_type = random.choice(("Horny"))

    if Horny_type == "Horny":

        temp = random.choice(_g_h_l_strings.Horny)
        reply = temp.format(user1=user1, user2=user2)
        reply_to.reply_text(reply, parse_mode=ParseMode.HTML)


LESBIAN_HANDLER = DisableAbleCommandHandler("lesbian", Lesbian)
GAY_HANDLER = DisableAbleCommandHandler("gay", Gay)
HORNY_HANDLER = DisableAbleCommandHandler("horny", Horny)


dispatcher.add_handler(HORNY_HANDLER)
dispatcher.add_handler(GAY_HANDLER)
dispatcher.add_handler(LESBIAN_HANDLER)

__mod_name__ = "Admin"
__command_list__ = [
    "horny", "lesbian", "gae"
]
__handlers__ = [
    HORNY_HANDLER, LESBIAN_HANDLER, GAY_HANDLER
]
