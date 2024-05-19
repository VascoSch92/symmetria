import pytest

from tests.test_factory import (
    validate_map,
    validate_sgn,
    validate_orbit,
    validate_order,
    validate_domain,
    validate_support,
    validate_equivalent,
    validate_cycle_notation,
    validate_is_derangement,
    validate_cycle_decomposition,
)
from tests.tests_permutation.test_cases import (
    TEST_MAP,
    TEST_SGN,
    TEST_ORBIT,
    TEST_ORDER,
    TEST_DOMAIN,
    TEST_SUPPORT,
    TEST_EQUIVALENT,
    TEST_CYCLE_NOTATION,
    TEST_IS_DERANGEMENT,
    TEST_ONE_LINE_NOTATION,
    TEST_CYCLE_DECOMPOSITION,
)


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
    argvalues=TEST_CYCLE_NOTATION,
    ids=[f"{c.rep()}.cycle_notation()={s}" for c, s in TEST_CYCLE_NOTATION],
)
def test_cycle_notation(permutation, expected_value) -> None:
    """Tests for the method `cycle_notation()`."""
    validate_cycle_notation(item=permutation, expected_value=expected_value)


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
    argnames="permutation, expected_value",
    argvalues=TEST_IS_DERANGEMENT,
    ids=[f"{p}.is_derangement()={e}" for p, e in TEST_IS_DERANGEMENT],
)
def test_is_derangement(permutation, expected_value) -> None:
    """Tests for the method `is_derangement()`."""
    validate_is_derangement(item=permutation, expected_value=expected_value)


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
