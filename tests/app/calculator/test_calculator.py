from app.calculator.calculator import Calculator
from app.calculator.day_work import DayWork


def test_get_name(calculator_fixture: Calculator) -> None:
    expected = "RENE"
    result = calculator_fixture.get_name("RENE=MO10:00-12:00,TU10:00-12:00")

    assert result == expected


def test_split_time_work_by_days(calculator_fixture: Calculator) -> None:
    expected = ["MO10:00-12:00", "TU10:00-12:00"]
    result = calculator_fixture.split_time_work_by_days("MO10:00-12:00,TU10:00-12:00")

    assert result == expected


def test_get_work_days(mocker: any,
                       calculator_fixture: Calculator,
                       work_day1_fixture: DayWork,
                       work_day2_fixture: DayWork) -> None:
    expected = [work_day1_fixture, work_day2_fixture]
    mocker.patch.object(Calculator, "split_time_work_by_days", side_effect=["MO10:00-12:00", "TU10:00-12:00"])
    result = calculator_fixture.get_work_days("MO10:00-12:00,TU10:00-12:00")

    assert result[0].day == expected[0].day


def test_get_work_days(mocker: any,
                       calculator_fixture: Calculator) -> None:
    expected = 70
    mocker.patch.object(DayWork, "get_total_hours", side_effect=[2, 3])
    mocker.patch.object(DayWork, "get_price", side_effect=[20, 10])
    result = calculator_fixture.calculate_amount()

    assert result == expected
