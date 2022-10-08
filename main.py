from pyrogram.handlers import MessageHandler
from config import app
from searching import search_system_filter
from crypto import get_popular_capitalization, get_crypto_dynamic, get_all_crypto_coins
from spam import message_spam, reaction_spam

if __name__ == '__main__':
    app.add_handler(MessageHandler(search_system_filter))      # search info in google (3 pages)
    app.add_handler(MessageHandler(get_popular_capitalization))        # get capitalization of popular coins
    app.add_handler(MessageHandler(get_all_crypto_coins))       # get list of available crypto coins
    app.add_handler(MessageHandler(get_crypto_dynamic))         # get 365 - day crypto dynamic
    app.add_handler(MessageHandler(message_spam))            # message spam (count)
    app.add_handler(MessageHandler(reaction_spam))           # reaction spam (all chat)
    app.run()
