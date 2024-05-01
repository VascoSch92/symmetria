from itertools import combinations
from math import lcm
from typing import (
    Tuple,
    Iterable,
    Dict,
    Any,
    Union,
    Set,
    List,
)

import symmetria.elements.permutations
from symmetria.interfaces import _Element


class Cycle(_Element):
    __slots__ = ["_cycle"]

    def __init__(self, *cycle: int) -> None:
        self._cycle: Tuple[int, ...] = self._validate_and_standardize(cycle)
        self._domain: Iterable[int] = range(1, max(self._cycle) + 1)

    @staticmethod
    def _validate_and_standardize(cycle: Tuple[int, ...]) -> Tuple[int, ...]:
        """
        Private method to validate and standardize a set of integers to form a cycle.
        A tuple is eligible to be a cycle if it contains only strictly positive integers.
        The standard form for a cycle is the (unique) one where the first element is the smallest.
        """
        for element in cycle:
            if isinstance(element, int) is False:
                raise ValueError(f"Expected `int` type, but got {type(element)}.")
            if element < 1:
                raise ValueError(f"Expected all strictly positive values, but got {element}.")

        smallest_element_index = cycle.index(min(cycle))
        if smallest_element_index == 0:
            return tuple(cycle)
        return cycle[smallest_element_index:] + cycle[:smallest_element_index]

    def __bool__(self) -> bool:
        r"""
        Check if the cycle is different from the identity cycle.

        :return: True if the cycle is different from the identity cycle, False otherwise.
        :rtype: bool

        :example:
            >>> cycle = Cycle(1)
            >>> bool(cycle)
            False
            >>> cycle = Cycle(2, 1, 3)
            >>> bool(cycle)
            True

        :note: Every cycle of the form ``Cycle(n)`` is considered empty for every :math:`n \in \mathbb{N}`, i.e.,
            ``bool(Cycle(n)) = False``.
        """
        return len(self.elements) != 1

    def __call__(self, item: Union[int, Iterable]) -> Union[int, Iterable]:
        """
        Call the cycle on the `item` object, i.e., mimic a cycle action on a set.
        If `item` is an integer, it applies the cycle to the integer.
        If `item` is an iterable, e.g., a str, list or tuple, it applies the cycle permuting
        the values using the indeces.

        :param item: The object on which the permutation acts.
        :type item: Union[int, Iterable]

        :return: The permuted object.
        :rtype: Union[int, Iterable]

        :raises AssertionError: If the length of the cycle is greater than the length of `item`, i.e.,
            the cycle cannot permute the `item`.
        :raises TypeError: If `item` is not an integer or an iterable.

        :example:
            >>> cycle = Cycle(3, 1, 2)
            >>> cycle(2)
            3
            >>> cycle("abc")
            "cab"
            >>> cycle([1, 2, 3])
            [3, 1, 2]
        """
        if isinstance(item, int):
            return self._call_on_integer(idx=item)
        elif isinstance(item, (str, List, Tuple)):
            assert max(self.elements) <= len(item), f"Not enough object to permute {item} using the cycle {self}."
            permuted = self._call_on_iterable(original=item)
            if isinstance(item, str):
                return "".join(permuted)
            elif isinstance(item, Tuple):
                return tuple(p for p in permuted)
            return self._call_on_iterable(original=item)
        raise TypeError(f"Expected type `int` or `Iterable`, but got {type(item)}")

    def _call_on_integer(self, idx: int) -> int:
        """Private method for calls on integer."""
        if idx in self.elements:
            return self[(self.elements.index(idx) + 1) % len(self)]
        return idx

    def _call_on_iterable(self, original: Iterable) -> List:
        """Private method for calls on iterable."""
        permuted = [None for _ in original]
        for idx, w in enumerate(original, 1):
            permuted[self._call_on_integer(idx=idx) - 1] = w
        return permuted

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Cycle):
            lhs_length, rhs_length = len(self), len(other)
            if lhs_length != rhs_length:
                return False
            else:
                # in this case we have the identity
                if lhs_length == 1:
                    return True
                # compare if the two cycles are equal
                lhs_elements, rhs_elements = self.elements, other.elements
                for idx, element in enumerate(lhs_elements):
                    if element not in rhs_elements:
                        return False
                    if self[(idx + 1) % lhs_length] != other[(rhs_elements.index(element) + 1) % rhs_length]:
                        return False
                return True
        elif isinstance(other, CycleDecomposition):
            # case where both are the identity
            if bool(self) is False and bool(other) is False:
                return max(self.elements) == max([max(cycle.elements) for cycle in other])
            # cases where is the identity but the other no
            elif (bool(self) is False and bool(other) is True) or (bool(self) is True and bool(other) is False):
                return False
            # both not the identity
            else:
                for cycle in other:
                    if len(cycle) > 1:
                        return self == cycle
        elif isinstance(other, symmetria.elements.permutations.Permutation):
            return self == other.cycle_decomposition()
        return False

    def __getitem__(self, item: int) -> int:
        """
        Returns the value of the cycle at the given index `item`.
        The index corresponds to the position in the cycle, starting from 0

        :param item: The index of the cycle.
        :type item: int

        :return: The value of the cycle at the specified index.
        :rtype: int

        :raises IndexError: If the index is out of range.
        """
        return self._cycle[item]

    def __int__(self) -> int:
        """
        Convert the cycle to its integer representation.

        :return: The integer representation of the cycle.
        :rtype: int

        :example:
            >>> cycle = Cycle(1)
            >>> int(cycle)
            1
            >>> cycle = Cycle(13)
            >>> int(cycle)
            13
            >>> cycle = Cycle(3, 1, 2)
            >>> int(cycle)
            312
            >>> cycle = Cycle(1, 3, 4, 5, 2, 6)
            >>> int(cycle)
            134526
        """
        return sum([element * 10 ** (len(self) - idx) for idx, element in enumerate(self.elements, 1)])

    def __len__(self) -> int:
        """
        Returns the length of the cycle, which is the number of elements in its domain.

        :return: The length of the cycle.
        :rtype: int

        :example:
            >>> cycle = Cycle(3, 1, 2)
            >>> len(cycle)
            3
            >>> Cycle = Cycle(1, 3, 4, 5, 2, 6)
            >>> len(cycle)
            6
        """
        return len(self._cycle)

    def __mul__(
            self,
            other: Union["Cycle", "CycleDecomposition", "Permutation"],
    ) -> Union["Cycle", "CycleDecomposition", "Permutation"]:
        if isinstance(other, Cycle):
            # case where the two cycles are disjoint
            if set(self.elements).isdisjoint(set(other.elements)):
                single_cycle = []
                _range = set(self.elements).union(set(other.elements))
                for idx in range(1, max(_range) + 1):
                    if idx not in _range:
                        single_cycle.append(Cycle(idx))
                return CycleDecomposition(self, *[other, *single_cycle])
            elif self.domain == other.domain:
                cycle = []
                for idx in self.domain:
                    _other = other[(idx+1) % len(other)]
                    cycle.append(self[(self.elements.index(_other) + 1) % len(self)])
                return Cycle(*cycle)
            else:
                return CycleDecomposition(self) * CycleDecomposition(other)
        if isinstance(other, symmetria.elements.permutations.Permutation):
            if set(self.domain).issubset(set(other.domain)) is False:
                raise ValueError(
                    f"Cannot compose permutation {self} with permutation {other},"
                    " because they don't live in the same Symmetric group."
                )
            return symmetria.elements.permutations.Permutation.from_dict(
                p={
                    idx: self.map[other[idx]] if other[idx] in self.map else other[idx]
                    for idx in other.domain
                }
            )
        elif isinstance(other, CycleDecomposition):
            if set(self.domain).issubset(set(other.domain)) is False:
                raise ValueError(
                    f"Cannot compose permutation {self} with cycle decomposition {other},"
                    " because they don't live in the same symmetric group."
                )
            return (self * symmetria.elements.permutations.Permutation.from_cycle_decomposition(other)).cycle_decomposition()
        raise TypeError(f"Product between types `Cycle` and {type(other)} is not implemented.")

    def __repr__(self) -> str:
        r"""
        Returns a string representation of the cycle in the format "Cycle(x, y, z, ...)",
        where :math:`x, y, z, ... \in \mathbb{N}` are the elements of the cycle.

        :return: A string representation of the cycle.
        :rtype: str

        :example:
            >>> cycle = Cycle(3, 1, 2)
            >>> cycle.__repr__()
            Cycle(3, 1, 2)
            >>> cycle = Cycle(1, 3, 4, 5, 2, 6)
            >>> cycle.__repr__()
            Cycle(1, 3, 4, 5, 2, 6)
        """
        return f"Cycle({', '.join(str(element) for element in self.elements)})"

    def __str__(self) -> str:
        """
        Returns a string representation of the cycle in the form of cycle notation.

        :return: A string representation of the cycle.
        :rtype: str

        :example:
            >>> cycle = Cycle(3, 1, 2)
            >>> print(cycle)
            (3 1 2)
            >>> cycle = Cycle(1, 3, 4, 5, 2, 6)
            >>> print(cycle)
            (1 3 4 5 2 6)
        """
        return "(" + " ".join([str(element) for element in self.elements]) + ")"

    @property
    def domain(self) -> Iterable[int]:
        # TODO: add description
        return self._domain

    @property
    def map(self) -> Dict[int, int]:
        return {element: self[(idx + 1) % len(self)] for idx, element in enumerate(self.elements)}

    @property
    def elements(self) -> Tuple[int]:
        # TODO: add description
        return self._cycle

    def cycle_notation(self) -> str:
        # TODO: add description
        return str(self)

    def is_derangement(self) -> bool:
        # TODO: add description
        return len(self) > 1

    def order(self) -> int:
        r"""
        Return the order of the cycle.

        Recall that the order of a permutation :math:`\sigma` is the smallest positive integer :math:`n \in \mathbb{N}`
        such that :math:`\sigma^n = id`, where :math:`id` is the identity permutation. Therefore, the order of a cycle
        is nothing but just its length.

        :return: The order of the cycle.
        :rtype: int

        :example:
            >>> cycle = Cycle(3, 1, 2)
            >>> cycle.order()
            1
            >>> cycle = Cycle(3, 1, 2)
            >>> cycle.order()
            3
            >>> cycle = Cycle(1, 3, 4, 5, 2, 6)
            >>> cycle.order()
            4
        """
        return len(self)

    def support(self) -> Set[int]:
        return set(self._cycle) if len(self) > 1 else set()


class CycleDecomposition(_Element):
    __slots__ = ["_cycles"]

    def __init__(self, *cycles: Cycle) -> None:
        self._cycles: Tuple[Cycle, ...] = self._validate_and_standardize(cycles=cycles)
        self._domain: Iterable[int] = range(1, max(max(cycle.elements) for cycle in self._cycles) + 1)

    @staticmethod
    def _validate_and_standardize(cycles: Tuple[Cycle, ...]) -> Tuple[Cycle, ...]:
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
        Check if the ``CycleDecomposition`` object is non-empty, i.e., it is different from the identity
        cycle decomposition.

        :return: True if the cycle decomposition is different from the identity cycle decomposition, False otherwise.
        :rtype: bool

        :example:
            >>> cycle_decomposition = CycleDecomposition(Cycle(1))
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
        if isinstance(other, CycleDecomposition):
            if len(self) != len(other):
                return False
            else:
                for cycle_a, cycle_b in zip(self, other):
                    if cycle_a != cycle_b:
                        return False
                return True
        elif isinstance(other, Cycle):
            if len(other) == 1:
                return other[0] == 1
            else:
                for cycle in self:
                    if len(cycle) > 1 and cycle != other:
                        return False
                return True
        elif isinstance(other, symmetria.elements.permutations.Permutation):
            return symmetria.elements.permutations.Permutation.from_cycle_decomposition(self) == other
        return False

    def __getitem__(self, item: int) -> Cycle:
        return self._cycles[item]

    def __int__(self) -> int:
        raise NotImplementedError(
            "This method is not implemented for the class `CycleDecomposition`, because it is not possible "
            "to clearly represent a cycle decomposition of a permutation using just an integer."
        )

    def __iter__(self) -> Iterable[Cycle]:
        return iter(self._cycles)

    def __len__(self) -> int:
        return len(self._cycles)

    def __repr__(self) -> str:
        return f"CycleDecomposition({self.cycle_notation()})"

    def __str__(self) -> str:
        return "".join([str(c) for c in self])

    @property
    def domain(self) -> Iterable[int]:
        return self._domain

    @property
    def map(self) -> Dict[int, int]:
        _map = {}
        for cycle in self:
            _map.update(cycle.map)
        return _map

    def cycle_notation(self) -> str:
        return str(self)

    def order(self) -> int:
        # TODO: add description
        return lcm(*[len(cycle) for cycle in self])

    def support(self) -> Set[int]:
        support = set()
        for cycle in self:
            if len(cycle) != 1:
                support.update(cycle.elements)
        return support

    def is_derangement(self) -> bool:
        for cycle in self:
            if len(cycle) == 1:
                return False
        return True
