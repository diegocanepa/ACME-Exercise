from datetime import datetime

from app.repository.data import data
from app.utils.date_formater import to_date


class KVSDatabse:
    def __init__(self) -> None:
        self.data = data

    def get_price(self, day: str, start_time: datetime, finish_time: datetime) -> int:
        """
        Returns the price of the hour taking into account the day, the start time and the end time

        :param day:
        :param start_time:
        :param finish_time:
        :return: int: the price
        """
        for prices in self.data.get(day):
            if start_time >= to_date(prices.get("start_hour")) and (finish_time <= to_date(prices.get("finish_hour"))
                                                                    or prices.get("finish_hour") == "00:00"):
                return prices.get("price")
