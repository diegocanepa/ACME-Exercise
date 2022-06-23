import pytest

from app.calculator.calculator import Calculator
from app.calculator.day_work import DayWork


@pytest.fixture()
def calculator_fixture():
    return Calculator("RENE=MO10:00-12:00,TU10:00-12:00")


@pytest.fixture()
def work_day1_fixture():
    return DayWork("MO10:00-12:00")


@pytest.fixture()
def work_day2_fixture():
    return DayWork("TU10:00-12:00")
