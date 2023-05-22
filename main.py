from pyrogram.handlers import MessageHandler
from config import app
from searching import search_system_filter
from crypto import get_popular_capitalization, get_crypto_dynamic, get_all_crypto_coins
from spam import message_spam, reaction_spam, send_quote
from account import time_avatar_on, time_avatar_off, display_help

if __name__ == '__main__':
    app.add_handler(MessageHandler(search_system_filter))  # search info in google (3 pages)
    app.add_handler(MessageHandler(get_popular_capitalization))  # get capitalization of popular coins
    app.add_handler(MessageHandler(get_all_crypto_coins))  # get list of available crypto coins
    app.add_handler(MessageHandler(get_crypto_dynamic))  # get crypto dynamic by count of the days
    app.add_handler(MessageHandler(message_spam))  # message spam (count)
    app.add_handler(MessageHandler(reaction_spam))  # reaction spam (all chat)
    app.add_handler(MessageHandler(time_avatar_on))  # avatar display current time
    app.add_handler(MessageHandler(time_avatar_off))  # displaying current time on avatar off
    app.add_handler(MessageHandler(display_help))  # display help of userbot
    app.add_handler(MessageHandler(send_quote))  # send random quote
    app.run()
