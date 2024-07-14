from random import randint, shuffle
from typing import List, Generator

from symmetria import Permutation


def _random_shuffle(permutation: List[int]) -> Permutation:
    """Private method to generate a random permutation using the random module of Python."""
    shuffle(permutation)
    return Permutation(*permutation)


def _random_shuffle_generator(degree: int) -> Generator[Permutation, None, None]:
    """Private method to generate random permutations using the random module of Python."""
    permutation = list(range(1, degree + 1))
    while True:
        yield _random_shuffle(permutation=permutation)


def _fisher_yates_shuffle(permutation: List[int]) -> Permutation:
    """Private method to generate a random permutation using the Fisher-Yates shuffle."""
    n = len(permutation)
    for i in range(n - 1, 0, -1):
        j = randint(0, i)
        permutation[i], permutation[j] = permutation[j], permutation[i]
    return Permutation(*permutation)


def _fisher_yates_shuffle_generator(degree: int) -> Generator[Permutation, None, None]:
    """Private method to generate random permutations using the Fisher-Yates shuffle."""
    permutation = list(range(1, degree + 1))
    while True:
        yield _fisher_yates_shuffle(permutation=permutation)
