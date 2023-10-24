from aiogram import Router, types, F
from keyboards.keyboards_collection import yes_no_keyboard, add_item_keyboard, menu_keyboard, add_special_item_keyboard
from database.db_actions import db_check_user
from aiogram.fsm.context import FSMContext
from states.my_states import AddItemState
from aiogram.types import FSInputFile


router = Router()


@router.message(AddItemState.confirmed_input, F.text == 'Назад')
@router.message(F.text == "⚙️Мои устройства")
async def add_item(message: types.Message, state: FSMContext):
    """
        Handles adding an item to the user's profile.

        Args:
            message (types.Message): The message object containing user information.
            state (FSMContext): The finite state machine context.
    """
    db_result = await db_check_user(message.from_user.id)
    if db_result:
        pass
    else:
        await state.set_state(AddItemState.start_input)
        has_item = False
        if has_item:
            pass
        else:
            key = await yes_no_keyboard()
            await message.answer('Я не нашел в вашем профиле активных устройств. Давайте добавим устройство к вашему '
                                 'профилю?', reply_markup=key)
            await state.set_state(AddItemState.confirmed_input)


@router.message(AddItemState.list_items, F.text == 'Назад')
@router.message(AddItemState.confirmed_input, F.text == 'Да')
async def add_confirmed(message: types.Message):
    """
        Handles confirming the addition of an item to the user's profile.

        Args:
            message (types.Message): The message object containing user information.
    """
    key = await add_item_keyboard()
    await message.answer('Выберите модель устройства, которое вы бы хотели добавить к аккаунту', reply_markup=key)


@router.message(AddItemState.confirmed_input, F.text == 'Отправить фотографию кода с коробки')
async def send_photo(message: types.Message):
    """
        Handles sending a photo of the product code on the box.

        Args:
            message (types.Message): The message object containing user information.
    """
    key = await menu_keyboard()
    image_from_pc = FSInputFile("media/picture_2.jpg")
    result = await message.answer_photo(
        image_from_pc,
        caption="Пожалуйста, пришлите четкую фотографию кода с коробки (см. пример).\nРазмер файла должен быть не "
                "более 10 МБ",
        reply_markup=key
    )


@router.message(AddItemState.confirmed_input, F.text == 'Под-система')
@router.message(AddItemState.confirmed_input, F.text == 'Одноразовое устройство')
@router.message(AddItemState.confirmed_input, F.text == 'Иное устройство')
async def send_photo(message: types.Message, state: FSMContext):
    """
        Handles sending a photo of the product code on the box for different device types.

        Args:
            message (types.Message): The message object containing user information.
            state (FSMContext): The state context for managing the conversation.
    """
    key = await add_special_item_keyboard()
    await state.set_state(AddItemState.list_items)
    image_from_pc = FSInputFile("media/picture_2.jpg")
    result = await message.answer_photo(
        image_from_pc,
        caption="Пожалуйста, пришлите четкую фотографию кода с коробки (см. пример).\nРазмер файла должен быть не "
                "более 10 МБ",
        reply_markup=key
    )

