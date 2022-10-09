from config import app
from pyrogram import filters
from PIL import ImageDraw, Image, ImageFont
from datetime import datetime, timedelta
from threading import Thread
import time

TIME_NAME_ON = False

@app.on_message(filters.command('help', prefixes='.'))
async def display_help(_, message):
    await message.edit('''
Functions of userbot:
1. **__.search [response]__** - search info in the internet and display in message
2. **__.capitalization__** - display the capitalization of popular cryptocurrencies
3. **__.crypto_coins__** - get list of available cryptocurrencies for commands
4. **__.get_crypto_dynamic [crypto-name] [count of days]__** - display the graphic of crypto-dynamic by count of days
5. **__.spam "message" [count of messages]__** - spam by count of messages
6. **__.react__** - set reaction on each message in the chat
7. **__.time_avatar on__** - set the avatar like clock
8. **__.time_avatar off__** - deactivate the time_avatar mode''')

@app.on_message(filters.command('time_avatar on', prefixes='.'))
def time_avatar_on(_, message):
    global TIME_NAME_ON
    TIME_NAME_ON = True

    def change_img():
        font_size = 50
        msk_utc = 3

        def convert_time_to_string(dt):
            dt += timedelta(hours=msk_utc)
            return f"{dt.hour}:{dt.minute:02}"

        start_time = datetime.utcnow()
        text = convert_time_to_string(start_time)
        row = Image.new('RGBA', (200, 200), "black")
        parsed = ImageDraw.Draw(row)
        font = ImageFont.truetype("utils/HEADPLANE.ttf", font_size)
        font2 = ImageFont.truetype("utils/HEADPLANE.ttf", 15)
        parsed.text((int(row.size[0] * 0.23), int(row.size[1] * 0.31)), f'{text}', align="center", font=font,
                    fill=(66, 206, 245))
        parsed.text((45, 110), 'MOSCOW TIME', align="center", font=font2, fill=(66, 206, 245))
        row.save('res/time_images/time.png', "PNG")

    def start_time_name_mode():
        while TIME_NAME_ON:
            change_img()
            photos_of_profile = [photo for photo in app.get_chat_photos("me")]
            app.delete_profile_photos(photos_of_profile[0].file_id)
            app.set_profile_photo(photo='res/time_images/time.png')
            time.sleep(15)

    thread = Thread(target=start_time_name_mode)
    thread.start()
    message.edit('Time mode activated')

@app.on_message(filters.command('time_avatar off', prefixes='.'))
async def time_avatar_off(_, message):
    global TIME_NAME_ON
    TIME_NAME_ON = False
    photos_of_profile = [photo async for photo in app.get_chat_photos("me")]
    await app.delete_profile_photos(photos_of_profile[0].file_id)
    await message.edit('Time mode deactivated')
