import pytest
from yellow_algorithm.implementations import binary_search


first_ten_list = list(range(10))


@pytest.mark.parametrize(
    "array, element, expected",
    [(first_ten_list, el, el) for el in range(10)] + [(first_ten_list, 10, None)],
)
def test_binary_search(array, element, expected):
    """Test that sorting functions correctly sort various lists."""
    assert binary_search(array, element) == expected
