import random

questions = [
    "Что ты на самом деле хочешь?",
    "Почему это важно для тебя?",
    "Что удерживает тебя от первого шага?",
    "Каким ты хочешь быть через год?",
    "Когда в последний раз ты чувствовал вдохновение?",
    "Что ты давно откладываешь?",
    "Что бы ты сказал себе из будущего?",
    "Что ты уже знаешь, но не применяешь?",
    "Кому выгодно, чтобы ты не менялся?",
    "Что ты хочешь отпустить?"
]

def get_random_question():
    return random.choice(questions)