from aiogram import Router, types, F
from keyboards.keyboards_collection import q_1, q_2, q_3, q_4, q_5
from database.db_actions import db_check_user


router = Router()


@router.message(F.text == "Пройти тест")
async def start_test(message: types.Message):
    """
        Handles the user's request to start a test and presents the first question.

        Args:
            message (types.Message): The incoming message object.

        Returns:
            None
    """
    db_result = await db_check_user(message.from_user.id)
    if db_result:
        pass
    else:
        key = await q_1()
        await message.answer("Вопрос 1. Выберите ответ:", reply_markup=key)


@router.message(F.text == "q1.Вариант 1")
async def test_1_1(message: types.Message):
    """
        Handles the user's response to the question.

        Args:
            message (types.Message): The incoming message object.

        Returns:
            None
    """
    db_result = await db_check_user(message.from_user.id)
    if db_result:
        pass
    else:
        key = await q_2()
        await message.answer("Верно!\nВопрос 2. Выберите ответ:", reply_markup=key)


@router.message(F.text == "q1.Вариант 2")
async def test_1_2(message: types.Message):
    """
            Handles the user's response to the question.

            Args:
                message (types.Message): The incoming message object.

            Returns:
                None
    """
    db_result = await db_check_user(message.from_user.id)
    if db_result:
        pass
    else:
        key = await q_2()
        await message.answer("Не верно!\nВопрос 2. Выберите ответ:", reply_markup=key)


@router.message(F.text == "q2.Вариант 1")
async def test_2_1(message: types.Message):
    """
            Handles the user's response to the question.

            Args:
                message (types.Message): The incoming message object.

            Returns:
                None
    """
    db_result = await db_check_user(message.from_user.id)
    if db_result:
        pass
    else:
        key = await q_3()
        await message.answer("Верно!\nВопрос 3. Выберите ответ:", reply_markup=key)


@router.message(F.text == "q2.Вариант 2")
async def test_2_2(message: types.Message):
    """
            Handles the user's response to the question.

            Args:
                message (types.Message): The incoming message object.

            Returns:
                None
    """
    db_result = await db_check_user(message.from_user.id)
    if db_result:
        pass
    else:
        key = await q_3()
        await message.answer("Не верно!\nВопрос 3. Выберите ответ:", reply_markup=key)


@router.message(F.text == "q3.Вариант 1")
async def test_3_1(message: types.Message):
    """
            Handles the user's response to the question.

            Args:
                message (types.Message): The incoming message object.

            Returns:
                None
    """
    db_result = await db_check_user(message.from_user.id)
    if db_result:
        pass
    else:
        key = await q_4()
        await message.answer("Верно!\nВопрос 4. Выберите ответ:", reply_markup=key)


@router.message(F.text == "q3.Вариант 2")
async def test_3_2(message: types.Message):
    """
            Handles the user's response to the question.

            Args:
                message (types.Message): The incoming message object.

            Returns:
                None
    """
    db_result = await db_check_user(message.from_user.id)
    if db_result:
        pass
    else:
        key = await q_4()
        await message.answer("Не верно!\nВопрос 4. Выберите ответ:", reply_markup=key)


@router.message(F.text == "q4.Вариант 1")
async def test_4_1(message: types.Message):
    """
            Handles the user's response to the question.

            Args:
                message (types.Message): The incoming message object.

            Returns:
                None
    """
    db_result = await db_check_user(message.from_user.id)
    if db_result:
        pass
    else:
        key = await q_5()
        await message.answer("Верно!\nВопрос 5. Выберите ответ:", reply_markup=key)


@router.message(F.text == "q4.Вариант 2")
async def test_4_2(message: types.Message):
    """
            Handles the user's response to the question.

            Args:
                message (types.Message): The incoming message object.

            Returns:
                None
     """
    db_result = await db_check_user(message.from_user.id)
    if db_result:
        pass
    else:
        key = await q_5()
        await message.answer("Не верно!\nВопрос 5. Выберите ответ:", reply_markup=key)


@router.message(F.text == "q5.Вариант 1")
async def test_5_1(message: types.Message):
    """
            Handles the user's response to the question.

            Args:
                message (types.Message): The incoming message object.

            Returns:
                None
    """
    db_result = await db_check_user(message.from_user.id)
    if db_result:
        pass
    else:
        await message.answer("Верно!\nПоздравляю! Тест пройден!", reply_markup=types.ReplyKeyboardRemove())


@router.message(F.text == "q5.Вариант 2")
async def test_5_2(message: types.Message):
    """
            Handles the user's response to the question.

            Args:
                message (types.Message): The incoming message object.

            Returns:
                None
    """
    db_result = await db_check_user(message.from_user.id)
    if db_result:
        pass
    else:
        await message.answer("Не верно!\nПоздравляю! Тест пройден!", reply_markup=types.ReplyKeyboardRemove())


