import pytest

from symmetria import CycleDecomposition
from tests.tests_cycle_decomposition.test_cases import (
    TEST_CONSTRUCTOR,
    TEST_CONSTRUCTOR_ERROR,
)


@pytest.mark.parametrize(
    argnames="cycle_decomposition",
    argvalues=TEST_CONSTRUCTOR,
    ids=[str(p) for p in TEST_CONSTRUCTOR],
)
def test_constructor(cycle_decomposition) -> None:
    """Tests for the constructor `__init__()`."""
    _ = CycleDecomposition(*cycle_decomposition)


@pytest.mark.parametrize(
    argnames="cycle_decomposition, error, msg",
    argvalues=TEST_CONSTRUCTOR_ERROR,
    ids=[msg for _, _, msg in TEST_CONSTRUCTOR_ERROR],
)
def test_constructor_error(cycle_decomposition, error, msg) -> None:
    """Tests for exceptions to the constructor `__init__()`."""
    with pytest.raises(error, match=msg):
        _ = CycleDecomposition(*cycle_decomposition)
