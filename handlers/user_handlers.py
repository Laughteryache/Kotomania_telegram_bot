import requests

from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from lexicon.lexicon import LEXICON_RU, LEXICON_ACHIEVEMENTS
from data.data import user_db
from services.services import top_list_function, user_in_data, user_achievements_list
from keyboards.beginning_keyboard import keyboard

router = Router()
API_URL = 'https://api.thecatapi.com/v1/images/search'

#START_HANDLER
@router.message(CommandStart())
async def start_process(message: Message):
    user_in_data(message)
    await message.answer(text=LEXICON_RU[message.text])

#HELP_HANDLER
@router.message(Command(commands='help'))
async def help_process(message: Message):
    user_in_data(message)
    await message.answer(text=LEXICON_RU[message.text])


#TOP_LIST_HANDLER
@router.message(Command(commands='top_list'))
async def top_list_process(message: Message):
    user_in_data(message)
    await message.answer(text=top_list_function(user_db))

#BEGINNING_HANDLER
@router.message(Command(commands='beginning'))
async def beginning_process(message: Message):
    user_in_data(message)
    user_db[message.from_user.id]['in_game'] = True
    await message.answer(text=LEXICON_RU[message.text],
                         reply_markup=keyboard)

#MINE_HANDLER
@router.message(lambda x: x.text=='Майнить!')
async def mine_process(message: Message):
    user_in_data(message)
    user_db[message.from_user.id]['coins']+=1
    if user_db[message.from_user.id]['coins'] in LEXICON_ACHIEVEMENTS.keys():
        user_db[message.from_user.id]['achievements'][user_db[message.from_user.id]['coins']][1] = True
        await message.answer_photo(photo=requests.get(API_URL).json()[0]['url'],
                                   caption=f'Вы заработали +1 <b>Kotocoin!</b>\n'
                                    f'На вашем балансе {user_db[message.from_user.id]["coins"]}')
        await message.answer(text=LEXICON_ACHIEVEMENTS[user_db[message.from_user.id]['coins']])
    #MINING
    else:
        await message.answer_photo(photo=requests.get(API_URL).json()[0]['url'],
                                   caption=f'Вы заработали +1 <b>Kotocoin!</b>\n'
                                    f'На вашем балансе {user_db[message.from_user.id]["coins"]}')

#STOP_HANDLER
@router.message(lambda x: x.text=='Закончить' or x.text=='/stop')
async def cancel_process(message: Message):
    user_in_data(message)
    if user_db[message.from_user.id]['in_game']:
        user_db[message.from_user.id]['in_game'] = False
        await message.answer(text=f"{LEXICON_RU['stop_true']}\n"
                                  f"Ваш баланс: {user_db[message.from_user.id]['coins']} <b>Kotocoin'ов</b>")
    else:
        await message.answer(text=LEXICON_RU['stop_false'])

#ACHIEVEMENTS_HANDLER
@router.message(Command(commands='achievements'))
async def achievements_process(message: Message):
    user_in_data(message)
    await message.answer(text=f'Список ваших достижений:\n'
                              f'{user_achievements_list(message.from_user.id, user_db)}')