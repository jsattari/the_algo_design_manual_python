import pytest
from chp_1_intro_to_algo_design.chp_1_insertion_sort import insertion_sort


@pytest.mark.parametrize("arr, sorted_arr", [
    ([4, 6, 8, 1, 3, 7, 2, 9, 0, 5], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ([0, 9, 8, 7, 6, 5, 4, 3, 2, 1], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ([3, 65, 3, 22, 1], [1, 3, 3, 22, 65])
])
def test_insertion_sort(arr, sorted_arr):
    assert insertion_sort(arr) == sorted_arr
