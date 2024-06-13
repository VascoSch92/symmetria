import pytest

from tests.test_utils import _check_values
from tests.tests_elements.tests_cycle_decomposition.test_cases import (
    TEST_MAP,
    TEST_SGN,
    TEST_ORBIT,
    TEST_ORDER,
    TEST_DEGREE,
    TEST_IS_ODD,
    TEST_ASCENTS,
    TEST_INVERSE,
    TEST_IS_EVEN,
    TEST_RECORDS,
    TEST_SUPPORT,
    TEST_DESCENTS,
    TEST_DESCRIBE,
    TEST_CYCLE_TYPE,
    TEST_EQUIVALENT,
    TEST_INVERSIONS,
    TEST_IS_REGULAR,
    TEST_EXCEEDANCES,
    TEST_IS_CONJUGATE,
    TEST_CYCLE_NOTATION,
    TEST_IS_DERANGEMENT,
    TEST_IS_CONJUGATE_ERROR,
    TEST_CYCLE_DECOMPOSITION,
)


@pytest.mark.parametrize(
    argnames="cycle_decomposition, expected_value",
    argvalues=TEST_ASCENTS,
    ids=[f"{p.__repr__()}.cycle_notation()={c}" for p, c in TEST_ASCENTS],
)
def test_ascents(cycle_decomposition, expected_value) -> None:
    """Tests for the method `ascents()`."""
    _check_values(
        expression=f"{cycle_decomposition.rep()}.ascents()",
        evaluation=cycle_decomposition.ascents(),
        expected=expected_value,
    )


@pytest.mark.parametrize(
    argnames="cycle_decomposition, expected_value",
    argvalues=TEST_CYCLE_DECOMPOSITION,
    ids=[f"{p.__repr__()}.cycle_notation()={c}" for p, c in TEST_CYCLE_DECOMPOSITION],
)
def test_cycle_decomposition(cycle_decomposition, expected_value) -> None:
    """Tests for the method `cycle_decomposition()`."""
    _check_values(
        expression=f"{cycle_decomposition.rep()}.cycle_notation()",
        evaluation=cycle_decomposition.cycle_decomposition(),
        expected=expected_value,
    )


@pytest.mark.parametrize(
    argnames="cycle_decomposition, expected_value",
    argvalues=TEST_CYCLE_NOTATION,
    ids=[f"{c}.cycle_notation()={s}" for c, s in TEST_CYCLE_NOTATION],
)
def test_cycle_notation(cycle_decomposition, expected_value) -> None:
    """Tests for the method `cycle_notation()`."""
    _check_values(
        expression=f"{cycle_decomposition.rep()}.cycle_notation()",
        evaluation=cycle_decomposition.cycle_notation(),
        expected=expected_value,
    )


@pytest.mark.parametrize(
    argnames="cycle_decomposition, expected_value",
    argvalues=TEST_CYCLE_TYPE,
    ids=[f"{c}.cycle_type()={s}" for c, s in TEST_CYCLE_TYPE],
)
def test_cycle_type(cycle_decomposition, expected_value) -> None:
    """Tests for the method `cycle_type()`."""
    _check_values(
        expression=f"{cycle_decomposition.rep()}.cycle_type()",
        evaluation=cycle_decomposition.cycle_type(),
        expected=expected_value,
    )


@pytest.mark.parametrize(
    argnames="cycle_decomposition, expected_value",
    argvalues=TEST_DESCENTS,
    ids=[f"{p.__repr__()}.descents()={c}" for p, c in TEST_DESCENTS],
)
def test_descents(cycle_decomposition, expected_value) -> None:
    """Tests for the method `descents()`."""
    _check_values(
        expression=f"{cycle_decomposition.rep()}.descents()",
        evaluation=cycle_decomposition.descents(),
        expected=expected_value,
    )


@pytest.mark.parametrize(
    argnames="cycle_decomposition, expected_value",
    argvalues=TEST_DEGREE,
    ids=[f"{p.rep()}.degree()={d}" for p, d in TEST_DEGREE],
)
def test_degree(cycle_decomposition, expected_value) -> None:
    """Tests for the method `degree()`."""
    _check_values(
        expression=f"{cycle_decomposition.rep()}.degree()",
        evaluation=cycle_decomposition.degree(),
        expected=expected_value,
    )


@pytest.mark.parametrize(
    argnames="cycle_decomposition, expected_value",
    argvalues=TEST_DESCRIBE,
    ids=[f"{p}.describe()" for p, _ in TEST_DESCRIBE],
)
def test_describe(cycle_decomposition, expected_value) -> None:
    """Tests for the property `describe`."""
    _check_values(
        expression=f"{cycle_decomposition.rep()}.describe()",
        evaluation=cycle_decomposition.describe(),
        expected=expected_value,
    )


@pytest.mark.parametrize(
    argnames="cycle_decomposition, weakly, expected_value",
    argvalues=TEST_EXCEEDANCES,
    ids=[f"{p.__repr__()}.exceedences(weakly={w})={i}" for p, w, i in TEST_EXCEEDANCES],
)
def test_exceedences(cycle_decomposition, weakly, expected_value) -> None:
    """Tests for the method `exceedences()`."""
    _check_values(
        expression=f"{cycle_decomposition.rep()}.exceedances(weakly={weakly})",
        evaluation=cycle_decomposition.exceedances(weakly=weakly),
        expected=expected_value,
    )


@pytest.mark.parametrize(
    argnames="cycle_decomposition, expected_value",
    argvalues=TEST_INVERSE,
    ids=[f"{cycle}.inverse()={s}" for cycle, s in TEST_INVERSE],
)
def test_inverse(cycle_decomposition, expected_value) -> None:
    """Tests for the method `inverse()`."""
    _check_values(
        expression=f"{cycle_decomposition.rep()}.inverse()",
        evaluation=cycle_decomposition.inverse(),
        expected=expected_value,
    )


@pytest.mark.parametrize(
    argnames="cycle_decomposition, expected_value",
    argvalues=TEST_INVERSIONS,
    ids=[f"{cycle}.inversions()={s}" for cycle, s in TEST_INVERSIONS],
)
def test_inversions(cycle_decomposition, expected_value) -> None:
    """Tests for the method `inversions()`."""
    _check_values(
        expression=f"{cycle_decomposition.rep()}.inversions()",
        evaluation=cycle_decomposition.inversions(),
        expected=expected_value,
    )


@pytest.mark.parametrize(
    argnames="cycle_decomposition, other, expected_value",
    argvalues=TEST_IS_CONJUGATE,
    ids=[f"{p}.is_conjugate({o})={e}" for p, o, e in TEST_IS_CONJUGATE],
)
def test_is_conjugate(cycle_decomposition, other, expected_value) -> None:
    """Tests for the method `is_derangement()`."""
    _check_values(
        expression=f"{cycle_decomposition.rep()}.is_conjugate({other.rep()})",
        evaluation=cycle_decomposition.is_conjugate(other),
        expected=expected_value,
    )


@pytest.mark.parametrize(
    argnames="cycle_decomposition, other, error, msg",
    argvalues=TEST_IS_CONJUGATE_ERROR,
    ids=[f"{p}.is_conjugate({o})" for p, o, _, _ in TEST_IS_CONJUGATE_ERROR],
)
def test_is_conjugate_error(cycle_decomposition, other, error, msg) -> None:
    """Tests for errors in the method `is_derangement()`."""
    with pytest.raises(error, match=msg):
        _ = cycle_decomposition.is_conjugate(other)


@pytest.mark.parametrize(
    argnames="cycle_decomposition, expected_value",
    argvalues=TEST_IS_DERANGEMENT,
    ids=[f"{cycle}.is_derangement()={s}" for cycle, s in TEST_IS_DERANGEMENT],
)
def test_is_derangement(cycle_decomposition, expected_value) -> None:
    """Tests for the method `is_derangement()`."""
    _check_values(
        expression=f"{cycle_decomposition.rep()}.is_derangement()",
        evaluation=cycle_decomposition.is_derangement(),
        expected=expected_value,
    )


@pytest.mark.parametrize(
    argnames="cycle_decomposition, expected_value",
    argvalues=TEST_IS_EVEN,
    ids=[f"{cycle}.is_even()={s}" for cycle, s in TEST_IS_EVEN],
)
def test_is_even(cycle_decomposition, expected_value) -> None:
    """Tests for the method `is_even()`."""
    _check_values(
        expression=f"{cycle_decomposition.rep()}.is_even()",
        evaluation=cycle_decomposition.is_even(),
        expected=expected_value,
    )


@pytest.mark.parametrize(
    argnames="cycle_decomposition, expected_value",
    argvalues=TEST_IS_ODD,
    ids=[f"{cycle}.is_odd()={s}" for cycle, s in TEST_IS_ODD],
)
def test_is_odd(cycle_decomposition, expected_value) -> None:
    """Tests for the method `is_odd()`."""
    _check_values(
        expression=f"{cycle_decomposition.rep()}.is_odd()",
        evaluation=cycle_decomposition.is_odd(),
        expected=expected_value,
    )


@pytest.mark.parametrize(
    argnames="cycle_decomposition, expected_value",
    argvalues=TEST_IS_REGULAR,
    ids=[f"{cycle}.is_regular()={s}" for cycle, s in TEST_IS_REGULAR],
)
def test_is_regular(cycle_decomposition, expected_value) -> None:
    """Tests for the method `is_regular()`."""
    _check_values(
        expression=f"{cycle_decomposition.rep()}.is_regular()",
        evaluation=cycle_decomposition.is_regular(),
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
    argnames="cycle_decomposition, expected_value",
    argvalues=TEST_MAP,
    ids=[f"{p}.map()={m}" for p, m in TEST_MAP],
)
def test_map(cycle_decomposition, expected_value) -> None:
    """Tests for the method `map()`."""
    _check_values(
        expression=f"{cycle_decomposition.rep()}.map()", evaluation=cycle_decomposition.map, expected=expected_value
    )


@pytest.mark.parametrize(
    argnames="cycle, item, expected_value",
    argvalues=TEST_ORBIT,
    ids=[f"{p.rep()}.orbit({i})" for p, i, _ in TEST_ORBIT],
)
def test_orbit(cycle, item, expected_value) -> None:
    """Tests for the method `orbit()`."""
    _check_values(expression=f"{cycle.rep()}.orbit({item})", evaluation=cycle.orbit(item=item), expected=expected_value)


@pytest.mark.parametrize(
    argnames="cycle_decomposition, expected_value",
    argvalues=TEST_ORDER,
    ids=[f"{p}.order()={o}" for p, o in TEST_ORDER],
)
def test_order(cycle_decomposition, expected_value) -> None:
    """Tests for the method `order()`."""
    _check_values(
        expression=f"{cycle_decomposition.rep()}.order()",
        evaluation=cycle_decomposition.order(),
        expected=expected_value,
    )


@pytest.mark.parametrize(
    argnames="cycle_decomposition, expected_value",
    argvalues=TEST_RECORDS,
    ids=[f"{p}.records()={o}" for p, o in TEST_RECORDS],
)
def test_records(cycle_decomposition, expected_value) -> None:
    """Tests for the method `records()`."""
    _check_values(
        expression=f"{cycle_decomposition.rep()}.records()",
        evaluation=cycle_decomposition.records(),
        expected=expected_value,
    )


@pytest.mark.parametrize(
    argnames="cycle_decomposition, expected_value",
    argvalues=TEST_SGN,
    ids=[f"{p}.sgn()={o}" for p, o in TEST_SGN],
)
def test_sgn(cycle_decomposition, expected_value) -> None:
    """Tests for the method `sgn()`."""
    _check_values(
        expression=f"{cycle_decomposition.rep()}.sgn()", evaluation=cycle_decomposition.sgn(), expected=expected_value
    )


@pytest.mark.parametrize(
    argnames="cycle_decomposition, expected_value",
    argvalues=TEST_SUPPORT,
    ids=[f"{p}.support()={o}" for p, o in TEST_SUPPORT],
)
def test_support(cycle_decomposition, expected_value) -> None:
    """Tests for the method `support()`."""
    _check_values(
        expression=f"{cycle_decomposition.rep()}.support()",
        evaluation=cycle_decomposition.support(),
        expected=expected_value,
    )
