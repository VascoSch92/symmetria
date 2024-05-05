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

    def __call__(self, item: Any) -> Any:
        """
        Call the cycle on the `item` object, i.e., mimic a cycle action on the element `item`.

        - If `item` is an integer, it applies the cycle to the integer.
        - If `item` is a string, a list or a tuple, it applies the cycle permuting the values using the indeces.
        - If `item` is a permutation, it returns the composition of the cycle with the permutation.
        - If `item` is a cycle or a cycle decomposition, it returns the composition in cycle decomposition.

        :param item: The object on which the cycle acts.
        :type item: Any

        :return: The permuted object.
        :rtype: Any

        :raises AssertionError: If the largest element moved by the cycle is greater than the length of `item`, i.e.,
            the cycle cannot permute the `item`.
        :raises ValueError: If the cycle and the object `item` don't belong to the same Symmetric group.
        :raises TypeError: If the `item` is not of a supported type. See list above for supported types.

        :example:
            >>> cycle = Cycle(3, 1, 2)
            >>> cycle(2)
            3
            >>> cycle("abc")
            "cab"
            >>> cycle([1, 2, 3])
            [3, 1, 2]
            >>> cycle(Permutation(3, 1, 2))
            Permutation(1, 2, 3)
        """
        if isinstance(item, int):
            return self._call_on_integer(original=item)
        elif isinstance(item, (str, List, Tuple)):
            if max(self.elements) > len(item):
                raise ValueError(f"Not enough object to permute {item} using the cycle {self}.")
            return self._call_on_str_list_tuple(original=item)
        elif isinstance(item, symmetria.elements.permutations.Permutation):
            if max(self.elements) > len(item):
                raise ValueError(
                    f"Cannot compose cycle {self} with permutation {item},"
                    " because they don't live in the same Symmetric group."
                )
            return self._call_on_permutation(original=item)
        elif isinstance(item, Cycle):
            if set(self.domain).issubset(set(item.domain)) is False:
                raise ValueError(
                    f"Cannot compose cycle {self} with cycle {item},"
                    " because they don't live in the same Symmetric group."
                )
            return self._call_on_cycle_decomposition(original=item.cycle_decomposition())
        elif isinstance(item, CycleDecomposition):
            if max(self.elements) > max(item.domain):
                raise ValueError(
                    f"Cannot compose cycle {self} with cycle decomposition {item},"
                    " because they don't live in the same Symmetric group."
                )
            return self._call_on_cycle_decomposition(original=item)
        raise TypeError(f"Calling a cycle on {type(item)} is not supported.")

    def _call_on_integer(self, original: int) -> int:
        """Private method for calls on integer."""
        if original in self.elements:
            return self[(self.elements.index(original) + 1) % len(self)]
        return original

    def _call_on_str_list_tuple(self, original: Union[str, Tuple, List]) -> Union[str, Tuple, List]:
        """Private method for calls on string, list and tuple."""
        permuted = [_ for _ in original]
        for idx, w in enumerate(original, 1):
            permuted[self._call_on_integer(original=idx) - 1] = w
        if isinstance(original, str):
            return "".join(permuted)
        elif isinstance(original, Tuple):
            return tuple(p for p in permuted)
        else:
            return permuted

    def _call_on_permutation(self, original: "Permutation") -> "Permutation":
        """Private method for calls on permutation."""
        cycles = [self]
        for idx in original.domain:
            if idx not in self:
                cycles.append(Cycle(idx))
        cycle_decomposition = CycleDecomposition(*cycles)
        return symmetria.elements.permutations.Permutation.from_cycle_decomposition(cycle_decomposition) * original

    def _call_on_cycle_decomposition(self, original: "CycleDecomposition") -> "CycleDecomposition":
        """Private method for calls on cycle decomposition."""
        cycles = [self]
        for idx in original.domain:
            if idx not in self:
                cycles.append(Cycle(idx))
        cycle_decomposition = CycleDecomposition(*cycles)
        return cycle_decomposition * original

    def __eq__(self, other: Any) -> bool:
        """
        Check if the cycle is equal to another object.

        :param other: The object to compare with.
        :type other: Any

        :return: True if the cycle is equal to `other`, i.e., they define the same map. Otherwise, False.
        :rtype: bool
        """
        if isinstance(other, Cycle):
            lhs_length, rhs_length = len(self), len(other)
            if lhs_length != rhs_length:
                return False
            else:
                # in this case we have the identity on both side
                if lhs_length == 1:
                    return True
                return self.map == other.map
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

    def __mul__(self, other: "Cycle") -> "Cycle":
        raise NotImplementedError(
            "Multiplication between cycles is not supported. However, composition is supported. \n"
            "Try to call your cycle on the cycle you would like to compose."
        )

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
        """
        Returns an iterable containing the elements of the domain of the cycle.
        The domain of a cycle is the set of indices for which the cycle is defined.

        :return: The domain of the cycle.
        :rtype: Iterable[int]

        :example:
            >>> cycle = Cycle(1)
            >>> cycle.domain()
            range(1, 2)
            >>> cycle = Cycle(13)
            >>> cycle.domain()
            range(1, 14)
            >>> cycle = Cycle(3, 1, 2)
            >>> cycle.domain()
            range(1, 4)
            >>> cycle = Cycle(1, 3, 4, 5, 2, 6)
            >>> cycle.domain()
            range(1, 7)
        """
        return self._domain

    @property
    def map(self) -> Dict[int, int]:
        """
        Returns a dictionary representing the mapping of the cycle,
        where keys are indices and values are the corresponding elements after the permutation.

        :return: The mapping of the cycle.
        :rtype: Dict[int, int]

        :example:
            >>> cycle = Cycle(1)
            >>> cycle.map
            {1: 1}
            >>> cycle = Cycle(3)
            >>> cycle.map
            {1: 1, 2: 2, 3: 3}
            >>> cycle = Cycle(3, 1, 2)
            >>> cycle.map
            {1: 2, 2: 3, 3: 1}
        """
        return {element: self[(idx + 1) % len(self)] for idx, element in enumerate(self.elements)}

    @property
    def elements(self) -> Tuple[int]:
        """
        Returns a tuple containing the elements of the cycle.

        :return: The elements of the cycle.
        :rtype: Tuple[int]

        :example:
            >>> cycle = Cycle(3, 1, 2)
            >>> cycle.elements
            (1, 2, 3)
        """
        return self._cycle

    def cycle_decomposition(self) -> "CycleDecomposition":
        """
        This method converts the cycle into its cycle decomposition,
        representing it as a product of disjoint cycles.

        In the specific case of a cycle, it converts it from the class `Cycle` to the class `CycleDecomposition`.

        :return: The cycle decomposition of the permutation.
        :rtype: CycleDecomposition

        :example:
            >>> cycle = Cycle(1)
            >>> cycle.cycle_decomposition()
            CycleDecomposition(Cycle(1))
            >>> cycle = Cycle(3)
            >>> cycle.cycle_decomposition()
            CycleDecomposition(Cycle(1), Cycle(2), Cycle(3))
            >>> cycle = Cycle(3, 1, 2)
            >>> cycle.cycle_decomposition()
            CycleDecomposition(Cycle(1, 2, 3))
        """
        return CycleDecomposition(*([Cycle(idx) for idx in self.domain if idx not in self] + [self]))

    def cycle_notation(self) -> str:
        """
        Returns a string representing the cycle notation of the cycle.

        :return: The cycle notation of the cycle.
        :rtype: str

        :example:
            >>> Cycle(1).cycle_notation()
            '(1)'
            >>> Cycle(3, 1, 2).cycle_notation()
            '(1 3 2)'
            >>> Cycle(3, 1, 2, 4, 5, 6).cycle_notation()
            '(1 3 2 4 5 6)'
        """
        return str(self)

    def equivalent(self, other: Any) -> bool:
        if isinstance(other, Cycle):
            return self == other
        if isinstance(other, CycleDecomposition):
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
            return symmetria.elements.permutations.Permutation.from_cycle(cycle=self) == other
        return False

    def is_derangement(self) -> bool:
        r"""
        Check if the cycle is a derangement.

        Recall that a permutation :math:`\sigma` is called a derangement if it has no fixed points, i.e.,
        :math:`\sigma(x) \neq x` for every :math:`x` in the permutation domain.

        By definition, a cycle is a derangement if and only if it is the identity cycle.

        :return: True if the cycle is a derangement, False otherwise.
        :rtype: bool

        :example:
            >>> cycle = cycle(1)
            >>> cycle.is_derangement()
            True
            >>> cycle = cycle(13)
            >>> cycle.is_derangement()
            True
            >>> cycle = cycle(1, 2, 3)
            >>> cycle.is_derangement()
            False
        """
        return len(self) > 1

    def orbit(self, item: Any) -> List[Any]:
        raise NotImplementedError

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
        """
        Returns a set containing the indices in the domain of the cycle
        whose images are different from their respective indices, i.e., the set of :math:`n` in the cycle
        domain which are not mapped to itself.

        The support of a cycle is elementwise equal to the domain of the cycle if and only if the cycle is not
        the identity cycle. Otherwise, it is empty.

        :return: The support set of the cycle.
        :rtype: Set[int]

        :example:
            >>> cycle = Cycle(1)
            >>> cycle.support()
            set()
            >>> cycle = Cycle(13)
            >>> cycle.support()
            set()
            >>> cycle = Cycle(3, 1, 2)
            >>> cycle.support()
            {1, 2, 3}
            >>> cycle = Cycle(1, 3, 4, 5, 2, 6)
            >>> cycle.support()
            {2, 3, 4, 5}
        """
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

    def __getitem__(self, item: int) -> Cycle:
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

    def __iter__(self) -> Iterable[Cycle]:
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
            return symmetria.elements.permutations.Permutation.from_dict(
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


    def orbit(self, item: Any) -> List[Any]:
        raise NotImplementedError


if __name__ == '__main__':
    cycle = Cycle(3, 1, 2)
    from symmetria import Permutation
    print(cycle(-1), cycle("abc"), cycle([1, 2, 3]), cycle(Permutation(3, 1, 2)))
