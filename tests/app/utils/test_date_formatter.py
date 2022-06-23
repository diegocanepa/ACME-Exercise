from datetime import datetime

from app.utils.date_formater import to_date


def test_to_date() -> None:
    expected = datetime.strptime("10:00", '%H:%M')
    assert expected == to_date("10:00")
