import logging
import httpx
import os
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv

# Загрузка переменных из .env
load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Логирование
logging.basicConfig(level=logging.INFO)

# Инициализация бота
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)

# Обращение к OpenAI через httpx
async def ask_openai(prompt):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    json_data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "Ты — мудрый коуч и НЛП-практик. Помогаешь мягко, через образы и вопросы."},
            {"role": "user", "content": prompt}
        ]
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(url, headers=headers, json=json_data)
            if response.status_code != 200:
                logging.error(f"OpenAI API error: {response.status_code} — {response.text}")
                return "Произошла ошибка при обращении к ИИ. Проверь доступ к модели или API-ключ."
            result = response.json()
            return result["choices"][0]["message"]["content"].strip()
    except Exception as e:
        logging.error(f"Exception: {e}")
        return f"Ошибка от OpenAI: {e}"

# Команда /start
@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    await message.reply(
        "Привет! Я — Джива, твой проводник на пути внутренней трансформации.\n"
        "Расскажи, что тебя волнует, и я помогу тебе взглянуть на это по-новому."
    )

# Ответы на обычные сообщения
@dp.message_handler()
async def handle_message(message: types.Message):
    user_input = message.text
    await message.chat.do("typing")
    reply = await ask_openai(user_input)
    await message.reply(reply)

if __name__ == "__main__":
    print("Бот запущен...")
    executor.start_polling(dp, skip_updates=True)