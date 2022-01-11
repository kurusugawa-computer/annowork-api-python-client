import more_itertools

from annoworkapi.schedule import create_schedules_daily

SCHEDULE_LIST = [
    {
        "job_id": "JOB_A",
        "organization_member_id": "alice",
        "start_date": "2021-11-01",
        "end_date": "2021-11-03",
        "type": "hours",
        "value": 8,
    },
    {
        "job_id": "JOB_A",
        "organization_member_id": "bob",
        "start_date": "2021-11-01",
        "end_date": "2021-11-03",
        "type": "percentage",
        "value": 50,
    },
]


EXPECTED_WORKING_HOURS_DICT = {
    ("2021-11-01", "bob"): 8,
    ("2021-11-03", "bob"): 6,
}


class Test_create_schedules_daily:
    def test_with_type_hours(self):
        actual = create_schedules_daily(SCHEDULE_LIST[0], {})
        assert len(actual) == 3

        assert (
            more_itertools.first_true(actual, pred=lambda e: e["date"] == "2021-11-01")["assigned_working_hours"] == 8.0
        )
        assert sum(e["assigned_working_hours"] for e in actual) == 8 * 3

    def test_with_type_percentage(self):
        actual = create_schedules_daily(SCHEDULE_LIST[1], EXPECTED_WORKING_HOURS_DICT)
        assert len(actual) == 2
        assert (
            more_itertools.first_true(actual, pred=lambda e: e["date"] == "2021-11-01")["assigned_working_hours"] == 4.0
        )
        assert sum(e["assigned_working_hours"] for e in actual) == 8 * 0.5 + 6 * 0.5

    def test_with_type_percentage2(self):
        actual = create_schedules_daily(SCHEDULE_LIST[1], {})
        assert len(actual) == 0
