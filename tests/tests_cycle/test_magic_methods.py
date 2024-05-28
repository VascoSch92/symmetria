import pytest

from tests.test_factory import (
    validate_eq,
    validate_int,
    validate_len,
    validate_pow,
    validate_bool,
    validate_call,
    validate_repr,
    validate_getitem,
    validate_mul_error,
    validate_pow_error,
    validate_call_error,
)
from tests.tests_cycle.test_cases import (
    TEST_EQ,
    TEST_INT,
    TEST_LEN,
    TEST_POW,
    TEST_BOOL,
    TEST_CALL,
    TEST_REPR,
    TEST_GETITEM,
    TEST_MUL_ERROR,
    TEST_POW_ERROR,
    TEST_CALL_ERROR,
)


@pytest.mark.parametrize(
    argnames="cycle, expected_value",
    argvalues=TEST_BOOL,
    ids=[f"bool({c.rep()})={b}" for c, b in TEST_BOOL],
)
def test_bool(cycle, expected_value) -> None:
    """Tests for the method `__bool__()`."""
    validate_bool(item=cycle, expected_value=expected_value)


@pytest.mark.parametrize(
    argnames="cycle, call_on, expected_value",
    argvalues=TEST_CALL,
    ids=[f"{p.rep()}({ens})" for p, ens, _ in TEST_CALL],
)
def test_call(cycle, call_on, expected_value) -> None:
    """Tests for the method `__call__()`."""
    validate_call(item=cycle, call_on=call_on, expected_value=expected_value)


@pytest.mark.parametrize(
    argnames="cycle, call_on, error, msg",
    argvalues=TEST_CALL_ERROR,
    ids=[msg for _, _, _, msg in TEST_CALL_ERROR],
)
def test_call_error(cycle, call_on, error, msg) -> None:
    """Tests for exceptions to the method `__call__()`."""
    validate_call_error(item=cycle, call_on=call_on, error=error, msg=msg)


@pytest.mark.parametrize(
    argnames="lhs, rhs, expected_value",
    argvalues=TEST_EQ,
    ids=[f"{lhs}={rhs}" for lhs, rhs, _ in TEST_EQ],
)
def test_eq(lhs, rhs, expected_value) -> None:
    """Tests for the method `__eq__()`."""
    validate_eq(lhs=lhs, rhs=rhs, expected_value=expected_value)


@pytest.mark.parametrize(
    argnames="cycle, idx, expected_value",
    argvalues=TEST_GETITEM,
    ids=[f"{c}[{i}]={e}" for c, i, e in TEST_GETITEM],
)
def test_getitem(cycle, idx, expected_value) -> None:
    """Tests for the method `__getitem__()`."""
    validate_getitem(item=cycle, idx=idx, expected_value=expected_value)


@pytest.mark.parametrize(
    argnames="cycle, expected_value",
    argvalues=TEST_INT,
    ids=[f"int({c})={i}" for c, i in TEST_INT],
)
def test_int(cycle, expected_value) -> None:
    """Tests for the method `__int__()`."""
    validate_int(item=cycle, expected_value=expected_value)


@pytest.mark.parametrize(
    argnames="cycle, expected_value",
    argvalues=TEST_LEN,
    ids=[f"len({c})={length}" for c, length in TEST_LEN],
)
def test_len(cycle, expected_value) -> None:
    """Tests for the method `__len__()`."""
    validate_len(item=cycle, expected_value=expected_value)


@pytest.mark.parametrize(
    argnames="lhs, rhs, error, msg",
    argvalues=TEST_MUL_ERROR,
    ids=[error for _, _, _, error in TEST_MUL_ERROR],
)
def test_multiplication_error(lhs, rhs, error, msg) -> None:
    """Tests for exceptions to the method `__mul__()`."""
    validate_mul_error(lhs=lhs, rhs=rhs, error=error, msg=msg)


@pytest.mark.parametrize(
    argnames="cycle, power, expected_value",
    argvalues=TEST_POW,
    ids=[f"{p}**{q}={r}" for p, q, r in TEST_POW],
)
def test_pow(cycle, power, expected_value) -> None:
    """Tests for the method `__pow__()`."""
    validate_pow(item=cycle, power=power, expected_value=expected_value)


@pytest.mark.parametrize(
    argnames="cycle, power, error, msg",
    argvalues=TEST_POW_ERROR,
    ids=[f"{p}**{q}" for p, q, _, _ in TEST_POW_ERROR],
)
def test_pow_error(cycle, power, error, msg) -> None:
    """Tests for exceptions to the method `__pow__()`."""
    validate_pow_error(item=cycle, power=power, error=error, msg=msg)


@pytest.mark.parametrize(
    argnames="cycle, expected_value",
    argvalues=TEST_REPR,
    ids=[f"{c}.__repr__()={r}" for c, r in TEST_REPR],
)
def test_repr(cycle, expected_value) -> None:
    """Tests for the method `__repr__()`."""
    validate_repr(item=cycle, expected_value=expected_value)
