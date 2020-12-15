"""Run Tests against the validation methods.

Documentation for pytests can be found here: https://docs.pytest.org"""

# Import testing framework.
import pytest
# Import file containing methods to test.
import sys
sys.path.insert(0, '/Users/ericfrisino/PycharmProjects/POSIXDate/')
from helpers import check_meridiem, convert_to_24_hour_time


def test_check_meridiem_low_a():
    assert check_meridiem("a") == ["AM", "", ""]


def test_check_meridiem_cap_a():
    assert check_meridiem("A") == ["AM", "", ""]


def test_check_meridiem_low_am():
    assert check_meridiem("am") == ["AM", "", ""]


def test_check_meridiem_cap_am():
    assert check_meridiem("AM") == ["AM", "", ""]


def test_check_meridiem_low_p():
    assert check_meridiem("p") == ["PM", "", ""]


def test_check_meridiem_cap_p():
    assert check_meridiem("P") == ["PM", "", ""]


def test_check_meridiem_low_pm():
    assert check_meridiem("pm") == ["PM", "", ""]


def test_check_meridiem_cap_pm():
    assert check_meridiem("PM") == ["PM", "", ""]


def test_check_meridiem_fake():
    assert check_meridiem("Fake") == [False,
                                      "No recognized meridiem annotation used.",
                                      "Please use one of the following : a, A, am, AM, p, P, pm, or PM"]


def test_check_meridiem_maple():
    assert check_meridiem("Maple") == [False,
                                       "No recognized meridiem annotation used.",
                                       "Please use one of the following : a, A, am, AM, p, P, pm, or PM"]


def test_check_meridiem_amo():
    assert check_meridiem("AMO") == [False,
                                     "No recognized meridiem annotation used.",
                                     "Please use one of the following : a, A, am, AM, p, P, pm, or PM"]


def test_convert_to_24_hour_time__single_digit_hms():
    assert convert_to_24_hour_time("9:5:1") == "21:5:1"


def test_convert_to_24_hour_time__single_digit_h():
    assert convert_to_24_hour_time("9:15:00") == "21:15:00"


def test_convert_to_24_hour_time__double_digit_hms():
    assert convert_to_24_hour_time("09:02:06") == "21:02:06"


def test_convert_to_24_hour_time__post_meridiem():
    assert convert_to_24_hour_time("13:02:06") == "13:02:06"
