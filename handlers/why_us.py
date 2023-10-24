from aiogram import Router, types, F
from aiogram.types import FSInputFile
from database.db_actions import db_check_user


router = Router()


@router.message(F.text == 'Почему Мы')
async def why_us(message: types.Message):
    """
        Provides a response explaining why users should choose RETRO CLUB with a captioned image.

        Args:
            message (types.Message): The incoming message object.

        Returns:
            None
    """
    db_result = await db_check_user(message.from_user.id)
    if db_result:
        pass
    else:
        image_from_pc = FSInputFile("media/picture_1.jpg")
        result = await message.answer_photo(
            image_from_pc,
            caption="Потому что мы ĸоманда профессионалов помогающих Вам пользоваться устройствами таĸ ĸаĸ вам бы "
                    "этого хотелось!",
            reply_markup=types.ReplyKeyboardRemove()
        )
