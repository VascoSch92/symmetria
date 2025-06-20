import sys

from symmetria import Permutation, __version__


class _Style:
    """Class to define the output messages style."""

    YELLOW: str = "\033[33m"
    RED: str = "\033[31m"
    END: str = "\033[0m"
    BOLD: str = "\033[1m"
    UNDERLINE: str = "\033[4m"


def _execute_error_message(message: str, exit_code: int) -> None:
    """Print an error message in case of wrong given commands."""
    sys.stderr.write(
        f"{_Style.RED}{_Style.BOLD}Error:{_Style.END} {message}. \n "
        f"For more information, try `{_Style.YELLOW}--help{_Style.END}`, or `{_Style.YELLOW}-h{_Style.END}`. \n"
    )
    sys.exit(exit_code)


def _execute_help_command() -> None:
    """Execute the `--help`, or `-h`, command."""
    sys.stdout.write(
        "Symmetria, an intuitive framework for working with the symmetric group and its elements.\n"
        "\n"
        f"{_Style.UNDERLINE}Usage:{_Style.END} symmetria <ARGUMENT> [OPTIONS] \n"
        "\n"
        f"{_Style.UNDERLINE}Options:{_Style.END} \n"
        " -h, --help        Print help \n"
        " -v, --version     Print version \n"
        "\n"
        f"{_Style.UNDERLINE}Argument (optional):{_Style.END} \n"
        " permutation       A permutation you want to learn more about. \n"
        "                   The permutation must be given in its one-line format, i.e., \n"
        "                   for the permutation Permutation(2, 3, 1), write 231. \n"
    )
    sys.exit(0)


def _execute_permutation_command(permutation: str) -> None:
    """Execute the command when a permutation is given."""
    parsed_permutation = _parse_permutation(permutation=permutation)
    sys.stdout.write(parsed_permutation.describe() + "\n")
    sys.exit(0)


def _execute_version_command() -> None:
    """Execute the `--version`, or `-v`, command."""
    sys.stdout.write(f"{_Style.BOLD}v{_Style.END}{__version__}" + "\n")
    sys.exit(0)


def _parse_permutation(permutation: str) -> Permutation:
    """Convert the provided string into a `Permutation` object."""
    return Permutation(*[int(d) for d in permutation])
