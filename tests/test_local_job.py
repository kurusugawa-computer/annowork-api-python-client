from annoworkapi.job import get_parent_job_id_from_job_tree


class Test_get_parent_job_id_from_job_tree:
    def test_normal(self):
        actual = get_parent_job_id_from_job_tree("org/foo/bar")
        excepted = "foo"
        assert actual == excepted

    def test_no_parent(self):
        actual = get_parent_job_id_from_job_tree("org/foo")
        assert actual is None

    def test_normal2(self):
        actual = get_parent_job_id_from_job_tree("org/foo/bar/buzz")
        excepted = "bar"
        assert actual == excepted
