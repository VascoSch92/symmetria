from itertools import combinations
from math import lcm
from typing import Tuple, List, Any, Dict, Iterable, Set

import symmetria.elements.cycle
import symmetria.elements.permutation
from symmetria.interfaces import _Element


class CycleDecomposition(_Element):
    __slots__ = ["_cycles"]

    def __init__(self, *cycles: "Cycle") -> None:
        self._cycles: Tuple["Cycle", ...] = self._validate_and_standardize(cycles=cycles)
        self._domain: Iterable[int] = range(1, max(max(cycle.elements) for cycle in self._cycles) + 1)

    @staticmethod
    def _validate_and_standardize(cycles: Tuple["Cycle", ...]) -> Tuple["Cycle", ...]:
        """
        Private method to validate and standardize a tuple of cycles to become a cycle decomposition.
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
                f"but this is not the case for the element(s): {set(range(1, len(elements) + 1)).difference(elements)}")

        # standardization
        cycles = sorted(cycles, key=lambda cycle: cycle[0])
        return tuple(cycles)

    def __bool__(self) -> bool:
        r"""
        Check if the cycle decomposition is non-empty, i.e., it is different from the identity
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

    def __eq__(self, other: Any) -> bool:
        """
        Check if the cycle decomposition is equal to another object.

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
                    if cycle_a != cycle_b:
                        return False
                return True
        return False

    def __getitem__(self, item: int) -> "Cycle":
        """
        Returns the cycle of the cycle decomposition at the given index `item`.
        The index corresponds to the position in the cycle decomposition, starting from 0.

        :param item: The index of the cycle.
        :type item: int

        :return: The cycle of the cycle decomposition at the specified index.
        :rtype: int

        :raises IndexError: If the index is out of range.
        """
        return self._cycles[item]

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
        return iter(self._cycles)

    def __len__(self) -> int:
        """
        Returns the length of the cycle permutation, which is the number of cycles present in the decomposition.

        :return: The length of the permutation.
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
        """
        Multiplies the cycle decomposition with another cycle decomposition, resulting in a new cycle decomposition
        that represents the composition of the two cycle decompositions.

        :param other: The other cycle decomposition to multiply with.
        :type other: CycleDecomposition

        :return: The composition of the two cycle decompositions.
        :rtype: CycleDecomposition

        :raises ValueError: If the cycle decompositions don't live in the same Symmetric group.
        :raises TypeError: If the other object is not a `CycleDecomposition`.
        """
        if isinstance(other, CycleDecomposition):
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
        r"""
        Returns a string representation of the cycle decomposition in the format
        "CycleDecompposition(Cycle(x, y), Cycle(z, ...), ...)", where :math:`x, y, z, ... \in \mathbb{N}` are
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
        """
        Returns a string representation of the cycle decmposition in the cycle notation.

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
        """
        Returns an iterable containing the elements of the domain of the cycle decomposition.
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
        """
        Returns a dictionary representing the mapping of the cycle decomposition,
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
        """
        Return the cycle decomposition of the permutation. As a cycle decomposition is already in the
        cycle decomposition, the method return the cycle decomposition itself.

        :return: The cycle decomposition of the permutation.
        :rtype: CycleDecomposition
        """
        return self

    def cycle_notation(self) -> str:
        """
        Returns a string representing the cycle notation of the cycle decomposition.

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
        r"""
        Return the order of the cycle permutation.

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
        """
        Returns a set containing the indices in the domain of the permutation
        whose images are different from their respective indices, i.e., the set of :math:`n` in the permutation
        domain which are not mapped to itself.

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
        r"""
        Check if the cycle decomposition is a derangement.

        Recall that a permutation :math:`\sigma` is called a derangement if it has no fixed points, i.e.,
        :math:`\sigma(x) \neq x` for every :math:`x` in the permutation domain.

        :return: True if the permutation is a derangement, False otherwise.
        :rtype: bool

        :example:
            >>> cycle_permutation = CycleDecomposition(Cycle((1)))
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
        raise NotImplementedError
