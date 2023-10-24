from aiogram import Router, types, F
from database.db_actions import db_check_user
from keyboards.keyboards_collection import buy_keyboard, for_item_keyboard, one_time_item_keyboard, liquids_keyboard, \
    location_stores_keyboard
from aiogram.fsm.context import FSMContext
from states.my_states import ShowAddressesState

router = Router()


@router.message(ShowAddressesState.spec_item, F.text == 'Назад')
@router.message(F.text == 'Покупка')
async def buy(message: types.Message, state: FSMContext):
    """
        Handle the user's request to initiate a purchase.

        Args:
            message (types.Message): The message from the user.
            state (FSMContext): The current state of the conversation.
    """
    db_result = await db_check_user(message.from_user.id)
    if db_result:
        pass
    else:
        key = await buy_keyboard()
        await message.answer('Выберите, пожалуйста, что вы хотите купить', reply_markup=key)
        await state.set_state(ShowAddressesState.start_input)


@router.message(ShowAddressesState.start_input, F.text == 'Под-устройство')
async def for_items(message: types.Message, state: FSMContext):
    """
        Handle the user's choice to buy a sub-device.

        Args:
            message (types.Message): The message from the user.
            state (FSMContext): The current state of the conversation.
    """
    key = await for_item_keyboard()
    await message.answer('Выберите, пожалуйста, что вы хотите купить', reply_markup=key)
    await state.set_state(ShowAddressesState.spec_item)


@router.message(ShowAddressesState.start_input, F.text == 'Одноразовое устройство')
async def one_time_item(message: types.Message, state: FSMContext):
    """
        Handle the user's choice to buy a one-time use device.

        Args:
            message (types.Message): The message from the user.
            state (FSMContext): The current state of the conversation.
    """
    key = await one_time_item_keyboard()
    await message.answer('Выберите, пожалуйста, что вы хотите купить', reply_markup=key)
    await state.set_state(ShowAddressesState.spec_item)


@router.message(ShowAddressesState.start_input, F.text == 'Испарители и Катриджи')
async def smoke(message: types.Message, state: FSMContext):
    """
        Handle the user's choice to buy vaporizers and cartridges.

        Args:
            message (types.Message): The message from the user.
            state (FSMContext): The current state of the conversation.
    """
    key = await for_item_keyboard()
    await message.answer('Выберите, пожалуйста, что вы хотите купить', reply_markup=key)
    await state.set_state(ShowAddressesState.spec_item)


@router.message(ShowAddressesState.start_input, F.text == 'Жидкости')
async def liquids(message: types.Message, state: FSMContext):
    """
        Handle the user's choice to buy liquids.

        Args:
            message (types.Message): The message from the user.
            state (FSMContext): The current state of the conversation.
    """
    key = await liquids_keyboard()
    await message.answer('Выберите, пожалуйста, что вы хотите купить', reply_markup=key)
    await state.set_state(ShowAddressesState.spec_item)


@router.message(ShowAddressesState.spec_item, F.text == 'Brusko')
@router.message(ShowAddressesState.spec_item, F.text == 'Geek Vape')
@router.message(ShowAddressesState.spec_item, F.text == 'Smoant')
@router.message(ShowAddressesState.spec_item, F.text == 'Voopoo')
@router.message(ShowAddressesState.spec_item, F.text == 'Rinsoe')
@router.message(ShowAddressesState.spec_item, F.text == 'Иные')
@router.message(ShowAddressesState.spec_item, F.text == 'Vaporesso')
@router.message(ShowAddressesState.spec_item, F.text == 'Soak')
@router.message(ShowAddressesState.spec_item, F.text == 'UDN')
@router.message(ShowAddressesState.spec_item, F.text == 'PODONKI')
@router.message(ShowAddressesState.spec_item, F.text == 'MIST')
@router.message(ShowAddressesState.spec_item, F.text == 'Husky')
@router.message(ShowAddressesState.spec_item, F.text == 'Tikobar')
@router.message(ShowAddressesState.spec_item, F.text == 'Toyz')
@router.message(ShowAddressesState.spec_item, F.text == 'Duall')
@router.message(ShowAddressesState.spec_item, F.text == 'Podonki')
@router.message(ShowAddressesState.spec_item, F.text == 'Ataku')
@router.message(ShowAddressesState.spec_item, F.text == 'А че Нет')
async def request_location(message: types.Message):
    """
        Handle the user's choice to specify their location for store selection.

        Args:
            message (types.Message): The message from the user.
    """
    key = await location_stores_keyboard()
    await message.answer('Отлично!\nВведите ваш точный адрес в формате «город, улица, дом» или поделитесь '
                         'геопозицией, чтобы я смог найти ближайшие к вам магазины.', reply_markup=key.as_markup(
        resize_keyboard=True))
