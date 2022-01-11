from annoworkapi.annofab import get_annofab_project_id_from_url


class Test_get_annofab_project_id_from_url:
    def test_url(self):
        actual = get_annofab_project_id_from_url("https://annofab.com/projects/bar")
        excepted = "bar"
        assert actual == excepted

    def test_url_with_trailing_slash(self):
        actual = get_annofab_project_id_from_url("https://annofab.com/projects/bar/")
        excepted = "bar"
        assert actual == excepted
