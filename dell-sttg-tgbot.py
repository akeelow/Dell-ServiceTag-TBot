from aiogram import Bot, Dispatcher, executor, types
from PIL import Image
import easyocr
from auth import token
import re

def text_recognition():
    reader = easyocr.Reader(["en"])
    result = reader.readtext("temp.jpg", detail = 0, paragraph = True) 
    ocr_text = ""
    for line in result:
        ocr_text = ocr_text + line
    
    result = re.search(r'(\b[A-Z0-9]{6}\d{1}\b)', ocr_text)

    return result[0] if result else "err"

bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.answer("Hi! Enter Dell Service Tag")

@dp.message_handler(content_types=['photo'])
async def handle_docs_photo(message):
    await message.photo[-1].download('temp.jpg')
    tag = text_recognition()
    if tag == "err":
        await message.answer("NOT FOUND Dell Service Tag")
    else:
        await message.answer(f"https://www.dell.com/support/home/ru-ru/product-support/servicetag/{tag}/overview")


def main():
    executor.start_polling(dp, skip_updates=True)
    
if __name__ == "__main__":
    main()