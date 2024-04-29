
import pytest
from tests.tests_cycle.test_cases import (
    TEST_IS_DERANGEMENT,
    TEST_ORDER,
)

from tests.tests_factory import (
    validate_is_derangement,
    validate_order,
)


@pytest.mark.parametrize(
    argnames="cycle, expected_value",
    argvalues=TEST_IS_DERANGEMENT,
    ids=[f"{cycle}" for cycle, s in TEST_IS_DERANGEMENT]
)
def test_is_derangement(cycle, expected_value) -> None:
    """Tests for the method `is_derangement()`."""
    validate_is_derangement(item=cycle, expected_value=expected_value)


@pytest.mark.parametrize(
    argnames="cycle, expected_value",
    argvalues=TEST_ORDER,
    ids=[f"Order of {p} is {o}" for p, o in TEST_ORDER]
)
def test_order(cycle, expected_value) -> None:
    """Tests for the method `order()`."""
    validate_order(item=cycle, expected_value=expected_value)