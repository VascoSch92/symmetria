import pytest

from symmetria import Cycle, CycleDecomposition
from tests.test_utils import _check_values
from tests.tests_elements.tests_cycle_decomposition.test_cases import (
    TEST_EQ,
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
    argnames="cycle_decomposition, expected_value",
    argvalues=TEST_BOOL,
    ids=[f"bool({c})={b}" for c, b in TEST_BOOL],
)
def test_bool(cycle_decomposition, expected_value) -> None:
    """Tests for the method `__bool__()`."""
    _check_values(
        expression=f"bool({cycle_decomposition.rep()})", evaluation=bool(cycle_decomposition), expected=expected_value
    )


@pytest.mark.parametrize(
    argnames="cycle_decomposition, call_on, expected_value",
    argvalues=TEST_CALL,
    ids=[f"{p.rep()}({ens})" for p, ens, _ in TEST_CALL],
)
def test_call(cycle_decomposition, call_on, expected_value) -> None:
    """Tests for the method `__call__()`."""
    _check_values(
        expression=f"{cycle_decomposition.rep()}({call_on})",
        evaluation=cycle_decomposition(call_on),
        expected=expected_value,
    )


@pytest.mark.parametrize(
    argnames="cycle_decomposition, call_on, error, msg",
    argvalues=TEST_CALL_ERROR,
    ids=[msg for _, _, _, msg in TEST_CALL_ERROR],
)
def test_call_error(cycle_decomposition, call_on, error, msg) -> None:
    """Tests for exceptions to the method `__call__()`."""
    with pytest.raises(error, match=msg):
        _ = cycle_decomposition(call_on)


@pytest.mark.parametrize(
    argnames="lhs, rhs, expected_value",
    argvalues=TEST_EQ,
    ids=[f"{lhs}={rhs}" for lhs, rhs, _ in TEST_EQ],
)
def test_eq(lhs, rhs, expected_value) -> None:
    """Tests for the method `__eq__()`."""
    _check_values(expression=f"{lhs.__repr__()}=={rhs.__repr__()}", evaluation=(lhs == rhs), expected=expected_value)


@pytest.mark.parametrize(
    argnames="cycle_decomposition, idx, expected_value",
    argvalues=TEST_GETITEM,
    ids=[f"{c}[{i}]={e}" for c, i, e in TEST_GETITEM],
)
def test_getitem(cycle_decomposition, idx, expected_value) -> None:
    """Tests for the method `__getitem__()`."""
    _check_values(
        expression=f"{cycle_decomposition.rep()}[{idx}]", evaluation=cycle_decomposition[idx], expected=expected_value
    )


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
    with pytest.raises(error, match=msg):
        _ = lhs * rhs


@pytest.mark.parametrize(
    argnames="cycle_decomposition, power, expected_value",
    argvalues=TEST_POW,
    ids=[f"{p}**{q}={r}" for p, q, r in TEST_POW],
)
def test_pow(cycle_decomposition, power, expected_value) -> None:
    """Tests for the method `__pow__()`."""
    _check_values(
        expression=f"{cycle_decomposition.rep()} ** {power}",
        evaluation=cycle_decomposition**power,
        expected=expected_value,
    )


@pytest.mark.parametrize(
    argnames="cycle_decomposition, power, error, msg",
    argvalues=TEST_POW_ERROR,
    ids=[f"{p}**{q}" for p, q, _, _ in TEST_POW_ERROR],
)
def test_pow_error(cycle_decomposition, power, error, msg) -> None:
    """Tests for exceptions to the method `__pow__()`."""
    with pytest.raises(error, match=msg):
        _ = cycle_decomposition**power


@pytest.mark.parametrize(
    argnames="cycle_decomposition, expected_value",
    argvalues=TEST_REPR,
    ids=[f"{c}.__repr__()={r}" for c, r in TEST_REPR],
)
def test_repr(cycle_decomposition, expected_value) -> None:
    """Tests for the method `__repr__()`."""
    _check_values(
        expression=f"{cycle_decomposition.typename}.__repr__()",
        evaluation=cycle_decomposition.__repr__(),
        expected=expected_value,
    )
