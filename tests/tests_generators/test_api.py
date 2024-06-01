import pytest

from symmetria import permutation_generator
from tests.tests_generators.test_cases import TEST_PERMUTATION_GENERATOR_EXCPETIONS


@pytest.mark.parametrize(
    argnames="algorithm, degree, error, msg",
    argvalues=TEST_PERMUTATION_GENERATOR_EXCPETIONS,
    ids=[f"permutation_generator({a}, {d})" for a, d, _, _ in TEST_PERMUTATION_GENERATOR_EXCPETIONS],
)
def test_permutation_generator_exceptions(algorithm, degree, error, msg) -> None:
    with pytest.raises(error, match=msg):
        _ = permutation_generator(algorithm=algorithm, degree=degree)
