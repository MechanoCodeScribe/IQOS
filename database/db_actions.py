import sqlite3 as sq


async def db_start():
    """
    Initialize the database connection and creates tables if they don't exist.

    Args:
        None

    Returns:
        None
    """
    global db, cur
    db = sq.connect('user_base.db')
    cur = db.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS profile (user_id INTEGER PRIMARY KEY, name TEXT, surname TEXT, sex TEXT, "
                "phone TEXT, birthday TEXT)")
    cur.execute(
        "CREATE TABLE IF NOT EXISTS orders (number INTEGER, user_id INTEGER, name TEXT, "
        "item TEXT, location TEXT)")
    db.commit()


async def db_check_user(user_id):
    """
        Check if a user with the given user_id exists in the database.

        Args:
            user_id (int): The user ID to check.

        Returns:
            bool: True if the user does not exist in the database, False otherwise.
        """
    global db, cur

    db = sq.connect('user_base.db')
    cur = db.cursor()

    cur.execute("SELECT * FROM profile WHERE user_id = ?", (user_id,))
    user_data = cur.fetchone()
    # Если пользователь не найден, добавляем его и возвращаем True
    if user_data is None:
        return True
    else:
        return False


async def add_user_to_db(message, user_data):
    """
        Add user information to the SQLite database.

        Args:
            message (types.Message): The message from the user.
            user_data (dict): User information to be added to the database.

        Returns:
            None
    """
    global db, cur

    db = sq.connect('user_base.db')
    cur = db.cursor()

    phone = user_data.get('phone', '')
    name = user_data.get('name', '')
    surname = user_data.get('surname', '')
    sex = user_data.get('sex', '')
    birthday = user_data.get('birthday', '')
    user_id = message.from_user.id

    cur.execute("INSERT INTO profile (user_id, phone, name, surname, sex, birthday) VALUES (?, ?, ?, ?, ?, ?)", (user_id, phone, name, surname, sex, birthday))
    db.commit()


async def add_order_to_db(message, user_data):
    """
        Add an order to the SQLite database.

        Args:
            message (types.Message): The message from the user.
            user_data (dict): User data containing order information.

        Returns:
            None
    """

    global db, cur

    db = sq.connect('user_base.db')
    cur = db.cursor()

    name = user_data.get('name', '')
    item = user_data.get('item', '')
    cur.execute("SELECT COUNT(*) FROM orders")
    result = cur.fetchone()
    number = result[0] + 1
    location = user_data.get('address', '')
    user_id = message.from_user.id

    cur.execute("INSERT INTO orders (number, user_id, name, item, location) VALUES (?, ?, ?, ?, ?)", (number, user_id, name, item, location))
    db.commit()


async def find_orders_by_user_id(message):
    """
        Find orders for a specific user in the SQLite database.

        Args:
            message (types.Message): The message from the user.

        Returns:
            list: A list of orders for the user.
    """
    global db, cur
    user_id = message.from_user.id
    db = sq.connect('user_base.db')
    cur = db.cursor()

    cur.execute("SELECT * FROM orders WHERE user_id=?", (user_id,))
    orders = cur.fetchall()
    print(orders)

    return orders


