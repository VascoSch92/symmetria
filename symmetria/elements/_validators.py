from typing import TYPE_CHECKING, Tuple
from itertools import combinations

if TYPE_CHECKING:
    from symmetria.elements.cycle import Cycle


def _validate_cycle(cycle: Tuple[int, ...]) -> None:
    """Private method to validate and standardize a set of integers to form a cycle.

    A tuple is eligible to be a cycle if it contains only strictly positive integers.
    """
    for element in cycle:
        if isinstance(element, int) is False:
            raise ValueError(f"Expected `int` type, but got {type(element)}.")
        if element < 1:
            raise ValueError(f"Expected all strictly positive values, but got {element}.")


def _validate_cycle_decomposition(cycles: Tuple["Cycle", ...]) -> None:
    """Private method to validate and standardize a tuple of cycles to become a cycle decomposition.

    A tuple of cycles is eligible to be a cycle decomposition if and only if:
        - every pair of cycles is disjoint, meaning their supports are disjoint;
        - every element from 1 to the largest permuted element is included in at least one cycle.
    """
    # checks that the cycles are disjoint
    for cycle_a, cycle_b in combinations(cycles, 2):
        if set(cycle_a.elements) & set(cycle_b.elements):
            raise ValueError(f"The cycles {cycle_a} and {cycle_b} don't have disjoint support.")

    # checks that every element is included in a cycle
    elements = {element for cycle in cycles for element in cycle.elements}
    if set(range(1, len(elements) + 1)) != elements:
        raise ValueError(
            "Every element from 1 to the biggest permuted element must be included in some cycle,\n "
            f"but this is not the case for the element(s): {set(range(1, len(elements) + 1)).difference(elements)}"
        )


def _validate_permutation(image: Tuple[int, ...]) -> None:
    """Private method to check if a set of integers is eligible as image for a permutation.

    Recall that, a tuple of integers represent the image of a permutation if the following conditions hold:
        - all the integers are strictly positive;
        - all the integers are bounded by the total number of integers;
        - there are no integer repeated.
    """
    values = set()
    for img in image:
        if isinstance(img, int) is False:
            raise ValueError(f"Expected `int` type, but got {type(img)}.")
        elif img < 1:
            raise ValueError(f"Expected all strictly positive values, but got {img}")
        elif img > len(image):
            raise ValueError(f"The permutation is not injecting on its image. Indeed, {img} is not in the image.")
        elif img in values:
            raise ValueError(
                f"It seems that the permutation is not bijective. Indeed, {img} has two, or more, pre-images."
            )
        else:
            values.add(img)
