import logging
from aiogram import Bot, Dispatcher, executor, types
from config import BOT_TOKEN, ADMIN_ID
from SQL import SQL
import random

logging.basicConfig(level=logging.INFO)

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)
db = SQL('db.db')


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` command
    """
    await message.reply("Hi!\nI'm RandomPicBot!")


@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    """
    This handler will be called when user sends '/help' command
    """
    await message.reply("I can repeat your text message and stickers")


@dp.message_handler(commands=['get'])
async def get_pic(message: types.Message):
    """
    This handler will be called when user sends '/get' command and return pic
    """
    chat_id = message.from_user.id
    lst = db.get_pic()
    length = len(lst)
    rand = random.randint(0, length - 1)
    await bot.send_photo(chat_id, lst[rand][-1])


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def take_message(message: types.Message):
    db.load_file(message.photo[-1].file_id)


@dp.message_handler(content_types=types.ContentType.STICKER)
async def take_message(message: types.Message):
    """
    This is echo sticker handler
    """
    file_id = getattr(message, 'sticker').file_id
    user_id = message.from_user.id
    await bot.send_sticker(user_id, file_id)


@dp.message_handler()
async def echo(message: types.Message):
    """
    This is echo text handler
    """
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
