from symmetria.elements.cycles import Cycle, CycleDecomposition
from symmetria.elements.permutations import Permutation

############################
# TEST CASES CONSTRUCTORS  #
############################

TEST_CONSTRUCTOR = [
    [Cycle(1)],
    [Cycle(1, 2)],
    [Cycle(3, 2, 1), Cycle(4)],
    [Cycle(4, 5), Cycle(6, 3), Cycle(2, 1)],
    [Cycle(4), Cycle(3), Cycle(2), Cycle(1)],
]
TEST_CONSTRUCTOR_ERROR = [
    ([Cycle(3, 2, 1), Cycle(3)], ValueError, "The cycles"),
    ([Cycle(2, 3)], ValueError, "Every element from 1 to the biggest permuted element must be included in some cycle"),
]

##############################
# TEST CASES GENERIC METHODS #
##############################

TEST_CYCLE_NOTATION = [
    (CycleDecomposition(Cycle(1)), "(1)"),
    (CycleDecomposition(Cycle(1), Cycle(2, 4, 7, 6), Cycle(3, 5)), "(1)(2 4 7 6)(3 5)"),
    (CycleDecomposition(Cycle(1, 6, 2, 4, 7), Cycle(3, 5)), "(1 6 2 4 7)(3 5)"),
]

TEST_IS_DERANGEMENT = [
    (CycleDecomposition(Cycle(1)), False),
    (CycleDecomposition(Cycle(1), Cycle(2, 4, 7, 6), Cycle(3, 5)), False),
    (CycleDecomposition(Cycle(1, 6, 2, 4, 7), Cycle(3, 5)), True),
]
TEST_MAP = [
    (CycleDecomposition(Cycle(1)), {1: 1}),
    (CycleDecomposition(Cycle(1), Cycle(2, 4, 7, 6), Cycle(3, 5)), {1: 1, 2: 4, 4: 7, 7: 6, 6: 2, 3: 5, 5: 3}),
]
TEST_ORDER = [
    (CycleDecomposition(Cycle(1)), 1),
    (CycleDecomposition(Cycle(1), Cycle(2, 4, 7, 6), Cycle(3, 5)), 4),
    (CycleDecomposition(Cycle(1, 6, 2, 4, 7), Cycle(3, 5)), 10),
]
TEST_SUPPORT = [
    (CycleDecomposition(Cycle(1)), set()),
    (CycleDecomposition(Cycle(1), Cycle(2, 4, 7, 6), Cycle(3, 5)), {2, 4, 7, 6, 3, 5}),
    (CycleDecomposition(Cycle(1, 6, 2, 4, 7), Cycle(3, 5)), {1, 6, 2, 4, 7, 3, 5})
]

############################
# TEST CASES MAGIC METHODS #
############################

TEST_BOOL = [
    (CycleDecomposition(Cycle(1)), False),
    (CycleDecomposition(Cycle(1), Cycle(2)), False),
    (CycleDecomposition(Cycle(1), Cycle(2), Cycle(3)), False),
    (CycleDecomposition(Cycle(1, 2)), True),
    (CycleDecomposition(Cycle(1, 2, 3), Cycle(4, 5)), True),
]
TEST_EQ = [
    (CycleDecomposition(Cycle(1)), CycleDecomposition(Cycle(1)), True),
    (CycleDecomposition(Cycle(1)), CycleDecomposition(Cycle(1), Cycle(2)), False),
    (CycleDecomposition(Cycle(1, 2), Cycle(3)), CycleDecomposition(Cycle(1), Cycle(2, 3)), False),
    (CycleDecomposition(Cycle(1)), Cycle(1), True),
    (CycleDecomposition(Cycle(1)), Cycle(2), False),
    (CycleDecomposition(Cycle(1, 2, 3)), Cycle(1, 2, 3), True),
    (CycleDecomposition(Cycle(3, 2, 1)), Cycle(1, 2, 3), False),
    (CycleDecomposition(Cycle(1)), Permutation(1), True),
    (CycleDecomposition(Cycle(1, 2)), Permutation(2, 1), True),
    (CycleDecomposition(Cycle(1), Cycle(2, 4, 7, 6), Cycle(3, 5)), Permutation(1, 4, 5, 7, 3, 2, 6), True),
    (CycleDecomposition(Cycle(1, 6, 2, 4, 7), Cycle(3, 5)), Permutation(6, 5, 4, 7, 3, 2, 1), False),
    (CycleDecomposition(Cycle(1)), "abc", False),
]
TEST_GETITEM = [
    (CycleDecomposition(Cycle(1)), 0, Cycle(1)),
    (CycleDecomposition(Cycle(1), Cycle(2, 4, 7, 6), Cycle(3, 5)), 1, Cycle(2, 4, 7, 6)),
    (CycleDecomposition(Cycle(1, 6, 2, 4, 7), Cycle(3, 5)), 1, Cycle(3, 5))
]
TEST_REPR = [
    (CycleDecomposition(Cycle(1)), "CycleDecomposition((1))"),
    (CycleDecomposition(Cycle(1, 2)), "CycleDecomposition((1 2))"),
    (CycleDecomposition(Cycle(1), Cycle(2, 3)), "CycleDecomposition((1)(2 3))")
]