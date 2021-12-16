from aiogram import Bot, Dispatcher, executor, types
from auth import token


bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.answer("Hi! Enter Dell Service Tag")

@dp.message_handler(regexp='(^[0-9A-Z]{7}?$)')
async def start(message: types.Message):
    await message.answer(f"https://www.dell.com/support/home/ru-ru/product-support/servicetag/{message.text}/overview")

@dp.message_handler()
async def start(message: types.Message):
    await message.answer(f"It's not a Dell Service Tag → {message.text}")
    
def main():
    executor.start_polling(dp, skip_updates=True)

if __name__ == "__main__":
    main()