from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


async def main_keyboard():
    kb_row1 = [
        types.KeyboardButton(text="💙PETPO CLUB"),
        types.KeyboardButton(text="✨Заĸазать устройство")
    ]

    kb_row2 = [
        types.KeyboardButton(text="📍Узнать адреса"),
        types.KeyboardButton(text="✈️Палитра Вĸусов")
    ]

    kb_row3 = [
        types.KeyboardButton(text="🔍Узнать об РЕТРО CLUB"),
        types.KeyboardButton(text="⏳Узнать статус заĸаза"),
    ]

    kb_row4 = [
        types.KeyboardButton(text="⚙️Мои устройства"),
        types.KeyboardButton(text="🔧Мое устройство сломалось")
    ]

    kb_row5 = [
        types.KeyboardButton(text="❓Задать другой вопрос"),
    ]

    kb = [kb_row1, kb_row2, kb_row3, kb_row4, kb_row5]

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    return keyboard


async def petpo_club_keyboard():
    kb_row1 = [
        types.KeyboardButton(text="О нас")
    ]

    kb_row2 = [
        types.KeyboardButton(text="Задать вопрос")
    ]

    kb_row3 = [
        types.KeyboardButton(text="Главное меню")
    ]

    kb = [kb_row1, kb_row2, kb_row3]

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    return keyboard


async def ask_question_inkeyboard():
    url = 'https://www.google.com/'
    button = InlineKeyboardButton(text="Начать видеозвонок", url=url)
    in_keyboard = InlineKeyboardMarkup(inline_keyboard=[[button]])

    return in_keyboard


async def ask_question_keyboard():
    kb_row1 = [
        types.KeyboardButton(text="Возраст подтвержден")
    ]

    kb_row2 = [
        types.KeyboardButton(text="Главное меню")
    ]

    kb = [kb_row1, kb_row2]

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    return keyboard


async def exit_keyboard():
    kb_row1 = [
        types.KeyboardButton(text="Выйти")
    ]

    kb = [kb_row1]

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    return keyboard


async def yes_no_keyboard():
    kb_row1 = [
        types.KeyboardButton(text="Да")
    ]

    kb_row2 = [
        types.KeyboardButton(text="Нет")
    ]

    kb = [kb_row1, kb_row2]

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    return keyboard


async def exit_back_keyboard():
    kb_row1 = [
        types.KeyboardButton(text="Назад")
    ]

    kb_row2 = [
        types.KeyboardButton(text="Выйти")
    ]

    kb = [kb_row1, kb_row2]

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    return keyboard


async def items_exit_keyboard():
    kb_row1 = [
        types.KeyboardButton(text="Под-система")
    ]

    kb_row2 = [
        types.KeyboardButton(text="Одноразовое устройство")
    ]

    kb_row3 = [
        types.KeyboardButton(text="Иное устройство")
    ]

    kb_row4 = [
        types.KeyboardButton(text="Назад")
    ]

    kb_row5 = [
        types.KeyboardButton(text="Выйти")
    ]

    kb = [kb_row1, kb_row2, kb_row3, kb_row4, kb_row5]

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    return keyboard


async def location_share_keyboard():
    builder = ReplyKeyboardBuilder()

    # Добавляем кнопку "Поделиться геолокацией"
    builder.row(types.KeyboardButton(text="Поделиться геопозицией", request_location=True))
    builder.row(types.KeyboardButton(text="Назад"))

    return builder


async def get_addresses_keyboard():
    kb_row1 = [
        types.KeyboardButton(text="Фирменные магазины")
    ]

    kb_row2 = [
        types.KeyboardButton(text="Покупка")
    ]

    kb = [kb_row1, kb_row2]

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    return keyboard


async def guide_keyboard():
    kb_row1 = [
        types.KeyboardButton(text="Кислые"),
        types.KeyboardButton(text="Сладкие")
    ]

    kb_row2 = [
        types.KeyboardButton(text="С холодком"),
        types.KeyboardButton(text="Выпечка")
    ]

    kb_row3 = [
        types.KeyboardButton(text="Мятные"),
        types.KeyboardButton(text="Экзотические"),
    ]

    kb = [kb_row1, kb_row2, kb_row3]

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    return keyboard


async def to_know_keyboard():
    kb_row1 = [
        types.KeyboardButton(text="Сервис")
    ]

    kb_row2 = [
        types.KeyboardButton(text="Почему Мы")
    ]

    kb_row3 = [
        types.KeyboardButton(text="Зачем Мы")
    ]

    kb_row4 = [
        types.KeyboardButton(text="Хочу быть Экспертом")
    ]

    kb_row5 = [
        types.KeyboardButton(text="Мы в социальных сетях")
    ]

    kb = [kb_row1, kb_row2, kb_row3, kb_row4, kb_row5]

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    return keyboard


async def show_orders_keyboard():
    kb_row1 = [
        types.KeyboardButton(text="Главное меню")
    ]

    kb_row2 = [
        types.KeyboardButton(text="Чат с оператором")
    ]

    kb = [kb_row1, kb_row2]

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    return keyboard


async def support_keyboard():
    kb_row1 = [
        types.KeyboardButton(text="Чат с оператором")
    ]

    kb_row2 = [
        types.KeyboardButton(text="Главное меню")
    ]

    kb = [kb_row1, kb_row2]

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    return keyboard


async def service_inkeyboard():
    url = 'https://www.google.com/'
    button = InlineKeyboardButton(text="Замена", url=url)
    in_keyboard = InlineKeyboardMarkup(inline_keyboard=[[button]])

    return in_keyboard


async def be_expert_keyboard():
    kb_row1 = [
        types.KeyboardButton(text="Пройти тест")
    ]

    kb_row2 = [
        types.KeyboardButton(text="Получить консультацию")
    ]

    kb = [kb_row1, kb_row2]

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    return keyboard


async def q_1():
    kb_row1 = [
        types.KeyboardButton(text="q1.Вариант 1")
    ]

    kb_row2 = [
        types.KeyboardButton(text="q1.Вариант 2")
    ]

    kb = [kb_row1, kb_row2]

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    return keyboard


async def q_2():
    kb_row1 = [
        types.KeyboardButton(text="q2.Вариант 1")
    ]

    kb_row2 = [
        types.KeyboardButton(text="q2.Вариант 2")
    ]

    kb = [kb_row1, kb_row2]

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    return keyboard


async def q_3():
    kb_row1 = [
        types.KeyboardButton(text="q3.Вариант 1")
    ]

    kb_row2 = [
        types.KeyboardButton(text="q3.Вариант 2")
    ]

    kb = [kb_row1, kb_row2]

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    return keyboard


async def q_4():
    kb_row1 = [
        types.KeyboardButton(text="q4.Вариант 1")
    ]

    kb_row2 = [
        types.KeyboardButton(text="q4.Вариант 2")
    ]

    kb = [kb_row1, kb_row2]

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    return keyboard


async def q_5():
    kb_row1 = [
        types.KeyboardButton(text="q5.Вариант 1")
    ]

    kb_row2 = [
        types.KeyboardButton(text="q5.Вариант 2")
    ]

    kb = [kb_row1, kb_row2]

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    return keyboard


async def social_inkeyboard():
    url1 = 'https://www.google.com/'
    url2 = 'https://www.google.com/'
    url3 = 'https://www.google.com/'
    url4 = 'https://www.google.com/'
    button1 = InlineKeyboardButton(text="Соцсеть1", url=url1)
    button2 = InlineKeyboardButton(text="Соцсеть2", url=url2)
    button3 = InlineKeyboardButton(text="Соцсеть3", url=url3)
    button4 = InlineKeyboardButton(text="Соцсеть4", url=url4)
    in_keyboard = InlineKeyboardMarkup(inline_keyboard=[[button1], [button2], [button3], [button4]])

    return in_keyboard


async def add_item_keyboard():
    kb_row1 = [
        types.KeyboardButton(text='Отправить фотографию кода с коробки'),
        types.KeyboardButton(text='Под-система')
    ]

    kb_row2 = [
        types.KeyboardButton(text='Одноразовое устройство'),
        types.KeyboardButton(text='Иное устройство')
    ]

    kb_row3 = [
        types.KeyboardButton(text="Назад"),
        types.KeyboardButton(text="Главное меню"),
    ]

    kb = [kb_row1, kb_row2, kb_row3]

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    return keyboard


async def menu_keyboard():
    kb_row1 = [
        types.KeyboardButton(text="Главное меню")
    ]

    kb = [kb_row1]

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    return keyboard


async def add_special_item_keyboard():
    kb_row1 = [
        types.KeyboardButton(text="Назад")
    ]

    kb_row2 = [
        types.KeyboardButton(text="Главное меню")
    ]

    kb_row3 = [
        types.KeyboardButton(text="Чат с оператором")
    ]

    kb = [kb_row1, kb_row2, kb_row3]

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    return keyboard


async def location_stores_keyboard():
    builder = ReplyKeyboardBuilder()

    # Добавляем кнопку "Поделиться геолокацией"
    builder.row(types.KeyboardButton(text="Поделиться геопозицией", request_location=True))
    builder.row(types.KeyboardButton(text="Назад"))
    builder.row(types.KeyboardButton(text="Главное меню"))

    return builder


async def buy_keyboard():
    kb_row1 = [
        types.KeyboardButton(text='Под-устройство'),
        types.KeyboardButton(text='Одноразовое устройство')
    ]

    kb_row2 = [
        types.KeyboardButton(text='Испарители и Катриджи'),
        types.KeyboardButton(text='Жидкости')
    ]

    kb_row3 = [
        types.KeyboardButton(text="Назад")
    ]

    kb_row4 = [
        types.KeyboardButton(text="Главное меню")
    ]

    kb = [kb_row1, kb_row2, kb_row3, kb_row4]

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    return keyboard


async def for_item_keyboard():
    kb_row1 = [
        types.KeyboardButton(text='Brusko'),
        types.KeyboardButton(text='Geek Vape')
    ]

    kb_row2 = [
        types.KeyboardButton(text='Vaporesso'),
        types.KeyboardButton(text='Smoant')
    ]

    kb_row3 = [
        types.KeyboardButton(text="Voopoo"),
        types.KeyboardButton(text='Rinsoe')
    ]

    kb_row4 = [
        types.KeyboardButton(text="Иные"),
        types.KeyboardButton(text='Назад')
    ]

    kb_row5 = [
        types.KeyboardButton(text="Главное меню")
    ]

    kb = [kb_row1, kb_row2, kb_row3, kb_row4, kb_row5]

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    return keyboard


async def one_time_item_keyboard():
    kb_row1 = [
        types.KeyboardButton(text='Soak'),
        types.KeyboardButton(text='UDN')
    ]

    kb_row2 = [
        types.KeyboardButton(text='PODONKI'),
        types.KeyboardButton(text='MIST')
    ]

    kb_row3 = [
        types.KeyboardButton(text="Husky"),
        types.KeyboardButton(text='Tikobar')
    ]

    kb_row4 = [
        types.KeyboardButton(text="Иные"),
        types.KeyboardButton(text='Назад')
    ]

    kb_row5 = [
        types.KeyboardButton(text="Главное меню")
    ]

    kb = [kb_row1, kb_row2, kb_row3, kb_row4, kb_row5]

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    return keyboard


async def liquids_keyboard():
    kb_row1 = [
        types.KeyboardButton(text='Husky'),
        types.KeyboardButton(text='Toyz')
    ]

    kb_row2 = [
        types.KeyboardButton(text='Duall'),
        types.KeyboardButton(text='Podonki')
    ]

    kb_row3 = [
        types.KeyboardButton(text="Soak"),
        types.KeyboardButton(text='Ataku')
    ]

    kb_row4 = [
        types.KeyboardButton(text="А че Нет"),
        types.KeyboardButton(text='Иные')
    ]

    kb_row5 = [
        types.KeyboardButton(text="Назад"),
        types.KeyboardButton(text="Главное меню")
    ]

    kb = [kb_row1, kb_row2, kb_row3, kb_row4, kb_row5]

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    return keyboard


async def type_choice_keyboard():
    kb_row1 = [
        types.KeyboardButton(text="Жидкость")
    ]

    kb_row2 = [
        types.KeyboardButton(text="Одноразки")
    ]

    kb = [kb_row1, kb_row2]

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    return keyboard


async def liquids_tg_keyboard():
    kb_row1 = [
        types.KeyboardButton(text='Husky'),
        types.KeyboardButton(text='Toyz')
    ]

    kb_row2 = [
        types.KeyboardButton(text='Duall'),
        types.KeyboardButton(text='Podonki')
    ]

    kb_row3 = [
        types.KeyboardButton(text="Soak"),
        types.KeyboardButton(text='Ataku')
    ]

    kb_row4 = [
        types.KeyboardButton(text="А че Нет"),
        types.KeyboardButton(text='Иные')
    ]

    kb = [kb_row1, kb_row2, kb_row3, kb_row4]

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    return keyboard


async def one_time_tg_keyboard():
    kb_row1 = [
        types.KeyboardButton(text='Soak'),
        types.KeyboardButton(text='UDN')
    ]

    kb_row2 = [
        types.KeyboardButton(text='PODONKI'),
        types.KeyboardButton(text='MIST')
    ]

    kb_row3 = [
        types.KeyboardButton(text="Husky"),
        types.KeyboardButton(text='Tikobar')
    ]

    kb_row4 = [
        types.KeyboardButton(text="Иные")
    ]

    kb = [kb_row1, kb_row2, kb_row3, kb_row4]

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    return keyboard


async def tg_keyboard():
    url = 'https://www.google.com/'
    button = InlineKeyboardButton(text="Ссылка на телеграм", url=url)
    in_keyboard = InlineKeyboardMarkup(inline_keyboard=[[button]])

    return in_keyboard