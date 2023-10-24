from aiogram import Router, types, F
from database.db_actions import db_check_user
from aiogram.fsm.context import FSMContext
from handlers.order_request import get_order


router = Router()


@router.message(F.text == "✨Заĸазать устройство")
async def create_order(message: types.Message, state: FSMContext):
    """
        Handle the user's request to create an order for a device.

        Args:
            message (types.Message): The message from the user.
            state (FSMContext): The current state of the conversation.
    """
    db_result = await db_check_user(message.from_user.id)
    if db_result:
        pass
    else:
        await get_order(message, state)
