import pytest

from symmetria import Permutation
from tests.tests_factory import (
    validate_from_dict,
    validate_from_cycle,
    validate_from_cycle_decomposition,
)
from tests.tests_permutation.test_cases import (
    TEST_CONSTRUCTOR,
    TEST_CONSTRUCTOR_ERROR,
    TEST_CONSTRUCTOR_FROM_DICT,
    TEST_CONSTRUCTOR_FROM_CYCLE,
    TEST_CONSTRUCTOR_FROM_CYCLE_DECOMPOSITION,
)


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
    argnames="dict_permutation, expected_value",
    argvalues=TEST_CONSTRUCTOR_FROM_DICT,
    ids=[f"{d}->{p}" for d, p in TEST_CONSTRUCTOR_FROM_DICT],
)
def test_constructor_from_dict(dict_permutation, expected_value) -> None:
    """Tests for the constructor method `from_dict()`."""
    validate_from_dict(
        class_=Permutation, constructor=dict_permutation, expected_value=expected_value
    )


@pytest.mark.parametrize(
    argnames="cycle, expected_value",
    argvalues=TEST_CONSTRUCTOR_FROM_CYCLE,
    ids=[f"{c}->{p}" for c, p in TEST_CONSTRUCTOR_FROM_CYCLE],
)
def test_constructor_from_cycle(cycle, expected_value) -> None:
    """Tests for the constructor method `from_cycle()`."""
    validate_from_cycle(
        class_=Permutation, constructor=cycle, expected_value=expected_value
    )


@pytest.mark.parametrize(
    argnames="cycle_decomposition, expected_value",
    argvalues=TEST_CONSTRUCTOR_FROM_CYCLE_DECOMPOSITION,
    ids=[f"{c}->{p}" for c, p in TEST_CONSTRUCTOR_FROM_CYCLE_DECOMPOSITION],
)
def test_constructor_from_cycle_decomposition(
    cycle_decomposition, expected_value
) -> None:
    """Tests for the constructor method `from_cycle_decomposition()`."""
    validate_from_cycle_decomposition(
        class_=Permutation,
        constructor=cycle_decomposition,
        expected_value=expected_value,
    )
