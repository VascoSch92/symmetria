from typing import List, Generator

import symmetria.elements.permutation
from symmetria import Permutation


def _lexicographic(degree: int) -> Generator[Permutation, None, None]:
    """Private method to generate all the permutations of degree `degree` in lexicographic order.

    The algorithm is described as follows:
        1. Consider the identity permutation in the given degree.
        2. Find the largest index k such that permutation[k] < permutation[k + 1].
        3. If no k exists, then it is permutation is the last permutation. END.
        4. Find the largest index j greater than k such that permutation[k] < permutation[j].
        5. Swap the value of permutation[k] with that of permutation[j].
        6. Reverse the sequence from permutation[k + 1] up to and including the final element permutation[degree].
        7. Go to point 2.
    """
    permutation = list(range(1, degree + 1))

    while True:
        yield symmetria.Permutation(*permutation)

        k = next((i for i in range(degree - 2, -1, -1) if permutation[i] < permutation[i + 1]), -1)
        if k == -1:
            return None

        j = next(i for i in range(degree - 1, k, -1) if permutation[k] < permutation[i])
        permutation[k], permutation[j] = permutation[j], permutation[k]
        permutation[k + 1 :] = reversed(permutation[k + 1 :])


def _heap(degree: int) -> Generator[Permutation, None, None]:
    """Private method to generate all the permutations of degree `degree` using the Heap's algorithm.

    A description of the algorithm can be founded in the article:
        `Permutations by interchanges.` B. R. Heap, The Computer Journal, 6(3) (1963), pp. 293-298
    """

    def _heap_recursion(degree: int, permutation: List[int]) -> Generator[Permutation, None, None]:
        if degree == 1:
            yield symmetria.Permutation(*permutation)
        else:
            # Generate permutations with k-th unaltered
            yield from _heap_recursion(degree - 1, permutation)

            # Generate permutations for k-th swapped with each k-1 initial
            for i in range(degree - 1):
                # Swap choice dependent on parity of k
                if degree % 2 == 0:
                    permutation[i], permutation[degree - 1] = permutation[degree - 1], permutation[i]
                else:
                    permutation[0], permutation[degree - 1] = permutation[degree - 1], permutation[0]
                yield from _heap_recursion(degree - 1, permutation)

    return _heap_recursion(degree, list(range(1, degree + 1)))


def _steinhaus_johnson_trotter(degree: int) -> Generator[Permutation, None, None]:
    """Private method to generate all the permutations of degree `degree` using the Steinhaus-Johnson-Trotter algorithm.

    A description of the algorithm is given at:
        https://en.wikipedia.org/wiki/Steinhaus–Johnson–Trotter_algorithm
    """
    permutation = list(range(1, degree + 1))
    # Direction of each element, 1 for right, -1 for left
    directions = [-1] * degree

    while True:
        yield symmetria.Permutation(*permutation)

        mobile, mobile_index = -1, -1

        for i in range(degree):
            if (directions[i] == -1 and i != 0 and permutation[i] > permutation[i - 1]) or (
                directions[i] == 1 and i != degree - 1 and permutation[i] > permutation[i + 1]
            ):
                if permutation[i] > mobile:
                    mobile, mobile_index = permutation[i], i
        if mobile_index == -1:
            return None

        # Swap the mobile element with the adjacent element it is looking at
        swap_with = mobile_index + directions[mobile_index]
        permutation[mobile_index], permutation[swap_with] = permutation[swap_with], permutation[mobile_index]
        directions[mobile_index], directions[swap_with] = directions[swap_with], directions[mobile_index]

        # Reverse the direction of all elements larger than the current mobile element
        for i in range(degree):
            if permutation[i] > permutation[swap_with]:
                directions[i] = -directions[i]


def _zaks(degree: int) -> Generator[Permutation, None, None]:
    """Private method to generate all permutations of degree `degree` using the Zaks algorithm.

    A description of the algorithm is given in:
        Zaks, S. A new algorithm for generation of permutations. BIT 24, 196–204 (1984).
    """

    def _zaks_recursion(elements: List[int]) -> List[List[int]]:
        """Generate permutations in the specific Zaks order."""
        n = len(elements)

        if n == 1:
            return [elements[:]]
        if n == 2:
            return [elements[:], [elements[1], elements[0]]]
        if n == 3:
            a, b, c = elements[0], elements[1], elements[2]
            return [
                [a, b, c],
                [b, a, c],
                [c, a, b],
                [a, c, b],
                [b, c, a],
                [c, b, a],
            ]

        result = []
        smaller_perms = _zaks_recursion(elements[:-1])

        # Insert the last element in all possible positions
        for perm in smaller_perms:
            for i in range(len(perm) + 1):
                new_perm = perm[:i] + [elements[-1]] + perm[i:]
                result.append(new_perm)

        return result

    start = list(range(1, degree + 1))
    all_permutations = _zaks_recursion(start)
    for perm_list in all_permutations:
        yield Permutation(*perm_list)
