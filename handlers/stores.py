from aiogram import Router, types, F
from database.db_actions import db_check_user
from keyboards.keyboards_collection import location_stores_keyboard
from aiogram.fsm.context import FSMContext
from states.my_states import ShowAddressesState


router = Router()


@router.message(F.text == 'Фирменные магазины')
async def stores(message: types.Message, state: FSMContext):
    """
        Handles the user's request to view brand stores and initializes the state for showing addresses.

        Args:
            message (types.Message): The incoming message object.
            state (FSMContext): The current state of the user.

        Returns:
            None
    """
    db_result = await db_check_user(message.from_user.id)
    if db_result:
        pass
    else:
        key = await location_stores_keyboard()
        await message.answer('Какой-то текст', reply_markup=key.as_markup(resize_keyboard=True))
        await state.set_state(ShowAddressesState.start_input)
