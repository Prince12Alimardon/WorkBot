from aiogram.types import Message, ReplyKeyboardMarkup
from aiogram import executor
from config import dp, bot
import requests, json

btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
btn.add("USD-UZS", "RUB-UZS", "EURO-UZS", "CNY-UZS", "WON-UZS", "DINOR-UZS")


@dp.message_handler(commands=["start"])
async def first(message: Message):
    await message.answer("Assalomu-alaykum, Prince12 | Valyuta Ayirboshlash | Botiga Hush Kelibsiz!", reply_markup=btn)


# @dp.message_handler(commands="start")
# async def start(msg: Message):
#     await msg.answer("Salom Qalesiz")


@dp.message_handler(content_types=["text"])
async def change(msg: Message):
    global input, output, result, caption, rasm
    text = msg.text
    if text == "USD-UZS":
        input = "USD"
        output = "UZS"

    if text == "RUB-UZS":
        input = "RUB"
        output = "UZS"

    if text == "EUR-UZS":
        input = "EUR"
        output = "UZS"

    if text == "CNY-UZS":
        input = "CNY"
        output = "UZS"

    url = " https://v6.exchangerate-api.com/v6/70f791307078a57d1626efae/latest/" + input
    response = requests.get(url)
    rest = json.loads(response.text)
    result = rest["conversion_rates"]["UZS"]
    if msg.text.isdigit():
        await bot.send_message(msg.chat.id, int(msg.text) * (result))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
