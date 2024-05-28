from symmetria import Cycle, Permutation, CycleDecomposition

############################
# TEST CASES CONSTRUCTORS  #
############################

TEST_CONSTRUCTOR = [[1], [1, 2], [3, 2, 1], [4, 5, 6, 3, 2, 1], [4, 3, 2, 1]]
TEST_CONSTRUCTOR_ERROR = [
    (["1"], ValueError, f"Expected `int` type, but got {str}."),
    ([1, 2, 3.4], ValueError, f"Expected `int` type, but got {float}."),
    ([1, 0], ValueError, f"Expected all strictly positive values, but got {0}."),
    ([1, -1], ValueError, f"Expected all strictly positive values, but got {-1}."),
]

##############################
# TEST CASES GENERIC METHODS #
##############################

TEST_CYCLE_NOTATION = [
    (Cycle(1), "(1)"),
    (Cycle(13), "(13)"),
    (Cycle(1, 2), "(1 2)"),
    (Cycle(1, 2, 3), "(1 2 3)"),
]
TEST_DOMAIN = [
    (Cycle(1), range(1, 2)),
    (Cycle(13), range(1, 14)),
    (Cycle(1, 2), range(1, 3)),
    (Cycle(1, 2, 3), range(1, 4)),
]
TEST_ELEMENTS = [
    (Cycle(1), (1,)),
    (Cycle(13), (13,)),
    (Cycle(1, 2), (1, 2)),
    (Cycle(1, 2, 3), (1, 2, 3)),
]
TEST_EQUIVALENT = [
    (Cycle(13), Cycle(13), True),
    (Cycle(3), CycleDecomposition(Cycle(1), Cycle(2), Cycle(3)), True),
    (Cycle(4), CycleDecomposition(Cycle(1), Cycle(2), Cycle(3)), False),
    (Cycle(1, 2), CycleDecomposition(Cycle(1), Cycle(2)), False),
    (Cycle(1, 2), CycleDecomposition(Cycle(1, 2)), True),
    (Cycle(1, 2, 4), CycleDecomposition(Cycle(1, 2)), False),
    (Cycle(1, 2), CycleDecomposition(Cycle(1, 2), Cycle(3)), True),
    (Cycle(1), Permutation(1), True),
    (Cycle(13), Permutation(1), False),
    (Cycle(13), 13, False),
    (Cycle(1), "13", False),
]
TEST_INVERSE = [
    (Cycle(1, 2, 3), Cycle(3, 2, 1)),
    (Cycle(1, 3, 4, 2), Cycle(2, 4, 3, 1)),
    (Cycle(2, 3, 1, 5, 4), Cycle(4, 5, 1, 3, 2)),
]
TEST_INVERSIONS = [
    (Cycle(1, 2, 3), []),
    (Cycle(1, 3, 4, 2), [(2, 4), (3, 4)]),
    (Cycle(1, 2, 5, 4, 3), [(3, 4), (3, 5), (4, 5)]),
]
TEST_IS_CONJUGATE_ERROR = [(Cycle(1, 2, 3), Cycle(1, 2, 3), NotImplementedError, "Method")]
TEST_IS_DERANGEMENT = [
    (Cycle(1), False),
    (Cycle(13), False),
    (Cycle(1, 2), True),
    (Cycle(1, 2, 3), True),
]
TEST_IS_EVEN = [
    (Cycle(1), True),
    (Cycle(1, 2), False),
    (Cycle(1, 2, 3, 4, 5, 6), False),
    (Cycle(1, 2, 3, 4, 5, 6, 7), True),
]
TEST_IS_ODD = [
    (Cycle(1), False),
    (Cycle(1, 2), True),
    (Cycle(1, 2, 3, 4, 5, 6), True),
    (Cycle(1, 2, 3, 4, 5, 6, 7), False),
]
TEST_IS_REGULAR_ERROR = [(Cycle(1, 2, 3), NotImplementedError, "Method")]
TEST_MAP = [
    (Cycle(1), {1: 1}),
    (Cycle(13), {13: 13}),
    (Cycle(1, 2), {1: 2, 2: 1}),
    (Cycle(1, 2, 3), {1: 2, 2: 3, 3: 1}),
]
TEST_ORBIT = [
    (Cycle(3, 1, 2), 1, [1, 2, 3]),
    (Cycle(3, 1, 2), "abc", ["abc", "cab", "bca"]),
    (Cycle(3, 1, 2), [1, 2, 3], [[1, 2, 3], [3, 1, 2], [2, 3, 1]]),
    (
        Cycle(3, 1, 2),
        Permutation(3, 1, 2),
        [Permutation(3, 1, 2), Permutation(1, 2, 3), Permutation(2, 3, 1)],
    ),
    (
        Cycle(3, 1, 2),
        Cycle(3, 1, 2),
        [
            CycleDecomposition(Cycle(1, 2, 3)),
            CycleDecomposition(Cycle(1, 3, 2)),
            CycleDecomposition(Cycle(1), Cycle(2), Cycle(3)),
        ],
    ),
]
TEST_ORDER = [
    (Cycle(1), 1),
    (Cycle(13), 1),
    (Cycle(1, 2), 2),
    (Cycle(1, 2, 3), 3),
]
TEST_SGN = [
    (Cycle(1), 1),
    (Cycle(13), 1),
    (Cycle(1, 2), -1),
    (Cycle(1, 2, 3), 1),
    (Cycle(1, 2, 3, 4, 5, 6), -1),
    (Cycle(1, 2, 3, 4, 5, 6, 7), 1),
]
TEST_SUPPORT = [
    (Cycle(1), set()),
    (Cycle(13), set()),
    (Cycle(1, 2), {1, 2}),
    (Cycle(1, 2, 3), {1, 2, 3}),
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
TEST_CALL = [
    (Cycle(1), 1, 1),
    (Cycle(2, 1), 2, 1),
    (Cycle(1, 3, 2), 17, 17),
    (Cycle(2, 1), [1, 2], [2, 1]),
    (Cycle(2, 1), [1, 17, 2], [17, 1, 2]),
    (Cycle(2, 1), (1, 2), (2, 1)),
    (Cycle(2, 1), (1, 17, 2), (17, 1, 2)),
    (Cycle(2, 1), "ab", "ba"),
    (Cycle(1), Cycle(2), CycleDecomposition(Cycle(1), Cycle(2))),
    (Cycle(1, 2), Cycle(4), CycleDecomposition(Cycle(1, 2), Cycle(3), Cycle(4))),
    (Cycle(1), Cycle(4), CycleDecomposition(Cycle(1), Cycle(2), Cycle(3), Cycle(4))),
    (Cycle(1, 2), Permutation(1, 2), Permutation(2, 1)),
    (Cycle(1, 2), Permutation(1, 2, 3), Permutation(2, 1, 3)),
    (
        Cycle(1),
        CycleDecomposition(Cycle(1), Cycle(2)),
        CycleDecomposition(Cycle(1), Cycle(2)),
    ),
]
TEST_CALL_ERROR = [
    (Cycle(1), 0.99, TypeError, "Calling a cycle"),
    (Cycle(2, 1), [1], ValueError, "Not enough object "),
    (Cycle(13), Permutation(1, 2, 3), ValueError, "Cannot compose"),
    (Cycle(13), Cycle(1), ValueError, "Cannot compose"),
    (
        Cycle(13),
        CycleDecomposition(Cycle(1), Cycle(2), Cycle(3)),
        ValueError,
        "Cannot compose",
    ),
]
TEST_EQ = [
    (Cycle(1), Cycle(1), True),
    (Cycle(1), Cycle(13), True),
    (Cycle(1), Cycle(1, 2), False),
    (Cycle(1, 2, 3), Cycle(1, 2, 3), True),
    (Cycle(1, 2, 3), Cycle(2, 3, 1), True),
    (Cycle(1, 2, 3), Cycle(2, 3, 4), False),
    (Cycle(1, 2, 3, 4), Cycle(4, 1, 2, 3), True),
    (Cycle(1, 3), "ab", False),
]
TEST_GETITEM = [
    (Cycle(1), 0, 1),
    (Cycle(2, 1), 1, 2),
    (Cycle(3, 1, 2), 2, 3),
    (Cycle(4, 3, 2, 1), 0, 1),
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
TEST_POW = [
    (Cycle(1, 3, 2), 0, Cycle(1, 2, 3)),
    (Cycle(1, 3, 2), 1, Cycle(1, 3, 2)),
    (Cycle(1, 3, 2), -1, Cycle(1, 2, 3)),
    (Cycle(1, 3, 2), 2, Cycle(1, 3, 2)(Cycle(1, 3, 2))),
    (Cycle(1, 3, 2), -2, Cycle(1, 3, 2).inverse()(Cycle(1, 3, 2).inverse())),
]
TEST_POW_ERROR = [
    (Cycle(1, 2, 3), "asd", TypeError, "Power"),
    (Cycle(1, 2, 3), 0.9, TypeError, "Power"),
]
TEST_REPR = [
    (Cycle(1), "Cycle(1)"),
    (Cycle(1, 2), "Cycle(1, 2)"),
    (Cycle(1, 3, 2), "Cycle(1, 3, 2)"),
]
TEST_MUL_ERROR = [
    (
        Cycle(1, 2, 3),
        Permutation(1, 2),
        NotImplementedError,
        "Multiplication between cycles is not supported.",
    ),
]
