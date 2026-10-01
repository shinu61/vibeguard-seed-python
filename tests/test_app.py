from app import add, fingerprint, http_pool, is_py3, normalize_url, square_all


def test_add():
    assert add(2, 3) == 5


def test_normalize_url():
    assert normalize_url("  https://Example.com  ") == "https://example.com"


def test_is_py3():
    assert is_py3() is True


def test_http_pool_created():
    assert http_pool() is not None


def test_fingerprint_is_stable():
    assert fingerprint([1, 2, 3]) == fingerprint([1, 2, 3])
    assert fingerprint([1, 2, 3]) != fingerprint([3, 2, 1])


def test_square_all():
    assert square_all([1, 2, 3]) == [1, 4, 9]
