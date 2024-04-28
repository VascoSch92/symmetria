from symmetria.elements import Cycle, CycleDecomposition, Permutation


############################
# TEST CASES CONSTRUCTORS  #
############################

TEST_CONSTRUCTOR = [
    [1], [1, 2], [3, 2, 1], [4, 5, 6, 3, 2, 1], [4, 3, 2, 1]
]
TEST_CONSTRUCTOR_ERROR = [
    (['1'], ValueError, f"Expected `int` type, but got {type('1')}."),
    ([1, 2, 3.4], ValueError, f"Expected `int` type, but got {type(3.4)}."),
    ([1, 0], ValueError, f"Expected all strictly positive values, but got {0}."),
    ([1, -1], ValueError, f"Expected all strictly positive values, but got {-1}.")
]

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
    (Cycle(3), CycleDecomposition(Cycle(1), Cycle(2), Cycle(3)), True),
    (Cycle(4), CycleDecomposition(Cycle(1), Cycle(2), Cycle(3)), False),
    (Cycle(1, 2), CycleDecomposition(Cycle(1), Cycle(2)), False),
    (Cycle(1, 2), CycleDecomposition(Cycle(1, 2)), True),
    (Cycle(1, 2, 4), CycleDecomposition(Cycle(1, 2)), False),
    (Cycle(1, 2), CycleDecomposition(Cycle(1, 2), Cycle(3)), True),
    (Cycle(1), Permutation(1), True),
    (Cycle(2), Permutation(1), False),
]
TEST_INT = [
    (Cycle(1), 1),
    (Cycle(2), 2),
    (Cycle(3), 3),
    (Cycle(2, 1), 12),
    (Cycle(3, 1, 2), 123),
    (Cycle(4, 3, 2, 1), 1432),
]
TEST_LEN = [
    (Cycle(1), 1),
    (Cycle(2), 1),
    (Cycle(13), 1),
    (Cycle(1, 2), 2),
    (Cycle(1, 3, 2), 3),
]
TEST_REPR = [
    (Cycle(1), "Cycle(1)"),
    (Cycle(1, 2), "Cycle(1, 2)"),
    (Cycle(1, 3, 2), "Cycle(1, 3, 2)"),
]
TEST_MUL = [

]