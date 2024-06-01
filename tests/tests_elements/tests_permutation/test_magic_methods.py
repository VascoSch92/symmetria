import pytest

from tests.test_utils import _check_values
from tests.tests_elements.tests_permutation.test_cases import (
    TEST_EQ,
    TEST_INT,
    TEST_LEN,
    TEST_MUL,
    TEST_POW,
    TEST_STR,
    TEST_BOOL,
    TEST_CALL,
    TEST_REPR,
    TEST_MUL_ERROR,
    TEST_POW_ERROR,
    TEST_CALL_ERROR,
)


@pytest.mark.parametrize(
    argnames="permutation, expected_value",
    argvalues=TEST_BOOL,
    ids=[f"bool({p.rep()})={b}" for p, b in TEST_BOOL],
)
def test_bool(permutation, expected_value) -> None:
    """Tests for the method `__bool__()`."""
    _check_values(expression=f"bool({permutation.rep()})", evaluation=bool(permutation), expected=expected_value)


@pytest.mark.parametrize(
    argnames="permutation, call_on, expected_value",
    argvalues=TEST_CALL,
    ids=[f"{p.rep()}({e})" for p, e, _ in TEST_CALL],
)
def test_call(permutation, call_on, expected_value) -> None:
    """Tests for the method `__call__()`."""
    _check_values(expression=f"{permutation.rep()}({call_on})", evaluation=permutation(call_on), expected=expected_value)


@pytest.mark.parametrize(
    argnames="permutation, call_on, error, msg",
    argvalues=TEST_CALL_ERROR,
    ids=[msg for _, _, _, msg in TEST_CALL_ERROR],
)
def test_call_error(permutation, call_on, error, msg) -> None:
    """Tests for exceptions to the method `__call__()`."""
    with pytest.raises(error, match=msg):
        _ = permutation(call_on)


@pytest.mark.parametrize(
    argnames="lhs, rhs, expected_value",
    argvalues=TEST_EQ,
    ids=[f"{p.rep()}={q}" for p, q, _ in TEST_EQ],
)
def test_equality(lhs, rhs, expected_value) -> None:
    """Tests for the method `__eq__()`."""
    _check_values(expression=f"{lhs.__repr__()}=={rhs.__repr__()}", evaluation=(lhs == rhs), expected=expected_value)


@pytest.mark.parametrize(
    argnames="permutation, expected_value",
    argvalues=TEST_INT,
    ids=[f"int({p.rep()})={i}" for p, i in TEST_INT],
)
def test_int(permutation, expected_value) -> None:
    """Tests for the method `__int__()`."""
    _check_values(expression=f"int({permutation.rep()})", evaluation=int(permutation), expected=expected_value)


@pytest.mark.parametrize(
    argnames="permutation, expected_value",
    argvalues=TEST_LEN,
    ids=[f"len({p.rep()})={length}" for p, length in TEST_LEN],
)
def test_len(permutation, expected_value) -> None:
    """Tests for the method `__len__()`."""
    _check_values(expression=f"len({permutation.rep()})", evaluation=len(permutation), expected=expected_value)


@pytest.mark.parametrize(
    argnames="lhs, rhs, expected_value",
    argvalues=TEST_MUL,
    ids=[f"{p.rep()}*{q.rep()}" for p, q, _ in TEST_MUL],
)
def test_multiplication(lhs, rhs, expected_value) -> None:
    """Tests for the method `__mul__()`."""
    _check_values(expression=f"{lhs.rep()}*{rhs.rep()}", evaluation=lhs * rhs, expected=expected_value)


@pytest.mark.parametrize(
    argnames="lhs, rhs, error, msg",
    argvalues=TEST_MUL_ERROR,
    ids=[error for _, _, _, error in TEST_MUL_ERROR],
)
def test_multiplication_error(lhs, rhs, error, msg) -> None:
    """Tests for exceptions to the method `__mul__()`."""
    with pytest.raises(error, match=msg):
        _ = lhs * rhs


@pytest.mark.parametrize(
    argnames="permutation, power, expected_value",
    argvalues=TEST_POW,
    ids=[f"{p}**{q}={r}" for p, q, r in TEST_POW],
)
def test_pow(permutation, power, expected_value) -> None:
    """Tests for the method `__pow__()`."""
    _check_values(expression=f"{permutation.rep()} ** {power}", evaluation=permutation**power, expected=expected_value)


@pytest.mark.parametrize(
    argnames="permutation, power, error, msg",
    argvalues=TEST_POW_ERROR,
    ids=[f"{p}**{q}" for p, q, _, _ in TEST_POW_ERROR],
)
def test_pow_error(permutation, power, error, msg) -> None:
    """Tests for exceptions to the method `__pow__()`."""
    with pytest.raises(error, match=msg):
        _ = permutation**power


@pytest.mark.parametrize(
    argnames="permutation, expected_value",
    argvalues=TEST_REPR,
    ids=[f"{p}.__repr__()={r}" for p, r in TEST_REPR],
)
def test_repr(permutation, expected_value) -> None:
    """Tests for the method `__repr__()`."""
    _check_values(
        expression=f"{permutation.typename}.__repr__()", evaluation=permutation.__repr__(), expected=expected_value
    )


@pytest.mark.parametrize(
    argnames="permutation, expected_value",
    argvalues=TEST_STR,
    ids=[f"str({p.rep()})={s}" for p, s in TEST_STR],
)
def test_str(permutation, expected_value) -> None:
    """Tests for the method `__str__()`."""
    _check_values(expression=f"{permutation.rep()}.__str__()", evaluation=permutation.__str__(), expected=expected_value)
