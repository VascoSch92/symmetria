from symmetria.elements import Cycle, CycleDecomposition

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