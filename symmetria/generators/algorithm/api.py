import warnings
from typing import Dict, Final, Callable, Generator

from symmetria import Permutation
from symmetria.generators._validators import _check_degree_parameter, _check_algorithm_parameter
from symmetria.generators.algorithm._algorithms import (
    _heap,
    _zaks,
    _lexicographic,
    _steinhaus_johnson_trotter,
)

__all__ = ["generate", "permutation_generator"]

_SUPPORTED_ALGORITHMS: Final[Dict[str, Callable]] = {
    "lexicographic": _lexicographic,
    "heap": _heap,
    "steinhaus-johnson-trotter": _steinhaus_johnson_trotter,
    "zaks": _zaks,
}


def generate(degree: int, algorithm: str = "lexicographic") -> Generator[Permutation, None, None]:
    """Generate all the permutations of the given degree based on the chosen algorithm.

    :warning: This function will be deprecated in a future version. Use 'permutation_generator' instead.

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
    warnings.warn(
        "This function will be deprecated in a future version. Use 'permutation_generator' instead.",
        PendingDeprecationWarning,
        stacklevel=1,
    )
    _check_algorithm_parameter(value=algorithm, supported=list(_SUPPORTED_ALGORITHMS.keys()))
    _check_degree_parameter(value=degree)
    return _relevant_generator(algorithm=algorithm, degree=degree)


def permutation_generator(degree: int, algorithm: str = "lexicographic") -> Generator[Permutation, None, None]:
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
        >>> from symmetria import permutation_generator
        ...
        >>> permutations = permutation_generator(degree=3, algorithm="lexicographic")
        >>> for permutation in permutations:
        ...     permutation
        Permutation(1, 2, 3)
        Permutation(1, 3, 2)
        Permutation(2, 1, 3)
        Permutation(2, 3, 1)
        Permutation(3, 1, 2)
        Permutation(3, 2, 1)
    """
    _check_algorithm_parameter(value=algorithm, supported=list(_SUPPORTED_ALGORITHMS.keys()))
    _check_degree_parameter(value=degree)
    return _relevant_generator(algorithm=algorithm, degree=degree)


def _relevant_generator(algorithm: str, degree: int) -> Generator[Permutation, None, None]:
    """Private method to pick the correct algorithm for generating permutations."""
    if algorithm in _SUPPORTED_ALGORITHMS:
        return _SUPPORTED_ALGORITHMS[algorithm](degree=degree)
    raise ValueError(
        f"The given algorithm ({algorithm}) is not supported. \n "
        f"Here, a list of supported algorithm for generations of permutations {list(_SUPPORTED_ALGORITHMS.keys())}."
    )
