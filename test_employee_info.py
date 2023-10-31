# Import the functions to be tested
from employee_info import get_employees_by_age_range, calculate_average_salary, get_employees_by_dept

# Sample employee data for testing (defined at the global level)
employee_data = [
    {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
    {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000},
    {"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000},
    {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}
]
# Test get_employees_by_age_range function
def test_get_employees_by_age_range():
    # Test case 1: Check employees within the age range 25-35
    result = get_employees_by_age_range(25, 35)
    expected = [
        {"name": "Chloe", "age": 35, "department": "Engineering", "salary": 70000},
        {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
        {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
        {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000},
    ]
    # Sort both result and expected for comparison
    result.sort(key=lambda x: x['name'])
    expected.sort(key=lambda x: x['name'])
    assert result == expected

# Test calculate_average_salary function
def test_calculate_average_salary():
    result = calculate_average_salary()
    expected = (50000 + 60000 + 56000 + 70000 + 65000 + 60000) / 6
    assert result == expected

# Test get_employees_by_dept function
def test_get_employees_by_dept():
    # Test case 1: Check employees in the Sales department
    result = get_employees_by_dept("Sales")
    expected = [{"name": "John", "age": 30, "department": "Sales", "salary": 50000},
        {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000},
]
    assert result == expected