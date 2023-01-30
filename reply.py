from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

startbtn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="USD-UZS"),
            KeyboardButton(text="RUB-UZS"),
            KeyboardButton(text="EUR-UZS"),
        ],
        [
            KeyboardButton(text="CNY-UZS"),
            KeyboardButton(text="FUNT-UZS"),
            KeyboardButton(text="TENGE-UZS"),
        ]
    ],
    resize_keyboard=True
)