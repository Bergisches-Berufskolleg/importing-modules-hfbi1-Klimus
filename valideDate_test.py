import pytest
from leapYear import isLeapYear
from valideDate import validateDate

@pytest.mark.parametrize("year, expected", [
    (2020, True),  # Leap year
    (2000, True),  # Leap year (divisible by 400)
    (2100, False), # Not a leap year (divisible by 100 but not 400)
    (2021, False), # Not a leap year
    (1900, False), # Not a leap year (divisible by 100 but not 400)
    (1600, True),  # Leap year (divisible by 400)
])
def test_isleapYear(year, expected):
    assert isLeapYear(year) == expected, f"{year} ist ein Schaltjahr: {expected}"

@pytest.mark.parametrize("day, month, year, expected", [
    (29, 2, 2020, True),  # Leap year, valid date
    (29, 2, 2000, True),  # Leap year, valid date
    (29, 2, 2100, False), # Not a leap year, invalid date
    (29, 2, 2025, False), # Not a leap year, invalid date
    (29, 2, 2021, False), # Non-leap year, invalid date
    (31, 4, 2021, False), # April has only 30 days
    (31, 12, 2021, True), # Valid date
    (0, 1, 2021, False),  # Day cannot be 0
    (1, 0, 2021, False),  # Month cannot be 0
    (1, 13, 2021, False), # Month cannot be greater than 12
    (15, 6, 2021, True),  # Valid date
    (31, 1, 2021, True),  # Valid date
    (30, 2, 2020, False), # February never has 30 days
    (-1, 1, 2021, False), # Negative day
    (1, -1, 2021, False), # Negative month
    (0, 0, 0, False),     # All values zero
    (31, 6, 2021, False), # June has only 30 days
    (31, 11, 2021, False),# November has only 30 days
    (28, 2, 2021, True),  # Non-leap year, valid February date
    (29, 2, 2024, True),  # Leap year, valid February date
])
def test_validateDate(day, month, year, expected):
    assert validateDate(day, month, year) == expected, f"Datum: {day}/{month}/{year} ist gültig: {expected}"
