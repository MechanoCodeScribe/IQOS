from aiogram import Router, types, F
from keyboards.keyboards_collection import show_orders_keyboard
from database.db_actions import db_check_user, find_orders_by_user_id


router = Router()


@router.message(F.text == "⏳Узнать статус заĸаза")
async def address(message: types.Message):
    """
        Handles the user's request to check the status of their order.

        Args:
            message (types.Message): The message object containing user information.
    """
    db_result = await db_check_user(message.from_user.id)
    if db_result:
        pass
    else:
        key = await show_orders_keyboard()
        orders = await find_orders_by_user_id(message)
        if orders:
            order_message = "Ваш заказ:\n\n"
            for order in orders:
                order_number, user_id, name, item, _ = order
                order_message += f"Намер заказа #{order_number}:\n"
                order_message += f"Имя: {name}\n"
                order_message += f"Устройство: {item}\n\n"

            await message.answer(order_message, reply_markup=key)
        else:
            await message.answer('Что-то я не могу найти ни один заказ по вашему номеру телефона 😔', reply_markup=key)

