from math import lcm
from typing import Any, Set, Dict, List, Tuple, Union, Iterable
from itertools import combinations

import symmetria.elements.cycle
import symmetria.elements.permutation
from symmetria._interfaces import _Element

__all__ = ["CycleDecomposition"]


class CycleDecomposition(_Element):
    r"""The ``CycleDecomposition`` class represents the cycle decomposition of a permutation of the symmetric group.

    Recall that every permutation of the symmetric group can be represented uniquely as the composition of a finite
    number of cycles thanks to the `Cycle Decomposition Theorem for Permutations`.

    To define a permutation as a cycle decomposition, you need to provide its cycles.

    For example, to define the permutation given by the cycles: ``Cycle(2, 1)`` and ``Cycle(4, 3)``, you should write
    ``CycleDecomposition(Cycle(2, 1), Cycle(4, 3))``.

    :param cycle: Cycle factors of the permutation.
    :type cycle: Cycle

    :raises ValueError: If there are two or more cycles with non-disjoint support.
    :raises ValueError: If there are missing cycles in the decomposition.

    :example:
        >>> cycle = CycleDecomposition(Cycle(2, 1), Cycle(4, 3))
        >>> cycle = CycleDecomposition(*[Cycle(2, 1), Cycle(4, 3)])
        >>> cycle = CycleDecomposition(*(Cycle(2, 1), Cycle(4, 3)))
    """

    __slots__ = ["_cycles", "_domain"]

    def __init__(self, *cycles: "Cycle") -> None:
        self._cycles: Tuple["Cycle", ...] = self._validate_and_standardize(
            cycles=cycles,
        )
        self._domain: Iterable[int] = range(
            1,
            max(max(cycle.elements) for cycle in self._cycles) + 1,
        )

    @staticmethod
    def _validate_and_standardize(cycles: Tuple["Cycle", ...]) -> Tuple["Cycle", ...]:
        """Private method to validate and standardize a tuple of cycles to become a cycle decomposition.

        A tuple of cycles is eligible to be a cycle decomposition if and only if:
            - every pair of cycles is disjoint, meaning their supports are disjoint;
            - every element from 1 to the largest permuted element is included in at least one cycle.
        Furthermore, the cycle decomposition is standardized, meaning the cycles are ordered by the first
        element of each cycle in increasing order.
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

        # standardization
        cycles = sorted(cycles, key=lambda cycle: cycle[0])
        return tuple(cycles)

    def __bool__(self) -> bool:
        r"""Check if the cycle decomposition is non-empty, i.e., it is different from the identity
        cycle decomposition.

        :return: True if the cycle decomposition is different from the identity cycle decomposition, False otherwise.
        :rtype: bool

        :example:
            >>> cycle_decomposition = CycleDecomposition(Cycle(1))
            >>> bool(cycle_decomposition)
            False
            >>> cycle_decomposition = CycleDecomposition(Cycle(1), Cycle(2))
            >>> bool(cycle_decomposition)
            False
            >>> cycle_decomposition = CycleDecomposition(Cycle(2, 1, 3))
            >>> bool(cycle_decomposition)
            True

        :note: Every cycle of the form ``CycleDecomposition(Cycle(n))`` is considered empty for every
            :math:`n \in \mathbb{N}`, i.e., ``bool(CycleDecomposition(Cycle(n))) = False``. Same for cycle decomposition
            of identity cycle, e.g., ``CycleDecomposition(Cycle(1), Cycle(2), Cycle(3)).``
        """
        return any(bool(cycle) for cycle in self)

    def __call__(self, item: Any) -> Any:
        """Call the cycle decomposition on the `item` object, i.e., mimic a cycle decomposition action on the
        element `item`.

        - If `item` is an integer, it applies the cycle decomposition to the integer.
        - If `item` is a string, a list or a tuple, it applies the cycle decomposition permuting the values by indexes.
        - If `item` is a permutation, it returns the composition of the cycle decomposition with the permutation.
        - If `item` is a cycle or a cycle decomposition, it returns the composition in cycle decomposition.

        :param item: The object on which the cycle acts.
        :type item: Any

        :return: The permuted object.
        :rtype: Any

        :raises ValueError: If there are not enough elements in the item to perform the permutation.
        :raises ValueError: If attempting to compose the cycle decomposition with a permutation, cycle, or cycle
            decomposition from a different symmetric group.
        :raises TypeError: If the item type is not supported.
        """
        if isinstance(item, int):
            return self._call_on_integer(original=item)
        elif isinstance(item, (str, List, Tuple)):
            if max(self.domain) > len(item):
                raise ValueError(f"Not enough object to permute {item} using the cycle {self}.")
            return self._call_on_str_list_tuple(original=item)
        elif isinstance(item, symmetria.elements.permutation.Permutation):
            if self.domain != item.domain:
                raise ValueError(
                    f"Cannot compose cycle decomposition {self} with permutation {item},"
                    " because they don't live in the same Symmetric group."
                )
            return self._call_on_permutation(original=item)
        elif isinstance(item, symmetria.elements.cycle.Cycle):
            if self.domain != item.domain:
                raise ValueError(
                    f"Cannot compose cycle decomposition {self} with cycle {item},"
                    " because they don't live in the same Symmetric group."
                )
            return self * CycleDecomposition(item)
        elif isinstance(item, symmetria.elements.cycle_decomposition.CycleDecomposition):
            if self.domain != item.domain:
                raise ValueError(
                    f"Cannot compose cycle decomposition {self} with cycle decomposition {item},"
                    " because they don't live in the same Symmetric group."
                )
            return self * item
        raise TypeError(f"Calling a cycle on {type(item)} is not supported.")

    def _call_on_integer(self, original: int) -> int:
        """Private method for calls on integer."""
        if original in self.domain:
            return self.map[original]
        return original

    def _call_on_str_list_tuple(self, original: Union[str, Tuple, List]) -> Union[str, Tuple, List]:
        """Private method for calls on string, list and tuple."""
        permuted = list(_ for _ in original)
        for idx, w in enumerate(original, 1):
            permuted[self._call_on_integer(original=idx) - 1] = w
        if isinstance(original, str):
            return "".join(permuted)
        elif isinstance(original, Tuple):
            return tuple(p for p in permuted)
        else:
            return permuted

    def _call_on_permutation(self, original: "Permutation") -> "Permutation":
        return symmetria.elements.permutation.Permutation.from_cycle_decomposition(self) * original

    def __eq__(self, other: Any) -> bool:
        """Check if the cycle decomposition is equal to the `another` object.

        :param other: The object to compare with.
        :type other: Any

        :return: True if the cycle decomposition is equal to `other`, i.e., they define the same map. Otherwise, False.
        :rtype: bool
        """
        if isinstance(other, CycleDecomposition):
            if len(self) != len(other):
                return False
            else:
                for cycle_a, cycle_b in zip(self, other):
                    if cycle_a.elements != cycle_b.elements:
                        return False
                return True
        return False

    def __getitem__(self, idx: int) -> "Cycle":
        """Return the cycle of the cycle decomposition at the given index `item`.

        The index corresponds to the position in the cycle decomposition, starting from 0.

        :param idx: The index of the cycle.
        :type idx: int

        :return: The cycle of the cycle decomposition at the specified index.
        :rtype: int

        :raises IndexError: If the index is out of range.

        :example:
            >>> cycle_decomposition = CycleDecomposition(Cycle(1, 2), Cycle(3, 4))
            >>> cycle_decomposition[0]
            Cycle(1, 2)
        """
        return self._cycles[idx]

    def __int__(self) -> int:
        """
        :raise NotImplementedError: The method is not implemented for the class ``CycleDecomposition``,
            because it is not possible to uniquely represent a cycle decomposition of a permutation using just
            an integer.
        """
        raise NotImplementedError(
            "The method is not implemented for the class `CycleDecomposition`, because it is not possible \n"
            "to clearly represent a cycle decomposition of a permutation using just an integer. \n"
            "If you want to have an integer representation for this object, convert it to a ``Permutation`` first."
        )

    def __iter__(self) -> Iterable["Cycle"]:
        """Return an iterator over the cycles in the cycle decomposition.

        :return: An iterator over the cycles in the cycle decomposition.
        :rtype: Iterable[Cycle]

        :example:
            >>> cycle_decomposition = CycleDecomposition(Cycle(1, 2), Cycle(3, 4))
            >>> for cycle in cycle_decomposition:
            >>>     print(cycle)
            Cycle(1, 2)
            Cycle(3, 4)
        """
        return iter(self._cycles)

    def __len__(self) -> int:
        """Return the length of the cycle decomposition, which is the number of cycles present in the decomposition.

        :return: The length of the cycle decomposition.
        :rtype: int

        :example:
            >>> cycle_decomposition = CycleDecomposition(Cycle(1))
            >>> len(cycle_decomposition)
            1
            >>> cycle_decomposition = CycleDecomposition(Cycle(1, 3), Cycle(2))
            >>> len(cycle_decomposition)
            3
            >>> cycle_decomposition = CycleDecomposition(Cycle(1, 3), Cycle(4, 5), Cycle(2, 6))
            >>> len(cycle_decomposition)
            6
        """
        return len(self._cycles)

    def __mul__(self, other: "CycleDecomposition") -> "CycleDecomposition":
        """Multiply the cycle decomposition with another cycle decomposition, resulting in a new cycle decomposition
        that represents the composition of the two cycle decompositions.

        :param other: The other cycle decomposition to multiply with.
        :type other: CycleDecomposition

        :return: The composition of the two cycle decompositions.
        :rtype: CycleDecomposition

        :raises ValueError: If the cycle decompositions don't live in the same Symmetric group.
        :raises TypeError: If the other object is not a `CycleDecomposition`.
        """
        if isinstance(other, symmetria.elements.cycle_decomposition.CycleDecomposition):
            if self.domain != other.domain:
                raise ValueError(
                    f"Cannot compose cycle decomposition {self} with cycle decomposition {other},"
                    " because they don't live in the same Symmetric group."
                )
            return symmetria.elements.permutation.Permutation.from_dict(
                p={idx: self.map[other.map[idx]] for idx in self.domain}
            ).cycle_decomposition()
        raise TypeError(f"Product between types `CycleDecomposition` and {type(other)} is not implemented.")

    def __repr__(self) -> str:
        r"""Return a string representation of the cycle decomposition in the format
        'CycleDecomposition(Cycle(x, ...), Cycle(y, ...), ...)', where :math:`x, y, ... \in \mathbb{N}` are
        the elements of the cycles.

        :return: A string representation of the cycle decomposition.
        :rtype: str

        :example:
            >>> cycle_decomposition = CycleDecomposition(Cycle(1))
            >>> cycle_decomposition.__repr__()
            CycleDecomposition(Cycle(1))
            >>> cycle_decomposition = CycleDecomposition(Cycle(1, 3), Cycle(2))
            >>> cycle_decomposition.__repr__()
            CycleDecomposition(Cycle(1, 3), Cycle(2))
            >>> cycle_decomposition = CycleDecomposition(Cycle(1, 3), Cycle(4, 5, 2, 6))
            >>> cycle_decomposition.__repr__()
            CycleDecomposition(Cycle(1, 3), Cycle(4, 5, 2, 6))
        """
        return f"CycleDecomposition({', '.join([cycle.__repr__() for cycle in self])})"

    def __str__(self) -> str:
        """Return a string representation of the cycle decmposition in the cycle notation.

        :return: A string representation of the cycle decomposition.
        :rtype: str

        :example:
            >>> cycle_decomposition = CycleDecomposition(Cycle(1))
            >>> str(cycle_decomposition)
            (1)
            >>> cycle_decomposition = CycleDecomposition(Cycle(1, 3), Cycle(2))
            >>> str(cycle_decomposition)
            (1 3)(2)
            >>> cycle_decomposition = CycleDecomposition(Cycle(1, 3), Cycle(4, 5, 2, 6))
            >>> str(cycle_decomposition)
            (1 3)(4 5 2 6)
        """
        return "".join([str(c) for c in self])

    @property
    def domain(self) -> Iterable[int]:
        """Return an iterable containing the elements of the domain of the cycle decomposition.

        The domain of a cycle decomposition is the set of indices for which the cycle decomposition is defined.

        :return: The domain of the cycle decomposition.
        :rtype: Iterable[int]

        :example:
            >>> cycle_decomposition = CycleDecomposition(Cycle(1))
            >>> cycle_decomposition.domain()
            range(1, 2)
            >>> cycle_decomposition = CycleDecomposition(Cycle(3, 1, 2))
            >>> cycle_decomposition.domain()
            range(1, 4)
            >>> cycle_decomposition = CycleDecomposition(Cycle(1), Cycle(3, 4, 5, 2, 6))
            >>> cycle_decomposition.domain()
            range(1, 7)
        """
        return self._domain

    @property
    def map(self) -> Dict[int, int]:
        """Return a dictionary representing the mapping of the cycle decomposition,
        where keys are indices and values are the corresponding elements after permutation.

        :return: The mapping of the cycle decompostiion.
        :rtype: Dict[int, int]

        :example:
            >>> cycle_decomposition = CycleDecomposition(Cycle(1))
            >>> cycle_decomposition.map()
            {1: 1}
            >>> cycle_decomposition = CycleDecomposition(Cycle(1, 2), Cycle(3, 4))
            >>> cycle_decomposition.map()
            {1: 2, 2: 1, 3: 4, 4: 3}
        """
        _map = {}
        for cycle in self:
            _map.update(cycle.map)
        return _map

    def cycle_decomposition(self) -> "CycleDecomposition":
        """Return the cycle decomposition of the permutation.

        As a cycle decomposition is already in the
        cycle decomposition, the method return the cycle decomposition itself.

        :return: The cycle decomposition of the permutation.
        :rtype: CycleDecomposition
        """
        return self

    def cycle_notation(self) -> str:
        """Return a string representing the cycle notation of the cycle decomposition.

        :return: The cycle notation of the permutation.
        :rtype: str

        :example:
            >>> cycle_decomposition = CycleDecomposition(Cycle(1))
            >>> cycle_decomposition.cycle_notation()
            '(1)'
            >>> cycle_decomposition = CycleDecomposition(Cycle(1, 3, 2))
            >>> cycle_decomposition.cycle_notation()
            '(1 3 2)'
            >>> cycle_decomposition = CycleDecomposition(Cycle(1, 3, 2), Cycle(4))
            >>> cycle_decomposition.cycle_notation()
            '(1 3 2)(4)'
        """
        return str(self)

    def order(self) -> int:
        r"""Return the order of the cycle permutation.

        Recall that the order of a cycle decompostion is the least common multiple of lengths (order) of its cycles.

        :return: The order of the cycle permutation.
        :rtype: int

        :example:
            >>> cycle_decomposition = CycleDecomposition(Cycle(1))
            >>> cycle_decomposition.order()
            1
            >>> cycle_decomposition = CycleDecomposition(Cycle(1, 3, 2))
            >>> cycle_decomposition.order()
            3
            >>> cycle_decomposition = CycleDecomposition(Cycle(1, 3, 2), Cycle(4, 5))
            >>> cycle_decomposition.order()
            6
        """
        return lcm(*[len(cycle) for cycle in self])

    def support(self) -> Set[int]:
        """Return a set containing the indices in the domain of the permutation whose images are different from
        their respective indices, i.e., the set of :math:`n` in the permutation domain which are not mapped to itself.

        :return: The support set of the cycle decomposition.
        :rtype: Set[int]

        :example:
            >>> cycle_decomposition = CycleDecomposition(Cycle(1))
            >>> cycle_decomposition.support()
            set()
            >>> cycle_decomposition = CycleDecomposition(Cycle(1), Cycle(2, 3))
            >>> cycle_decomposition.support()
            {2, 3}
        """
        return {element for cycle in self if len(cycle) != 1 for element in cycle.elements}

    def is_derangement(self) -> bool:
        r"""Check if the cycle decomposition is a derangement.

        Recall that a permutation :math:`\sigma` is called a derangement if it has no fixed points, i.e.,
        :math:`\sigma(x) \neq x` for every :math:`x` in the permutation domain.

        :return: True if the permutation is a derangement, False otherwise.
        :rtype: bool

        :example:
            >>> cycle_permutation = CycleDecomposition(Cycle(1))
            >>> cycle_permutation.is_derangement()
            False
            >>> cycle_decomposition = CycleDecomposition(Cycle(1, 2, 3))
            >>> cycle_decomposition.is_derangement()
            True
            >>> cycle_decomposition = CycleDecomposition(Cycle(1), Cycle(2, 3))
            >>> cycle_decomposition.is_derangement()
            False
        """
        for cycle in self:
            if len(cycle) == 1:
                return False
        return True

    def equivalent(self, other: Any) -> bool:
        """Check if the cycle decomposition is equivalent to another object.

        This method is introduced because we can have different representation of the same cycle decomposition, e.g.,
        as a cycle, or as permutation.

        :param other: The object to compare with.
        :type other: Any

        :return: True if the cycle decomposition is equivalent to the other object, False otherwise.
        :rtype: bool

        :example:
            >>> cycle_decomposition = CycleDecomposition(Cycle(1, 2, 3)))
            >>> cycle_decomposition.equivalent(cycle_decomposition)
            True
            >>> cycle = Cycle(1, 2, 3)
            >>> cycle_decomposition.equivalent(cycle)
            True
            >>> permutation = Permutation(2, 3, 1)
            >>> cycle_decomposition.equivalent(permutation)
            True
        """
        if isinstance(other, CycleDecomposition):
            return self == other
        elif isinstance(other, symmetria.elements.cycle.Cycle):
            if len(other) == 1:
                return other[0] == 1
            else:
                for cycle in self:
                    if len(cycle) > 1 and cycle != other:
                        return False
            return True
        elif isinstance(other, symmetria.elements.permutation.Permutation):
            return symmetria.elements.permutation.Permutation.from_cycle_decomposition(self) == other
        return False

    def orbit(self, item: Any) -> List[Any]:
        r"""Compute the orbit of `item` object under the action of the cycle decomposition.

        Recall that the orbit of the action of a cycle decomposition :math:`\sigma` on an element x is given by the set
        :math:`\{ \sigma^n(x): n \in \mathbb{N}\}`.

        :param item: The initial element or iterable to compute the orbit for.
        :type item: Any

        :return: The orbit of the specified element under the permutation.
        :rtype: List[Any]
        """
        if isinstance(item, symmetria.elements.cycle.Cycle):
            item = item.cycle_decomposition()
        orbit = [item]
        next_element = self(item)
        while next_element != item:
            orbit.append(next_element)
            next_element = self(next_element)
        return orbit
