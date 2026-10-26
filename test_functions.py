
import pytest

from calculator import add, subtract, multiply, divide
from user_utils import normalize_username, is_valid_email
from file_utils import get_extension


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 3) == 2


def test_multiply():
    assert multiply(3, 4) == 12


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)


def test_normalize_username():
    assert normalize_username(" Surendra ") == "surendra"


def test_valid_email():
    assert is_valid_email("user@example.com") is True


def test_invalid_email():
    assert is_valid_email("invalid-email") is False


def test_get_extension():
    assert get_extension("report.pdf") == "pdf"


def test_filename_without_extension():
    assert get_extension("README") == ""
