import pytest

from symmetria import Permutation
from tests.tests_permutation.test_cases import (
    TEST_CONSTRUCTOR,
    TEST_CONSTRUCTOR_ERROR,
    TEST_CONSTRUCTOR_FROM_DICT,
    TEST_CONSTRUCTOR_FROM_LIST,
    TEST_CONSTRUCTOR_FROM_TUPLE,
    TEST_CONSTRUCTOR_FROM_CYCLE,
    TEST_CONSTRUCTOR_FROM_CYCLE_DECOMPOSITION,
)
from tests.utils import error_message


@pytest.mark.parametrize(
    argnames="permutation",
    argvalues=TEST_CONSTRUCTOR,
    ids=[str(p) for p in TEST_CONSTRUCTOR],
)
def test_constructor(permutation) -> None:
    """Tests for the constructor `__init__()`."""
    _ = Permutation(*permutation)


@pytest.mark.parametrize(
    argnames="permutation, error, msg",
    argvalues=TEST_CONSTRUCTOR_ERROR,
    ids=[msg for _, _, msg in TEST_CONSTRUCTOR_ERROR],
)
def test_constructor_error(permutation, error, msg) -> None:
    """Tests for exceptions to the constructor `__init__()`."""
    with pytest.raises(error, match=msg):
        _ = Permutation(*permutation)


@pytest.mark.parametrize(
    argnames="dict_permutation, expected_permutation",
    argvalues=TEST_CONSTRUCTOR_FROM_DICT,
    ids=[f"{d}->{p}" for d, p, in TEST_CONSTRUCTOR_FROM_DICT],
)
def test_constructor_from_dict(dict_permutation, expected_permutation) -> None:
    """Tests for the constructor method `from_dict()`."""
    if Permutation.from_dict(dict_permutation) != expected_permutation:
        raise ValueError(
            error_message(
                expected=expected_permutation,
                got=Permutation.from_dict(dict_permutation),
            )
        )


@pytest.mark.parametrize(
    argnames="list_permutation, expected_permutation",
    argvalues=TEST_CONSTRUCTOR_FROM_LIST,
    ids=[f"{list_permutation}->{p}" for list_permutation, p in TEST_CONSTRUCTOR_FROM_LIST],
)
def test_constructor_from_list(list_permutation, expected_permutation) -> None:
    """Tests for the constructor method `from_list()`."""
    if Permutation.from_list(list_permutation) != expected_permutation:
        raise ValueError(
            error_message(
                expected=expected_permutation,
                got=Permutation.from_list(list_permutation),
            )
        )


@pytest.mark.parametrize(
    argnames="tuple_permutation, expected_permutation",
    argvalues=TEST_CONSTRUCTOR_FROM_TUPLE,
    ids=[f"{t}->{p}" for t, p in TEST_CONSTRUCTOR_FROM_TUPLE],
)
def test_constructor_from_tuple(tuple_permutation, expected_permutation) -> None:
    """Tests for the constructor method `from_tuple()`."""
    if Permutation.from_tuple(tuple_permutation) != expected_permutation:
        raise ValueError(
            error_message(
                expected=expected_permutation,
                got=Permutation.from_tuple(tuple_permutation),
            )
        )


@pytest.mark.parametrize(
    argnames="cycle, expected_permutation",
    argvalues=TEST_CONSTRUCTOR_FROM_CYCLE,
    ids=[f"{c}->{p}" for c, p in TEST_CONSTRUCTOR_FROM_CYCLE],
)
def test_constructor_from_cycle(cycle, expected_permutation) -> None:
    """Tests for the constructor method `from_cycle()`."""
    if Permutation.from_cycle(cycle) != expected_permutation:
        raise ValueError(
            error_message(
                expected=expected_permutation,
                got=Permutation.from_cycle(cycle),
            )
        )


@pytest.mark.parametrize(
    argnames="cycle_decomposition, expected_permutation",
    argvalues=TEST_CONSTRUCTOR_FROM_CYCLE_DECOMPOSITION,
    ids=[f"{c}->{p}" for c, p in TEST_CONSTRUCTOR_FROM_CYCLE_DECOMPOSITION],
)
def test_constructor_from_cycle_decomposition(cycle_decomposition, expected_permutation) -> None:
    """Tests for the constructor method `from_cycle_decomposition()`."""
    if Permutation.from_cycle_decomposition(cycle_decomposition) != expected_permutation:
        raise ValueError(
            error_message(
                expected=expected_permutation,
                got=Permutation.from_cycle_decomposition(cycle_decomposition),
            )
        )

