from symmetria import Permutation

TEST_PERMUTATION_GENERATOR_EXCPETIONS = [
    (13, 3, TypeError, "The parameter `algorithm` must be of type string"),
    ("test", 3, ValueError, "The given algorithm"),
    ("lexicographic", "test", TypeError, "The parameter `degree`"),
    ("lexicographic", 0, ValueError, "The parameter `degree` must be a non-zero positive integer"),
]
TEST_LEXICOGRAPHIC_GENERATOR = [
    (1, [Permutation(1)]),
    (
        3,
        [
            Permutation(1, 2, 3),
            Permutation(1, 3, 2),
            Permutation(2, 1, 3),
            Permutation(2, 3, 1),
            Permutation(3, 1, 2),
            Permutation(3, 2, 1),
        ],
    ),
    (
        4,
        [
            Permutation(1, 2, 3, 4),
            Permutation(1, 2, 4, 3),
            Permutation(1, 3, 2, 4),
            Permutation(1, 3, 4, 2),
            Permutation(1, 4, 2, 3),
            Permutation(1, 4, 3, 2),
            Permutation(2, 1, 3, 4),
            Permutation(2, 1, 4, 3),
            Permutation(2, 3, 1, 4),
            Permutation(2, 3, 4, 1),
            Permutation(2, 4, 1, 3),
            Permutation(2, 4, 3, 1),
            Permutation(3, 1, 2, 4),
            Permutation(3, 1, 4, 2),
            Permutation(3, 2, 1, 4),
            Permutation(3, 2, 4, 1),
            Permutation(3, 4, 1, 2),
            Permutation(3, 4, 2, 1),
            Permutation(4, 1, 2, 3),
            Permutation(4, 1, 3, 2),
            Permutation(4, 2, 1, 3),
            Permutation(4, 2, 3, 1),
            Permutation(4, 3, 1, 2),
            Permutation(4, 3, 2, 1),
        ],
    ),
]
