from itertools import combinations
from math import lcm
from typing import Dict, List, Union, Tuple, Set, Iterable, Any

from symmetria.interfaces import _Element

__all__ = ["Permutation", "Cycle", "CycleDecomposition"]


class Permutation(_Element):
    __slots__ = ["_map", "_domain"]

    def __init__(self, *image: int) -> None:
        self._map: Dict[int, int] = self._validate_image(image)
        self._domain: Iterable[int] = range(1, len(self._map) + 1)

    @staticmethod
    def _validate_image(image: Tuple[int, ...]) -> Dict[int, int]:
        """
        Private method to check if a set of integers is eligible as image for a permutation.
        Recall that, a tuple of integers represent the image of a permutation if the following conditions hold:
            - all the integers are strictly positive;
            - all the integers are bounded by the total number of integer;
            - there are no integer repeated.
        """
        _map = {}
        for idx, img in enumerate(image):
            if isinstance(img, int) is False:
                raise ValueError(f"Expected `int` type, but got {type(img)}.")
            if img < 1:
                raise ValueError(f"Expected all strictly positive values, but got {img}")
            elif img > len(image):
                raise ValueError(f"The permutation is not injecting on its image. Indeed, {img} is not in the image.")
            elif img in _map.values():
                raise ValueError(
                    f"It seems that the permutation is not bijective. Indeed, {img} has two, or more, pre-images."
                )
            else:
                _map[idx + 1] = img
        return _map

    def __bool__(self) -> bool:
        return self != Permutation(*self.domain())

    def __call__(self, i: Union[int, Iterable]) -> Union[int, str, List, Tuple]:
        if isinstance(i, int):
            return self._call_on_integer(idx=i)

        elif isinstance(i, (str, List, Tuple)):
            assert len(self) <= len(i), f"Not enough object to permute {i} using the permutation {self}."
            permuted = self._call_on_iterable(original=i)
            if isinstance(i, str):
                return "".join(permuted)
            elif isinstance(i, Tuple):
                return tuple(p for p in permuted)
            return self._call_on_iterable(original=i)

        raise TypeError(f"Expected type `int` or `Iterable`, but got {type(i)}")

    def _call_on_integer(self, idx: int) -> int:
        """Private method for calls on integer."""
        return self[idx] if 1 <= idx <= len(self) else idx

    def _call_on_iterable(self, original: Iterable) -> List:
        """Private method for calls on iterable."""
        permuted = [None for _ in original]
        for idx, w in enumerate(original, 1):
            permuted[self._call_on_integer(idx=idx) - 1] = w
        return permuted

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Permutation):
            return self._map == other._map
        elif isinstance(other, Cycle):
            return self == Permutation.from_cycle(other)
        elif isinstance(other, CycleDecomposition):
            return self == Permutation.from_cycle_decomposition(other)
        return False

    def __getitem__(self, item: int) -> int:
        return self._map[item]

    def __int__(self) -> int:
        permutation_length = len(self)
        return sum([self[element] * 10 ** (permutation_length - element) for element in self.domain()])

    def __len__(self) -> int:
        return len(list(self.domain()))

    def __mul__(self, other: Union["Permutation", "Cycle", "CycleDecomposition"]) -> "Permutation":
        if isinstance(other, Permutation):
            if self.domain() != other.domain():
                raise ValueError(
                    f"Cannot compose permutation {self} with permutation {other},"
                    " because they don't live in the same Symmetric group."
                )
            return Permutation.from_dict(p={idx: self._map[other._map[idx]] for idx in self._domain})
        elif isinstance(other, Cycle):
            if set(other.domain()).issubset(set(self.domain())) is False:
                raise ValueError(
                    f"Cannot compose permutation {self} with cycle {other},"
                    " because they don't live in the same Symmetric group."
                )
            permutation = []
            for element in self.domain():
                if element in other:
                    idx = other.elements().index(element)
                    permutation.append(self[other[(idx + 1) % len(other)]])
                else:
                    permutation.append(self[element])
            return Permutation(*permutation)
        elif isinstance(other, CycleDecomposition):
            if self.domain() != other.domain():
                raise ValueError(
                    f"Cannot compose permutation {self} with cycle decomposition {other},"
                    " because they don't live in the same Symmetric group."
                )
            return Permutation.from_dict(p={idx: self._map[other.map()[idx]] for idx in self.domain()})
        raise TypeError(f"Product between types `Permutation` and {type(other)} is not implemented.")

    def __repr__(self) -> str:
        image = ", ".join([str(self._map[idx]) for idx in self.domain()])
        return f"Permutation({image})"

    def __str__(self) -> str:
        return "(" + ", ".join([str(self[idx]) for idx in self.domain()]) + ")"

    @staticmethod
    def from_dict(p: Dict[int, int]) -> "Permutation":
        return Permutation(*[p[idx] for idx in range(1, len(p) + 1)])

    @staticmethod
    def from_list(p: List[int]) -> "Permutation":
        return Permutation(*p)

    @staticmethod
    def from_tuple(p: Tuple[int, ...]) -> "Permutation":
        return Permutation(*p)

    @staticmethod
    def from_cycle(cycle: "Cycle") -> "Permutation":
        image = []
        cycle_length = len(cycle)
        for element in range(1, max(cycle.domain()) + 1):
            if element in cycle:
                idx = cycle.elements().index(element)
                image.append(cycle[(idx + 1) % cycle_length])
            else:
                image.append(element)
        return Permutation(*image)

    @staticmethod
    def from_cycle_decomposition(cycle_decomposition: "CycleDecomposition") -> "Permutation":
        return Permutation.from_dict(p=cycle_decomposition.map())

    def order(self) -> int:
        return self.cycle_decomposition().order()

    def orbit(self, item: Union[int, Iterable]) -> List[Union[int, Iterable]]:
        orbit = [item]
        next_element = self(item)
        while next_element != item:
            orbit.append(next_element)
            next_element = self(next_element)
        return orbit

    def cycle_decomposition(self) -> "CycleDecomposition":
        visited = set()
        cycles = []
        for idx in self.domain():
            if idx not in visited:
                orbit = self.orbit(idx)
                cycles.append(Cycle(*orbit))
                visited.update(orbit)
        return CycleDecomposition(*cycles)

    def is_derangement(self) -> bool:
        for idx in self._domain:
            if self(idx) == idx:
                return False
        return True

    def domain(self) -> Iterable[int]:
        return self._domain

    def support(self) -> Set[int]:
        return {idx for idx in self.domain() if self(idx) != idx}

    def one_line_notation(self) -> str:
        return str(int(self))

    def map(self) -> Dict[int, int]:
        return self._map


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

    def __call__(self, *args, **kwargs) -> int:
        # TODO: what is happening for lists?
        for arg in args:
            if arg in self._cycle:
                return self._cycle[(self._cycle.index(arg) + 1) % len(self)]
            else:
                return arg

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
        elif isinstance(other, Permutation):
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
        if isinstance(other, Permutation):
            if set(self.domain()).issubset(set(other.domain())) is False:
                raise ValueError(
                    f"Cannot compose permutation {self} with permutation {other},"
                    " because they don't live in the same Symmetric group."
                )
            return Permutation.from_dict(
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
            return (self * Permutation.from_cycle_decomposition(other)).cycle_decomposition()
        raise TypeError(f"Product between types `Cycle` and {type(other)} is not implemented.")

    def __repr__(self) -> str:
        return f"Cycle({', '.join(str(element) for element in self.elements())})"

    def __str__(self) -> str:
        return "(" + " ".join([str(element) for element in self.elements()]) + ")"

    def cycle_notation(self) -> str:
        # TODO: add description
        return str(self)

    def is_derangement(self) -> bool:
        # TODO: add description
        return len(self) > 1

    def domain(self) -> Iterable[int]:
        # TODO: add description
        return self._domain

    def elements(self) -> Tuple[int]:
        # TODO: add description
        return self._cycle

    def support(self) -> Set[int]:
        return set(self._cycle) if len(self) > 1 else set()

    def order(self) -> int:
        return len(self)

    def map(self) -> Dict[int, int]:
        return {element: self[(idx + 1) % len(self)] for idx, element in enumerate(self.elements())}


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
            for cycle in self:
                if cycle == other:
                    return True
            return False
        elif isinstance(other, Permutation):
            return Permutation.from_cycle_decomposition(self) == other
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
        cycles = self.cycle_notation()
        return f"CyclePermutation({cycles})"

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
            if len(cycle) == 1:
                support.add(cycle[0])
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


if __name__ == "__main__":
    a = Cycle(3, 2).map()
    b = CycleDecomposition(Cycle(1, 2), Cycle(4, 3)).map()
    c = CycleDecomposition(Cycle(4, 3), Cycle(1, 2))

    print(Permutation.from_cycle_decomposition(cycle_decomposition=c))
