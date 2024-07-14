from typing import List, Generator

from symmetria import Permutation
from symmetria.generators._validators import _check_degree_parameter, _check_algorithm_parameter
from symmetria.generators.algorithm._algorithms import (
    _heap,
    _lexicographic,
    _steinhaus_johnson_trotter,
)

__all__ = ["generate"]

_SUPPORTED_ALGORITHM: List[str] = [
    "lexicographic",
    "heap",
    "steinhaus-johnson-trotter",
]


def generate(degree: int, algorithm: str = "lexicographic") -> Generator[Permutation, None, None]:
    """Generate all the permutations of the given degree based on the chosen algorithm.

    The method generates all the permutations of the given degree using the specified algorithm.

    :param degree: The degree of the permutations to be generated. Must be a non-zero positive integer.
    :type degree: int
    :param algorithm: The algorithm to use for generating permutations.
        It must be one of: ``lexicographic``, ``heap``.
        Default is ``lexicographic``.
    :type algorithm: str, optional

    :return: A generator yielding permutations.
    :rtype: Generator["Permutation", None, None]

    :raises ValueError: If the algorithm is not supported or the degree is invalid.

    :examples:
        >>> import symmetria
        ...
        >>> permutations = symmetria.generate(degree=3, algorithm="lexicographic")
        >>> for permutation in permutations:
        ...     permutation
        Permutation(1, 2, 3)
        Permutation(1, 3, 2)
        Permutation(2, 1, 3)
        Permutation(2, 3, 1)
        Permutation(3, 1, 2)
        Permutation(3, 2, 1)
    """
    _check_algorithm_parameter(value=algorithm, supported=_SUPPORTED_ALGORITHM)
    _check_degree_parameter(value=degree)
    return _relevant_generator(algorithm=algorithm, degree=degree)


def _relevant_generator(algorithm: str, degree: int) -> Generator[Permutation, None, None]:
    """Private method to pick the correct algorithm for generating permutations."""
    if algorithm == "lexicographic":
        return _lexicographic(degree=degree, start=list(range(1, degree + 1)))
    elif algorithm == "heap":
        return _heap(degree=degree, start=list(range(1, degree + 1)))
    elif algorithm == "steinhaus-johnson-trotter":
        return _steinhaus_johnson_trotter(degree=degree, start=list(range(1, degree + 1)))
