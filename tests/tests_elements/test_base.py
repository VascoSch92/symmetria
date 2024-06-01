import pytest

from symmetria import Cycle, Permutation, CycleDecomposition
from tests.test_utils import _check_values
from symmetria.elements._base import _Element


@pytest.mark.parametrize(
    argnames="expression, evaluation, expected",
    argvalues=[
        ("_element.name()", _Element().typename(), "_Element"),
        ("Permutation(1).name()", Permutation(1).typename(), "Permutation"),
        ("Cycle(1).name()", Cycle(1).typename(), "Cycle"),
        ("CycleDecomposition(Cycle(1)).name()", CycleDecomposition(Cycle(1)).typename(), "CycleDecomposition"),
    ],
)
def test_name(expression, evaluation, expected) -> None:
    _check_values(expression=expression, evaluation=evaluation, expected=expected)


@pytest.mark.parametrize(
    argnames="expression, evaluation, expected",
    argvalues=[
        ("_element.rep()", _Element().rep(), "_Element()"),
        ("Permutation(1).rep()", Permutation(1).rep(), Permutation(1).__repr__()),
        ("Cycle(1).rep()", Cycle(1).rep(), Cycle(1).__repr__()),
        (
            "CycleDecomposition(Cycle(1)).rep()",
            CycleDecomposition(Cycle(1)).rep(),
            CycleDecomposition(Cycle(1)).__repr__(),
        ),
    ],
)
def test_rep(expression, evaluation, expected) -> None:
    _check_values(expression=expression, evaluation=evaluation, expected=expected)
