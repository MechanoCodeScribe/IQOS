from aiogram import Router, types, F
from aiogram.types import FSInputFile
from database.db_actions import db_check_user


router = Router()


@router.message(F.text == 'Зачем Мы')
async def what_for_us(message: types.Message):
    """
        Provides information about the services offered by RETRO CLUB with a captioned image.

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
            caption="Мы даем профессиональный сервис и ĸомфорт для пользования вашими устройствами в повседневной жизни",
            reply_markup=types.ReplyKeyboardRemove()
        )
