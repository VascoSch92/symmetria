import pytest

from tests.test_factory import (
    validate_map,
    validate_orbit,
    validate_order,
    validate_support,
    validate_equivalent,
    validate_cycle_notation,
    validate_is_derangement,
    validate_cycle_decomposition,
)
from tests.tests_cycle_decomposition.test_cases import (
    TEST_MAP,
    TEST_ORBIT,
    TEST_ORDER,
    TEST_SUPPORT,
    TEST_EQUIVALENT,
    TEST_CYCLE_NOTATION,
    TEST_IS_DERANGEMENT,
    TEST_CYCLE_DECOMPOSITION,
)


@pytest.mark.parametrize(
    argnames="cycle_decomposition, expected_value",
    argvalues=TEST_CYCLE_DECOMPOSITION,
    ids=[f"{p.__repr__()}.cycle_notation()={c}" for p, c in TEST_CYCLE_DECOMPOSITION],
)
def test_cycle_decomposition(cycle_decomposition, expected_value) -> None:
    """Tests for the method `cycle_decomposition()`."""
    validate_cycle_decomposition(item=cycle_decomposition, expected_value=expected_value)


@pytest.mark.parametrize(
    argnames="cycle_decomposition, expected_value",
    argvalues=TEST_CYCLE_NOTATION,
    ids=[f"{c}.cycle_notation()={s}" for c, s in TEST_CYCLE_NOTATION],
)
def test_cycle_notation(cycle_decomposition, expected_value) -> None:
    """Tests for the method `cycle_notation()`."""
    validate_cycle_notation(item=cycle_decomposition, expected_value=expected_value)


@pytest.mark.parametrize(
    argnames="cycle_decomposition, expected_value",
    argvalues=TEST_IS_DERANGEMENT,
    ids=[f"{cycle}.is_derangement()={s}" for cycle, s in TEST_IS_DERANGEMENT],
)
def test_is_derangement(cycle_decomposition, expected_value) -> None:
    """Tests for the method `is_derangement()`."""
    validate_is_derangement(item=cycle_decomposition, expected_value=expected_value)


@pytest.mark.parametrize(
    argnames="lhs, rhs, expected_value",
    argvalues=TEST_EQUIVALENT,
    ids=[f"{lhs}.equivalent({rhs})" for lhs, rhs, _ in TEST_EQUIVALENT],
)
def test_equivalent(lhs, rhs, expected_value) -> None:
    """Tests for the method `equivalent()`."""
    validate_equivalent(lhs=lhs, rhs=rhs, expected_value=expected_value)


@pytest.mark.parametrize(
    argnames="cycle_decomposition, expected_value",
    argvalues=TEST_MAP,
    ids=[f"{p}.map()={m}" for p, m in TEST_MAP],
)
def test_map(cycle_decomposition, expected_value) -> None:
    """Tests for the method `map()`."""
    validate_map(item=cycle_decomposition, expected_value=expected_value)


@pytest.mark.parametrize(
    argnames="cycle, item, expected_value",
    argvalues=TEST_ORBIT,
    ids=[f"{p.rep()}.orbit({i})" for p, i, _ in TEST_ORBIT],
)
def test_orbit(cycle, item, expected_value) -> None:
    """Tests for the method `orbit()`."""
    validate_orbit(element=cycle, item=item, expected_value=expected_value)


@pytest.mark.parametrize(
    argnames="cycle_decomposition, expected_value",
    argvalues=TEST_ORDER,
    ids=[f"{p}.order()={o}" for p, o in TEST_ORDER],
)
def test_order(cycle_decomposition, expected_value) -> None:
    """Tests for the method `order()`."""
    validate_order(item=cycle_decomposition, expected_value=expected_value)


@pytest.mark.parametrize(
    argnames="cycle_decomposition, expected_value",
    argvalues=TEST_SUPPORT,
    ids=[f"{p}.support()={o}" for p, o in TEST_SUPPORT],
)
def test_support(cycle_decomposition, expected_value) -> None:
    """Tests for the method `support()`."""
    validate_support(item=cycle_decomposition, expected_value=expected_value)
