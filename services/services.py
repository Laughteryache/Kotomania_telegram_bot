from aiogram.types import Message
from data.data import user_dict_template, user_db
from copy import deepcopy
from lexicon.lexicon import LEXICON_CRITERIONS

def top_list_function(database: dict) -> str:
    top_list = []
    for key, value in database.items():
        top_list.append([value['username'], value['coins']])
    top_list = sorted(top_list, key=lambda x: x[1], reverse=True)[:5]
    return '\n'.join([f"{i+1}. <b>@{top_list[i][0]}</b> - {top_list[i][1]} Kotocoin'ов" for i in range(len(top_list))])

def user_in_data(message: Message) -> None:
    if message.from_user.id not in user_db:
        user_db[message.from_user.id] = deepcopy(user_dict_template)
        user_db[message.from_user.id]['username'] = message.from_user.username

def user_achievements_list(user_id: int, database: dict) -> str:
    achievement_list = []
    for key, value in database[user_id]['achievements'].items():
        if value[1]:
            achievement_list.append(f'<b>· {value[0]}</b> - {LEXICON_CRITERIONS[key]}\n'
                                    f'<code>(Выполнено)</code>')
        else:
            achievement_list.append(f'<b>· {value[0]}</b> - {LEXICON_CRITERIONS[key]}\n'
                                    f'<code>(Не выполнено)</code>')
    return '\n\n'.join(achievement_list)