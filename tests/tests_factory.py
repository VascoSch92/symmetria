from typing import Any, Type, Dict, Set
import pytest


def error_message(expected: Any, got: Any) -> str:
    """
    Return an error message in the format "Expected: <expected>. Got <got>" comparing the expected value with
    the actual value.

    :param expected: The expected value.
    :type expected: Any
    :param got: The actual value.
    :type got: Any

    :return: A string containing the error message.
    :rtype: str
    """
    return f"Expected {expected}, but got {got}."


##########################
# CONSTRUCTOR VALIDATORS #
##########################


def validate_from_dict(class_: Any, constructor: Dict, expected_value: Any) -> None:
    if class_.from_dict(constructor) != expected_value:
        raise ValueError(
            f"The expression `{class_.__class__.__name__}.from_dict({constructor}))` must evaluate {expected_value}, "
            f"but got {class_.from_dict(constructor)}."
        )


def validate_from_list(class_: Any, constructor: Dict, expected_value: Any) -> None:
    if class_.from_list(constructor) != expected_value:
        raise ValueError(
            f"The expression `{class_.__class__.__name__}.from_list({constructor}))` must evaluate {expected_value}, "
            f"but got {class_.from_list(constructor)}."
        )


def validate_from_tuple(class_: Any, constructor: Dict, expected_value: Any) -> None:
    if class_.from_tuple(constructor) != expected_value:
        raise ValueError(
            f"The expression `{class_.__class__.__name__}.from_tuple({constructor}))` must evaluate {expected_value}, "
            f"but got {class_.from_tuple(constructor)}."
        )


def validate_from_cycle(class_: Any, constructor: Dict, expected_value: Any) -> None:
    if class_.from_cycle(constructor) != expected_value:
        raise ValueError(
            f"The expression `{class_.__class__.__name__}.from_cycle({constructor}))` must evaluate {expected_value}, "
            f"but got {class_.from_cycle(constructor)}."
        )


def validate_from_cycle_decomposition(class_: Any, constructor: Dict, expected_value: Any) -> None:
    if class_.from_cycle_decomposition(constructor) != expected_value:
        raise ValueError(
            f"The expression `{class_.__class__.__name__}.from_cycle_decomposition({constructor}))` must evaluate {expected_value}, "
            f"but got {class_.from_cycle_decomposition(constructor)}."
        )


##############################
# GENERIC METHODS VALIDATORS #
##############################

def validate_cycle_notation(item: Any, expected_value: str) -> None:
    if item.cycle_notation() != expected_value:
        raise ValueError(
            f"The expression `{item.__repr__()}.cycle_notation()` must evaluate {expected_value}, "
            f"but got {item.cycle_notation()}."
        )


def validate_is_derangement(item: Any, expected_value: bool) -> None:
    if item.is_derangement() is not expected_value:
        raise ValueError(
            f"The expression `{item.__repr__()}.is_derangement()` must evaluate {expected_value}, "
            f"but got {item.is_derangement()}."
        )


def validate_domain(item: Any, expected_value: bool) -> None:
    if item.domain() != expected_value:
        raise ValueError(
            f"The expression `{item.__repr__()}.domain()` must evaluate {expected_value}, "
            f"but got {item.domain()}."
        )


def validate_map(item:Any, expected_value: Dict[int, int]) -> None:
    if item.map() != expected_value:
        raise ValueError(
            f"The expression `{item.__repr__()}.map()` must evaluate {expected_value}, "
            f"but got {item.map()}."
        )


def validate_order(item: Any, expected_value: int) -> None:
    if item.order() != expected_value:
        raise ValueError(
            f"The expression `{item.__repr__()}.order()` must evaluate {expected_value}, "
            f"but got {item.order()}."
        )


def validate_support(item: Any, expected_value: Set[int]) -> None:
    if item.support() != expected_value:
        raise ValueError(
            f"The expression `{item.__repr__()}.support()` must evaluate {expected_value}, "
            f"but got {item.support()}."
        )

############################
# MAGIC METHODS VALIDATORS #
############################


def validate_bool(item: Any, expected_value: bool) -> None:
    if bool(item) != expected_value:
        raise ValueError(
            f"The expression `bool({item})` must evaluate {expected_value}, but got {bool(item)}."
        )


def validate_call(item: Any, call_on: Any, expected_value: Any) -> None:
    if item(call_on) != expected_value:
        raise ValueError(
            f"The expression `{item}({call_on})` must evaluate {expected_value}, but got {item(call_on)}."
        )


def validate_call_error(item: Any, call_on: Any, error: Type[Exception], msg: str) -> None:
    with pytest.raises(error, match=msg):
        _ = item(call_on)


def validate_eq(lhs: Any, rhs: Any, expected_value: bool) -> None:
    if (lhs == rhs) != expected_value:
        raise ValueError(
            f"The expression `{lhs}=={rhs}` must evaluate {expected_value}, but got {lhs == rhs}."
        )


def validate_getitem(item: Any, idx: int, expected_value: int) -> None:
    if item[idx] != expected_value:
        raise ValueError(
            f"The expression {item.__repr__()}[{idx}] must evaluate {expected_value}, but got {item[idx]}."
        )


def validate_int(item: Any, expected_value: int) -> None:
    if int(item) != expected_value:
        raise ValueError(
            f"The expression `int({item})` must evaluate {expected_value}, but got {int(item)}."
        )


def validate_len(item: Any, expected_value: int) -> None:
    if len(item) != expected_value:
        raise ValueError(
            f"The expression `len({item})` must evaluate {expected_value}, but got {len(item)}."
        )


def validate_mul(lhs: Any, rhs: Any, expected_value: Any) -> None:
    if (lhs * rhs) != expected_value:
        raise ValueError(
            f"The expression `{lhs}*{rhs}` must evaluate {expected_value}, but got {lhs*rhs}."
        )


def validate_mul_error(lhs: Any, rhs: Any, error: Type[Exception], msg: str) -> None:
    with pytest.raises(error, match=msg):
        _ = lhs*rhs


def validate_repr(item: Any, expected_value: str) -> None:
    if item.__repr__() != expected_value:
        raise ValueError(
            f"The expression `{item}.__repr__()` must evaluate {expected_value}, but got {item.__repr__()}."
        )


def validate_str(item: Any, expected_value: str) -> None:
    if item.__str__() != expected_value:
        raise ValueError(
            f"The expression `{item}.__str__()` must evaluate {expected_value}, but got {item.__str__()}."
        )
