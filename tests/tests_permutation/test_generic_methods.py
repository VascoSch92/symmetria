import pytest

from tests.test_factory import (
    validate_map,
    validate_sgn,
    validate_orbit,
    validate_order,
    validate_domain,
    validate_is_odd,
    validate_ascents,
    validate_inverse,
    validate_is_even,
    validate_support,
    validate_descents,
    validate_cycle_type,
    validate_equivalent,
    validate_inversions,
    validate_is_regular,
    validate_exceedances,
    validate_is_conjugate,
    validate_cycle_notation,
    validate_is_derangement,
    validate_cycle_decomposition,
)
from tests.tests_permutation.test_cases import (
    TEST_MAP,
    TEST_SGN,
    TEST_IMAGE,
    TEST_ORBIT,
    TEST_ORDER,
    TEST_DOMAIN,
    TEST_IS_ODD,
    TEST_ASCENTS,
    TEST_INVERSE,
    TEST_IS_EVEN,
    TEST_SUPPORT,
    TEST_DESCENTS,
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
    validate_ascents(item=permutation, expected_value=expected_value)


@pytest.mark.parametrize(
    argnames="permutation, expected_value",
    argvalues=TEST_CYCLE_DECOMPOSITION,
    ids=[f"{p.__repr__()}.cycle_notation()={c}" for p, c in TEST_CYCLE_DECOMPOSITION],
)
def test_cycle_decomposition(permutation, expected_value) -> None:
    """Tests for the method `cycle_decomposition()`."""
    validate_cycle_decomposition(item=permutation, expected_value=expected_value)


@pytest.mark.parametrize(
    argnames="permutation, expected_value",
    argvalues=TEST_CYCLE_TYPE,
    ids=[f"{p.__repr__()}.cycle_type()={c}" for p, c in TEST_CYCLE_TYPE],
)
def test_cycle_type(permutation, expected_value) -> None:
    """Tests for the method `cycle_type()`."""
    validate_cycle_type(item=permutation, expected_value=expected_value)


@pytest.mark.parametrize(
    argnames="permutation, expected_value",
    argvalues=TEST_CYCLE_NOTATION,
    ids=[f"{c.rep()}.cycle_notation()={s}" for c, s in TEST_CYCLE_NOTATION],
)
def test_cycle_notation(permutation, expected_value) -> None:
    """Tests for the method `cycle_notation()`."""
    validate_cycle_notation(item=permutation, expected_value=expected_value)


@pytest.mark.parametrize(
    argnames="permutation, expected_value",
    argvalues=TEST_DESCENTS,
    ids=[f"{p.__repr__()}.descents()={c}" for p, c in TEST_DESCENTS],
)
def test_descents(permutation, expected_value) -> None:
    """Tests for the method `descents()`."""
    validate_descents(item=permutation, expected_value=expected_value)


@pytest.mark.parametrize(
    argnames="permutation, expected_value",
    argvalues=TEST_DOMAIN,
    ids=[f"{p.rep()}.domain()={s}" for p, s in TEST_DOMAIN],
)
def test_domain(permutation, expected_value) -> None:
    """Tests for the method `domain()`."""
    validate_domain(item=permutation, expected_value=expected_value)


@pytest.mark.parametrize(
    argnames="lhs, rhs, expected_value",
    argvalues=TEST_EQUIVALENT,
    ids=[f"{lhs.rep()}.equivalent({rhs})" for lhs, rhs, _ in TEST_EQUIVALENT],
)
def test_equivalent(lhs, rhs, expected_value) -> None:
    """Tests for the method `equivalent()`."""
    validate_equivalent(lhs=lhs, rhs=rhs, expected_value=expected_value)


@pytest.mark.parametrize(
    argnames="permutation, weakly, expected_value",
    argvalues=TEST_EXCEEDANCES,
    ids=[f"{p}.exceedances(weakly={w})={i}" for p, w, i in TEST_EXCEEDANCES],
)
def test_exceedances(permutation, weakly, expected_value) -> None:
    """Tests the method `exceedances()`."""
    validate_exceedances(item=permutation, weakly=weakly, expected_value=expected_value)


@pytest.mark.parametrize(
    argnames="permutation, expected_value",
    argvalues=TEST_IMAGE,
    ids=[f"{p}.image={i}" for p, i in TEST_IMAGE],
)
def test_image(permutation, expected_value) -> None:
    """Tests the property `image`."""
    if permutation.image != expected_value:
        raise ValueError(
            f"The expression `{permutation.rep()}.image` must evaluate {expected_value}, "
            f"but got {permutation.image}."
        )


@pytest.mark.parametrize(
    argnames="permutation, expected_value",
    argvalues=TEST_INVERSE,
    ids=[f"{p}.inverse()={e}" for p, e in TEST_INVERSE],
)
def test_inverse(permutation, expected_value) -> None:
    """Tests for the method `inverse()`."""
    validate_inverse(item=permutation, expected_value=expected_value)


@pytest.mark.parametrize(
    argnames="permutation, expected_value",
    argvalues=TEST_INVERSIONS,
    ids=[f"{p}.inversions()={e}" for p, e in TEST_INVERSIONS],
)
def test_inversions(permutation, expected_value) -> None:
    """Tests for the method `inversions()`."""
    validate_inversions(item=permutation, expected_value=expected_value)


@pytest.mark.parametrize(
    argnames="permutation, other, expected_value",
    argvalues=TEST_IS_CONJUGATE,
    ids=[f"{p}.is_conjugate({o})={e}" for p, o, e in TEST_IS_CONJUGATE],
)
def test_is_conjugate(permutation, other, expected_value) -> None:
    """Tests for the method `is_derangement()`."""
    validate_is_conjugate(item=permutation, other=other, expected_value=expected_value)


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
    validate_is_derangement(item=permutation, expected_value=expected_value)


@pytest.mark.parametrize(
    argnames="permutation, expected_value",
    argvalues=TEST_IS_EVEN,
    ids=[f"{p}.is_even()={e}" for p, e in TEST_IS_EVEN],
)
def test_is_even(permutation, expected_value) -> None:
    """Tests for the method `is_even()`."""
    validate_is_even(item=permutation, expected_value=expected_value)


@pytest.mark.parametrize(
    argnames="permutation, expected_value",
    argvalues=TEST_IS_ODD,
    ids=[f"{p}.is_odd()={e}" for p, e in TEST_IS_ODD],
)
def test_is_odd(permutation, expected_value) -> None:
    """Tests for the method `is_odd()`."""
    validate_is_odd(item=permutation, expected_value=expected_value)


@pytest.mark.parametrize(
    argnames="permutation, expected_value",
    argvalues=TEST_IS_REGULAR,
    ids=[f"{p}.is_regular()={e}" for p, e in TEST_IS_REGULAR],
)
def test_is_regular(permutation, expected_value) -> None:
    """Tests for the method `is_regular()`."""
    validate_is_regular(item=permutation, expected_value=expected_value)


@pytest.mark.parametrize(
    argnames="permutation, expected_value",
    argvalues=TEST_MAP,
    ids=[f"{p}.map()={m}" for p, m in TEST_MAP],
)
def test_map(permutation, expected_value) -> None:
    """Tests for the method `map()`."""
    validate_map(item=permutation, expected_value=expected_value)


@pytest.mark.parametrize(
    argnames="permutation, expected_value",
    argvalues=TEST_SUPPORT,
    ids=[f"{p.rep()}.support()={s}" for p, s in TEST_SUPPORT],
)
def test_support(permutation, expected_value) -> None:
    """Tests for the method `support()`."""
    validate_support(item=permutation, expected_value=expected_value)


@pytest.mark.parametrize(
    argnames="permutation, item, expected_value",
    argvalues=TEST_ORBIT,
    ids=[f"{p.rep()}.orbit({i})" for p, i, _ in TEST_ORBIT],
)
def test_orbit(permutation, item, expected_value) -> None:
    """Tests for the method `orbit()`."""
    validate_orbit(element=permutation, item=item, expected_value=expected_value)


@pytest.mark.parametrize(
    argnames="permutation, expected_value",
    argvalues=TEST_ONE_LINE_NOTATION,
    ids=[f"{p.rep()}.one_line_notation()={o}" for p, o in TEST_ONE_LINE_NOTATION],
)
def test_one_line_notation(permutation, expected_value) -> None:
    """Tests for the method `one_line_notation()`."""
    if permutation.one_line_notation() != expected_value:
        ValueError(
            f"The expression `{permutation.__repr__()}.one_line_notation()` must evaluate {expected_value}, "
            f"but got {permutation.one_line_notation()}."
        )


@pytest.mark.parametrize(
    argnames="permutation, expected_value",
    argvalues=TEST_SGN,
    ids=[f"{p.rep()}.sgn()={s}" for p, s in TEST_SGN],
)
def test_sgn(permutation, expected_value) -> None:
    """Tests for the method `sgn()`."""
    validate_sgn(item=permutation, expected_value=expected_value)


@pytest.mark.parametrize(
    argnames="permutation, expected_value",
    argvalues=TEST_ORDER,
    ids=[f"{p}.order()={o}" for p, o in TEST_ORDER],
)
def test_order(permutation, expected_value) -> None:
    """Tests for the method `order()`."""
    validate_order(item=permutation, expected_value=expected_value)
