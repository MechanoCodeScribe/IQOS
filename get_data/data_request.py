from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from states.my_states import GetDataState
from aiogram import types, Router
from checker.check_funcs import check_format, check_age, check_sex
from database.db_actions import add_user_to_db

router = Router()


async def get_phone(message: types.Message, state: FSMContext):
    """
        Start the process of collecting the user's phone number.

        Args:
            message (types.Message): The message from the user.
            state (FSMContext): The FSM context to manage the conversation state.
    """
    builder = ReplyKeyboardBuilder()
    builder.row(types.KeyboardButton(text="Поделиться номером", request_contact=True))
    await message.answer('Для перехода в Главное меню, пожалуйста, поделитесь номером телефона, кликнув на кнопку '
                         '«Поделиться номером». Так вы подтверждаете, что согласны на обработку персональных '
                         'данных.', reply_markup=builder.as_markup(resize_keyboard=True)
                         )
    await state.set_state(GetDataState.phone_input)


@router.message(GetDataState.phone_input)
async def get_name(message: types.Message, state: FSMContext):
    """
        Handle the user's phone input state. If the user shares their phone number,
        it stores the phone number, prompts the user to enter their name, and transitions to the name input state.
        If the user doesn't share their phone number, it calls the `incorrect_phone` function.

        Args:
            message (types.Message): The message from the user.
            state (FSMContext): The FSM context to manage the conversation state.
    """
    if message.contact and message.contact.phone_number:
        phone_number = message.contact.phone_number
        await state.update_data(phone=phone_number)
        await message.answer('Пожалуйста, введите ваше имя:', reply_markup=types.ReplyKeyboardRemove())
        await state.set_state(GetDataState.name_input)
    else:
        await incorrect_phone(message)


@router.message(GetDataState.name_input)
async def get_surname(message: types.Message, state: FSMContext):
    """
        Handle the user's name input state. It stores the user's name, prompts the user to enter their surname,
        and transitions to the surname input state.

        Args:
            message (types.Message): The message from the user.
            state (FSMContext): The FSM context to manage the conversation state.
    """
    name = message.text
    await state.update_data(name=name)
    await message.answer('Пожалуйста, введите вашу фамилию:')
    await state.set_state(GetDataState.surname_input)


@router.message(GetDataState.surname_input)
async def process_sex_input(message: types.Message, state: FSMContext):
    """
        Handle the user's surname input state. It stores the user's surname, prompts the user to enter their gender,
        and transitions to the gender input state.

        Args:
            message (types.Message): The message from the user.
            state (FSMContext): The FSM context to manage the conversation state.
    """
    surname = message.text
    await state.update_data(surname=surname)
    await message.answer('Подскажите ваш пол.\n\nВведите ниже М или Ж:')
    await state.set_state(GetDataState.sex_input)


@router.message(GetDataState.sex_input)
async def process_birth_input(message: types.Message, state: FSMContext):
    """
        Handle the user's gender input state. It stores the user's gender, checks if the gender format is valid,
        and transitions to the date of birth input state if the format is valid.

        Args:
            message (types.Message): The message from the user.
            state (FSMContext): The FSM context to manage the conversation state.
    """
    sex = message.text.lower()
    await state.update_data(sex=sex)
    check_sex_format = await check_sex(sex)
    if check_sex_format:
        await message.answer(
            'Подскажите вашу дату рождения, а я посчитаю, есть ли вам уже 18 лет.\n\nВведите ниже дату в формате '
            'ДД.ММ.ГГГГ:')
        await state.set_state(GetDataState.birthday_input)
    else:
        await incorrect_sex(message)


@router.message(GetDataState.birthday_input)
async def process_confirm(message: types.Message, state: FSMContext):
    """
        Handle the user's date of birth input state. It validates the date format, checks if the user is at least 18 years old,
        stores the user's date of birth, and adds the user to the database if the age is confirmed.

        Args:
            message (types.Message): The message from the user containing the date of birth.
            state (FSMContext): The FSM context to manage the conversation state.
    """
    birthday = message.text
    check_birthday_format = await check_format(birthday)
    if check_birthday_format:
        age_confirmed = await check_age(birthday)
        if age_confirmed:
            await state.update_data(birthday=birthday)
            user_data = await state.get_data()
            await add_user_to_db(message, user_data)
            name = user_data['name']
            await message.answer(f'{name}, вы успешно зарегистрированы! Для перехода в Главное меню воспользуйтесь командой /show_buttons')
            await state.clear()
        else:
            await incorrect_age(message)
    else:
        await incorrect_date_format(message)


async def incorrect_age(message: types.Message):
    """
        Handle the case where the user's age is below 18. It sends a message to the user indicating that the offer
        is only for adult consumers of tobacco or other nicotine-containing products.

        Args:
            message (types.Message): The message from the user.
    """
    await message.answer('Наше предложение только для совершеннолетних потребителей табака или иной '
                         'никотиносодержащей продукции. Было приятно поболтать.\n\nВаш чат-бот РЕТРО.')


async def incorrect_sex(message: types.Message):
    """
        Handle the case where the user provides an incorrect gender input. It sends a message to the user
        indicating that they should enter 'М' for male or 'Ж' for female.

        Args:
            message (types.Message): The message from the user.
    """
    await message.answer('Неверный формат, пожалуйста введите М или Ж:')


async def incorrect_phone(message: types.Message):
    """
        Handle the case where the user provides an incorrect phone number input. It sends a message to the user
        indicating that they should share their phone number by clicking the "Поделиться номером" (Share phone number) button.

        Args:
            message (types.Message): The message from the user.
    """
    await message.answer('Неверный ввод, пожалуйста поделитесь номером телефона нажав на кнопку «Поделиться номером».')


async def incorrect_date_format(message: types.Message):
    """
        Handle the case where the user provides an incorrect date format. It sends a message to the user
        indicating that they should enter the date in the format ДД.ММ.ГГГГ (DD.MM.YYYY).

        Args:
            message (types.Message): The message from the user.
    """
    await message.answer('Пожалуйста, введите дату в формате ДД.ММ.ГГГГ:')
