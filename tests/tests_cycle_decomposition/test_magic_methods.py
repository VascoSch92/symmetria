import pytest
from tests.tests_cycle_decomposition.test_cases import (
    TEST_BOOL,
    TEST_EQ,
)
from tests.utils import error_message


@pytest.mark.parametrize(
    argnames="cycle_decomposition, expected_output",
    argvalues=TEST_BOOL,
    ids=[f"bool({c})={b}" for c, b in TEST_BOOL]
)
def test_bool(cycle_decomposition, expected_output) -> None:
    """Tests for the method `__bool__()`."""
    if bool(cycle_decomposition) != expected_output:
        raise ValueError(error_message(expected=expected_output, got=bool(cycle_decomposition)))


@pytest.mark.parametrize(
    argnames="lhs, rhs, expected_output",
    argvalues=TEST_EQ,
    ids=[f"{lhs}={rhs}" for lhs, rhs, _ in TEST_EQ]
)
def test_eq(lhs, rhs, expected_output) -> None:
    """Tests for the method `__eq__()`."""
    if (lhs == rhs) != expected_output:
        raise ValueError(
            f"The expression `{lhs}=={rhs}` should be {expected_output}, but got {lhs == rhs}."
        )