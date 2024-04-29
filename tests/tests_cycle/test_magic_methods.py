import pytest

from tests.tests_cycle.test_cases import (
    TEST_BOOL,
    TEST_EQ,
    TEST_INT,
    TEST_LEN,
    TEST_REPR,
    TEST_MUL,
    TEST_MUL_ERROR,
)
from tests.utils import error_message


@pytest.mark.parametrize(
    argnames="cycle, expected_output",
    argvalues=TEST_BOOL,
    ids=[f"bool({c})={b}" for c, b in TEST_BOOL]
)
def test_bool(cycle, expected_output) -> None:
    """Tests for the method `__bool__()`."""
    if bool(cycle) != expected_output:
        raise ValueError(error_message(expected=expected_output, got=bool(cycle)))


@pytest.mark.parametrize(
    argnames="lhs, rhs, expected_output",
    argvalues=TEST_EQ,
    ids=[f"{lhs}={rhs}" for lhs, rhs, _ in TEST_EQ]
)
def test_eq(lhs, rhs, expected_output) -> None:
    """Tests for the method `__eq__()`."""
    if (lhs == rhs) != expected_output:
        raise ValueError(
            f"The expression `{lhs}=={rhs}` should be {expected_output}, but got {lhs == rhs}."
        )


@pytest.mark.parametrize(
    argnames="cycle, expected_value",
    argvalues=TEST_INT,
    ids=[f"int({c})={i}" for c, i in TEST_INT]
)
def test_int(cycle, expected_value) -> None:
    """Tests for the method `__int__()`."""
    if int(cycle) != expected_value:
        raise ValueError(error_message(expected=expected_value, got=int(cycle)))


@pytest.mark.parametrize(
    argnames="cycle, expected_output",
    argvalues=TEST_LEN,
    ids=[f"len({c})={l}" for c, l in TEST_LEN],
)
def test_len(cycle, expected_output) -> None:
    """Tests for the method `__len__()`."""
    if len(cycle) != expected_output:
        raise ValueError(error_message(expected=expected_output, got=len(cycle)))


@pytest.mark.parametrize(
    argnames="lhs, rhs, expected_output",
    argvalues=TEST_MUL,
    ids=[f"{p}*{q}" for p, q, _ in TEST_MUL]
)
def test_multiplication(lhs, rhs, expected_output) -> None:
    """Tests for the method `__mul__()`."""
    if lhs * rhs != expected_output:
        raise ValueError(error_message(expected=expected_output, got=lhs * rhs))


@pytest.mark.parametrize(
    argnames="lhs, rhs, error, msg",
    argvalues=TEST_MUL_ERROR,
    ids=[error for _, _, _, error in TEST_MUL_ERROR]
)
def test_multiplication_error(lhs, rhs, error, msg) -> None:
    """Tests for exceptions to the method `__mul__()`."""
    with pytest.raises(error, match=msg):
        _ = lhs * rhs


@pytest.mark.parametrize(
    argnames="cycle, expected_output",
    argvalues=TEST_REPR,
    ids=[f"{c}={r}" for c, r in TEST_REPR],
)
def test_repr(cycle, expected_output) -> None:
    """Tests for the method `__repr__()`."""
    if cycle.__repr__() != expected_output:
        raise ValueError(error_message(expected=expected_output, got=cycle.__repr__()))


