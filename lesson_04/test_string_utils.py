import pytest
from string_utils import StringUtils


string_utils = StringUtils()


# 1_capitalize
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


# 2_trim
def test_trim_positive():
    assert string_utils.trim("   skypro") == "skypro"
    assert string_utils.trim("  hello") == "hello"


def test_trim_negative():
    assert string_utils.trim("") == ""
    assert string_utils.trim("   ") == ""
    assert string_utils.trim("skypro") == "skypro"


# 3_contains
def test_contains_positive():
    assert string_utils.contains("SkyPro", "S") is True
    assert string_utils.contains("Hello World", " ") is True
    assert string_utils.contains("12345", "3") is True


def test_contains_negative():
    assert string_utils.contains("SkyPro", "U") is False
    assert string_utils.contains("", "a") is False
    assert string_utils.contains("test", "T") is False


# 4_delete_symbol
def test_delete_symbol_positive():
    assert string_utils.delete_symbol("SkyPro", "k") == "SyPro"
    assert string_utils.delete_symbol("SkyPro", "Pro") == "Sky"
    assert string_utils.delete_symbol("hello world", "o") == "hell wrld"


def test_delete_symbol_negative():
    assert string_utils.delete_symbol("SkyPro", "X") == "SkyPro"
    assert string_utils.delete_symbol("", "a") == ""
    assert string_utils.delete_symbol("   test   ", "e") == "   tst   "
