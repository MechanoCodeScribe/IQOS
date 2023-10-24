from aiogram import Router, types, F
from keyboards.keyboards_collection import social_inkeyboard
from database.db_actions import db_check_user


router = Router()


@router.message(F.text == 'Мы в социальных сетях')
async def social(message: types.Message):
    """
        Handles the user's request to view social media links.

        Args:
            message (types.Message): The message object containing user information.
    """
    db_result = await db_check_user(message.from_user.id)
    if db_result:
        pass
    else:
        key = await social_inkeyboard()
        await message.answer("Хотите быть в курсе всех новостей об PETPO CLUB?\nПодписывайтесь на наши официальные "
                             "каналы в социальных сетях!", reply_markup=key)

