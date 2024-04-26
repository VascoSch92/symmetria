from symmetria.elements import Cycle, CycleDecomposition

############################
# TEST CASES MAGIC METHODS #
############################

TEST_BOOL = [
    (Cycle(1), False),
    (Cycle(2), False),
    (Cycle(130692), False),
    (Cycle(1, 2), True),
    (Cycle(2, 5, 23, 54), True),
]
TEST_EQ = [
    (Cycle(1), Cycle(1), True),
    (Cycle(1), Cycle(13), True),
    (Cycle(1), Cycle(1, 2), False),
    (Cycle(1, 2, 3), Cycle(2, 3, 1), True),
    (Cycle(1, 2, 3), Cycle(2, 3, 4), False),
    (Cycle(1, 2, 3, 4), Cycle(4, 1, 2, 3), True),
    (Cycle(1, 2), CycleDecomposition(Cycle(1, 2)), True),
    (Cycle(1, 2, 4), CycleDecomposition(Cycle(1, 2)), False),
    (Cycle(1, 2), CycleDecomposition(Cycle(1, 2), Cycle(3)), True),
]