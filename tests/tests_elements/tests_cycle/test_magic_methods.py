import pytest

from tests.test_utils import _check_values
from tests.tests_elements.tests_cycle.test_cases import (
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
    _check_values(expression=f"bool({cycle.rep()})", evaluation=bool(cycle), expected=expected_value)


@pytest.mark.parametrize(
    argnames="cycle, call_on, expected_value",
    argvalues=TEST_CALL,
    ids=[f"{p.rep()}({ens})" for p, ens, _ in TEST_CALL],
)
def test_call(cycle, call_on, expected_value) -> None:
    """Tests for the method `__call__()`."""
    _check_values(expression=f"{cycle.rep()}({call_on})", evaluation=cycle(call_on), expected=expected_value)


@pytest.mark.parametrize(
    argnames="cycle, call_on, error, msg",
    argvalues=TEST_CALL_ERROR,
    ids=[msg for _, _, _, msg in TEST_CALL_ERROR],
)
def test_call_error(cycle, call_on, error, msg) -> None:
    """Tests for exceptions to the method `__call__()`."""
    with pytest.raises(error, match=msg):
        _ = cycle(call_on)


@pytest.mark.parametrize(
    argnames="lhs, rhs, expected_value",
    argvalues=TEST_EQ,
    ids=[f"{lhs}={rhs}" for lhs, rhs, _ in TEST_EQ],
)
def test_eq(lhs, rhs, expected_value) -> None:
    """Tests for the method `__eq__()`."""
    _check_values(expression=f"{lhs.__repr__()}=={rhs.__repr__()}", evaluation=(lhs == rhs), expected=expected_value)


@pytest.mark.parametrize(
    argnames="cycle, idx, expected_value",
    argvalues=TEST_GETITEM,
    ids=[f"{c}[{i}]={e}" for c, i, e in TEST_GETITEM],
)
def test_getitem(cycle, idx, expected_value) -> None:
    """Tests for the method `__getitem__()`."""
    _check_values(expression=f"{cycle.rep()}[{idx}]", evaluation=cycle[idx], expected=expected_value)


@pytest.mark.parametrize(
    argnames="cycle, expected_value",
    argvalues=TEST_INT,
    ids=[f"int({c})={i}" for c, i in TEST_INT],
)
def test_int(cycle, expected_value) -> None:
    """Tests for the method `__int__()`."""
    _check_values(expression=f"int({cycle.rep()})", evaluation=int(cycle), expected=expected_value)


@pytest.mark.parametrize(
    argnames="cycle, expected_value",
    argvalues=TEST_LEN,
    ids=[f"len({c})={length}" for c, length in TEST_LEN],
)
def test_len(cycle, expected_value) -> None:
    """Tests for the method `__len__()`."""
    _check_values(expression=f"len({cycle.rep()})", evaluation=len(cycle), expected=expected_value)


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
    argnames="cycle, power, expected_value",
    argvalues=TEST_POW,
    ids=[f"{p}**{q}={r}" for p, q, r in TEST_POW],
)
def test_pow(cycle, power, expected_value) -> None:
    """Tests for the method `__pow__()`."""
    _check_values(expression=f"{cycle.rep()} ** {power}", evaluation=cycle**power, expected=expected_value)


@pytest.mark.parametrize(
    argnames="cycle, power, error, msg",
    argvalues=TEST_POW_ERROR,
    ids=[f"{p}**{q}" for p, q, _, _ in TEST_POW_ERROR],
)
def test_pow_error(cycle, power, error, msg) -> None:
    """Tests for exceptions to the method `__pow__()`."""
    with pytest.raises(error, match=msg):
        _ = cycle**power


@pytest.mark.parametrize(
    argnames="cycle, expected_value",
    argvalues=TEST_REPR,
    ids=[f"{c}.__repr__()={r}" for c, r in TEST_REPR],
)
def test_repr(cycle, expected_value) -> None:
    """Tests for the method `__repr__()`."""
    _check_values(expression=f"{cycle.typename}.__repr__()", evaluation=cycle.__repr__(), expected=expected_value)
