import sys

from symmetria.elements.cycle import Cycle
from symmetria.generators.api import generate
from symmetria.elements.permutation import Permutation
from symmetria.elements.cycle_decomposition import CycleDecomposition

__version__ = "0.1.1"
__all__ = ["__version__", "generate", "Permutation", "Cycle", "CycleDecomposition"]


def _log_version() -> None:
    """Private method which take a command line argument and log the version of `symmetria`."""
    if len(sys.argv) == 0 or len(sys.argv) == 1:
        raise Exception("No command provided.")
    elif len(sys.argv) == 2:
        if sys.argv[1] == "--version":
            print(f"v{__version__}")
        else:
            raise ValueError(f"command not found: {sys.argv[1]}")

    else:
        raise ValueError(f"Expected 1 command, but got {len(sys.argv) -1}")


if __name__ == "__main__":
    _log_version()
