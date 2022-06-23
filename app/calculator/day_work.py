from datetime import datetime

from app.repository.kvs_database import KVSDatabse
from app.utils.date_formater import to_date


class DayWork:
    def __init__(self, day_work: str) -> None:
        self.day = self.get_day(day_work)
        self.start_time = self.get_start_hour(day_work)
        self.finish_time = self.get_finish_hour(day_work)
        self.databse = KVSDatabse()

    def get_day(self, day_work: str) -> str:
        """
        get the day of the string. Ex: MO18:00-20:00 the day is MO

        :param day_work:
        :return: str: day
        """
        return day_work[:2]

    def get_start_hour(self, day_work: str) -> datetime:
        """
        from a string get the start hour. Ex: MO18:00-20:00 the start hour is 18:00

        :param day_work:
        :return: datetime
        """
        return to_date(day_work[2:].split("-")[0])

    def get_finish_hour(self, day_work: str) -> datetime:
        """
        from a string get the finish hour. Ex: MO18:00-20:00 the finish hour is 20:00

        :param day_work:
        :return: datetime
        """

        return to_date(day_work[2:].split("-")[1])

    def get_price(self) -> int:
        """
        get the price of the hour in the period of the start time and finish time

        :return: int: the price
        """
        return self.databse.get_price(self.day, self.start_time, self.finish_time)

    def get_total_hours(self) -> int:
        """
        get the quantity of hours between finish hour and start hour.

        :return: int: hours
        """
        hours = self.finish_time - self.start_time
        return hours.seconds//3600
