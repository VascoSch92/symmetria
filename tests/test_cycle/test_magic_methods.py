import pytest

from tests.test_cycle.test_cases import (
    TEST_BOOL,
)
from tests.utils import error_message


@pytest.mark.parametrize(
    argnames="cycle, expected_output",
    argvalues=TEST_BOOL,
    ids=[f"bool({c})={b}" for c, b in TEST_BOOL]
)
def test_bool(cycle, expected_output) -> None:
    """Tests for the method `__bool__()`."""
    if bool(cycle) != expected_output:
        raise ValueError(error_message(expected=expected_output, got=bool(cycle)))
