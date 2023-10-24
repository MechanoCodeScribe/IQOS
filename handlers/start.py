from aiogram import Router, types, F
from keyboards.keyboards_collection import main_keyboard
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from states.my_states import GetOrderState, AddItemState
from database.db_actions import db_check_user
from get_data.data_request import get_phone
import logging


router = Router()


@router.message(Command('start'))
@router.message(Command('show_buttons'))
@router.message(F.text == 'Главное меню')
@router.message(AddItemState.confirmed_input, F.text == 'Нет')
@router.message(GetOrderState.exit_input, F.text == 'Выйти')
@router.message(GetOrderState.exit_input, F.text == 'Да')
@router.message(GetOrderState.birthday_input, F.text == 'Да')
@router.message(GetOrderState.name_input, F.text == 'Да')
@router.message(GetOrderState.city_input, F.text == 'Да')
@router.message(GetOrderState.item_input, F.text == 'Да')
async def start_command(message: types.Message, state: FSMContext):
    """
        Handle the start command from the user.

        Args:
            message (types.Message): The incoming message object.

        Returns:
            None
            :param message:
            :param state:
    """

    logging.info('new start')
    await state.clear()
    db_result = await db_check_user(message.from_user.id)
    if db_result:
        await message.answer('Рад встрече!👋🏻Я чат-бот РЕТРО. Помогаю пользователям РЕТРО CLUB')
        await get_phone(message, state)
    else:
        key = await main_keyboard()
        await message.answer('Итак, вы здесь, чтобы...', reply_markup=key)


