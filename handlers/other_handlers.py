from aiogram import Router
from aiogram.types import Message
from lexicon.lexicon import OTHER_LEXICON_LIST
from random import choice

#Добавить магаз

router = Router()

@router.message()
async def all_messages(message: Message):
    await message.answer(text=choice(OTHER_LEXICON_LIST))