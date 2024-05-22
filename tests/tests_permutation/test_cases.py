from symmetria import Cycle, Permutation, CycleDecomposition

############################
# TEST CASES CONSTRUCTORS  #
############################

TEST_CONSTRUCTOR = [[1], [1, 2], [3, 2, 1], [4, 5, 6, 3, 2, 1], [4, 3, 2, 1]]
TEST_CONSTRUCTOR_ERROR = [
    (["1"], ValueError, f"Expected `int` type, but got {str}"),
    ([-1], ValueError, "Expected all strictly positive values, but got -1"),
    (
        [1, 3],
        ValueError,
        "The permutation is not injecting on its image. Indeed, 3 is not in the image.",
    ),
    (
        [1, 1],
        ValueError,
        "It seems that the permutation is not bijective. Indeed, 1 has two, or more, pre-images.",
    ),
]
TEST_CONSTRUCTOR_FROM_DICT = [
    ({1: 1}, Permutation(1)),
    ({1: 1, 2: 2}, Permutation(1, 2)),
    ({1: 3, 2: 2, 3: 1}, Permutation(3, 2, 1)),
    ({1: 4, 2: 3, 3: 2, 4: 1}, Permutation(4, 3, 2, 1)),
    ({1: 4, 2: 5, 3: 6, 4: 3, 5: 2, 6: 1}, Permutation(4, 5, 6, 3, 2, 1)),
]
TEST_CONSTRUCTOR_FROM_CYCLE = [
    (Cycle(1), Permutation(1)),
    (Cycle(1, 2), Permutation(2, 1)),
    (Cycle(3, 1), Permutation(3, 2, 1)),
    (Cycle(4, 3, 2, 1), Permutation(4, 1, 2, 3)),
    (Cycle(4, 5, 6, 3, 2, 1), Permutation(4, 1, 2, 5, 6, 3)),
]
TEST_CONSTRUCTOR_FROM_CYCLE_DECOMPOSITION = [
    (CycleDecomposition(Cycle(1)), Permutation(1)),
    (CycleDecomposition(Cycle(1, 2)), Permutation(2, 1)),
    (CycleDecomposition(Cycle(1), Cycle(2)), Permutation(1, 2)),
    (CycleDecomposition(Cycle(4, 3), Cycle(1, 2)), Permutation(2, 1, 4, 3)),
]

##############################
# TEST CASES GENERIC METHODS #
##############################

TEST_CYCLE_DECOMPOSITION = [
    (Permutation(1), CycleDecomposition(Cycle(1))),
    (Permutation(2, 1), CycleDecomposition(Cycle(1, 2))),
    (Permutation(1, 3, 2), CycleDecomposition(Cycle(1), Cycle(2, 3))),
    (Permutation(1, 4, 3, 2), CycleDecomposition(Cycle(1), Cycle(2, 4), Cycle(3))),
    (
        Permutation(1, 4, 5, 7, 3, 2, 6),
        CycleDecomposition(Cycle(1), Cycle(2, 4, 7, 6), Cycle(3, 5)),
    ),
    (
        Permutation(6, 4, 5, 7, 3, 2, 1),
        CycleDecomposition(Cycle(1, 6, 2, 4, 7), Cycle(3, 5)),
    ),
]
TEST_CYCLE_TYPE = [
    (Permutation(1), (1,)),
    (Permutation(3, 1, 2), (3,)),
    (Permutation(3, 1, 2, 4, 5, 6), (1, 1, 1, 3)),
    (Permutation(1, 4, 5, 7, 3, 2, 6), (1, 2, 4)),
]
TEST_CYCLE_NOTATION = [
    (Permutation(1), "(1)"),
    (Permutation(3, 1, 2), "(1 3 2)"),
    (Permutation(3, 1, 2, 4, 5, 6), "(1 3 2)(4)(5)(6)"),
]
TEST_DOMAIN = [
    (Permutation(1), range(1, 2)),
    (Permutation(2, 1), range(1, 3)),
    (Permutation(1, 3, 2), range(1, 4)),
    (Permutation(1, 4, 3, 2), range(1, 5)),
]
TEST_EQUIVALENT = [
    (Permutation(1), Permutation(1), True),
    (Permutation(1, 2, 3), Permutation(1, 2, 3), True),
    (Permutation(1, 2, 3), Permutation(3, 2, 1), False),
    (Permutation(1), Cycle(1), True),
    (Permutation(1), Cycle(1, 2), False),
    (Permutation(1), CycleDecomposition(Cycle(1)), True),
    (Permutation(1, 3, 2), CycleDecomposition(Cycle(3, 2), Cycle(1)), True),
    (Permutation(1, 2, 3), 123, False),
    (Permutation(1, 3, 2, 4), "hello-world", False),
]
TEST_INVERSE = [
    (Permutation(1, 2, 3), Permutation(1, 2, 3)),
    (Permutation(1, 3, 4, 2), Permutation(1, 4, 2, 3)),
    (Permutation(2, 3, 1, 5, 4), Permutation(3, 1, 2, 5, 4)),
]
TEST_IS_DERANGEMENT = [
    (Permutation(1), False),
    (Permutation(2, 1), True),
    (Permutation(1, 3, 2), False),
    (Permutation(1, 4, 3, 2), False),
    (Permutation(1, 4, 5, 7, 3, 2, 6), False),
    (Permutation(6, 4, 5, 7, 3, 2, 1), True),
]
TEST_IS_EVEN = [
    (Permutation(1), True),
    (Permutation(2, 1), False),
    (Permutation(2, 1, 3), False),
    (Permutation(2, 3, 4, 5, 6, 1), False),
]
TEST_IS_ODD = [
    (Permutation(1), False),
    (Permutation(2, 1), True),
    (Permutation(2, 1, 3), True),
    (Permutation(2, 3, 4, 5, 6, 1), True),
]
TEST_MAP = [
    (Permutation(1), {1: 1}),
    (Permutation(2, 1), {1: 2, 2: 1}),
    (Permutation(1, 3, 2), {1: 1, 2: 3, 3: 2}),
    (Permutation(1, 4, 3, 2), {1: 1, 2: 4, 3: 3, 4: 2}),
]
TEST_SUPPORT = [
    (Permutation(1), set()),
    (Permutation(2, 1), {1, 2}),
    (Permutation(1, 3, 2), {2, 3}),
    (Permutation(1, 4, 3, 2), {2, 4}),
]
TEST_ONE_LINE_NOTATION = [
    (Permutation(1), "1"),
    (Permutation(2, 1), "21"),
    (Permutation(1, 3, 2), "132"),
    (Permutation(1, 4, 3, 2), "1432"),
    (Permutation(1, 4, 5, 7, 3, 2, 6), "1457326"),
]
TEST_ORBIT = [
    (Permutation(3, 1, 2), 1, [1, 3, 2]),
    (Permutation(3, 1, 2), [1, 2, 3], [[1, 2, 3], [2, 3, 1], [3, 1, 2]]),
    (Permutation(3, 1, 2), "abc", ["abc", "bca", "cab"]),
    (
        Permutation(3, 1, 2),
        Cycle(1, 2, 3),
        [
            CycleDecomposition(Cycle(1, 2, 3)),
            CycleDecomposition(Cycle(1), Cycle(2), Cycle(3)),
            CycleDecomposition(Cycle(1, 3, 2)),
        ],
    ),
]
TEST_ORDER = [
    (Permutation(1), 1),
    (Permutation(2, 1), 2),
    (Permutation(1, 3, 2), 2),
    (Permutation(1, 4, 3, 2), 2),
    (Permutation(1, 4, 5, 7, 3, 2, 6), 4),
]
TEST_SGN = [(Permutation(1), 1), (Permutation(2, 1), -1), (Permutation(2, 3, 4, 5, 6, 1), -1)]

############################
# TEST CASES MAGIC METHODS #
############################

TEST_BOOL = [
    (Permutation(1), False),
    (Permutation(1, 2), False),
    (Permutation(2, 1), True),
    (Permutation(1, 2, 3), False),
    (Permutation(3, 2, 1), True),
]
TEST_CALL = [
    (Permutation(1), 1, 1),
    (Permutation(2, 1), 2, 1),
    (Permutation(1, 3, 2), 17, 17),
    (Permutation(2, 1), [1, 2], [2, 1]),
    (Permutation(2, 1), [1, 17, 2], [17, 1, 2]),
    (Permutation(2, 1), (1, 2), (2, 1)),
    (Permutation(2, 1), (1, 17, 2), (17, 1, 2)),
    (Permutation(2, 1), "ab", "ba"),
    (Permutation(1, 2, 3), Permutation(3, 2, 1), Permutation(3, 2, 1)),
    (
        Permutation(3, 4, 5, 1, 2),
        Permutation(3, 5, 1, 2, 4),
        Permutation(5, 2, 3, 4, 1),
    ),
    (
        Permutation(1, 2, 4, 3),
        Cycle(2, 1),
        CycleDecomposition(Cycle(1, 2), Cycle(3, 4)),
    ),
    (Permutation(1, 2, 3, 4), Cycle(1, 2, 3, 4), CycleDecomposition(Cycle(2, 3, 4, 1))),
    (Permutation(1, 2), Cycle(1), CycleDecomposition(Cycle(1), Cycle(2))),
    (Permutation(1, 2), Cycle(2), CycleDecomposition(Cycle(1), Cycle(2))),
    (
        Permutation(1, 2),
        CycleDecomposition(Cycle(1), Cycle(2)),
        CycleDecomposition(Cycle(1), Cycle(2)),
    ),
]
TEST_CALL_ERROR = [
    (Permutation(1), 0.99, TypeError, "Calling a permutation"),
    (Permutation(2, 1), [1], ValueError, "Not enough object"),
    (Permutation(2, 1), Cycle(3), ValueError, "Cannot compose permutation"),
    (
        Permutation(2, 1),
        CycleDecomposition(Cycle(1, 3), Cycle(2)),
        ValueError,
        "Cannot compose permutation",
    ),
]
TEST_EQ = [
    (Permutation(1), Permutation(1), True),
    (Permutation(1), Permutation(1, 2), False),
    (Permutation(1, 2, 3), 123, False),
    (Permutation(1, 3, 2, 4), "hello-world", False),
]
TEST_INT = [
    (Permutation(1), 1),
    (Permutation(2, 1), 21),
    (Permutation(3, 1, 2), 312),
    (Permutation(4, 3, 2, 1), 4321),
]
TEST_LEN = [
    (Permutation(1), 1),
    (Permutation(1, 2), 2),
    (Permutation(1, 3, 2), 3),
]
TEST_MUL = [
    (Permutation(1), Permutation(1), Permutation(1)),
    (Permutation(1, 2, 3), Permutation(3, 2, 1), Permutation(3, 2, 1)),
    (
        Permutation(3, 4, 5, 1, 2),
        Permutation(3, 5, 1, 2, 4),
        Permutation(5, 2, 3, 4, 1),
    ),
]
TEST_MUL_ERROR = [
    (Permutation(1, 2, 3), Permutation(1, 2), ValueError, "Cannot compose permutation"),
    (Permutation(1, 2), Cycle(1, 2, 3), TypeError, "Product between types "),
    (Permutation(1, 2), 123, TypeError, "Product between types `Permutation` and"),
    (
        Permutation(1, 2),
        CycleDecomposition(Cycle(3, 2), Cycle(1)),
        TypeError,
        "Product between",
    ),
]
TEST_REPR = [
    (Permutation(1), "Permutation(1)"),
    (Permutation(1, 2), "Permutation(1, 2)"),
    (Permutation(1, 3, 2), "Permutation(1, 3, 2)"),
]
TEST_STR = [
    (Permutation(1), "(1)"),
    (Permutation(1, 2), "(1, 2)"),
    (Permutation(1, 3, 2), "(1, 3, 2)"),
]
