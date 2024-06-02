from typing import Generator

import symmetria.elements.permutation


def _lexicographic_generator(degree: int) -> Generator["Permutation", None, None]:
    """Private method to generate all the permutations of degree `degree` in lexicographic order.

    The algorithm is described as follows:
        - Step 1: Consider the identity permutation in the given degree.
        - Step 2: Find the largest index k such that permutation[k] < permutation[k + 1].
        - Step 3: If no k exists, then it is permutation is the last permutation. END.
        - Step 4: Find the largest index j greater than k such that permutation[k] < permutation[j].
        - Step 5: Swap the value of permutation[k] with that of permutation[j].
        - Step 6: Reverse the sequence from permutation[k + 1] up to and including the final element permutation[degree].
        - Step 7: Go to Step 2.
    """
    # step 1
    permutation = list(range(1, degree + 1))

    while True:
        yield symmetria.Permutation(*permutation)

        # step 2
        k = next((i for i in range(degree - 2, -1, -1) if permutation[i] < permutation[i + 1]), -1)

        # step 3
        if k == -1:
            return None

        # step 4
        j = next(i for i in range(degree - 1, k, -1) if permutation[k] < permutation[i])

        # step 5
        permutation[k], permutation[j] = permutation[j], permutation[k]

        # step 6
        permutation[k + 1 :] = reversed(permutation[k + 1 :])
