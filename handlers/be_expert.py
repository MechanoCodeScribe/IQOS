from aiogram import Router, types, F
from keyboards.keyboards_collection import be_expert_keyboard
from database.db_actions import db_check_user


router = Router()


@router.message(F.text == "Хочу быть Экспертом")
async def be_expert(message: types.Message):
    """
        Handle the user's request to become an expert and provide guidance.

        Args:
            message (types.Message): The message from the user.
    """
    db_result = await db_check_user(message.from_user.id)
    if db_result:
        pass
    else:
        key = await be_expert_keyboard()
        await message.answer('Вы настоящий эксперт по вкусам?\nПроверьте себя по кнопке ниже⬇️', reply_markup=key)