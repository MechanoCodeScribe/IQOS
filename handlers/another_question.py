from aiogram import Router, types, F
from keyboards.keyboards_collection import support_keyboard
from database.db_actions import db_check_user


router = Router()


@router.message(F.text == "❓Задать другой вопрос")
async def guide(message: types.Message):
    """
        Handle the user's request to ask another question and provide guidance.

        Args:
            message (types.Message): The message from the user.
    """
    db_result = await db_check_user(message.from_user.id)
    if db_result:
        pass
    else:
        key = await support_keyboard()
        await message.answer('Выберите удобный канал для связи с оператором', reply_markup=key)
