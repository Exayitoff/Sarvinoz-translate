
import requests

import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN ="6299358910:AAErUwetbeTfF4JVlt79xnYdFPJXJ2S0PtQ"

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Assalomu alaykum ushbu bot 3 ta tilga tarjima qila oladi!")



@dp.message_handler()
async def echo(message: types.Message):
    xabar = message.text
    r = requests.get(f"https://trans.noxi8.repl.co/ru/text={xabar}")
    r2 = requests.get(f"https://trans.noxi8.repl.co/en/text={xabar}")
    r3 = requests.get(f"https://trans.noxi8.repl.co/kk/text={xabar}")
    r4 = requests.get(f"https://trans.noxi8.repl.co/ky/text={xabar}")
    response4 = r4.json()["text"]
    response3 = r3.json()["text"]
    response2 = r2.json()["text"]
    response = r.json()["text"]
    
    await message.reply(f"rus tilidagi tarjimasi : {response}\nIngliz tilidagi tarjimasi : {response2}\nkk tilidagi tarjimasi :{response3}\nky tilidagi tarjimasi :{response4}")

    
    

    

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)