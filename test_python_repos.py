import python_repos


def test_status_code():
    assert python_repos.r.status_code == 200


def test_total_count():
    assert python_repos.response_dict["total_count"] > 100
