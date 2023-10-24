import re
from datetime import datetime


async def check_sex(text):
    """
        Check if the input text is a valid gender identifier.

        Args:
            text (str): The input text to check.

        Returns:
            bool: True if the input is 'м' (for male) or 'ж' (for female), False otherwise.
    """
    if text.lower() == 'м' or text.lower() == 'ж':
        return True
    else:
        return False


async def check_format(text):
    """
        Check if the input text has a valid date format (DD.MM.YYYY).

        Args:
            text (str): The input text to check.

        Returns:
            bool: True if the input text has a valid date format, False otherwise.
    """

    # Регулярное выражение для проверки формата ДД.ММ.ГГГГ
    date_pattern = r'^\d{2}\.\d{2}\.\d{4}$'
    if re.match(date_pattern, text):
        day, month, year = map(int, text.split('.'))
        if day < 1 or day > 31 or month < 1 or month > 12 or year < 1900:
            return False
        return True
    else:
        return False


async def check_age(text):
    """
        Check if the user is at least 18 years old based on their birthdate.

        Args:
            text (str): The user's birthdate in the format DD.MM.YYYY.

        Returns:
            bool: True if the user is at least 18 years old, False otherwise.
    """

    day, month, year = map(int, text.split('.'))

    current_date = datetime.now()

    age = current_date.year - year - ((current_date.month, current_date.day) < (month, day))

    return age >= 18