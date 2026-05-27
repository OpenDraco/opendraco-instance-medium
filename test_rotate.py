from rotate import rotate_left


def test_rotate_basic():
    assert rotate_left([1, 2, 3, 4, 5], 2) == [3, 4, 5, 1, 2]


def test_rotate_zero():
    assert rotate_left([1, 2, 3], 0) == [1, 2, 3]


def test_rotate_empty():
    assert rotate_left([], 5) == []


def test_rotate_n_equals_len():
    assert rotate_left([1, 2, 3], 3) == [1, 2, 3]


def test_rotate_n_greater_than_len():
    assert rotate_left([1, 2, 3], 5) == [2, 3, 1]
