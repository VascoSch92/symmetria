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
        return len(self.elements()) != 1

    def __call__(self, i: Union[int, Iterable]) -> Union[int, Iterable]:
        if isinstance(i, int):
            return self._call_on_integer(idx=i)
        elif isinstance(i, (str, List, Tuple)):
            assert max(self.elements()) <= len(i), f"Not enough object to permute {i} using the cycle {self}."
            permuted = self._call_on_iterable(original=i)
            if isinstance(i, str):
                return "".join(permuted)
            elif isinstance(i, Tuple):
                return tuple(p for p in permuted)
            return self._call_on_iterable(original=i)
        raise TypeError(f"Expected type `int` or `Iterable`, but got {type(i)}")

    def _call_on_integer(self, idx: int) -> int:
        """Private method for calls on integer."""
        if idx in self.elements():
            return self[(self.elements().index(idx) + 1) % len(self)]
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
                lhs_elements, rhs_elements = self.elements(), other.elements()
                for idx, element in enumerate(lhs_elements):
                    if element not in rhs_elements:
                        return False
                    if self[(idx + 1) % lhs_length] != other[(rhs_elements.index(element) + 1) % rhs_length]:
                        return False
                return True
        elif isinstance(other, CycleDecomposition):
            # case where both are the identity
            if bool(self) is False and bool(other) is False:
                return max(self.elements()) == max([max(cycle.elements()) for cycle in other])
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
        return self._cycle[item]

    def __int__(self) -> int:
        cycle_length = len(self)
        return sum([element * 10 ** (cycle_length - idx) for idx, element in enumerate(self.elements(), 1)])

    def __len__(self) -> int:
        return len(self._cycle)

    def __mul__(
            self,
            other: Union["Cycle", "CycleDecomposition", "Permutation"],
    ) -> Union["Cycle", "CycleDecomposition", "Permutation"]:
        if isinstance(other, Cycle):
            # case where the two cycles are disjoint
            if set(self.elements()).isdisjoint(set(other.elements())):
                single_cycle = []
                _range = set(self.elements()).union(set(other.elements()))
                for idx in range(1, max(_range) + 1):
                    if idx not in _range:
                        single_cycle.append(Cycle(idx))
                return CycleDecomposition(self, *[other, *single_cycle])
            elif self.domain() == other.domain():
                cycle = []
                for idx in self.domain():
                    _other = other[(idx+1) % len(other)]
                    cycle.append(self[(self.elements().index(_other) + 1) % len(self)])
                return Cycle(*cycle)
            else:
                return CycleDecomposition(self) * CycleDecomposition(other)
        if isinstance(other, symmetria.elements.permutations.Permutation):
            if set(self.domain()).issubset(set(other.domain())) is False:
                raise ValueError(
                    f"Cannot compose permutation {self} with permutation {other},"
                    " because they don't live in the same Symmetric group."
                )
            return symmetria.elements.permutations.Permutation.from_dict(
                p={
                    idx: self.map()[other[idx]] if other[idx] in self.map() else other[idx]
                    for idx in other.domain()
                }
            )
        elif isinstance(other, CycleDecomposition):
            if set(self.domain()).issubset(set(other.domain())) is False:
                raise ValueError(
                    f"Cannot compose permutation {self} with cycle decomposition {other},"
                    " because they don't live in the same symmetric group."
                )
            return (self * symmetria.elements.permutations.Permutation.from_cycle_decomposition(other)).cycle_decomposition()
        raise TypeError(f"Product between types `Cycle` and {type(other)} is not implemented.")

    def __repr__(self) -> str:
        return f"Cycle({', '.join(str(element) for element in self.elements())})"

    def __str__(self) -> str:
        return "(" + " ".join([str(element) for element in self.elements()]) + ")"

    def cycle_notation(self) -> str:
        # TODO: add description
        return str(self)

    def domain(self) -> Iterable[int]:
        # TODO: add description
        return self._domain

    def elements(self) -> Tuple[int]:
        # TODO: add description
        return self._cycle

    def is_derangement(self) -> bool:
        # TODO: add description
        return len(self) > 1

    def map(self) -> Dict[int, int]:
        return {element: self[(idx + 1) % len(self)] for idx, element in enumerate(self.elements())}

    def order(self) -> int:
        return len(self)

    def support(self) -> Set[int]:
        return set(self._cycle) if len(self) > 1 else set()


class CycleDecomposition(_Element):
    __slots__ = ["_cycles"]

    def __init__(self, *cycles: Cycle) -> None:
        self._cycles: Tuple[Cycle, ...] = self._validate_and_standardize(cycles=cycles)
        self._domain: Iterable[int] = range(1, max(max(cycle.elements()) for cycle in self._cycles) + 1)

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
            if set(cycle_a.elements()) & set(cycle_b.elements()):
                raise ValueError(f"The cycles {cycle_a} and {cycle_b} don't have disjoint support.")

        # checks that every element is included in a cycle
        elements = {element for cycle in cycles for element in cycle.elements()}
        if set(range(1, len(elements) + 1)) != elements:
            raise ValueError(
                "Every element from 1 to the biggest permuted element must be included in some cycle,\n "
                f"but this is not the case for the element(s): {set(range(1, len(elements) + 1)).difference(elements)}")

        # standardization
        cycles = sorted(cycles, key=lambda cycle: cycle[0])
        return tuple(cycles)

    def __bool__(self) -> bool:
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

    def cycle_notation(self) -> str:
        return str(self)

    def order(self) -> int:
        # TODO: add description
        return lcm(*[len(cycle) for cycle in self])

    def domain(self) -> Iterable[int]:
        return self._domain

    def support(self) -> Set[int]:
        support = set()
        for cycle in self:
            if len(cycle) != 1:
                support.update(cycle.elements())
        return support

    def is_derangement(self) -> bool:
        for cycle in self:
            if len(cycle) == 1:
                return False
        return True

    def map(self) -> Dict[int, int]:
        _map = {}
        for cycle in self:
            _map.update(cycle.map())
        return _map
