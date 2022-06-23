from datetime import datetime

from app.repository.kvs_database import KVSDatabse
from tests.app.repository.test_data import test_data


def test_get_price() -> None:
    kvs_database = KVSDatabse()
    kvs_database.data = test_data
    expected = 50
    start_hour = datetime.strptime("17:00", '%H:%M')
    finish_hour = datetime.strptime("18:00", '%H:%M')
    result = kvs_database.get_price("TU", start_hour, finish_hour)

    assert expected == result
