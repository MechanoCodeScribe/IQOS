from aiogram import Router, types, F
from keyboards.keyboards_collection import to_know_keyboard
from database.db_actions import db_check_user


router = Router()


@router.message(F.text == "🔍Узнать об РЕТРО CLUB")
async def to_know(message: types.Message):
    """
        Handles the user's request to learn more about RETRO CLUB and provides options for assistance.

        Args:
            message (types.Message): The incoming message object.

        Returns:
            None
    """
    db_result = await db_check_user(message.from_user.id)
    if db_result:
        pass
    else:
        key = await to_know_keyboard()
        await message.answer('Чем я могу помочь?', reply_markup=key)
