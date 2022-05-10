import configparser
import os

import annoworkapi

os.chdir(os.path.dirname(os.path.abspath(__file__)) + "/../")
inifile = configparser.ConfigParser()
inifile.read("./pytest.ini", "UTF-8")

workspace_id = inifile["annowork"]["workspace_id"]

service = annoworkapi.build()


class Testworkspace:
    def test_get_workspace(self):
        workspace = service.api.get_workspace(workspace_id)
        assert workspace["workspace_id"] == workspace_id
