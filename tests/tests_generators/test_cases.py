TEST_PERMUTATION_GENERATOR_EXCPETIONS = [
    (13, 3, TypeError, "The parameter `algorithm` must be of type string"),
    ("test", 3, ValueError, "The given algorithm"),
    ("lexicographic", "test", TypeError, "The parameter `degree`"),
    ("lexicographic", 0, ValueError, "The parameter `degree` must be a non-zero positive integer"),
]
