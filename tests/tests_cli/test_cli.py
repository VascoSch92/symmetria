import pytest

from tests.test_utils import _check_values
from symmetria.cli.cli import (
    _is_a_flag,
    _is_a_permutation,
)
from symmetria.cli._commands import (
    _parse_permutation,
    _execute_help_command,
    _execute_error_message,
    _execute_version_command,
    _execute_permutation_command,
)
from tests.tests_cli.test_cases import (
    TEST_IS_A_FLAG,
    TEST_IS_PERMUTATION,
    TEST_PARSE_PERMUTATION,
)


@pytest.mark.parametrize(
    argnames="command, expected_value",
    argvalues=TEST_IS_A_FLAG,
    ids=[f"_is_a_flag('{command}') = {b}" for command, b in TEST_IS_A_FLAG],
)
def test_is_a_flag(command, expected_value) -> None:
    """Test method `_is_a_flag()`."""
    _check_values(
        expression=f"_is_a_flag('{command}') = {expected_value}",
        evaluation=_is_a_flag(command=command),
        expected=expected_value,
    )


@pytest.mark.parametrize(
    argnames="command, expected_value",
    argvalues=TEST_IS_PERMUTATION,
    ids=[f"_is_a_permutation('{command}') = {b}" for command, b in TEST_IS_PERMUTATION],
)
def test_is_a_permutation(command, expected_value) -> None:
    """Test method `_is_a_permutation()`."""
    _check_values(
        expression=f"_is_a_permutation('{command}')",
        evaluation=_is_a_permutation(command=command),
        expected=expected_value,
    )


@pytest.mark.parametrize(
    argnames="permutation, expected_value",
    argvalues=TEST_PARSE_PERMUTATION,
    ids=[f"_parse_permutation('{p}') = {b}" for p, b in TEST_PARSE_PERMUTATION],
)
def test_parse_permutation(permutation, expected_value) -> None:
    """Test method `_parse_permutation()`."""
    _check_values(
        expression=f"_parse_permutation('{permutation}')",
        evaluation=_parse_permutation(permutation=permutation),
        expected=expected_value,
    )


def test_execute_version_command() -> None:
    with pytest.raises(SystemExit):
        _execute_version_command()


def test_execute_error_message() -> None:
    with pytest.raises(SystemExit):
        _execute_error_message("hello-world", 2)


def test_execute_help_command() -> None:
    with pytest.raises(SystemExit):
        _execute_help_command()


def test_permutation_command() -> None:
    with pytest.raises(SystemExit):
        _execute_permutation_command(permutation="123")
