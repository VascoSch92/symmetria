from symmetria.elements import Cycle, CycleDecomposition


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
]