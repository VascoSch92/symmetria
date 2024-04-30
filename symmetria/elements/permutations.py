from typing import Dict, List, Union, Tuple, Set, Iterable, Any

from symmetria.interfaces import _Element
import symmetria.elements.cycles

__all__ = ["Permutation"]


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

    def __call__(self, i: Union[int, Iterable]) -> Union[int, Iterable]:
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
        elif isinstance(other, symmetria.elements.cycles.Cycle):
            return self == Permutation.from_cycle(other)
        elif isinstance(other, symmetria.elements.cycles.CycleDecomposition):
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
        elif isinstance(other, symmetria.elements.cycles.Cycle):
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
        elif isinstance(other, symmetria.elements.cycles.CycleDecomposition):
            if self.domain() != other.domain():
                raise ValueError(
                    f"Cannot compose permutation {self} with cycle decomposition {other},"
                    " because they don't live in the same Symmetric group."
                )
            return Permutation.from_dict(p={idx: self._map[other.map()[idx]] for idx in self.domain()})
        raise TypeError(f"Product between types `Permutation` and {type(other)} is not implemented.")

    def __repr__(self) -> str:
        return f"Permutation({', '.join([str(self._map[idx]) for idx in self.domain()])})"

    def __str__(self) -> str:
        return "(" + ", ".join([str(self[idx]) for idx in self.domain()]) + ")"

    @classmethod
    def from_dict(cls, p: Dict[int, int]) -> "Permutation":
        return Permutation(*[p[idx] for idx in range(1, len(p) + 1)])

    @classmethod
    def from_list(cls, p: List[int]) -> "Permutation":
        return Permutation(*p)

    @classmethod
    def from_tuple(cls, p: Tuple[int, ...]) -> "Permutation":
        return Permutation(*p)

    @classmethod
    def from_cycle(cls, cycle: "Cycle") -> "Permutation":
        image = []
        cycle_length = len(cycle)
        for element in range(1, max(cycle.domain()) + 1):
            if element in cycle:
                idx = cycle.elements().index(element)
                image.append(cycle[(idx + 1) % cycle_length])
            else:
                image.append(element)
        return Permutation(*image)

    @classmethod
    def from_cycle_decomposition(cls, cycle_decomposition: "CycleDecomposition") -> "Permutation":
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
                cycles.append(symmetria.elements.cycles.Cycle(*orbit))
                visited.update(orbit)
        return symmetria.elements.cycles.CycleDecomposition(*cycles)

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


