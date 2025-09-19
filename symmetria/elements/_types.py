from typing import Union

from symmetria.elements.cycle import Cycle
from symmetria.elements.permutation import Permutation
from symmetria.elements.cycle_decomposition import CycleDecomposition

PermutationLike = Union[Permutation, Cycle, CycleDecomposition]
Permutable = Union[
    int,
    str,
    list,
    tuple,
    Permutation,
    Cycle,
    CycleDecomposition,
]
