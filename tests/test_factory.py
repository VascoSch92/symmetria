from typing import Any, Set, Dict, List, Type, Tuple

import pytest

from symmetria import CycleDecomposition


def _check_values(expression: str, evaluation: Any, expected: Any) -> None:
    if evaluation != expected:
        raise ValueError(f"The expression `{expression}` must evaluate {expected}, but got {evaluation}.")


##############################
# GENERIC METHODS VALIDATORS #
##############################


def validate_ascents(item: Any, expected_value: List[int]) -> None:
    _check_values(expression=f"{item.rep()}.ascents()", evaluation=item.ascents(), expected=expected_value)


def validate_cycle_decomposition(item: Any, expected_value: CycleDecomposition) -> None:
    _check_values(
        expression=f"{item.rep()}.cycle_notation()", evaluation=item.cycle_decomposition(), expected=expected_value
    )


def validate_cycle_type(item: Any, expected_value: Tuple[int]) -> None:
    _check_values(expression=f"{item.rep()}.cycle_type()", evaluation=item.cycle_type(), expected=expected_value)


def validate_cycle_notation(item: Any, expected_value: str) -> None:
    _check_values(expression=f"{item.rep()}.cycle_notation()", evaluation=item.cycle_notation(), expected=expected_value)


def validate_descents(item: Any, expected_value: List[int]) -> None:
    _check_values(expression=f"{item.rep()}.descents()", evaluation=item.descents(), expected=expected_value)


def validate_exceedances(item: Any, weakly: bool, expected_value: List[int]) -> None:
    _check_values(
        expression=f"{item.rep()}.exceedances(weakly={weakly})",
        evaluation=item.exceedances(weakly=weakly),
        expected=expected_value,
    )


def validate_inverse(item: Any, expected_value: Any) -> None:
    _check_values(expression=f"{item.rep()}.inverse()", evaluation=item.inverse(), expected=expected_value)


def validate_inversions(item: Any, expected_value: List[Tuple[int, int]]) -> None:
    _check_values(expression=f"{item.rep()}.inversions()", evaluation=item.inversions(), expected=expected_value)


def validate_is_conjugate(item: Any, other: Any, expected_value: bool) -> None:
    _check_values(
        expression=f"{item.rep()}.is_conjugate({other.rep()})",
        evaluation=item.is_conjugate(other),
        expected=expected_value,
    )


def validate_is_derangement(item: Any, expected_value: bool) -> None:
    _check_values(expression=f"{item.rep()}.is_derangement()", evaluation=item.is_derangement(), expected=expected_value)


def validate_is_even(item: Any, expected_value: bool) -> None:
    _check_values(expression=f"{item.rep()}.is_even()", evaluation=item.is_even(), expected=expected_value)


def validate_is_odd(item: Any, expected_value: bool) -> None:
    _check_values(expression=f"{item.rep()}.is_odd()", evaluation=item.is_odd(), expected=expected_value)


def validate_is_regular(item: Any, expected_value: bool) -> None:
    _check_values(expression=f"{item.rep()}.is_regular()", evaluation=item.is_regular(), expected=expected_value)


def validate_equivalent(lhs: Any, rhs: Any, expected_value: bool) -> None:
    _check_values(
        expression=f"{lhs.rep()}.equivalent({rhs.__repr__()})",
        evaluation=lhs.equivalent(other=rhs),
        expected=expected_value,
    )


def validate_domain(item: Any, expected_value: bool) -> None:
    _check_values(expression=f"{item.rep()}.domain()", evaluation=item.domain, expected=expected_value)


def validate_map(item: Any, expected_value: Dict[int, int]) -> None:
    _check_values(expression=f"{item.rep()}.map()", evaluation=item.map, expected=expected_value)


def validate_orbit(element: Any, item: Any, expected_value: int) -> None:
    _check_values(
        expression=f"{element.rep()}.orbit({item})", evaluation=element.orbit(item=item), expected=expected_value
    )


def validate_order(item: Any, expected_value: int) -> None:
    _check_values(expression=f"{item.rep()}.order()", evaluation=item.order(), expected=expected_value)


def validate_sgn(item: Any, expected_value: int) -> None:
    _check_values(expression=f"{item.rep()}.sgn()", evaluation=item.sgn(), expected=expected_value)


def validate_support(item: Any, expected_value: Set[int]) -> None:
    _check_values(expression=f"{item.rep()}.support()", evaluation=item.support(), expected=expected_value)


############################
# MAGIC METHODS VALIDATORS #
############################


def validate_bool(item: Any, expected_value: bool) -> None:
    _check_values(expression=f"bool({item.rep()})", evaluation=bool(item), expected=expected_value)


def validate_call(item: Any, call_on: Any, expected_value: Any) -> None:
    _check_values(expression=f"{item.rep()}({call_on})", evaluation=item(call_on), expected=expected_value)


def validate_call_error(item: Any, call_on: Any, error: Type[Exception], msg: str) -> None:
    with pytest.raises(error, match=msg):
        _ = item(call_on)


def validate_eq(lhs: Any, rhs: Any, expected_value: bool) -> None:
    _check_values(expression=f"{lhs.__repr__()}=={rhs.__repr__()}", evaluation=(lhs == rhs), expected=expected_value)


def validate_getitem(item: Any, idx: int, expected_value: int) -> None:
    _check_values(expression=f"{item.rep()}[{idx}]", evaluation=item[idx], expected=expected_value)


def validate_int(item: Any, expected_value: int) -> None:
    _check_values(expression=f"int({item.rep()})", evaluation=int(item), expected=expected_value)


def validate_len(item: Any, expected_value: int) -> None:
    _check_values(expression=f"len({item.rep()})", evaluation=len(item), expected=expected_value)


def validate_mul(lhs: Any, rhs: Any, expected_value: Any) -> None:
    _check_values(expression=f"{lhs.rep()}*{rhs.rep()}", evaluation=lhs * rhs, expected=expected_value)


def validate_mul_error(lhs: Any, rhs: Any, error: Type[Exception], msg: str) -> None:
    with pytest.raises(error, match=msg):
        _ = lhs * rhs


def validate_pow(item: Any, power: int, expected_value: Any) -> None:
    _check_values(expression=f"{item.rep()} ** {power}", evaluation=item**power, expected=expected_value)


def validate_pow_error(item: Any, power: Any, error: Type[Exception], msg: str) -> None:
    with pytest.raises(error, match=msg):
        _ = item**power


def validate_repr(item: Any, expected_value: str) -> None:
    _check_values(expression=f"{item.name}.__repr__()", evaluation=item.__repr__(), expected=expected_value)


def validate_str(item: Any, expected_value: str) -> None:
    _check_values(expression=f"{item.rep()}.__str__()", evaluation=item.__str__(), expected=expected_value)


@pytest.mark.parametrize(
    argnames="expression, evaluation, expected",
    argvalues=[
        ("test_1", 1, 1),
        ("test_2", "a", "a"),
        ("test_3", [], []),
        ("test_4", [1, 2, 3], [1, 2, 3]),
    ],
)
def test_check_value(expression, evaluation, expected) -> None:
    _check_values(expression=expression, evaluation=evaluation, expected=expected)


@pytest.mark.parametrize(
    argnames="expression, evaluation, expected, message",
    argvalues=[
        ("test_1", 1, 0, "The expression `test_1` must evaluate 0, but got 1."),
        ("test_2", "a", "b", "The expression `test_2` must evaluate b, but got a."),
        ("test_3", [], {}, r"The expression `test_3` must evaluate \{\}, but got \[\]."),
    ],
)
def test_check_value_raise_exception(expression, evaluation, expected, message) -> None:
    with pytest.raises(ValueError, match=message):
        _check_values(expression=expression, evaluation=evaluation, expected=expected)
