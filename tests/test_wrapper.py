import configparser
import datetime
import os

import annoworkapi

os.chdir(os.path.dirname(os.path.abspath(__file__)) + "/../")
inifile = configparser.ConfigParser()
inifile.read("./pytest.ini", "UTF-8")

workspace_id = inifile["annowork"]["workspace_id"]

service = annoworkapi.build()


class TestActualWorkingTime:
    jtc_tzinfo = datetime.timezone(datetime.timedelta(hours=9))

    def test_get_actual_working_times_daily(self):
        tmp = service.wrapper.get_actual_working_times_daily(
            workspace_id, term_start_date="2021-11-15", term_end_date="2021-11-15", tzinfo=self.jtc_tzinfo
        )

    def test_get_actual_working_times_by_workspace_member_daily(self):
        print(f"{workspace_id=}")
        tmp = service.wrapper.get_actual_working_times_by_workspace_member_daily(
            workspace_id,
            "c566151e-f8bb-4f73-9c78-af40da1814ef",
            term_start_date="2021-11-15",
            term_end_date="2021-11-16",
            tzinfo=self.jtc_tzinfo,
        )


class TestSchedule:
    def test_get_schedules_daily(self):
        tmp = service.wrapper.get_schedules_daily(
            workspace_id,
            term_start="2021-11-15",
            term_end="2021-11-15",
            job_id="4ec6c1cf-84ed-4e28-8074-491dbce64599",
        )
