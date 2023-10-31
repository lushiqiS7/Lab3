import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending():
    # Test for sorting in ascending order
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [11, 12, 22, 25, 34, 64, 90]
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
    assert result == test_arr  # Expecting sorted ascending order as per REQ-01

def test_bubble_sort_descending():
    # Test for sorting in descending order
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [90, 64, 34, 25, 22, 12, 11]
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)
    assert result == test_arr  # Expecting sorted descending order as per REQ-02

def test_bubble_sort_more_than_10():
    # Test for more than 10 numbers
    input_arr = [64, 34, 25, 12, 22, 11, 90, 55, 33, 45, 99, 87]
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
    assert result == 1  # Expecting 1 as per REQ-03

def test_bubble_sort_no_numbers():
    # Test for 0 numbers
    input_arr = []
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)
    assert result == 0  # Expecting 0 as per REQ-04

def test_bubble_sort_non_integer():
    # Test for non-integer values
    input_arr = [64, 34, 25, 12, "string", 11, 90]
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
    assert result == 2  # Expecting 2 as per REQ-5

def test_bubble_sort_invalid():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]

    result = Lab3.bubble_sort(input_arr, 3)

    assert (result == [])