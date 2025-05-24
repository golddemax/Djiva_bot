import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
from dotenv import load_dotenv
import os
from questions import get_random_question

load_dotenv()
logging.basicConfig(level=logging.INFO)

bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher(bot)

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton("Получить карту"))

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer(
        "Привет. Я — бот Карты Дживы. Я буду присылать тебе коучинговые вопросы, которые помогают лучше понять себя.",
        reply_markup=keyboard
    )

@dp.message_handler(lambda message: message.text == "Получить карту")
async def send_card(message: types.Message):
    question = get_random_question()
    await message.answer(f"**Твоя карта дня:**\n\n{question}", parse_mode='Markdown')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)