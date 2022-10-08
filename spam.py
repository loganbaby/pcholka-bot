from config import app
from pyrogram import filters
import shlex
import random

@app.on_message(filters.command('spam', prefixes='.') & filters.me)
async def message_spam(_, message):
    recognized_command = shlex.split(message.text)
    recognized_command.remove('.spam')
    print(recognized_command, ' ', len(recognized_command))

    for index in range(int(recognized_command[len(recognized_command) - 1])):
        await app.send_message(message.chat.id, recognized_command[0])

@app.on_message(filters.command('react', prefixes='.') & filters.me)
async def reaction_spam(_, message):
    reactions = ['❤', '😈', '💋', '👍', '👎', '🔥', '🥰', '👏', '😁', '🤔', '🤯', '😱', '🤬', '🎉']

    async for message in app.get_chat_history(message.chat.id):
        if message.reactions is None:
            await message.react(emoji=random.choice(reactions))
