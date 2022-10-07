from pyrogram.handlers import MessageHandler
from config import app
from searching import search_system_filter
from crypto import get_capitalization, get_crypto_dynamic, get_all_crypto_coins

if __name__ == '__main__':
    app.add_handler(MessageHandler(search_system_filter))
    app.add_handler(MessageHandler(get_capitalization))
    app.add_handler(MessageHandler(get_all_crypto_coins))
    app.add_handler(MessageHandler(get_crypto_dynamic))
    app.run()
