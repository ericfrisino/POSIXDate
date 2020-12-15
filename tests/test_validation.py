"""Run Tests against the validation methods.

Documentation for pytests can be found here: https://docs.pytest.org"""
import sys
sys.path.insert(0, '/Volumes/EMBR/Development/Software Development/Python/POSIXDate')
# Import testing framework.
import pytest
# Import file containing methods to test.
from validation import check_date, check_time


# Correctly formatted date
def test_check_date__correct():
    assert check_date("2020-10-10", True) == [True, '2020-10-10 00:00:00']


# Incorrectly formatted year.
def test_check_date__letter_in_year():
    assert check_date("20D0-10-10", True) == [False, False]


def test_check_date__year_3_digits():
    assert check_date("200-10-10", True) == [False, False]


def test_check_date__year_2_digits():
    assert check_date("20-10-10", True) == [False, False]


def test_check_date__year_1_digit():
    assert check_date("2-10-10", True) == [False, False]


def test_check_date__year_too_low():
    assert check_date("1960-10-10", True) == [False, False]


# Incorrectly formatted month.
def test_check_date__month_one_digit():
    assert check_date("2020-1-10", True) == [True, '2020-01-10 00:00:00']


def test_check_date__month_over_12():
    assert check_date("2020-37-10", True) == [False, False]


def test_check_date__month_as_zero():
    assert check_date("2020-0-10", True) == [False, False]


def test_check_date__month_with_letter():
    assert check_date("2020-1e-10", True) == [False, False]


def test_check_date__month_only_letters():
    assert check_date("2020-Rg-10", True) == [False, False]


def test_check_date__month_only_one_symbol():
    assert check_date("2020-/-10", True) == [False, False]


# Incorrectly formatted day
def test_check_date__day_one_digit():
    assert check_date("2020-10-1", True) == [True, '2020-10-01 00:00:00']


def test_check_date__day_aug_31():
    assert check_date("2020-08-31", True) == [True, '2020-08-31 00:00:00']


def test_check_date__day_with_letter():
    assert check_date("2020-08-1v", True) == [False, False]


def test_check_date__day_with_only_letters():
    assert check_date("2020-08-Pv", True) == [False, False]


def test_check_date__day_to_low():
    assert check_date("2020-08-0", True) == [False, False]


def test_check_date__day_to_high():
    assert check_date("2020-08-40", True) == [False, False]


def test_check_date__day_way_to_high():
    assert check_date("2020-08-490", True) == [False, False]


def test_check_date__not_even_close():
    assert check_date("This is how we do it!", True) == [False, False]


# Moving on... Checking time validation
def test_check_time__correct():
    assert check_time("10:15:45") == [True, '1900-01-01 10:15:45']


def test_check_time__wrong_time_sep():
    assert check_time("10-15-45") == [False, False]


def test_check_time__first_second():
    assert check_time("00:00:00") == [True, '1900-01-01 00:00:00']


def test_check_time__last_second():
    assert check_time("23:59:59") == [True, '1900-01-01 23:59:59']


def test_check_time__one_second_over():
    assert check_time("24:00:00") == [False, False]


def test_check_time__hour_letter():
    assert check_time("2G:59:59") == [False, False]


def test_check_time__minute_letter():
    assert check_time("21:l9:59") == [False, False]


def test_check_time__second_letter():
    assert check_time("21:59:5Z") == [False, False]


def test_check_time__anti_meridiem_a_lc():
    assert check_time("09:12:57 a") == [True, "1900-01-01 09:12:57"]


def test_check_time__anti_meridiem_a_uc():
    assert check_time("09:12:57 A") == [True, "1900-01-01 09:12:57"]


def test_check_time__anti_meridiem_am_lc():
    assert check_time("09:12:57 am") == [True, "1900-01-01 09:12:57"]


def test_check_time__anti_meridiem_am_uc():
    assert check_time("09:12:57 AM") == [True, "1900-01-01 09:12:57"]


def test_check_time__post_meridiem_p_lc():
    assert check_time("09:12:57 p") == [True, "1900-01-01 21:12:57"]


def test_check_time__post_meridiem_p_uc():
    assert check_time("09:12:57 P") == [True, "1900-01-01 21:12:57"]


def test_check_time__post_meridiem_pm_lc():
    assert check_time("09:12:57 pm") == [True, "1900-01-01 21:12:57"]


def test_check_time__post_meridiem_pm_uc():
    assert check_time("09:12:57 PM") == [True, "1900-01-01 21:12:57"]


def test_check_time__rand_meridiem():
    assert check_time("09:12:57 fE") == [True, "1900-01-01 09:12:57"]
