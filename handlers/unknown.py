from aiogram import types, Router, F
from database.db_actions import db_check_user


router = Router()


@router.message(F.text)
async def unknown(message: types.Message):
    """
    Handle unknown commands.

    Responds to unknown commands with a message.

    Args:
        message (types.Message): The incoming message object.

    Returns:
        None
    """
    db_result = await db_check_user(message.from_user.id)
    if db_result:
        await message.answer('Я вас не понимаю')
    else:
        await message.answer('Я вас не понимаю\nПожалуйста, нажмите на одну из кнопок меню ⬇️')