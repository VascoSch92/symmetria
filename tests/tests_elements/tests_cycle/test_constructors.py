import pytest

from symmetria import Cycle
from tests.tests_elements.tests_cycle.test_cases import (
    TEST_CONSTRUCTOR,
    TEST_CONSTRUCTOR_ERROR,
)


@pytest.mark.parametrize(
    argnames="cycle",
    argvalues=TEST_CONSTRUCTOR,
    ids=[str(c) for c in TEST_CONSTRUCTOR],
)
def test_constructor(cycle) -> None:
    """Tests for the constructor `__init__()`."""
    _ = Cycle(*cycle)


@pytest.mark.parametrize(
    argnames="cycle, error, msg",
    argvalues=TEST_CONSTRUCTOR_ERROR,
    ids=[msg for _, _, msg in TEST_CONSTRUCTOR_ERROR],
)
def test_constructor_error(cycle, error, msg) -> None:
    """Tests for exceptions to the constructor `__init__()`."""
    with pytest.raises(error, match=msg):
        _ = Cycle(*cycle)
