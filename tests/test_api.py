import configparser
import os

import annoworkapi

os.chdir(os.path.dirname(os.path.abspath(__file__)) + "/../")
inifile = configparser.ConfigParser()
inifile.read("./pytest.ini", "UTF-8")

organization_id = inifile["annowork"]["organization_id"]

service = annoworkapi.build()


class TestOrganization:
    def test_get_organization(self):
        organization = service.api.get_organization(organization_id)
        assert organization["organization_id"] == organization_id
