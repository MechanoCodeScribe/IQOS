from aiogram.fsm.context import FSMContext
from states.my_states import GetOrderState
from aiogram import types, Router, F
from checker.check_funcs import check_format, check_age
from database.db_actions import db_check_user, add_order_to_db
from keyboards.keyboards_collection import exit_keyboard, yes_no_keyboard, exit_back_keyboard, items_exit_keyboard, location_share_keyboard
from get_data.data_request import incorrect_date_format

router = Router()


@router.message(GetOrderState.birthday_input, F.text == 'Нет')
async def get_order(message: types.Message, state: FSMContext):
    """
        Handle user's choice when they don't confirm their age.

        Args:
            message (types.Message): The message from the user.
            state (FSMContext): The state machine context.
    """
    db_result = await db_check_user(message.from_user.id)
    if db_result:
        pass
    else:
        key = await exit_keyboard()
        await message.answer('Рад встрече! 👋🏻 Я чат-бот PETPO CLUB.\nПомогу вам оформить заявку на покупку '
                             'устройства.\n\nПодскажите, пожалуйста, вашу дату рождения, а я быстренько посчитаю, '
                             'что вам уже есть 18 лет 😉Введите ниже дату в формате ДД.ММ.ГГГГ', reply_markup=key)

        await state.set_state(GetOrderState.birthday_input)


@router.message(GetOrderState.name_input, F.text == 'Назад')
async def delete_birthday(message: types.Message, state: FSMContext):
    """
        Handle the user's choice to go back and delete the previously entered birthday.

        Args:
            message (types.Message): The message from the user.
            state (FSMContext): The state machine context.
    """
    await state.update_data(birthday=None)
    key = await exit_keyboard()
    await message.answer('Рад встрече! 👋🏻 Я чат-бот PETPO CLUB.\nПомогу вам оформить заявку на покупку '
                         'устройства.\n\nПодскажите, пожалуйста, вашу дату рождения, а я быстренько посчитаю, '
                         'что вам уже есть 18 лет 😉Введите ниже дату в формате ДД.ММ.ГГГГ', reply_markup=key)

    await state.set_state(GetOrderState.birthday_input)


@router.message(GetOrderState.city_input, F.text == 'Назад')
async def delete_name(message: types.Message, state: FSMContext):
    """
        Handle the user's choice to go back and delete the previously entered name.

        Args:
            message (types.Message): The message from the user.
            state (FSMContext): The state machine context.
    """
    await state.update_data(name=None)
    key = await exit_back_keyboard()
    await message.answer('Давайте познакомимся. Укажите ваше имя, как в паспорте', reply_markup=key)

    await state.set_state(GetOrderState.name_input)


@router.message(GetOrderState.item_input, F.text == 'Назад')
async def delete_city(message: types.Message, state: FSMContext):
    """
        Handle the user's choice to go back and delete the previously entered city.

        Args:
            message (types.Message): The message from the user.
            state (FSMContext): The state machine context.
    """
    user_data = await state.get_data()
    name = user_data['name']
    await state.update_data(city=None)
    key = await exit_back_keyboard()
    await message.answer(f'Очень приятно, {name}! Чувствую, мы подружимся! 🙂\n\n👍🏼 Ура!! Давайте проверим способы '
                         f'получения устройства. А в каком вы городе?', reply_markup=key)

    await state.set_state(GetOrderState.city_input)


@router.message(GetOrderState.address_input, F.text == 'Назад')
async def delete_item(message: types.Message, state: FSMContext):
    """
        Handle the user's choice to go back and delete the previously entered item.

        Args:
            message (types.Message): The message from the user.
            state (FSMContext): The state machine context.
    """
    user_data = await state.get_data()
    city = user_data['city']
    await state.update_data(item=None)
    key = await items_exit_keyboard()
    await message.answer(
        f'{city} - Классный город! Я просто бот, а то бы я сам доставил вам устройство.\nНо я знаю людей из нашей '
        f'команды, которые всё организуют.🕺🏼\nПожалуйста, выберите устройство:',
        reply_markup=key)
    await state.set_state(GetOrderState.item_input)


async def incorrect_age_order(message: types.Message):
    """
        Handle the case when a user doesn't meet the age requirement for making an order.

        Args:
            message (types.Message): The message from the user.
    """
    await message.answer(
        'Как вы молоды! 😉\n\nНаше предложение только для совершеннолетних потребителей табака или иной '
        'никотиносодержащей продукции. Было приятно поболтать.\n\nВаш чат-бот РЕТРО.')


@router.message(GetOrderState.birthday_input, F.text == 'Выйти')
@router.message(GetOrderState.name_input, F.text == 'Выйти')
@router.message(GetOrderState.city_input, F.text == 'Выйти')
@router.message(GetOrderState.item_input, F.text == 'Выйти')
@router.message(GetOrderState.address_input, F.text == 'Выйти')
async def exit_from_order(message: types.Message):
    """
        Handle the user's request to exit from the order creation process.

        Args:
            message (types.Message): The message from the user.
    """
    db_result = await db_check_user(message.from_user.id)
    if db_result:
        pass
    else:
        key = await yes_no_keyboard()
        await message.answer('Вы уверены, что хотите прервать оформление заказа?', reply_markup=key)


@router.message(GetOrderState.name_input, F.text == 'Нет')
@router.message(GetOrderState.birthday_input)
async def get_name_data(message: types.Message, state: FSMContext):
    """
        Handle user data input for the user's name during the order creation process.

        Args:
            message (types.Message): The message from the user.
            state (FSMContext): The FSM context for maintaining conversation state.
    """
    user_data = await state.get_data()
    if 'birthday' not in user_data or user_data['birthday'] is None:
        birthday = message.text
        check_birthday_format = await check_format(birthday)
        if check_birthday_format:
            age_confirmed = await check_age(birthday)
            if age_confirmed:
                await state.update_data(birthday=birthday)
                key = await exit_back_keyboard()
                await message.answer('Давайте познакомимся. Укажите ваше имя, как в паспорте', reply_markup=key)
                await state.set_state(GetOrderState.name_input)
            else:
                await state.set_state(GetOrderState.exit_input)
                await incorrect_age_order(message)
        else:
            await incorrect_date_format(message)
    else:
        key = await exit_back_keyboard()
        await message.answer('Давайте познакомимся. Укажите ваше имя, как в паспорте', reply_markup=key)
        await state.set_state(GetOrderState.name_input)


@router.message(GetOrderState.city_input, F.text == 'Нет')
@router.message(GetOrderState.name_input)
async def get_surname(message: types.Message, state: FSMContext):
    """
        Handle user data input for the user's surname during the order creation process.

        Args:
            message (types.Message): The message from the user.
            state (FSMContext): The FSM context for maintaining conversation state.
    """
    user_data = await state.get_data()
    if 'name' not in user_data or user_data['name'] is None:
        name = message.text
        await state.update_data(name=name)
        key = await exit_back_keyboard()
        await message.answer(
            f'Очень приятно, {name}! Чувствую, мы подружимся! 🙂\n\n👍🏼 Ура!! Давайте проверим способы получения '
            f'устройства. А в каком вы городе?', reply_markup=key)
        await state.set_state(GetOrderState.city_input)
    else:
        name = user_data['name']
        key = await exit_back_keyboard()
        await message.answer(
            f'Очень приятно, {name}! Чувствую, мы подружимся! 🙂\n\n👍🏼 Ура!! Давайте проверим способы получения '
            f'устройства. А в каком вы городе?',
            reply_markup=key)
        await state.set_state(GetOrderState.city_input)


@router.message(GetOrderState.item_input, F.text == 'Нет')
@router.message(GetOrderState.city_input)
async def get_city(message: types.Message, state: FSMContext):
    """
        Handle user data input for the user's city during the order creation process.

        Args:
            message (types.Message): The message from the user.
            state (FSMContext): The FSM context for maintaining conversation state.
    """
    user_data = await state.get_data()
    if 'city' not in user_data or user_data['city'] is None:
        city = message.text
        await state.update_data(city=city)
        key = await items_exit_keyboard()
        await message.answer(
            f'{city} - Классный город! Я просто бот, а то бы я сам доставил вам устройство.\nНо я знаю людей из нашей '
            f'команды, которые всё организуют.🕺🏼\nПожалуйста, выберите устройство:', reply_markup=key)
        await state.set_state(GetOrderState.item_input)
    else:
        city = user_data['city']
        key = await items_exit_keyboard()
        await message.answer(
            f'{city} - Классный город! Я просто бот, а то бы я сам доставил вам устройство.\nНо я знаю людей из нашей '
            f'команды, которые всё организуют.🕺🏼\nПожалуйста, выберите устройство:',
            reply_markup=key)
        await state.set_state(GetOrderState.item_input)


@router.message(GetOrderState.address_input, F.text == 'Нет')
@router.message(GetOrderState.item_input, F.text == 'Под-система')
@router.message(GetOrderState.item_input, F.text == 'Одноразовое устройство')
@router.message(GetOrderState.item_input, F.text == 'Иное устройство')
async def get_item(message: types.Message, state: FSMContext):
    """
        Handle user data input for the selected item during the order creation process.

        Args:
            message (types.Message): The message from the user.
            state (FSMContext): The FSM context for maintaining conversation state.
    """
    item = message.text
    user_data = await state.get_data()
    if 'item' not in user_data or user_data['item'] is None:
        await state.update_data(item=item)
        key = await location_share_keyboard()
        await message.answer('Скиньте свою геолокацию или введите точный адрес📍, мы покажем магазины рядом с вами:', reply_markup=key.as_markup(resize_keyboard=True))
        await state.set_state(GetOrderState.address_input)
    else:
        key = await location_share_keyboard()
        await message.answer('Скиньте свою геолокацию или введите точный адрес📍, мы покажем магазины рядом с вами:', reply_markup=key.as_markup(resize_keyboard=True))
        await state.set_state(GetOrderState.address_input)


@router.message(GetOrderState.item_input, F.text)
async def wrong_item_input(message, state):
    """
        Handles incorrect input for the selected item in the order process.

        Args:
            message (types.Message): The message object containing user information.
            state (FSMContext): The FSM (Finite State Machine) context.
    """
    key = await items_exit_keyboard()
    await message.answer('Пожалуйста, выберите устройство:', reply_markup=key)
    await state.set_state(GetOrderState.item_input)


@router.message(GetOrderState.address_input)
async def confirm_order(message, state):
    """
        Handles the confirmation of an order and stores it in the database.

        Args:
            message (types.Message): The message object containing user information.
            state (FSMContext): The FSM (Finite State Machine) context.
    """
    if message.location:
        address = str(message.location)
    elif message.text:
        address = message.text
    await state.update_data(address=address)
    user_data = await state.get_data()
    await message.answer('Заявка успешно оформлена!', reply_markup=types.ReplyKeyboardRemove())
    await state.clear()
    await add_order_to_db(message, user_data)

