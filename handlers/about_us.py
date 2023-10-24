from aiogram import Router, types, F
from database.db_actions import db_check_user


router = Router()


@router.message(F.text == 'О нас')
async def about_us(message: types.Message):
    """
        Handle the user's request to get information about the service.

        Args:
            message (types.Message): The message from the user.
    """
    db_result = await db_check_user(message.from_user.id)
    if db_result:
        pass
    else:
        await message.answer('Какой-то текст', reply_markup=types.ReplyKeyboardRemove())
