from aiogram import Router, types, F
from keyboards.keyboards_collection import get_addresses_keyboard
from database.db_actions import db_check_user
from states.my_states import ShowAddressesState


router = Router()


@router.message(ShowAddressesState.start_input, F.text == 'Назад')
@router.message(F.text == '📍Узнать адреса')
async def address(message: types.Message):
    """
        Handle the user's request to get addresses of stores or services.

        Args:
            message (types.Message): The message from the user.
    """
    db_result = await db_check_user(message.from_user.id)
    if db_result:
        pass
    else:
        key = await get_addresses_keyboard()
        await message.answer('Здесь вы можете подобрать ближайший фирменный магазинили магазины с необходимым для вас '
                             'сервисом.\nВыберите по ĸнопĸе ниже интересующий вас сервис.☺️️️️️️️', reply_markup=key)
