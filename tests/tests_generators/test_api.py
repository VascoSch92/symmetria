import pytest

import symmetria
from tests.test_utils import _check_values
from tests.tests_generators.test_cases import (
    TEST_SJT_GENERATOR,
    TEST_HEAP_GENERATOR,
    TEST_LEXICOGRAPHIC_GENERATOR,
    TEST_COLEXICOGRAPHIC_GENERATOR,
    TEST_PERMUTATION_GENERATOR_EXCPETIONS,
)


@pytest.mark.parametrize(
    argnames="algorithm, degree, error, msg",
    argvalues=TEST_PERMUTATION_GENERATOR_EXCPETIONS,
    ids=[f"symmetria.generate({a}, {d})" for a, d, _, _ in TEST_PERMUTATION_GENERATOR_EXCPETIONS],
)
def test_permutation_generator_exceptions(algorithm, degree, error, msg) -> None:
    with pytest.raises(error, match=msg):
        _ = symmetria.generate(algorithm=algorithm, degree=degree)


@pytest.mark.parametrize(
    argnames="degree, expected_value",
    argvalues=TEST_LEXICOGRAPHIC_GENERATOR,
    ids=[f"symmetria.generate(lexicographic, {d})" for d, _ in TEST_LEXICOGRAPHIC_GENERATOR],
)
def test_lexicographic_generator(degree, expected_value) -> None:
    _check_values(
        expression=f"symmetria.generate('lexicographic', {degree})",
        evaluation=list(symmetria.generate(algorithm="lexicographic", degree=degree)),
        expected=expected_value,
    )


@pytest.mark.parametrize(
    argnames="degree, expected_value",
    argvalues=TEST_COLEXICOGRAPHIC_GENERATOR,
    ids=[f"symmetria.generate(colexicographic, {d})" for d, _ in TEST_COLEXICOGRAPHIC_GENERATOR],
)
def test_colexicographic_generator(degree, expected_value) -> None:
    _check_values(
        expression=f"symmetria.generate('colexicographic', {degree})",
        evaluation=list(symmetria.generate(algorithm="colexicographic", degree=degree)),
        expected=expected_value,
    )


@pytest.mark.parametrize(
    argnames="degree, expected_value",
    argvalues=TEST_HEAP_GENERATOR,
    ids=[f"symmetria.generate('heap', {d})" for d, _ in TEST_HEAP_GENERATOR],
)
def test_heap_generator(degree, expected_value) -> None:
    _check_values(
        expression=f"symmetria.generate('heap', {degree})",
        evaluation=list(symmetria.generate(algorithm="heap", degree=degree)),
        expected=expected_value,
    )


@pytest.mark.parametrize(
    argnames="degree, expected_value",
    argvalues=TEST_SJT_GENERATOR,
    ids=[f"symmetria.generate('steinhaus-johnson-trotter', {d})" for d, _ in TEST_SJT_GENERATOR],
)
def test_steinhaus_johnson_trotter_generator(degree, expected_value) -> None:
    _check_values(
        expression=f"symmetria.generate('steinhaus-johnson-trotter', {degree})",
        evaluation=list(symmetria.generate(algorithm="steinhaus-johnson-trotter", degree=degree)),
        expected=expected_value,
    )
