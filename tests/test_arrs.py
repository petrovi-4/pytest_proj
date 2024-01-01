from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]


def test_empty_list_slice():
    assert arrs.my_slice([], 0) == []


def test_start_is_none():
    assert arrs.my_slice([1, 2, 3], None) == [1, 2, 3]
    assert arrs.my_slice([1, 2, 3], None, 2) == [1, 2]
