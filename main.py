import logging
from aiogram import Bot, Dispatcher, executor, types
from config import BOT_TOKEN, ADMIN_ID

logging.basicConfig(level=logging.INFO)

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` command
    """
    await message.reply("Hi!\nI'm QuotesBot!")


@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    """
    This handler will be called when user sends '/help' command
    """
    await message.reply("I almost do nothing but I'll be a good bot soon")


@dp.message_handler()
async def echo(message: types.Message):
    """
    This is echo handler
    """
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
