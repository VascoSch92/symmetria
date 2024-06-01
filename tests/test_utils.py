from typing import Any

import pytest


def _check_values(expression: str, evaluation: Any, expected: Any) -> None:
    """
    Private method is used to compare two objects, and, in the case where they are different, it raises a
    valuer error, and it displays a descriptive error message.
    """
    if evaluation != expected:
        raise ValueError(f"The expression `{expression}` must evaluate {expected}, but got {evaluation}.")


@pytest.mark.parametrize(
    argnames="expression, evaluation, expected",
    argvalues=[
        ("test_1", 1, 1),
        ("test_2", "a", "a"),
        ("test_3", [], []),
        ("test_4", [1, 2, 3], [1, 2, 3]),
    ],
)
def test_check_value(expression, evaluation, expected) -> None:
    """Tests for method `_check_values`."""
    _check_values(expression=expression, evaluation=evaluation, expected=expected)


@pytest.mark.parametrize(
    argnames="expression, evaluation, expected, message",
    argvalues=[
        ("test_1", 1, 0, "The expression `test_1` must evaluate 0, but got 1."),
        ("test_2", "a", "b", "The expression `test_2` must evaluate b, but got a."),
        ("test_3", [], {}, r"The expression `test_3` must evaluate \{\}, but got \[\]."),
    ],
)
def test_check_value_raise_exception(expression, evaluation, expected, message) -> None:
    """Tests for method `_check_values`."""
    with pytest.raises(ValueError, match=message):
        _check_values(expression=expression, evaluation=evaluation, expected=expected)
