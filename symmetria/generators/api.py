from typing import List, Generator

from symmetria.generators._algorithms import (
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


def generate(degree: int, algorithm: str = "lexicographic") -> Generator["Permutation", None, None]:
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
    _check_algorithm_parameter(value=algorithm)
    _check_degree_parameter(value=degree)
    return _relevant_generator(algorithm=algorithm, degree=degree)


def _check_algorithm_parameter(value: str) -> None:
    """Private method to check the value provided for the parameter `algorithm`.

    Recall that the parameter `algorithm` must be a string present in the list _SUPPORTED_ALGORITHM
    """
    if isinstance(value, str) is False:
        raise TypeError(f"The parameter `algorithm` must be of type string, but {type(value)} was provided.")
    if value not in _SUPPORTED_ALGORITHM:
        raise ValueError(
            f"The given algorithm ({value}) is not supported. \n "
            f"Here, a list of supported algorithm for generations of permutations {_SUPPORTED_ALGORITHM}."
        )


def _check_degree_parameter(value: int) -> None:
    """Private method to check the value provided for the parameter `degree`.

    Recall that the parameter `degree` must be a non-negative integer different from zero.
    """
    if isinstance(value, int) is False:
        raise TypeError(f"The parameter `degree` must be of type int, but {type(value)} was provided.")
    if value < 1:
        raise ValueError(f"The parameter `degree` must be a non-zero positive integer, but {value} was provided.")


def _relevant_generator(algorithm: str, degree: int) -> Generator["Permutation", None, None]:
    """Private method to pick the correct algorithm for generating permutations."""
    if algorithm == "lexicographic":
        return _lexicographic(degree=degree, start=list(range(1, degree + 1)))
    elif algorithm == "heap":
        return _heap(degree=degree, start=list(range(1, degree + 1)))
    elif algorithm == "steinhaus-johnson-trotter":
        return _steinhaus_johnson_trotter(degree=degree, start=list(range(1, degree + 1)))
