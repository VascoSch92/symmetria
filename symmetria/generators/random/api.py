from typing import List, Generator

from symmetria import Permutation
from symmetria.generators._validators import _check_degree_parameter, _check_algorithm_parameter
from symmetria.generators.random._algorithms import (
    _random_shuffle,
    _fisher_yates_shuffle,
    _random_shuffle_generator,
    _fisher_yates_shuffle_generator,
)

__all__ = ["random", "random_generator"]

_SUPPORTED_ALGORITHM: List[str] = [
    "random",
    "fisher-yates",
]


def random(degree: int, algorithm: str = "random") -> Permutation:
    """Generate a random permutation of the given degree based on the chosen algorithm.

    The method generate a random permutation of the given degree using the specified algorithm.

    :param degree: The degree of the permutation to be generated. Must be a non-zero positive integer.
    :type degree: int
    :param algorithm: The algorithm to use for generating permutations.
        Default is ``random``.
    :type algorithm: str, optional

    :return: A permutation object.
    :rtype: Permutation

    :raises ValueError: If the algorithm is not supported or the degree is invalid.

    :examples:
        >>> import symmetria
        ...
        >>> permutation = symmetria.random(degree=3, algorithm="fisher-yates")
    """
    _check_algorithm_parameter(value=algorithm, supported=_SUPPORTED_ALGORITHM)
    _check_degree_parameter(value=degree)
    return _relevant_random_permutation(algorithm=algorithm, degree=degree)


def _relevant_random_permutation(algorithm: str, degree: int) -> Permutation:
    """Private method to pick the correct algorithm to generate the permutation."""
    if algorithm == "random":
        return _random_shuffle(permutation=list(range(1, degree + 1)))
    elif algorithm == "fisher-yates":
        return _fisher_yates_shuffle(permutation=list(range(1, degree + 1)))


def random_generator(degree: int, algorithm: str = "random") -> Generator[Permutation, None, None]:
    """Generate random permutations of the given degree based on the chosen algorithm.

    The method generates random permutations of the given degree using the specified algorithm.

    :param degree: The degree of the permutations to be generated. Must be a non-zero positive integer.
    :type degree: int
    :param algorithm: The algorithm to use for generating permutations.
        Default is ``random``.
    :type algorithm: str, optional

    :return: An infinite generator yielding permutations.
    :rtype: Generator[Permutation, None, None]

    :raises ValueError: If the algorithm is not supported or the degree is invalid.

    :examples:
        >>> import symmetria
        ...
        >>> permutations = symmetria.random_generator(degree=3, algorithm="fisher-yates")
    """
    _check_algorithm_parameter(value=algorithm, supported=_SUPPORTED_ALGORITHM)
    _check_degree_parameter(value=degree)
    return _relevant_random_generator(algorithm=algorithm, degree=degree)


def _relevant_random_generator(algorithm: str, degree: int) -> Generator[Permutation, None, None]:
    """Private method to pick the correct algorithm for generating random permutations."""
    if algorithm == "random":
        return _random_shuffle_generator(degree=degree)
    elif algorithm == "fisher-yates":
        return _fisher_yates_shuffle_generator(degree=degree)


if __name__ == "__main__":
    print(random(3, "fisher-yates").rep())
    for idx, p in enumerate(random_generator(12, "fisher-yates")):
        print(p.rep())

        if idx == 10:
            break
