import pytest
from tests.utils import error_message

from tests.tests_permutation.test_cases import (
    TEST_SUPPORT,
    TEST_DOMAIN,
    TEST_ORDER,
    TEST_ONE_LINE_NOTATION,
    TEST_IS_DERANGEMENT,
    TEST_CYCLE_DECOMPOSITION,
    TEST_MAP,
)


@pytest.mark.parametrize(
    argnames="permutation, expected_value",
    argvalues=TEST_CYCLE_DECOMPOSITION,
    ids=[f"{p}={c}" for p, c in TEST_CYCLE_DECOMPOSITION]
)
def test_cycle_decomposition(permutation, expected_value) -> None:
    """Tests for the method `cycle_decomposition()`."""
    if permutation.cycle_decomposition() != expected_value:
        raise ValueError(error_message(expected=expected_value, got=permutation.cycle_decomposition()))


@pytest.mark.parametrize(
    argnames="permutation, expected_value",
    argvalues=TEST_DOMAIN,
    ids=[f"Domain{p}={s}" for p, s in TEST_DOMAIN]
)
def test_domain(permutation, expected_value) -> None:
    """Tests for the method `domain()`."""
    if permutation.domain() != expected_value:
        raise ValueError(error_message(expected=expected_value, got=permutation.domain()))


@pytest.mark.parametrize(
    argnames="permutation, expected_value",
    argvalues=TEST_IS_DERANGEMENT,
    ids=[f"{p}" for p, s in TEST_IS_DERANGEMENT]
)
def test_is_derangement(permutation, expected_value) -> None:
    """Tests for the method `is_derangement()`."""
    if permutation.is_derangement() is not expected_value:
        raise ValueError(error_message(expected=expected_value, got=permutation.is_derangement()))


@pytest.mark.parametrize(
    argnames="permutation, expected_value",
    argvalues=TEST_MAP,
    ids=[f"{p}->{m}" for p, m in TEST_MAP]
)
def test_map(permutation, expected_value) -> None:
    """Tests for the method `map()`."""
    if permutation.map() != expected_value:
        raise ValueError(error_message(expected=expected_value, got=permutation.map()))


@pytest.mark.parametrize(
    argnames="permutation, expected_value",
    argvalues=TEST_SUPPORT,
    ids=[f"Support{p}={s}" for p, s in TEST_SUPPORT]
)
def test_support(permutation, expected_value) -> None:
    """Tests for the method `support()`."""
    if permutation.support() != expected_value:
        raise ValueError(error_message(expected=expected_value, got=permutation.support()))


@pytest.mark.parametrize(
    argnames="permutation, expected_value",
    argvalues=TEST_ONE_LINE_NOTATION,
    ids=[f"{p}->{o}" for p, o in TEST_ONE_LINE_NOTATION]
)
def test_one_line_notation(permutation, expected_value) -> None:
    """Tests for the method `one_line_notation()`."""
    if permutation.one_line_notation() != expected_value:
        raise ValueError(error_message(expected=expected_value, got=permutation.one_line_notation()))


@pytest.mark.parametrize(
    argnames="permutation, expected_value",
    argvalues=TEST_ORDER,
    ids=[f"Order of {p} is {o}" for p, o in TEST_ORDER]
)
def test_order(permutation, expected_value) -> None:
    """Tests for the method `order()`."""
    if permutation.order() != expected_value:
        raise ValueError(error_message(expected=expected_value, got=permutation.order()))
