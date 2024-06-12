import sys

from symmetria.cli._commands import (
    _Style,
    _execute_help_command,
    _execute_error_message,
    _execute_version_command,
    _execute_permutation_command,
)


def run_command_line_interface() -> None:
    """Run and manage the command line interface."""
    commands = sys.argv[1:]

    # case where no commands are provided
    if len(commands) == 0:
        _execute_error_message(
            message="no command provided",
            exit_code=1,
        )

    # case where one command is provided
    elif len(commands) == 1:
        command = commands[0]
        if _is_a_flag(command=command):
            if command in {"-h", "--help"}:
                _execute_help_command()
            elif command in {"-v", "--version"}:
                _execute_version_command()
            _execute_error_message(
                message=f"unexpected argument `{_Style.YELLOW}{command}{_Style.END}` found",
                exit_code=1,
            )
        elif _is_a_permutation(command=command):
            _execute_permutation_command(permutation=command)
        _execute_error_message(
            message=f"unexpected argument `{_Style.YELLOW}{command}{_Style.END}` found",
            exit_code=1,
        )

    # otherwise
    _execute_error_message(
        message=f"Expected 1 command, but got {_Style.YELLOW}{len(sys.argv) - 1}{_Style.END} commands",
        exit_code=1,
    )


def _is_a_flag(command: str) -> bool:
    """Check if an argument has to be interpreted as a flag."""
    return command.startswith(("-", "--"))


def _is_a_permutation(command: str) -> bool:
    """Check if an argument has to be interpreted as a permutation."""
    return command.isdigit()
