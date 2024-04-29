import pytest

from tests.tests_cycle_decomposition.test_cases import (
    TEST_BOOL,
    TEST_EQ,
)
from tests.tests_factory import (
    validate_bool,
    validate_mul,
)


@pytest.mark.parametrize(
    argnames="cycle_decomposition, expected_value",
    argvalues=TEST_BOOL,
    ids=[f"bool({c})={b}" for c, b in TEST_BOOL]
)
def test_bool(cycle_decomposition, expected_value) -> None:
    """Tests for the method `__bool__()`."""
    validate_bool(item=cycle_decomposition, expected_value=expected_value)


@pytest.mark.parametrize(
    argnames="lhs, rhs, expected_value",
    argvalues=TEST_EQ,
    ids=[f"{lhs}={rhs}" for lhs, rhs, _ in TEST_EQ]
)
def test_eq(lhs, rhs, expected_value) -> None:
    """Tests for the method `__eq__()`."""
    validate_mul(lhs=lhs, rhs=rhs, expected_value=expected_value)
