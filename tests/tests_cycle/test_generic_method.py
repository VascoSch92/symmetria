import pytest

from tests.test_factory import (
    validate_map,
    validate_sgn,
    validate_orbit,
    validate_order,
    validate_domain,
    validate_inverse,
    validate_support,
    validate_equivalent,
    validate_cycle_notation,
    validate_is_derangement,
)
from tests.tests_cycle.test_cases import (
    TEST_MAP,
    TEST_SGN,
    TEST_ORBIT,
    TEST_ORDER,
    TEST_DOMAIN,
    TEST_INVERSE,
    TEST_SUPPORT,
    TEST_ELEMENTS,
    TEST_EQUIVALENT,
    TEST_CYCLE_NOTATION,
    TEST_IS_DERANGEMENT,
)


@pytest.mark.parametrize(
    argnames="cycle, expected_value",
    argvalues=TEST_CYCLE_NOTATION,
    ids=[f"{cycle}.cycle_notation()={s}" for cycle, s in TEST_CYCLE_NOTATION],
)
def test_cycle_notation(cycle, expected_value) -> None:
    """Tests for the method `cycle_notation()`."""
    validate_cycle_notation(item=cycle, expected_value=expected_value)


@pytest.mark.parametrize(
    argnames="cycle, expected_value",
    argvalues=TEST_ELEMENTS,
    ids=[f"{cycle}.elements={e}" for cycle, e in TEST_ELEMENTS],
)
def test_elements(cycle, expected_value) -> None:
    """Tests for the property `elements`."""
    if cycle.elements != expected_value:
        raise ValueError(
            f"The expression `{cycle.__repr__()}.elements()` must evaluate {expected_value}, "
            f"but got {cycle.elements}."
        )


@pytest.mark.parametrize(
    argnames="lhs, rhs, expected_value",
    argvalues=TEST_EQUIVALENT,
    ids=[f"{lhs}.equivalent({rhs})" for lhs, rhs, _ in TEST_EQUIVALENT],
)
def test_equivalent(lhs, rhs, expected_value) -> None:
    """Tests for the method `equivalent()`."""
    validate_equivalent(lhs=lhs, rhs=rhs, expected_value=expected_value)


@pytest.mark.parametrize(
    argnames="cycle, expected_value",
    argvalues=TEST_DOMAIN,
    ids=[f"{p}.domain()={s}" for p, s in TEST_DOMAIN],
)
def test_domain(cycle, expected_value) -> None:
    """Tests for the property `domain`."""
    validate_domain(item=cycle, expected_value=expected_value)


@pytest.mark.parametrize(
    argnames="cycle, expected_value",
    argvalues=TEST_INVERSE,
    ids=[f"{cycle}.inverse()={s}" for cycle, s in TEST_INVERSE],
)
def test_inverse(cycle, expected_value) -> None:
    """Tests for the method `inverse()`."""
    validate_inverse(item=cycle, expected_value=expected_value)


@pytest.mark.parametrize(
    argnames="cycle, expected_value",
    argvalues=TEST_IS_DERANGEMENT,
    ids=[f"{cycle}.is_derangement()={s}" for cycle, s in TEST_IS_DERANGEMENT],
)
def test_is_derangement(cycle, expected_value) -> None:
    """Tests for the method `is_derangement()`."""
    validate_is_derangement(item=cycle, expected_value=expected_value)


@pytest.mark.parametrize(
    argnames="cycle, expected_value",
    argvalues=TEST_MAP,
    ids=[f"{p}.map()={m}" for p, m in TEST_MAP],
)
def test_map(cycle, expected_value) -> None:
    """Tests for the property `map`."""
    validate_map(item=cycle, expected_value=expected_value)


@pytest.mark.parametrize(
    argnames="cycle, item, expected_value",
    argvalues=TEST_ORBIT,
    ids=[f"{p.rep()}.orbit({i})" for p, i, _ in TEST_ORBIT],
)
def test_orbit(cycle, item, expected_value) -> None:
    """Tests for the method `orbit()`."""
    validate_orbit(element=cycle, item=item, expected_value=expected_value)


@pytest.mark.parametrize(
    argnames="cycle, expected_value",
    argvalues=TEST_ORDER,
    ids=[f"{p}.order()={o}" for p, o in TEST_ORDER],
)
def test_order(cycle, expected_value) -> None:
    """Tests for the method `order()`."""
    validate_order(item=cycle, expected_value=expected_value)


@pytest.mark.parametrize(
    argnames="cycle, expected_value",
    argvalues=TEST_SGN,
    ids=[f"{p}.sgn()={o}" for p, o in TEST_SGN],
)
def test_sgn(cycle, expected_value) -> None:
    """Tests for the method `sgn()`."""
    validate_sgn(item=cycle, expected_value=expected_value)


@pytest.mark.parametrize(
    argnames="cycle, expected_value",
    argvalues=TEST_SUPPORT,
    ids=[f"{p}.support()={o}" for p, o in TEST_SUPPORT],
)
def test_support(cycle, expected_value) -> None:
    """Tests for the method `support()`."""
    validate_support(item=cycle, expected_value=expected_value)
