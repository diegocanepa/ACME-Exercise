from datetime import datetime

import app.utils.date_formater
from app.calculator.day_work import DayWork


def test_day_work_create_class(work_day1_fixture):
    expected_day = 'MO'
    expected_start_hour = datetime.strptime("10:00", '%H:%M')
    expected_finish_hour = datetime.strptime("12:00", '%H:%M')
    assert work_day1_fixture.day == expected_day
    assert work_day1_fixture.start_time == expected_start_hour
    assert work_day1_fixture.finish_time == expected_finish_hour


def test_get_day(work_day1_fixture: DayWork) -> None:
    expected_day = 'MO'
    day = work_day1_fixture.get_day("MO10:00-12:00")
    assert day == expected_day


def test_get_start_hour(mocker: any, work_day1_fixture: DayWork) -> None:
    expected_start_hour = datetime.strptime("10:00", '%H:%M')
    mocker.patch("app.utils.date_formater.to_date", return_value=datetime.strptime("10:00", '%H:%M'))
    start_hour = work_day1_fixture.get_start_hour("MO10:00-12:00")
    assert start_hour == expected_start_hour


def test_finish_hour(mocker: any, work_day1_fixture: DayWork) -> None:
    expected_finish_hour = datetime.strptime("12:00", '%H:%M')
    mocker.patch("app.utils.date_formater.to_date", return_value=datetime.strptime("12:00", '%H:%M'))
    finish_hour = work_day1_fixture.get_finish_hour("MO12:00-12:00")
    assert finish_hour == expected_finish_hour
