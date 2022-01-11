import datetime

import pytest

from annoworkapi.utils import datetime_to_str, str_to_datetime


class Test_str_to_datetime:
    def test_normal(self):
        actual = str_to_datetime("2021-04-01T01:23:45.678Z")
        expected = datetime.datetime(2021, 4, 1, 1, 23, 45, 678000, tzinfo=datetime.timezone.utc)
        assert actual == expected

    def test_with_microseconds(self):
        actual = str_to_datetime("2021-04-01T01:23:45.678123Z")
        expected = datetime.datetime(2021, 4, 1, 1, 23, 45, 678123, tzinfo=datetime.timezone.utc)
        assert actual == expected


class Test_datetime_to_str:
    def test_normal(self):
        dt = datetime.datetime(2021, 4, 1, 1, 23, 45, 678123, tzinfo=datetime.timezone.utc)
        actual = datetime_to_str(dt)
        expected = "2021-04-01T01:23:45.678Z"
        assert actual == expected

    def test_with_jtc(self):
        jtc_tzinfo = datetime.timezone(datetime.timedelta(hours=9))
        dt = datetime.datetime(2021, 4, 1, 1, 23, 45, 678123, tzinfo=jtc_tzinfo)
        actual = datetime_to_str(dt)
        expected = "2021-03-31T16:23:45.678Z"
        assert actual == expected

    def test_with_native_datetime_object(self):
        dt = datetime.datetime(2021, 4, 1, 1, 23, 45, 678123)
        with pytest.raises(ValueError):
            datetime_to_str(dt)
