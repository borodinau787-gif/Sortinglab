import pytest
from main import bubble_sort, binary_insertion_sort

@pytest.mark.parametrize("func", [bubble_sort, binary_insertion_sort])
@pytest.mark.parametrize("data, expected", [
    ([64, 34, 11], [11, 34, 64]), ([], []), ([1], [1]), ([3, -1, 0], [-1, 0, 3]), ([5, 2, 2], [2, 2, 5])
])
def test_sorts(func, data, expected):
    assert func(data.copy()) == expected