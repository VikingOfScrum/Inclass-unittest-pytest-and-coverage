import pytest
from joseph_hanson_hw1 import print_if_leap

@pytest.mark.parametrize("year, expected", [
    (1804, True),
    (1908, True),
    (1884, True),
    (2012, True),
    (1803, False),
    (1909, False),
    (1885, False),
    (2013, False),
])

def test_loop_for_print_if_leap(year, expected):
    result = print_if_leap(year)
    assert result == expected