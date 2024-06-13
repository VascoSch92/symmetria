import pytest

from tests.test_utils import _check_values
from tests.tests_elements.tests_permutation.test_cases import (
    TEST_MAP,
    TEST_SGN,
    TEST_IMAGE,
    TEST_ORBIT,
    TEST_ORDER,
    TEST_DEGREE,
    TEST_DOMAIN,
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
    TEST_ONE_LINE_NOTATION,
    TEST_IS_CONJUGATE_ERROR,
    TEST_CYCLE_DECOMPOSITION,
)


@pytest.mark.parametrize(
    argnames="permutation, expected_value",
    argvalues=TEST_ASCENTS,
    ids=[f"{p.__repr__()}.ascents()={c}" for p, c in TEST_ASCENTS],
)
def test_ascents(permutation, expected_value) -> None:
    """Tests for the method `ascents()`."""
    _check_values(expression=f"{permutation.rep()}.ascents()", evaluation=permutation.ascents(), expected=expected_value)


@pytest.mark.parametrize(
    argnames="permutation, expected_value",
    argvalues=TEST_CYCLE_DECOMPOSITION,
    ids=[f"{p.__repr__()}.cycle_notation()={c}" for p, c in TEST_CYCLE_DECOMPOSITION],
)
def test_cycle_decomposition(permutation, expected_value) -> None:
    """Tests for the method `cycle_decomposition()`."""
    _check_values(
        expression=f"{permutation.rep()}.cycle_notation()",
        evaluation=permutation.cycle_decomposition(),
        expected=expected_value,
    )


@pytest.mark.parametrize(
    argnames="permutation, expected_value",
    argvalues=TEST_CYCLE_TYPE,
    ids=[f"{p.__repr__()}.cycle_type()={c}" for p, c in TEST_CYCLE_TYPE],
)
def test_cycle_type(permutation, expected_value) -> None:
    """Tests for the method `cycle_type()`."""
    _check_values(
        expression=f"{permutation.rep()}.cycle_type()", evaluation=permutation.cycle_type(), expected=expected_value
    )


@pytest.mark.parametrize(
    argnames="permutation, expected_value",
    argvalues=TEST_CYCLE_NOTATION,
    ids=[f"{c.rep()}.cycle_notation()={s}" for c, s in TEST_CYCLE_NOTATION],
)
def test_cycle_notation(permutation, expected_value) -> None:
    """Tests for the method `cycle_notation()`."""
    _check_values(
        expression=f"{permutation.rep()}.cycle_notation()",
        evaluation=permutation.cycle_notation(),
        expected=expected_value,
    )


@pytest.mark.parametrize(
    argnames="permutation, expected_value",
    argvalues=TEST_DEGREE,
    ids=[f"{p.rep()}.degree()={d}" for p, d in TEST_DEGREE],
)
def test_degree(permutation, expected_value) -> None:
    """Tests for the method `degree()`."""
    _check_values(expression=f"{permutation.rep()}.degree()", evaluation=permutation.degree(), expected=expected_value)


@pytest.mark.parametrize(
    argnames="permutation, expected_value",
    argvalues=TEST_DESCENTS,
    ids=[f"{p.__repr__()}.descents()={c}" for p, c in TEST_DESCENTS],
)
def test_descents(permutation, expected_value) -> None:
    """Tests for the method `descents()`."""
    _check_values(
        expression=f"{permutation.rep()}.descents()", evaluation=permutation.descents(), expected=expected_value
    )


@pytest.mark.parametrize(
    argnames="permutation, expected_value",
    argvalues=TEST_DESCRIBE,
    ids=[f"{p}.describe()" for p, _ in TEST_DESCRIBE],
)
def test_describe(permutation, expected_value) -> None:
    """Tests for the property `describe`."""
    _check_values(
        expression=f"{permutation.rep()}.describe()", evaluation=permutation.describe(), expected=expected_value
    )


@pytest.mark.parametrize(
    argnames="permutation, expected_value",
    argvalues=TEST_DOMAIN,
    ids=[f"{p.rep()}.domain()={s}" for p, s in TEST_DOMAIN],
)
def test_domain(permutation, expected_value) -> None:
    """Tests for the method `domain()`."""
    _check_values(expression=f"{permutation.rep()}.domain()", evaluation=permutation.domain, expected=expected_value)


@pytest.mark.parametrize(
    argnames="lhs, rhs, expected_value",
    argvalues=TEST_EQUIVALENT,
    ids=[f"{lhs.rep()}.equivalent({rhs})" for lhs, rhs, _ in TEST_EQUIVALENT],
)
def test_equivalent(lhs, rhs, expected_value) -> None:
    """Tests for the method `equivalent()`."""
    _check_values(
        expression=f"{lhs.rep()}.equivalent({rhs.__repr__()})",
        evaluation=lhs.equivalent(other=rhs),
        expected=expected_value,
    )


@pytest.mark.parametrize(
    argnames="permutation, weakly, expected_value",
    argvalues=TEST_EXCEEDANCES,
    ids=[f"{p}.exceedances(weakly={w})={i}" for p, w, i in TEST_EXCEEDANCES],
)
def test_exceedances(permutation, weakly, expected_value) -> None:
    """Tests the method `exceedances()`."""
    _check_values(
        expression=f"{permutation.rep()}.exceedances(weakly={weakly})",
        evaluation=permutation.exceedances(weakly=weakly),
        expected=expected_value,
    )


@pytest.mark.parametrize(
    argnames="permutation, expected_value",
    argvalues=TEST_IMAGE,
    ids=[f"{p}.image={i}" for p, i in TEST_IMAGE],
)
def test_image(permutation, expected_value) -> None:
    """Tests the property `image`."""
    _check_values(expression=f"{permutation.rep()}.image", evaluation=permutation.image, expected=expected_value)


@pytest.mark.parametrize(
    argnames="permutation, expected_value",
    argvalues=TEST_INVERSE,
    ids=[f"{p}.inverse()={e}" for p, e in TEST_INVERSE],
)
def test_inverse(permutation, expected_value) -> None:
    """Tests for the method `inverse()`."""
    _check_values(expression=f"{permutation.rep()}.inverse()", evaluation=permutation.inverse(), expected=expected_value)


@pytest.mark.parametrize(
    argnames="permutation, expected_value",
    argvalues=TEST_INVERSIONS,
    ids=[f"{p}.inversions()={e}" for p, e in TEST_INVERSIONS],
)
def test_inversions(permutation, expected_value) -> None:
    """Tests for the method `inversions()`."""
    _check_values(
        expression=f"{permutation.rep()}.inversions()", evaluation=permutation.inversions(), expected=expected_value
    )


@pytest.mark.parametrize(
    argnames="permutation, other, expected_value",
    argvalues=TEST_IS_CONJUGATE,
    ids=[f"{p}.is_conjugate({o})={e}" for p, o, e in TEST_IS_CONJUGATE],
)
def test_is_conjugate(permutation, other, expected_value) -> None:
    """Tests for the method `is_derangement()`."""
    _check_values(
        expression=f"{permutation.rep()}.is_conjugate({other.rep()})",
        evaluation=permutation.is_conjugate(other),
        expected=expected_value,
    )


@pytest.mark.parametrize(
    argnames="permutation, other, error, msg",
    argvalues=TEST_IS_CONJUGATE_ERROR,
    ids=[f"{p}.is_conjugate({o})" for p, o, _, _ in TEST_IS_CONJUGATE_ERROR],
)
def test_is_conjugate_error(permutation, other, error, msg) -> None:
    """Tests for errors in the method `is_derangement()`."""
    with pytest.raises(error, match=msg):
        _ = permutation.is_conjugate(other)


@pytest.mark.parametrize(
    argnames="permutation, expected_value",
    argvalues=TEST_IS_DERANGEMENT,
    ids=[f"{p}.is_derangement()={e}" for p, e in TEST_IS_DERANGEMENT],
)
def test_is_derangement(permutation, expected_value) -> None:
    """Tests for the method `is_derangement()`."""
    _check_values(
        expression=f"{permutation.rep()}.is_derangement()",
        evaluation=permutation.is_derangement(),
        expected=expected_value,
    )


@pytest.mark.parametrize(
    argnames="permutation, expected_value",
    argvalues=TEST_IS_EVEN,
    ids=[f"{p}.is_even()={e}" for p, e in TEST_IS_EVEN],
)
def test_is_even(permutation, expected_value) -> None:
    """Tests for the method `is_even()`."""
    _check_values(expression=f"{permutation.rep()}.is_even()", evaluation=permutation.is_even(), expected=expected_value)


@pytest.mark.parametrize(
    argnames="permutation, expected_value",
    argvalues=TEST_IS_ODD,
    ids=[f"{p}.is_odd()={e}" for p, e in TEST_IS_ODD],
)
def test_is_odd(permutation, expected_value) -> None:
    """Tests for the method `is_odd()`."""
    _check_values(expression=f"{permutation.rep()}.is_odd()", evaluation=permutation.is_odd(), expected=expected_value)


@pytest.mark.parametrize(
    argnames="permutation, expected_value",
    argvalues=TEST_IS_REGULAR,
    ids=[f"{p}.is_regular()={e}" for p, e in TEST_IS_REGULAR],
)
def test_is_regular(permutation, expected_value) -> None:
    """Tests for the method `is_regular()`."""
    _check_values(
        expression=f"{permutation.rep()}.is_regular()", evaluation=permutation.is_regular(), expected=expected_value
    )


@pytest.mark.parametrize(
    argnames="permutation, expected_value",
    argvalues=TEST_MAP,
    ids=[f"{p}.map()={m}" for p, m in TEST_MAP],
)
def test_map(permutation, expected_value) -> None:
    """Tests for the method `map()`."""
    _check_values(expression=f"{permutation.rep()}.map()", evaluation=permutation.map, expected=expected_value)


@pytest.mark.parametrize(
    argnames="permutation, expected_value",
    argvalues=TEST_RECORDS,
    ids=[f"{p.rep()}.records()={s}" for p, s in TEST_RECORDS],
)
def test_records(permutation, expected_value) -> None:
    """Tests for the method `records()`."""
    _check_values(expression=f"{permutation.rep()}.records()", evaluation=permutation.records(), expected=expected_value)


@pytest.mark.parametrize(
    argnames="permutation, expected_value",
    argvalues=TEST_SUPPORT,
    ids=[f"{p.rep()}.support()={s}" for p, s in TEST_SUPPORT],
)
def test_support(permutation, expected_value) -> None:
    """Tests for the method `support()`."""
    _check_values(expression=f"{permutation.rep()}.support()", evaluation=permutation.support(), expected=expected_value)


@pytest.mark.parametrize(
    argnames="permutation, item, expected_value",
    argvalues=TEST_ORBIT,
    ids=[f"{p.rep()}.orbit({i})" for p, i, _ in TEST_ORBIT],
)
def test_orbit(permutation, item, expected_value) -> None:
    """Tests for the method `orbit()`."""
    _check_values(
        expression=f"{permutation.rep()}.orbit({item})", evaluation=permutation.orbit(item=item), expected=expected_value
    )


@pytest.mark.parametrize(
    argnames="permutation, expected_value",
    argvalues=TEST_ONE_LINE_NOTATION,
    ids=[f"{p.rep()}.one_line_notation()={o}" for p, o in TEST_ONE_LINE_NOTATION],
)
def test_one_line_notation(permutation, expected_value) -> None:
    """Tests for the method `one_line_notation()`."""
    _check_values(
        expression=f"{permutation.__repr__()}.one_line_notation()",
        evaluation=permutation.one_line_notation(),
        expected=expected_value,
    )


@pytest.mark.parametrize(
    argnames="permutation, expected_value",
    argvalues=TEST_SGN,
    ids=[f"{p.rep()}.sgn()={s}" for p, s in TEST_SGN],
)
def test_sgn(permutation, expected_value) -> None:
    """Tests for the method `sgn()`."""
    _check_values(expression=f"{permutation.rep()}.sgn()", evaluation=permutation.sgn(), expected=expected_value)


@pytest.mark.parametrize(
    argnames="permutation, expected_value",
    argvalues=TEST_ORDER,
    ids=[f"{p}.order()={o}" for p, o in TEST_ORDER],
)
def test_order(permutation, expected_value) -> None:
    """Tests for the method `order()`."""
    _check_values(expression=f"{permutation.rep()}.order()", evaluation=permutation.order(), expected=expected_value)
