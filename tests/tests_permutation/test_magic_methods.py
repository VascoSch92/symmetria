import pytest

from tests.tests_factory import (
    validate_bool,
    validate_call,
    validate_call_error,
    validate_eq,
    validate_int,
    validate_len,
    validate_mul,
    validate_mul_error,
    validate_repr,
    validate_str,
)
from tests.tests_permutation.test_cases import (
    TEST_BOOL,
    TEST_CALL,
    TEST_CALL_ERROR,
    TEST_EQ,
    TEST_LEN,
    TEST_REPR,
    TEST_MUL,
    TEST_INT,
    TEST_MUL_ERROR,
    TEST_STR,
)


@pytest.mark.parametrize(
    argnames="permutation, expected_value",
    argvalues=TEST_BOOL,
    ids=[f"bool({p})={b}" for p, b in TEST_BOOL]
)
def test_bool(permutation, expected_value) -> None:
    """Tests for the method `__bool__()`."""
    validate_bool(item=permutation, expected_value=expected_value)


@pytest.mark.parametrize(
    argnames="permutation, call_on, expected_value",
    argvalues=TEST_CALL,
    ids=[f"{p} on {ens}" for p, ens, _ in TEST_CALL]
)
def test_call(permutation, call_on, expected_value) -> None:
    """Tests for the method `__call__()`."""
    validate_call(item=permutation, call_on=call_on, expected_value=expected_value)


@pytest.mark.parametrize(
    argnames="permutation, call_on, error, msg",
    argvalues=TEST_CALL_ERROR,
    ids=[msg for _, _, _, msg in TEST_CALL_ERROR]
)
def test_call_error(permutation, call_on, error, msg) -> None:
    """Tests for exceptions to the method `__call__()`."""
    validate_call_error(item=permutation, call_on=call_on, error=error, msg=msg)


@pytest.mark.parametrize(
    argnames="lhs, rhs, expected_value",
    argvalues=TEST_EQ,
    ids=[f"{p}={q}" for p, q, _ in TEST_EQ],
)
def test_equality(lhs, rhs, expected_value) -> None:
    """Tests for the method `__eq__()`."""
    validate_eq(lhs=lhs, rhs=rhs, expected_value=expected_value)


@pytest.mark.parametrize(
    argnames="permutation, expected_value",
    argvalues=TEST_INT,
    ids=[f"int({p})={i}" for p, i in TEST_INT]
)
def test_int(permutation, expected_value) -> None:
    """Tests for the method `__int__()`."""
    validate_int(item=permutation, expected_value=expected_value)


@pytest.mark.parametrize(
    argnames="permutation, expected_value",
    argvalues=TEST_LEN,
    ids=[f"len({p})={l}" for p, l in TEST_LEN],
)
def test_len(permutation, expected_value) -> None:
    """Tests for the method `__len__()`."""
    validate_len(item=permutation, expected_value=expected_value)


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
    argnames="permutation, expected_value",
    argvalues=TEST_REPR,
    ids=[f"{p}->{r}" for p, r in TEST_REPR],
)
def test_repr(permutation, expected_value) -> None:
    """Tests for the method `__repr__()`."""
    validate_repr(item=permutation, expected_value=expected_value)


@pytest.mark.parametrize(
    argnames="permutation, expected_value",
    argvalues=TEST_STR,
    ids=[f"str({p})={s}" for p, s in TEST_STR],
)
def test_str(permutation, expected_value) -> None:
    """Tests for the method `__str__()`."""
    validate_str(item=permutation, expected_value=expected_value)
