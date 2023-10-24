from aiogram import Router, types, F
from keyboards.keyboards_collection import petpo_club_keyboard
from aiogram.types import FSInputFile
from database.db_actions import db_check_user


router = Router()


@router.message(F.text == '💙PETPO CLUB')
@router.message(F.text == 'Возраст подтвержден')
async def petpo_club(message: types.Message):
    """
        Handles the interaction with PETPO CLUB and age confirmation.

        Args:
            message (types.Message): The message object containing user information.
    """
    db_result = await db_check_user(message.from_user.id)
    if db_result:
        pass
    else:
        key = await petpo_club_keyboard()
        image_from_pc = FSInputFile("media/picture_1.jpg")
        result = await message.answer_photo(
            image_from_pc,
            caption="Какой-то текст",
            reply_markup=key
        )
