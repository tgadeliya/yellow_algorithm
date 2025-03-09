import pytest
from yellow_algorithm.implementations import (
    merge_sort,
    selection_sort,
    insertion_sort,
    counting_sort,
    direct_access_aray_sort,
    tuple_sort,
    radix_sort,
)


# Test cases
@pytest.mark.parametrize(
    "sorting_function", [selection_sort, merge_sort, insertion_sort]
)
@pytest.mark.parametrize(
    "input_list, expected",
    [
        ([4, 3, 2, 1], [1, 2, 3, 4]),
        ([3, 1, 4, 1, 5, 9], [1, 1, 3, 4, 5, 9]),
        ([10, -1, 2, 5, 0, 6], [-1, 0, 2, 5, 6, 10]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([], []),
        ([1], [1]),
        ([2, 2, 2], [2, 2, 2]),
        ([9, 9, 9, 8, 8, 8], [8, 8, 8, 9, 9, 9]),
    ],
)
def test_all_sorting(sorting_function, input_list, expected):
    """Test that sorting functions correctly sort various lists."""
    inp_list = [x for x in input_list]
    sorting_function(inp_list)
    assert inp_list == expected


# Test cases
@pytest.mark.parametrize("sorting_function", [counting_sort])
@pytest.mark.parametrize(
    "input_list, expected",
    [
        ([3, 1, 4, 1, 5, 9], [1, 1, 3, 4, 5, 9]),
        ([9, 9, 9, 8, 8, 8], [8, 8, 8, 9, 9, 9]),
    ],
)
def test_dupl_sorting(sorting_function, input_list, expected):
    inp_list = [x for x in input_list]
    sorting_function(inp_list)
    assert inp_list == expected


# Test cases
@pytest.mark.parametrize("sorting_function", [direct_access_aray_sort, radix_sort])
@pytest.mark.parametrize("input_list, expected", [([4, 3, 2, 1], [1, 2, 3, 4])])
def test_unique_sorting(sorting_function, input_list, expected):
    """Test that sorting functions correctly sort various lists."""
    inp_list = [x for x in input_list]
    sorting_function(inp_list)
    assert inp_list == expected


# Test cases
@pytest.mark.parametrize("sorting_function", [tuple_sort])
@pytest.mark.parametrize(
    "input_list, expected",
    [
        ([(4,), (3,), (2,), (1,)], [(1,), (2,), (3,), (4,)]),
        (
            [(1, 3, 4), (1, 4, 3), (2, 8, 1), (1, 0, 7)],
            [(1, 0, 7), (1, 3, 4), (1, 4, 3), (2, 8, 1)],
        ),
    ],
)
def test_tuple_sorting(sorting_function, input_list, expected):
    """Test that sorting functions correctly sort various lists."""
    inp_list = [x for x in input_list]
    sorting_function(inp_list)
    assert inp_list == expected
