from aiogram.fsm.state import StatesGroup, State


class GetDataState(StatesGroup):
    phone_input = State()
    name_input = State()
    surname_input = State()
    sex_input = State()
    birthday_input = State()


class GetOrderState(StatesGroup):
    birthday_input = State()
    exit_input = State()
    name_input = State()
    city_input = State()
    item_input = State()
    address_input = State()


class AddItemState(StatesGroup):
    start_input = State()
    confirmed_input = State()
    list_items = State()


class ShowAddressesState(StatesGroup):
    start_input = State()
    spec_item = State()
    final = State()


class GuideState(StatesGroup):
    start_input = State()



