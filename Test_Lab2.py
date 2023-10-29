import pytest
from exercise3 import find_min_max
from exercise3 import calc_average
from exercise6 import calc_median_temperature

# Test cases for find_min_max
def test_find_min_max():
    # Test case 1: Empty list
    assert find_min_max([]) == [None, None]

    # Test case 2: List with one element
    assert find_min_max([5.0]) == [5.0, 5.0]

    # Test case 3: List with multiple elements
    assert find_min_max([5.0, 2.5, 10.0, 0.5, 7.5]) == [0.5, 10.0]

# Test cases for calc_average
def test_calc_average():
    # Test case 1: Empty list
    assert calc_average([]) == None

    # Test case 2: List with one element
    assert calc_average([5.0]) == 5.0

    # Test case 3: List with multiple elements
    assert calc_average([5.0, 2.5, 10.0, 0.5, 7.5]) == 5.5

# Test cases for calc_median_temperature
def test_calc_median_temperature():
    # Test case 1: Empty list
    assert calc_median_temperature([]) == None

    # Test case 2: List with one element
    assert calc_median_temperature([5.0]) == 5.0

    # Test case 3: List with odd number of elements
    assert calc_median_temperature([5.0, 2.5, 10.0, 0.5, 7.5]) == 5.0

    # Test case 4: List with even number of elements
    assert calc_median_temperature([5.0, 2.5, 10.0, 0.5]) == 3.75

if __name__ == "__main":
    pytest.main()