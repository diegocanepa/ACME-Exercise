from datetime import datetime


def to_date(date: str) -> datetime:
    """
    Returns a datetime from a string of the following structure HH:MM

    :param date:
    :return:
    """
    return datetime.strptime(date, '%H:%M')
