from symmetria import Permutation

TEST_IS_A_FLAG = [
    ("", False),
    ("not-a-flag", False),
    ("-flag", True),
    ("--flag", True),
    ("-_still a flag", True),
    ("-_still-dr-dre", True),
]
TEST_IS_PERMUTATION = [
    ("", False),
    ("asd", False),
    ("12 34", False),
    ("123-hello", False),
    ("hello-world", False),
    ("123,456", False),
    ("13245", True),
    ("1", True),
    ("23451", True),
]
TEST_PARSE_PERMUTATION = [
    ("123", Permutation(1, 2, 3)),
    ("2341", Permutation(2, 3, 4, 1)),
    ("2143", Permutation(2, 1, 4, 3)),
]
