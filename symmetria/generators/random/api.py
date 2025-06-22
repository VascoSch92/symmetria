import warnings
from typing import Dict, Final, Callable, Generator

from symmetria import Permutation
from symmetria.generators._validators import _check_degree_parameter, _check_algorithm_parameter
from symmetria.generators.random._algorithms import (
    _random_shuffle,
    _fisher_yates_shuffle,
    _random_shuffle_generator,
    _fisher_yates_shuffle_generator,
)

__all__ = ["random", "random_generator", "random_permutation"]

_SUPPORTED_ALGORITHM: Final[Dict[str, Dict[str, Callable]]] = {
    "random": {
        "random": _random_shuffle,
        "fisher-yates": _fisher_yates_shuffle,
    },
    "generator": {
        "random": _random_shuffle_generator,
        "fisher-yates": _fisher_yates_shuffle_generator,
    },
}


def random(degree: int, algorithm: str = "random") -> Permutation:
    """Generate a random permutation of the given degree based on the chosen algorithm.

    :warning: This function will be deprecated in a future version. Use 'random_permutation' instead.

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
    warnings.warn(
        "This function will be deprecated in a future version. Use 'random_permutation' instead.",
        PendingDeprecationWarning,
        stacklevel=1,
    )
    _check_algorithm_parameter(value=algorithm, supported=list(_SUPPORTED_ALGORITHM["random"].keys()))
    _check_degree_parameter(value=degree)
    return _relevant_random_permutation(algorithm=algorithm, degree=degree)


def random_permutation(degree: int, algorithm: str = "random") -> Permutation:
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
        >>> from symmetria import random_permutation
        ...
        >>> permutation = random_permutation(degree=3, algorithm="fisher-yates")
    """
    _check_algorithm_parameter(value=algorithm, supported=list(_SUPPORTED_ALGORITHM["random"].keys()))
    _check_degree_parameter(value=degree)
    return _relevant_random_permutation(algorithm=algorithm, degree=degree)


def _relevant_random_permutation(algorithm: str, degree: int) -> Permutation:
    """Private method to pick the correct algorithm to generate the permutation."""
    if algorithm == "random":
        return _random_shuffle(permutation=list(range(1, degree + 1)))
    elif algorithm == "fisher-yates":
        return _fisher_yates_shuffle(permutation=list(range(1, degree + 1)))
    raise NotImplementedError(
        f"Algorithm '{algorithm}' is not supported yet.\n"
        f"Supported algorithms are {', '.join(_SUPPORTED_ALGORITHM['random'].keys())}"
    )


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
        >>> from symmetria import random_generator
        ...
        >>> permutations = random_generator(degree=3, algorithm="fisher-yates")
    """
    warnings.warn(
        "The API of this method will be deprecated in a future version. \n"
        "Use 'from symmetria import random_generator' instead of 'import symmetria.",
        PendingDeprecationWarning,
        stacklevel=1,
    )
    _check_algorithm_parameter(value=algorithm, supported=list(_SUPPORTED_ALGORITHM["generator"].keys()))
    _check_degree_parameter(value=degree)
    return _relevant_random_generator(algorithm=algorithm, degree=degree)


def _relevant_random_generator(algorithm: str, degree: int) -> Generator[Permutation, None, None]:
    """Private method to pick the correct algorithm for generating random permutations."""
    if algorithm in _SUPPORTED_ALGORITHM["generator"]:
        return _SUPPORTED_ALGORITHM["generator"][algorithm](degree=degree)
    raise NotImplementedError(
        f"Algorithm '{algorithm}' is not supported yet.\n"
        f"Supported algorithms are {', '.join(_SUPPORTED_ALGORITHM['generator'].keys())}"
    )
