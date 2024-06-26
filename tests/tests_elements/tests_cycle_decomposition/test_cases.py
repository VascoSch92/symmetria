from symmetria import Cycle, Permutation, CycleDecomposition

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
    (
        [Cycle(2, 3)],
        ValueError,
        "Every element from 1 to the biggest permuted element must be included in some cycle",
    ),
]

##############################
# TEST CASES GENERIC METHODS #
##############################

TEST_ASCENTS = [
    (CycleDecomposition(Cycle(1, 2, 3)), [1]),
    (CycleDecomposition(Cycle(1), Cycle(2), Cycle(3)), [1, 2]),
    (CycleDecomposition(Cycle(2, 3), Cycle(4, 5, 1)), [3]),
]
TEST_CYCLE_NOTATION = [
    (CycleDecomposition(Cycle(1)), "(1)"),
    (CycleDecomposition(Cycle(1), Cycle(2, 4, 7, 6), Cycle(3, 5)), "(1)(2 4 7 6)(3 5)"),
    (CycleDecomposition(Cycle(1, 6, 2, 4, 7), Cycle(3, 5)), "(1 6 2 4 7)(3 5)"),
]
TEST_CYCLE_DECOMPOSITION = [
    (CycleDecomposition(Cycle(1)), CycleDecomposition(Cycle(1))),
    (
        CycleDecomposition(Cycle(1), Cycle(2, 4, 7, 6), Cycle(3, 5)),
        CycleDecomposition(Cycle(1), Cycle(2, 4, 7, 6), Cycle(3, 5)),
    ),
]
TEST_CYCLE_TYPE = [
    (CycleDecomposition(Cycle(1)), (1,)),
    (CycleDecomposition(Cycle(3, 1, 2)), (3,)),
    (CycleDecomposition(Cycle(1, 3, 2), Cycle(4)), (1, 3)),
    (CycleDecomposition(Cycle(1, 2), Cycle(3, 4)), (2, 2)),
]
TEST_DEGREE = [
    (CycleDecomposition(Cycle(1)), 1),
    (CycleDecomposition(Cycle(1), Cycle(2, 3)), 3),
    (CycleDecomposition(Cycle(1), Cycle(2), Cycle(3)), 3),
]
TEST_DESCENTS = [
    (CycleDecomposition(Cycle(1, 2, 3)), [2]),
    (CycleDecomposition(Cycle(1), Cycle(2), Cycle(3)), []),
    (CycleDecomposition(Cycle(2, 3), Cycle(4, 5, 1)), [1, 2, 4]),
]
TEST_DESCRIBE = [
    (
        CycleDecomposition(Cycle(1)),
        """+--------------------------------------------------------------+
|                 CycleDecomposition(Cycle(1))                 |
+--------------------------------------------------------------+
| order                         |              1               |
+-------------------------------+------------------------------+
| degree                        |              1               |
+-------------------------------+------------------------------+
| is derangement                |            False             |
+-------------------------------+------------------------------+
| inverse                       |             (1)              |
+-------------------------------+------------------------------+
| parity                        |          +1 (even)           |
+-------------------------------+------------------------------+
| cycle notation                |             (1)              |
+-------------------------------+------------------------------+
| cycle type                    |             (1,)             |
+-------------------------------+------------------------------+
| inversions                    |              []              |
+-------------------------------+------------------------------+
| ascents                       |              []              |
+-------------------------------+------------------------------+
| descents                      |              []              |
+-------------------------------+------------------------------+
| excedencees                   |              []              |
+-------------------------------+------------------------------+
| records                       |             [1]              |
+-------------------------------+------------------------------+""",
    ),
    (
        CycleDecomposition(Cycle(1, 3), Cycle(2)),
        """+--------------------------------------------------------------------------------------+
|                      CycleDecomposition(Cycle(1, 3), Cycle(2))                       |
+--------------------------------------------------------------------------------------+
| order                                     |                    2                     |
+-------------------------------------------+------------------------------------------+
| degree                                    |                    2                     |
+-------------------------------------------+------------------------------------------+
| is derangement                            |                  False                   |
+-------------------------------------------+------------------------------------------+
| inverse                                   |                 (1 3)(2)                 |
+-------------------------------------------+------------------------------------------+
| parity                                    |                 -1 (odd)                 |
+-------------------------------------------+------------------------------------------+
| cycle notation                            |                 (1 3)(2)                 |
+-------------------------------------------+------------------------------------------+
| cycle type                                |                  (1, 2)                  |
+-------------------------------------------+------------------------------------------+
| inversions                                |         [(1, 2), (1, 3), (2, 3)]         |
+-------------------------------------------+------------------------------------------+
| ascents                                   |                    []                    |
+-------------------------------------------+------------------------------------------+
| descents                                  |                  [1, 2]                  |
+-------------------------------------------+------------------------------------------+
| excedencees                               |                   [1]                    |
+-------------------------------------------+------------------------------------------+
| records                                   |                   [1]                    |
+-------------------------------------------+------------------------------------------+""",
    ),
]
TEST_EXCEEDANCES = [
    (CycleDecomposition(Cycle(1, 2), Cycle(3)), False, [1]),
    (CycleDecomposition(Cycle(1, 2), Cycle(3)), True, [1, 3]),
    (CycleDecomposition(Cycle(2, 3), Cycle(4, 5, 1)), False, [1, 2, 4]),
    (CycleDecomposition(Cycle(1), Cycle(2), Cycle(3)), False, []),
    (CycleDecomposition(Cycle(1), Cycle(2), Cycle(3)), True, [1, 2, 3]),
]
TEST_INVERSE = [
    (CycleDecomposition(Cycle(1, 2, 3)), CycleDecomposition(Cycle(3, 2, 1))),
    (CycleDecomposition(Cycle(1, 2), Cycle(3, 4)), CycleDecomposition(Cycle(2, 1), Cycle(4, 3))),
]
TEST_INVERSIONS = [
    (CycleDecomposition(Cycle(1), Cycle(2), Cycle(3)), []),
    (CycleDecomposition(Cycle(1, 2, 3)), [(1, 3), (2, 3)]),
]
TEST_IS_CONJUGATE = [
    (CycleDecomposition(Cycle(1, 2, 3)), CycleDecomposition(Cycle(1, 2, 3)), True),
    (CycleDecomposition(Cycle(1, 3, 2, 5, 4)), CycleDecomposition(Cycle(1, 4, 3, 5, 2)), True),
    (CycleDecomposition(Cycle(1, 4, 3, 5, 2)), CycleDecomposition(Cycle(1, 3, 2, 5, 4)), True),
    (CycleDecomposition(Cycle(1, 2), Cycle(3, 4)), CycleDecomposition(Cycle(1), Cycle(3, 2, 4)), False),
    (CycleDecomposition(Cycle(1), Cycle(3, 2, 4)), CycleDecomposition(Cycle(1, 2), Cycle(3, 4)), False),
]
TEST_IS_CONJUGATE_ERROR = [
    (CycleDecomposition(Cycle(1, 2, 3)), "abc", TypeError, "Method"),
    (CycleDecomposition(Cycle(1, 2, 3)), Permutation(1, 2, 3), TypeError, "Method"),
    (CycleDecomposition(Cycle(1, 2, 3)), Cycle(3, 4), TypeError, "Method"),
]
TEST_IS_DERANGEMENT = [
    (CycleDecomposition(Cycle(1)), False),
    (CycleDecomposition(Cycle(1), Cycle(2, 4, 7, 6), Cycle(3, 5)), False),
    (CycleDecomposition(Cycle(1, 6, 2, 4, 7), Cycle(3, 5)), True),
]
TEST_IS_EVEN = [
    (CycleDecomposition(Cycle(1)), True),
    (CycleDecomposition(Cycle(1, 2), Cycle(3)), False),
    (CycleDecomposition(Cycle(1), Cycle(2, 4, 7, 6), Cycle(3, 5)), True),
]
TEST_IS_ODD = [
    (CycleDecomposition(Cycle(1)), False),
    (CycleDecomposition(Cycle(1, 2), Cycle(3)), True),
    (CycleDecomposition(Cycle(1), Cycle(2, 4, 7, 6), Cycle(3, 5)), False),
]
TEST_IS_REGULAR = [
    (CycleDecomposition(Cycle(1)), True),
    (CycleDecomposition(Cycle(2, 1)), True),
    (CycleDecomposition(Cycle(2, 1), Cycle(3)), False),
]
TEST_EQUIVALENT = [
    (CycleDecomposition(Cycle(1)), CycleDecomposition(Cycle(1)), True),
    (CycleDecomposition(Cycle(1)), Cycle(1), True),
    (CycleDecomposition(Cycle(1)), Cycle(2), False),
    (CycleDecomposition(Cycle(1, 2, 3)), Cycle(1, 2, 3), True),
    (CycleDecomposition(Cycle(3, 2, 1)), Cycle(1, 2, 3), False),
    (CycleDecomposition(Cycle(1)), Permutation(1), True),
    (CycleDecomposition(Cycle(1, 2)), Permutation(2, 1), True),
    (CycleDecomposition(Cycle(1)), "hello world", False),
    (
        CycleDecomposition(Cycle(1), Cycle(2, 4, 7, 6), Cycle(3, 5)),
        Permutation(1, 4, 5, 7, 3, 2, 6),
        True,
    ),
    (
        CycleDecomposition(Cycle(1, 6, 2, 4, 7), Cycle(3, 5)),
        Permutation(6, 5, 4, 7, 3, 2, 1),
        False,
    ),
]
TEST_MAP = [
    (CycleDecomposition(Cycle(1)), {1: 1}),
    (
        CycleDecomposition(Cycle(1), Cycle(2, 4, 7, 6), Cycle(3, 5)),
        {1: 1, 2: 4, 4: 7, 7: 6, 6: 2, 3: 5, 5: 3},
    ),
]
TEST_ORBIT = [
    (CycleDecomposition(Cycle(1, 2), Cycle(3, 4)), 1, [1, 2]),
    (CycleDecomposition(Cycle(1, 2), Cycle(3, 4)), "abcd", ["abcd", "badc"]),
    (
        CycleDecomposition(Cycle(1, 2), Cycle(3, 4)),
        [1, 2, 3, 4],
        [[1, 2, 3, 4], [2, 1, 4, 3]],
    ),
    (
        CycleDecomposition(Cycle(1, 2), Cycle(3, 4)),
        Permutation(1, 2, 3, 4),
        [Permutation(1, 2, 3, 4), Permutation(2, 1, 4, 3)],
    ),
    (
        CycleDecomposition(Cycle(1, 2), Cycle(3, 4)),
        Cycle(1, 2, 3, 4),
        [CycleDecomposition(Cycle(1, 2, 3, 4)), CycleDecomposition(Cycle(1), Cycle(2, 4), Cycle(3))],
    ),
]
TEST_ORDER = [
    (CycleDecomposition(Cycle(1)), 1),
    (CycleDecomposition(Cycle(1), Cycle(2, 4, 7, 6), Cycle(3, 5)), 4),
    (CycleDecomposition(Cycle(1, 6, 2, 4, 7), Cycle(3, 5)), 10),
]
TEST_RECORDS = [
    (CycleDecomposition(Cycle(1)), [1]),
    (CycleDecomposition(Cycle(1, 2), Cycle(3)), [1, 3]),
    (CycleDecomposition(Cycle(1), Cycle(2, 4, 7, 6), Cycle(3, 5)), [1, 2, 3, 4]),
]
TEST_SUPPORT = [
    (CycleDecomposition(Cycle(1)), set()),
    (CycleDecomposition(Cycle(1), Cycle(2, 4, 7, 6), Cycle(3, 5)), {2, 4, 7, 6, 3, 5}),
    (CycleDecomposition(Cycle(1, 6, 2, 4, 7), Cycle(3, 5)), {1, 6, 2, 4, 7, 3, 5}),
]
TEST_SGN = [
    (CycleDecomposition(Cycle(1)), 1),
    (CycleDecomposition(Cycle(1, 2), Cycle(3)), -1),
    (CycleDecomposition(Cycle(1), Cycle(2, 4, 7, 6), Cycle(3, 5)), 1),
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
TEST_CALL = [
    (CycleDecomposition(Cycle(1, 2), Cycle(3, 4)), 1, 2),
    (CycleDecomposition(Cycle(1, 2), Cycle(3, 4)), -1, -1),
    (CycleDecomposition(Cycle(1, 2), Cycle(3, 4)), "abcd", "badc"),
    (CycleDecomposition(Cycle(1, 2), Cycle(3, 4)), [1, 2, 3, 4], [2, 1, 4, 3]),
    (CycleDecomposition(Cycle(1, 2), Cycle(3, 4)), (1, 2, 3, 4), (2, 1, 4, 3)),
    (
        CycleDecomposition(Cycle(1, 2), Cycle(3, 4)),
        Permutation(1, 2, 3, 4),
        Permutation(2, 1, 4, 3),
    ),
    (
        CycleDecomposition(Cycle(1, 2), Cycle(3, 4)),
        Cycle(1, 2, 3, 4),
        CycleDecomposition(Cycle(1), Cycle(2, 4), Cycle(3)),
    ),
    (
        CycleDecomposition(Cycle(1, 2), Cycle(3, 4)),
        CycleDecomposition(Cycle(1, 2), Cycle(3, 4)),
        CycleDecomposition(Cycle(1), Cycle(2), Cycle(3), Cycle(4)),
    ),
]
TEST_CALL_ERROR = [
    (CycleDecomposition(Cycle(1, 2), Cycle(3, 4)), 0.99, TypeError, "Calling"),
    (CycleDecomposition(Cycle(1, 2), Cycle(3, 4)), [1, 2, 3], ValueError, "Not enough"),
    (
        CycleDecomposition(Cycle(1, 2), Cycle(3, 4)),
        Permutation(1, 2),
        ValueError,
        "Cannot compose",
    ),
    (
        CycleDecomposition(Cycle(1, 2), Cycle(3, 4)),
        Cycle(1, 3),
        ValueError,
        "Cannot compose",
    ),
    (
        CycleDecomposition(Cycle(1, 2), Cycle(3, 4)),
        CycleDecomposition(Cycle(1)),
        ValueError,
        "Cannot compose",
    ),
]
TEST_EQ = [
    (CycleDecomposition(Cycle(1)), CycleDecomposition(Cycle(1)), True),
    (CycleDecomposition(Cycle(1)), CycleDecomposition(Cycle(1), Cycle(2)), False),
    (CycleDecomposition(Cycle(1, 2, 3)), CycleDecomposition(Cycle(1, 2, 3)), True),
    (
        CycleDecomposition(Cycle(1, 2), Cycle(3)),
        CycleDecomposition(Cycle(1), Cycle(2, 3)),
        False,
    ),
    (CycleDecomposition(Cycle(1)), "abc", False),
]
TEST_GETITEM = [
    (CycleDecomposition(Cycle(1)), 0, Cycle(1)),
    (
        CycleDecomposition(Cycle(1), Cycle(2, 4, 7, 6), Cycle(3, 5)),
        1,
        Cycle(2, 4, 7, 6),
    ),
    (CycleDecomposition(Cycle(1, 6, 2, 4, 7), Cycle(3, 5)), 1, Cycle(3, 5)),
]
TEST_MUL_ERROR = [
    (
        CycleDecomposition(Cycle(1, 2, 3)),
        CycleDecomposition(Cycle(1, 2)),
        ValueError,
        "Cannot",
    ),
    (CycleDecomposition(Cycle(1, 2, 3)), "Hello world", TypeError, "Product"),
]
TEST_POW = [
    (CycleDecomposition(Cycle(3), Cycle(1), Cycle(2)), 0, CycleDecomposition(Cycle(3), Cycle(1), Cycle(2))),
    (CycleDecomposition(Cycle(1, 2), Cycle(3)), 1, CycleDecomposition(Cycle(1, 2), Cycle(3))),
    (CycleDecomposition(Cycle(1, 2), Cycle(3)), -1, CycleDecomposition(Cycle(1, 2), Cycle(3))),
    (
        CycleDecomposition(Cycle(1, 3), Cycle(2, 4)),
        2,
        CycleDecomposition(Cycle(1, 3), Cycle(2, 4)) * CycleDecomposition(Cycle(1, 3), Cycle(2, 4)),
    ),
]
TEST_POW_ERROR = [
    (CycleDecomposition(Cycle(1, 3), Cycle(2, 4)), "abc", TypeError, "Power"),
    (CycleDecomposition(Cycle(1, 3), Cycle(2, 4)), 0.9, TypeError, "Power"),
]
TEST_REPR = [
    (CycleDecomposition(Cycle(1)), "CycleDecomposition(Cycle(1))"),
    (CycleDecomposition(Cycle(1, 2)), "CycleDecomposition(Cycle(1, 2))"),
    (
        CycleDecomposition(Cycle(1), Cycle(2, 3)),
        "CycleDecomposition(Cycle(1), Cycle(2, 3))",
    ),
]
