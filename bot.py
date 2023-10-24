import asyncio
import logging
from loader import bot
from handlers import start, petpo_club, about_us, ask_question, create_order, order_request, get_addresses, stores, buy, guide, to_know, service, why_us, what_for_us, be_expert, test, social, show_orders, show_items, fix, another_question, unknown
from get_data import data_request
from aiogram import Dispatcher
from database.db_actions import db_start
from utils.set_bot_commands import set_default_commands


async def main() -> None:
    """
        Main function to start the bot.

        Returns:
            None
    """

    dp = Dispatcher()
    await set_default_commands()

    dp.include_router(start.router)
    dp.include_router(data_request.router)
    dp.include_router(petpo_club.router)
    dp.include_router(about_us.router)
    dp.include_router(ask_question.router)
    dp.include_router(create_order.router)
    dp.include_router(order_request.router)
    dp.include_router(get_addresses.router)
    dp.include_router(stores.router)
    dp.include_router(buy.router)
    dp.include_router(guide.router)
    dp.include_router(to_know.router)
    dp.include_router(service.router)
    dp.include_router(why_us.router)
    dp.include_router(what_for_us.router)
    dp.include_router(show_orders.router)
    dp.include_router(be_expert.router)
    dp.include_router(test.router)
    dp.include_router(social.router)
    dp.include_router(show_items.router)
    dp.include_router(fix.router)
    dp.include_router(another_question.router)
    dp.include_router(unknown.router)

    logging.basicConfig(filename='info.log', level=logging.INFO, encoding='utf-8')
    error_handler = logging.FileHandler('errors.log', encoding='utf-8')
    error_handler.setLevel(logging.ERROR)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    error_handler.setFormatter(formatter)
    logging.getLogger().addHandler(error_handler)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(console_formatter)
    logging.getLogger().addHandler(console_handler)

    await db_start()

    # Delete any pending updates from the webhook
    await bot.delete_webhook(drop_pending_updates=True)

    # Start polling for updates using the dispatcher
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
