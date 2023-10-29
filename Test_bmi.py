from Lab2 import bmi
import pytest

# Test for Normal Weight
def test_bmi_normal_weight():
    # BMI within the normal weight range
    result = bmi.calculate_bmi(weight=70, height=1.75)
    assert result == 0  # Expected result for normal weight

# Test for Over Weight
def test_bmi_over_weight():
    # BMI above the normal weight range
    result = bmi.calculate_bmi(weight=85, height=1.75)
    assert result == 1  # Expected result for over weight

# Test for Under Weight
def test_bmi_under_weight():
    # BMI below the normal weight range
    result = bmi.calculate_bmi(weight=50, height=1.75)
    assert result == -1  # Expected result for under weight