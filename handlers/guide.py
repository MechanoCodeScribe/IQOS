from aiogram import Router, types, F
from keyboards.keyboards_collection import guide_keyboard, type_choice_keyboard, one_time_tg_keyboard, \
    liquids_tg_keyboard, tg_keyboard
from database.db_actions import db_check_user
from aiogram.fsm.context import FSMContext
from states.my_states import GuideState

router = Router()


@router.message(F.text == '✈️Палитра Вĸусов')
async def guide(message: types.Message):
    """
        Handle the user's request to explore the flavor palette.

        Args:
            message (types.Message): The message from the user.
    """
    db_result = await db_check_user(message.from_user.id)
    if db_result:
        pass
    else:
        key = await guide_keyboard()
        await message.answer(
            'О вкусах не спорят. Их выбирают! Хотите проверить, какой вкус PETPO подойдет именно вам? Подберите '
            'персональную коллекцию вкусов PETPO на основе ваших предпочтений.',
            reply_markup=key)


@router.message(F.text == 'Кислые')
@router.message(F.text == 'Сладкие')
@router.message(F.text == 'С холодком')
@router.message(F.text == 'Выпечка')
@router.message(F.text == 'Мятные')
@router.message(F.text == 'Экзотические')
async def taste(message: types.Message, state: FSMContext):
    """
        Handle user's flavor preference selection.

        Args:
            message (types.Message): The message from the user.
            state (FSMContext): The FSM state context.
    """
    db_result = await db_check_user(message.from_user.id)
    if db_result:
        pass
    else:
        key = await type_choice_keyboard()
        await message.answer('Жидкость или одноразки?', reply_markup=key)
        await state.set_state(GuideState.start_input)


@router.message(GuideState.start_input, F.text == 'Жидкость')
async def taste_liquid(message: types.Message):
    """
        Handle the user's selection of liquid flavors.

        Args:
            message (types.Message): The message from the user.
    """
    key = await liquids_tg_keyboard()
    await message.answer('Жидкости', reply_markup=key)


@router.message(GuideState.start_input, F.text == 'Одноразки')
async def taste_one_time(message: types.Message):
    """
        Handle the user's selection of one-time devices.

        Args:
            message (types.Message): The message from the user.
    """
    key = await one_time_tg_keyboard()
    await message.answer('Одноразовое устройство', reply_markup=key)


@router.message(GuideState.start_input, F.text == 'Soak')
@router.message(GuideState.start_input, F.text == 'UDN')
@router.message(GuideState.start_input, F.text == 'PODONKI')
@router.message(GuideState.start_input, F.text == 'MIST')
@router.message(GuideState.start_input, F.text == 'Husky')
@router.message(GuideState.start_input, F.text == 'Tikobar')
@router.message(GuideState.start_input, F.text == 'Toyz')
@router.message(GuideState.start_input, F.text == 'Duall')
@router.message(GuideState.start_input, F.text == 'Podonki')
@router.message(GuideState.start_input, F.text == 'Ataku')
@router.message(GuideState.start_input, F.text == 'А че Нет')
@router.message(GuideState.start_input, F.text == 'Иные')
async def send_link(message: types.Message):
    """
        Send a link based on the user's selection.

        Args:
            message (types.Message): The message from the user.
    """
    key = await tg_keyboard()
    await message.answer('Отличный выбор!', reply_markup=key)
    await message.answer('Переходите в наш Телеграм канал', reply_markup=types.ReplyKeyboardRemove())



