from app.calculator.day_work import DayWork


class Calculator:
    def __init__(self, txt: str) -> None:
        self.name = self.get_name(txt)
        self.work_days = self.get_work_days(txt.split("=")[1])

    def get_work_days(self, days: str) -> list[DayWork]:
        """
        Transforms the strings of days worked to a list of DayWork objects

        :param days: int
        :return: list[DayWork]
        """

        list = []
        for day in self.split_time_work_by_days(days):
            list.append(DayWork(day))
        return list

    def get_name(self, txt: str) -> str:
        """
        from a string you get the name of the person.

        :param txt: str
        :return: str: name of person
        """
        return txt.split("=")[0]

    def split_time_work_by_days(self, txt: str) -> list[str]:
        """
        split the string with , as separator

        :param txt:
        :return: list[str] lists of strings
        """
        return txt.split(",")

    def calculate_amount(self) -> int:
        """
        calculated the salary of the person multiplying the number of hours by their respective value
        for each of the days worked.

        :return:
        """
        amount = 0
        for work_day in self.work_days:
            amount += work_day.get_total_hours() * work_day.get_price()

        return amount

