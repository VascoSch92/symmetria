import pytest

from symmetria.elements.cycle import Cycle
from symmetria.elements.cycle_decomposition import CycleDecomposition
from tests.tests_cycle_decomposition.test_cases import (
    TEST_BOOL,
    TEST_EQ,
    TEST_GETITEM,
    TEST_REPR,
    TEST_CALL,
    TEST_CALL_ERROR,
    TEST_MUL_ERROR,
)
from tests.tests_factory import (
    validate_bool,
    validate_eq,
    validate_getitem,
    validate_repr,
    validate_call,
    validate_call_error,
    validate_mul_error,
)


@pytest.mark.parametrize(
    argnames="cycle_decomposition, expected_value",
    argvalues=TEST_BOOL,
    ids=[f"bool({c})={b}" for c, b in TEST_BOOL],
)
def test_bool(cycle_decomposition, expected_value) -> None:
    """Tests for the method `__bool__()`."""
    validate_bool(item=cycle_decomposition, expected_value=expected_value)


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
    argnames="cycle_decomposition, idx, expected_value",
    argvalues=TEST_GETITEM,
    ids=[f"{c}[{i}]={e}" for c, i, e in TEST_GETITEM],
)
def test_getitem(cycle_decomposition, idx, expected_value) -> None:
    """Tests for the method `__getitem__()`."""
    validate_getitem(item=cycle_decomposition, idx=idx, expected_value=expected_value)


def test_int() -> None:
    """Tests for the method `__int__()`."""
    with pytest.raises(NotImplementedError, match="The method is not implemented"):
        _ = int(CycleDecomposition(Cycle(1)))


@pytest.mark.parametrize(
    argnames="lhs, rhs, error, msg",
    argvalues=TEST_MUL_ERROR,
    ids=[error for _, _, _, error in TEST_MUL_ERROR],
)
def test_multiplication_error(lhs, rhs, error, msg) -> None:
    """Tests for exceptions to the method `__mul__()`."""
    validate_mul_error(lhs=lhs, rhs=rhs, error=error, msg=msg)


@pytest.mark.parametrize(
    argnames="cycle_decomposition, expected_value",
    argvalues=TEST_REPR,
    ids=[f"{c}.__repr__()={r}" for c, r in TEST_REPR],
)
def test_repr(cycle_decomposition, expected_value) -> None:
    """Tests for the method `__repr__()`."""
    validate_repr(item=cycle_decomposition, expected_value=expected_value)
