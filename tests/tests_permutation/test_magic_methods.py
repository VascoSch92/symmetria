import pytest

from tests.tests_permutation.test_cases import (
    TEST_BOOL,
    TEST_CALL,
    TEST_CALL_ERROR,
    TEST_EQUALITY,
    TEST_LEN,
    TEST_REPR,
    TEST_MULTIPLICATION,
    TEST_INT,
    TEST_MULTIPLICATION_ERROR,
)
from tests.utils import error_message


@pytest.mark.parametrize(
    argnames="permutation, expected_output",
    argvalues=TEST_BOOL,
    ids=[f"bool({p})={b}" for p, b in TEST_BOOL]
)
def test_bool(permutation, expected_output) -> None:
    """Tests for the method `__bool__()`."""
    if bool(permutation) != expected_output:
        raise ValueError(error_message(expected=expected_output, got=bool(permutation)))


@pytest.mark.parametrize(
    argnames="permutation, call_on, expected_output",
    argvalues=TEST_CALL,
    ids=[f"{p} on {ens}" for p, ens, _ in TEST_CALL]
)
def test_call(permutation, call_on, expected_output) -> None:
    """Tests for the method `__call__()`."""
    if permutation(call_on) != expected_output:
        raise ValueError(error_message(expected=expected_output, got=permutation(call_on)))


@pytest.mark.parametrize(
    argnames="permutation, call_on, error, msg",
    argvalues=TEST_CALL_ERROR,
    ids=[msg for _, _, _, msg in TEST_CALL_ERROR]
)
def test_call_error(permutation, call_on, error, msg) -> None:
    """Tests for exceptions to the method `__call__()`."""
    with pytest.raises(error, match=msg):
        _ = permutation(call_on)


@pytest.mark.parametrize(
    argnames="lhs, rhs, expected_output",
    argvalues=TEST_EQUALITY,
    ids=[f"{p}={q}" for p, q, _ in TEST_EQUALITY],
)
def test_equality(lhs, rhs, expected_output) -> None:
    """Tests for the method `__eq__()`."""
    if (lhs == rhs) != expected_output:
        raise ValueError(f"The expression `{lhs}=={rhs}` should be {expected_output}, but got {expected_output}.")


@pytest.mark.parametrize(
    argnames="permutation, expected_value",
    argvalues=TEST_INT,
    ids=[f"int({p})={i}" for p, i in TEST_INT]
)
def test_int(permutation, expected_value) -> None:
    """Tests for the method `__int__()`."""
    if int(permutation) != expected_value:
        raise ValueError(error_message(expected=expected_value, got=int(permutation)))


@pytest.mark.parametrize(
    argnames="permutation, expected_output",
    argvalues=TEST_LEN,
    ids=[f"len({p})={l}" for p, l in TEST_LEN],
)
def test_len(permutation, expected_output) -> None:
    """Tests for the method `__len__()`."""
    if len(permutation) != expected_output:
        raise ValueError(error_message(expected=expected_output, got=len(permutation)))


@pytest.mark.parametrize(
    argnames="permutation, expected_output",
    argvalues=TEST_REPR,
    ids=[f"{p}={r}" for p, r in TEST_REPR],
)
def test_repr(permutation, expected_output) -> None:
    """Tests for the method `__repr__()`."""
    if permutation.__repr__() != expected_output:
        raise ValueError(error_message(expected=expected_output, got=len(permutation)))


@pytest.mark.parametrize(
    argnames="lhs, rhs, expected_output",
    argvalues=TEST_MULTIPLICATION,
    ids=[f"{p}*{q}" for p, q, _ in TEST_MULTIPLICATION]
)
def test_multiplication(lhs, rhs, expected_output) -> None:
    """Tests for the method `__mul__()`."""
    if lhs * rhs != expected_output:
        raise ValueError(error_message(expected=expected_output, got=lhs * rhs))


@pytest.mark.parametrize(
    argnames="lhs, rhs, error, msg",
    argvalues=TEST_MULTIPLICATION_ERROR,
    ids=[error for _, _, _, error in TEST_MULTIPLICATION_ERROR]
)
def test_multiplication(lhs, rhs, error, msg) -> None:
    """Tests for exceptions to the method `__mul__()`."""
    with pytest.raises(error, match=msg):
        _ = lhs * rhs
