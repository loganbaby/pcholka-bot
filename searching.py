from googlesearch import search as google_search
from config import SEARCH_SYSTEM, app
from pyrogram import filters

@app.on_message(filters.command('search', prefixes='.') & filters.me)
async def search_system_filter(_, message):
    async def search(response_text):
        if SEARCH_SYSTEM == 'google':
            buffer = ''
            for link in google_search(response_text, stop=3):
                buffer += link + '\n\n'
            return buffer
        else:
            raise TypeError('Exception: wrong search system in config')

    response_text = message.text.split('.search ', maxsplit=1)[1]
    await message.edit(await search(response_text))
