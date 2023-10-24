from aiogram import Router, types, F
from keyboards.keyboards_collection import ask_question_inkeyboard, ask_question_keyboard
from database.db_actions import db_check_user


router = Router()


@router.message(F.text == 'Задать вопрос')
async def ask_question(message: types.Message):
    """
        Handle the user's request to ask a question and provide guidance.

        Args:
            message (types.Message): The message from the user.
    """
    db_result = await db_check_user(message.from_user.id)
    if db_result:
        pass
    else:
        key = await ask_question_inkeyboard()
        await message.answer('Для соединения с оператором нажмите на кнопку под этим сообщением', reply_markup=key)
        keyboard = await ask_question_keyboard()
        await message.answer('После подтверждения возраста нажмите на кнопку "Возраст подтвержден"', reply_markup=keyboard)