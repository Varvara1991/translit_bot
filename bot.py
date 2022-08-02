import os

import logging

from aiogram import Bot, Dispatcher, executor, types

# from config import TOKEN

logging.basicConfig(level=logging.INFO)

TOKEN=os.getenv('TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f'Привет, {user_name}! Введи текст кириллицей и я транслитерирую его в латиницу'
    logging.info(f'{user_name=} {user_id=} sent message: {message.text}')
    await message.reply(text)

@dp.message_handler()
async def translit_ru_eng(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id

    dic_translit = {'А' : 'A', 'Б' : 'B', 'В' : 'V', 'Г' : 'G', 'Д' : 'D', 'Е' : 'E', 'Ё' : 'E', 'Ж' : 'ZH', 'З' : 'Z', 'И' : 'I', 'Й' : 'I', 'К' : 'K', 'Л' : 'L', 'М' : 'M', 'Н' : 'N', 'О' : 'O', 'П' : 'P', 'Р' : 'R', 'С' : 'S', 'Т' : 'T', 'У' : 'U', 'Ф' : 'F', 'Х' : 'KH', 'Ц' : 'TS', 'Ч' : 'CH', 'Ш' : 'SH', 'Щ' : 'SHCH', 'Ы' : 'Y', 'Ъ' : 'IE', 'Э' : 'E', 'Ю' : 'IU', 'Я' : 'IA', 'Ь' : '', ' ' : ' '}
    
    text_ru = message.text
    text_eng = text_ru
    list_not_kirill = []
    for char in text_ru:
        if char.upper() not in list(dic_translit.keys()):
            list_not_kirill.append(char)
        else:
            for ru_char, eng_char in dic_translit.items():
                text_eng = text_eng.upper().replace(ru_char, eng_char)
        
    letters_lat = ','.join(list_not_kirill)
        
    if len(list_not_kirill) == 1:
        text = f'В вашем тексте "{text_ru}" буква {letters_lat} не написана кириллицей, попробуйте еще раз'
    elif len(list_not_kirill) > 1:
        text = f'В вашем тексте "{text_ru}" буквы {letters_lat} не написаны кириллицей, попробуйте еще раз'
    else:
        text = f'Из {text_ru} получилось {text_eng}'   
    
    logging.info(f'{user_name=} {user_id=} sent message: {message.text}')        
    # await message.reply(text)
    await message.answer(text)


if __name__ == '__main__':
    executor.start_polling(dp)