from symmetria.elements import Cycle

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
