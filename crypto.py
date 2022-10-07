import requests
from config import app
from pyrogram import filters
import pandas as pd
import matplotlib.pyplot as plt
import os
from pathlib import Path

@app.on_message(filters.command('capitalization', prefixes='.') & filters.me)
async def get_capitalization(_, message):
    r = requests.get(
        "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=5&page=1",
        headers={'User-Agent': 'Mozilla/5.0'}
    )

    if r.status_code == 200:
        json_data = {
            'Crypto name': [i['id'] for i in r.json()],
            'symbol': [i['symbol'].upper() for i in r.json()],
            'capitalization': [str(i['market_cap']) + '$' for i in r.json()]
        }

        name = json_data['Crypto name']
        symbol = json_data['symbol']
        capitalization = json_data['capitalization']

        buffer = ''
        for index in range(len(name)):
            buffer += name[index] + ' ' + symbol[index] + ' ' + str(capitalization[index]) + '\n'
            await message.edit(buffer)
    else:
        print('Cannot send the response to API')

@app.on_message(filters.command('crypto_coins', prefixes='.') & filters.me)
async def get_all_crypto_coins(_, message):
    r = requests.get(
        "https://api.coingecko.com/api/v3/coins/list",
        headers={'User-Agent': 'Mozilla/5.0'}
    )

    if r.status_code == 200:
        json_data = {
            'Crypto name': [i['id'] for i in r.json()],
            'symbol': [i['symbol'].upper() for i in r.json()],
        }

        if not os.path.exists('res/available_coins.txt'):
            file = Path('res/available_coins.txt')
            file.touch(exist_ok=True)

        with open('res/available_coins.txt', 'w') as file:
            for line in json_data['Crypto name']:
                file.write(line + '\n')
            file.close()

        await message.edit('Now available cryptocurrencies:')
        await app.send_document(message.chat.id, 'res/available_coins.txt')
    else:
        print('Cannot send the response to API')

@app.on_message(filters.command('crypto_dynamic', prefixes='.') & filters.me)
async def get_crypto_dynamic(_, message):
    type_of_crypto = message.text.split('.crypto_dynamic ', maxsplit=1)[1]

    r = requests.get(
        f"https://api.coingecko.com/api/v3/coins/{type_of_crypto}/market_chart?vs_currency=usd&days=365",
         headers={'User-Agent': 'Mozilla/5.0'}
    )

    if r.status_code == 200:
        json_data = {
            'datetime': [i[0] for i in r.json()['market_caps']],
            'market_cap':   [i[1] for i in r.json()['market_caps']],
            'price': [i[1] for i in r.json()['prices']],
        }

        df_ydynamic = pd.DataFrame(json_data)
        df_ydynamic['datetime'] = pd.to_datetime(df_ydynamic['datetime'], unit='ms')
        df_ydynamic.set_index('datetime', inplace=True)

        ax = df_ydynamic['market_cap'].plot()
        ax.set_ylabel('market_cap')
        ax1 = df_ydynamic['price'].plot(secondary_y=True, style='r')
        ax1.set_ylabel('price')

        ax.set_title(f"{type_of_crypto} market cap and price changes")
        h1, l1 = ax.get_legend_handles_labels()
        h2, l2 = ax1.get_legend_handles_labels()
        ax.legend(h1 + h2, l1 + l2)
        plt.savefig('res/dynamic.png')

        await message.edit(f'{type_of_crypto} market cap and price changes')
        await app.send_photo(message.chat.id, 'res/dynamic.png')
    else:
        print('Cannot send the response to API')
