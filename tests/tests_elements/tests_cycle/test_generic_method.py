import pytest

from tests.test_utils import _check_values
from tests.tests_elements.tests_cycle.test_cases import (
    TEST_MAP,
    TEST_SGN,
    TEST_ORBIT,
    TEST_ORDER,
    TEST_DEGREE,
    TEST_DOMAIN,
    TEST_IS_ODD,
    TEST_INVERSE,
    TEST_IS_EVEN,
    TEST_SUPPORT,
    TEST_DESCRIBE,
    TEST_ELEMENTS,
    TEST_EQUIVALENT,
    TEST_INVERSIONS,
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
    _check_values(
        expression=f"{cycle.rep()}.cycle_notation()", evaluation=cycle.cycle_notation(), expected=expected_value
    )


@pytest.mark.parametrize(
    argnames="cycle, expected_value",
    argvalues=TEST_ELEMENTS,
    ids=[f"{cycle}.elements={e}" for cycle, e in TEST_ELEMENTS],
)
def test_elements(cycle, expected_value) -> None:
    """Tests for the property `elements`."""
    _check_values(
        expression=f"{cycle.__repr__()}.elements()",
        evaluation=cycle.elements,
        expected=expected_value,
    )


@pytest.mark.parametrize(
    argnames="lhs, rhs, expected_value",
    argvalues=TEST_EQUIVALENT,
    ids=[f"{lhs}.equivalent({rhs})" for lhs, rhs, _ in TEST_EQUIVALENT],
)
def test_equivalent(lhs, rhs, expected_value) -> None:
    """Tests for the method `equivalent()`."""
    _check_values(
        expression=f"{lhs.rep()}.equivalent({rhs.__repr__()})",
        evaluation=lhs.equivalent(other=rhs),
        expected=expected_value,
    )


@pytest.mark.parametrize(
    argnames="cycle, expected_value",
    argvalues=TEST_DEGREE,
    ids=[f"{c.rep()}.degree()={d}" for c, d in TEST_DEGREE],
)
def test_degree(cycle, expected_value) -> None:
    """Tests for the method `degree()`."""
    _check_values(expression=f"{cycle.rep()}.degree()", evaluation=cycle.degree(), expected=expected_value)


@pytest.mark.parametrize(
    argnames="cycle, expected_value",
    argvalues=TEST_DESCRIBE,
    ids=[f"{p}.describe()" for p, _ in TEST_DESCRIBE],
)
def test_describe(cycle, expected_value) -> None:
    """Tests for the property `describe`."""
    _check_values(expression=f"{cycle.rep()}.describe()", evaluation=cycle.describe(), expected=expected_value)


@pytest.mark.parametrize(
    argnames="cycle, expected_value",
    argvalues=TEST_DOMAIN,
    ids=[f"{p}.domain()={s}" for p, s in TEST_DOMAIN],
)
def test_domain(cycle, expected_value) -> None:
    """Tests for the property `domain`."""
    _check_values(expression=f"{cycle.rep()}.domain()", evaluation=cycle.domain, expected=expected_value)


@pytest.mark.parametrize(
    argnames="cycle, expected_value",
    argvalues=TEST_INVERSE,
    ids=[f"{cycle}.inverse()={s}" for cycle, s in TEST_INVERSE],
)
def test_inverse(cycle, expected_value) -> None:
    """Tests for the method `inverse()`."""
    _check_values(expression=f"{cycle.rep()}.inverse()", evaluation=cycle.inverse(), expected=expected_value)


@pytest.mark.parametrize(
    argnames="cycle, expected_value",
    argvalues=TEST_INVERSIONS,
    ids=[f"{cycle}.inversions()={s}" for cycle, s in TEST_INVERSIONS],
)
def test_inversions(cycle, expected_value) -> None:
    """Tests for the method `inversions()`."""
    _check_values(expression=f"{cycle.rep()}.inversions()", evaluation=cycle.inversions(), expected=expected_value)


@pytest.mark.parametrize(
    argnames="cycle, expected_value",
    argvalues=TEST_IS_DERANGEMENT,
    ids=[f"{cycle}.is_derangement()={s}" for cycle, s in TEST_IS_DERANGEMENT],
)
def test_is_derangement(cycle, expected_value) -> None:
    """Tests for the method `is_derangement()`."""
    _check_values(
        expression=f"{cycle.rep()}.is_derangement()", evaluation=cycle.is_derangement(), expected=expected_value
    )


@pytest.mark.parametrize(
    argnames="cycle, expected_value",
    argvalues=TEST_IS_EVEN,
    ids=[f"{cycle}.is_even()={s}" for cycle, s in TEST_IS_EVEN],
)
def test_is_even(cycle, expected_value) -> None:
    """Tests for the method `is_even()`."""
    _check_values(expression=f"{cycle.rep()}.is_even()", evaluation=cycle.is_even(), expected=expected_value)


@pytest.mark.parametrize(
    argnames="cycle, expected_value",
    argvalues=TEST_IS_ODD,
    ids=[f"{cycle}.is_odd()={s}" for cycle, s in TEST_IS_ODD],
)
def test_is_odd(cycle, expected_value) -> None:
    """Tests for the method `is_odd()`."""
    _check_values(expression=f"{cycle.rep()}.is_odd()", evaluation=cycle.is_odd(), expected=expected_value)


@pytest.mark.parametrize(
    argnames="cycle, expected_value",
    argvalues=TEST_MAP,
    ids=[f"{p}.map()={m}" for p, m in TEST_MAP],
)
def test_map(cycle, expected_value) -> None:
    """Tests for the property `map`."""
    _check_values(expression=f"{cycle.rep()}.map()", evaluation=cycle.map, expected=expected_value)


@pytest.mark.parametrize(
    argnames="cycle, item, expected_value",
    argvalues=TEST_ORBIT,
    ids=[f"{p.rep()}.orbit({i})" for p, i, _ in TEST_ORBIT],
)
def test_orbit(cycle, item, expected_value) -> None:
    """Tests for the method `orbit()`."""
    _check_values(expression=f"{cycle.rep()}.orbit({item})", evaluation=cycle.orbit(item=item), expected=expected_value)


@pytest.mark.parametrize(
    argnames="cycle, expected_value",
    argvalues=TEST_ORDER,
    ids=[f"{p}.order()={o}" for p, o in TEST_ORDER],
)
def test_order(cycle, expected_value) -> None:
    """Tests for the method `order()`."""
    _check_values(expression=f"{cycle.rep()}.order()", evaluation=cycle.order(), expected=expected_value)


@pytest.mark.parametrize(
    argnames="cycle, expected_value",
    argvalues=TEST_SGN,
    ids=[f"{p}.sgn()={o}" for p, o in TEST_SGN],
)
def test_sgn(cycle, expected_value) -> None:
    """Tests for the method `sgn()`."""
    _check_values(expression=f"{cycle.rep()}.sgn()", evaluation=cycle.sgn(), expected=expected_value)


@pytest.mark.parametrize(
    argnames="cycle, expected_value",
    argvalues=TEST_SUPPORT,
    ids=[f"{p}.support()={o}" for p, o in TEST_SUPPORT],
)
def test_support(cycle, expected_value) -> None:
    """Tests for the method `support()`."""
    _check_values(expression=f"{cycle.rep()}.support()", evaluation=cycle.support(), expected=expected_value)
