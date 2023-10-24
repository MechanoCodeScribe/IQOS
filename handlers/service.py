from aiogram import Router, types, F
from keyboards.keyboards_collection import service_inkeyboard
from database.db_actions import db_check_user


router = Router()


@router.message(F.text == 'Сервис')
async def service(message: types.Message):
    """
        Handles the user's request for service and provides service options.

        Args:
            message (types.Message): The message object containing user information.
    """
    db_result = await db_check_user(message.from_user.id)
    if db_result:
        pass
    else:
        key = await service_inkeyboard()
        await message.answer('Замена испарителя и ĸартриджа', reply_markup=key)
        await message.answer('ПРОФЕССИОНАЛЬНО-БЕСПЛАТНО', reply_markup=types.ReplyKeyboardRemove())
