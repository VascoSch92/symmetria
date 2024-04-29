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
from tests.tests_factory import (
    validate_bool,
    validate_eq,
    validate_int,
    validate_len,
    validate_mul,
    validate_mul_error,
    validate_repr,
)


@pytest.mark.parametrize(
    argnames="cycle, expected_value",
    argvalues=TEST_BOOL,
    ids=[f"bool({c})={b}" for c, b in TEST_BOOL]
)
def test_bool(cycle, expected_value) -> None:
    """Tests for the method `__bool__()`."""
    validate_bool(item=cycle, expected_value=expected_value)


@pytest.mark.parametrize(
    argnames="lhs, rhs, expected_value",
    argvalues=TEST_EQ,
    ids=[f"{lhs}={rhs}" for lhs, rhs, _ in TEST_EQ]
)
def test_eq(lhs, rhs, expected_value) -> None:
    """Tests for the method `__eq__()`."""
    validate_eq(lhs=lhs, rhs=rhs, expected_value=expected_value)


@pytest.mark.parametrize(
    argnames="cycle, expected_value",
    argvalues=TEST_INT,
    ids=[f"int({c})={i}" for c, i in TEST_INT]
)
def test_int(cycle, expected_value) -> None:
    """Tests for the method `__int__()`."""
    validate_int(item=cycle, expected_value=expected_value)


@pytest.mark.parametrize(
    argnames="cycle, expected_value",
    argvalues=TEST_LEN,
    ids=[f"len({c})={l}" for c, l in TEST_LEN],
)
def test_len(cycle, expected_value) -> None:
    """Tests for the method `__len__()`."""
    validate_len(item=cycle, expected_value=expected_value)


@pytest.mark.parametrize(
    argnames="lhs, rhs, expected_value",
    argvalues=TEST_MUL,
    ids=[f"{p}*{q}" for p, q, _ in TEST_MUL]
)
def test_multiplication(lhs, rhs, expected_value) -> None:
    """Tests for the method `__mul__()`."""
    validate_mul(lhs=lhs, rhs=rhs, expected_value=expected_value)


@pytest.mark.parametrize(
    argnames="lhs, rhs, error, msg",
    argvalues=TEST_MUL_ERROR,
    ids=[error for _, _, _, error in TEST_MUL_ERROR]
)
def test_multiplication_error(lhs, rhs, error, msg) -> None:
    """Tests for exceptions to the method `__mul__()`."""
    validate_mul_error(lhs=lhs, rhs=rhs, error=error, msg=msg)


@pytest.mark.parametrize(
    argnames="cycle, expected_value",
    argvalues=TEST_REPR,
    ids=[f"{c}={r}" for c, r in TEST_REPR],
)
def test_repr(cycle, expected_value) -> None:
    """Tests for the method `__repr__()`."""
    validate_repr(item=cycle, expected_value=expected_value)
