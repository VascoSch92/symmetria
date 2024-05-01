from typing import Dict, List, Union, Tuple, Set, Iterable, Any

from symmetria.interfaces import _Element
import symmetria.elements.cycles

__all__ = ["Permutation"]


class Permutation(_Element):
    """
    BLa bla per la classe
    :todo: write that we can also do with list and tuple and give examples
    """
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
        """
        Check if the permutation is different from the identity permutation.

        :return: True if the permutation is different from the identity, False otherwise.
        :rtype: bool

        :example:
            >>> permutation = Permutation(1)
            >>> bool(permutation)
            False
            >>> permutation = Permutation(2, 1, 3)
            >>> bool(permutation)
            True
        """
        return self != Permutation(*self.domain)

    def __call__(self, item: Union[int, Iterable, "Permutation"]) -> Union[int, Iterable, "Permutation"]:
        """
        Call the permutation on the `item` object, i.e., mimic a permutation action on a set.

        - If `item` is an integer, it applies the permutation to the integer.
        - If `item` is an iterable, e.g., a ``str``, ``list`` or ``tuple``, it applies the permutation permuting
            the values using the indeces.
        - If `item` is a permutation, it returns the multiplication of the two permutations.

        :param item: The object on which the permutation acts.
        :type item: Union[int, Iterable, Permutation]

        :return: The permuted object.
        :rtype: Union[int, Iterable, Permutation]

        :raises AssertionError: If the length of the permutation is greater than the length of `item`, i.e.,
            the permutation cannot permute the `item`.
        :raises TypeError: If `item` is not an integer, an iterable or a permutation.

        :example:
            >>> permutation = Permutation(3, 1, 2)
            >>> permutation(2)
            1
            >>> permutation("abc")
            "cab"
            >>> permutation([1, 2, 3])
            [3, 1, 2]
            >>> permutation(Permutation(3, 1, 2))
            [3, 1, 2]
        """
        if isinstance(item, int):
            return self._call_on_integer(idx=item)
        elif isinstance(item, (str, List, Tuple)):
            assert len(self) <= len(item), f"Not enough object to permute {item} using the permutation {self}."
            permuted = self._call_on_iterable(original=item)
            if isinstance(item, str):
                return "".join(permuted)
            elif isinstance(item, Tuple):
                return tuple(p for p in permuted)
            return self._call_on_iterable(original=item)
        elif isinstance(item, Permutation):
            return self * item
        raise TypeError(f"Expected type `int`, `Iterable` or `Permutation`, but got {type(item)}")

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
        """
        Check if the permutation object is equal to another object.

        - If `other` is a ``Permutation``, it checks whether the permutation maps are equal.
        - If `other` is a ``Cycle``, it converts it to a ``Permutation`` and checks for equality.
        - If `other` is a ``CycleDecomposition``, it converts it to a ``Permutation`` and checks for equality.
        - If `other` is not of any above type, it returns False.

        :param other: The object to compare with.
        :type other: Any

        :return: True if the ``Permutation`` is equal to `other`, False otherwise.
        :rtype: bool
        """
        if isinstance(other, Permutation):
            return self.map == other.map
        elif isinstance(other, symmetria.elements.cycles.Cycle):
            return self == Permutation.from_cycle(other)
        elif isinstance(other, symmetria.elements.cycles.CycleDecomposition):
            return self == Permutation.from_cycle_decomposition(other)
        return False

    def __getitem__(self, item: int) -> int:
        """
        Returns the value of the permutation at the given index `item`.
        The index corresponds to the position in the permutation, starting from 0

        :param item: The index of the permutation.
        :type item: int

        :return: The value of the permutation at the specified index.
        :rtype: int

        :raises IndexError: If the index is out of range.
        """
        return self.map[item]

    def __int__(self) -> int:
        """
        Convert the permutation to its integer representation.

        :return: The integer representation of the permutation.
        :rtype: int

        :example:
            >>> permutation = Permutation(3, 1, 2)
            >>> int(permutation)
            312
            >>> permutation = Permutation(1, 3, 4, 5, 2, 6)
            >>> int(permutation)
            134526
        """
        return sum([self[element] * 10 ** (len(self) - element) for element in self.domain])

    def __len__(self) -> int:
        """
        Returns the length of the permutation, which is the number of elements in its domain.

        :return: The length of the permutation.
        :rtype: int

        :example:
            >>> permutation = Permutation(3, 1, 2)
            >>> len(permutation)
            3
            >>> permutation = Permutation(1, 3, 4, 5, 2, 6)
            >>> len(permutation)
            6
        """
        return len(list(self.domain))

    def __mul__(self, other: Union["Permutation", "Cycle", "CycleDecomposition"]) -> "Permutation":
        if isinstance(other, Permutation):
            if self.domain != other.domain:
                raise ValueError(
                    f"Cannot compose permutation {self} with permutation {other},"
                    " because they don't live in the same Symmetric group."
                )
            return Permutation.from_dict(p={idx: self._map[other._map[idx]] for idx in self.domain})
        elif isinstance(other, symmetria.elements.cycles.Cycle):
            if set(other.domain).issubset(set(self.domain)) is False:
                raise ValueError(
                    f"Cannot compose permutation {self} with cycle {other},"
                    " because they don't live in the same Symmetric group."
                )
            permutation = []
            for element in self.domain:
                if element in other:
                    idx = other.elements.index(element)
                    permutation.append(self[other[(idx + 1) % len(other)]])
                else:
                    permutation.append(self[element])
            return Permutation(*permutation)
        elif isinstance(other, symmetria.elements.cycles.CycleDecomposition):
            if self.domain != other.domain:
                raise ValueError(
                    f"Cannot compose permutation {self} with cycle decomposition {other},"
                    " because they don't live in the same Symmetric group."
                )
            return Permutation.from_dict(p={idx: self._map[other.map[idx]] for idx in self.domain})
        raise TypeError(f"Product between types `Permutation` and {type(other)} is not implemented.")

    def __repr__(self) -> str:
        r"""
        Returns a string representation of the permutation in the format "Permutation(x, y, z, ...)",
        where :math:`x, y, z, ... \in \mathbb{N}` are the elements of the permutation.

        :return: A string representation of the permutation.
        :rtype: str

        :example:
            >>> permutation = Permutation(3, 1, 2)
            >>> permutation.__repr__()
            Permutation(3, 1, 2)
            >>> permutation = Permutation(1, 3, 4, 5, 2, 6)
            >>> permutation.__repr__()
            Permutation(1, 3, 4, 5, 2, 6)
        """
        return f"Permutation({', '.join([str(self._map[idx]) for idx in self.domain])})"

    def __str__(self) -> str:
        """
        Returns a string representation of the permutation in the form of tuples.

        :return: A string representation of the permutation.
        :rtype: str

        :example:
            >>> permutation = Permutation(3, 1, 2)
            >>> print(permutation)
            (3, 1, 2)
            >>> permutation = Permutation(1, 3, 4, 5, 2, 6)
            >>> print(permutation)
            (1, 3, 4, 5, 2, 6)
        """
        return "(" + ", ".join([str(self[idx]) for idx in self.domain]) + ")"

    @classmethod
    def from_dict(cls, p: Dict[int, int]) -> "Permutation":
        """
        Creates a permutation object from a dictionary where keys represent indices and values represent the
        images of the indeces.

        :param p: A dictionary representing the permutation.
        :type p: Dict[int, int]

        :return: A permutation created from the dictionary.
        :rtype: Permutation

        :example:
            >>> permutation = Permutation.from_dict({1: 3, 2: 1, 3:, 2})
            >>> print(permutation) # Permutation(2, 1, 2)
            (3, 1, 2)
        """
        return Permutation(*[p[idx] for idx in range(1, len(p) + 1)])

    @classmethod
    def from_cycle(cls, cycle: "Cycle") -> "Permutation":
        """
        Return a permutation from a cycle. In other word, it converts a cycle into a permutation.

        :param cycle: A cycle.
        :type cycle: Cycle

        :return: A permutation equivalent to the given cycle.
        :rtype: Permutation

        :example:
            >>> permutation = Permutation.from_cycle(Cycle(1))
            >>> print(permutation) # Permutation(1)
            (1)
            >>> permutation = Permutation.from_cycle(Cycle(1, 2, 3)) # Permutation(2, 3, 1)
            >>> print(permutation) # Permutation(2, 3, 1)
            (2, 3, 1)
            >>> permutation = Permutation.from_cycle(Cycle(3)) # Permutation(1, 2, 3)
            >>> print(permutation) # Permutation(1, 2, 3)
            (1, 2, 3)
        """
        image = []
        cycle_length = len(cycle)
        for element in range(1, max(cycle.domain) + 1):
            if element in cycle:
                idx = cycle.elements.index(element)
                image.append(cycle[(idx + 1) % cycle_length])
            else:
                image.append(element)
        return Permutation(*image)

    @classmethod
    def from_cycle_decomposition(cls, cycle_decomposition: "CycleDecomposition") -> "Permutation":
        return Permutation.from_dict(p=cycle_decomposition.map)

    @property
    def domain(self) -> Iterable[int]:
        """
        Returns an iterable containing the elements of the domain of the permutation.
        The domain of a permutation is the set of indices for which the permutation is defined.

        :return: The domain of the permutation.
        :rtype: Iterable[int]

        :example:
            >>> permutation = Permutation(1)
            >>> permutation.domain()
            range(1, 2)
            >>> permutation = Permutation(3, 1, 2)
            >>> permutation.domain()
            range(1, 4)
            >>> permutation = Permutation(1, 3, 4, 5, 2, 6)
            >>> permutation.domain()
            range(1, 7)
        """
        return self._domain

    @property
    def map(self) -> Dict[int, int]:
        """
        Returns a dictionary representing the mapping of the permutation,
        where keys are indices and values are the corresponding elements after permutation.

        :return: The mapping of the permutation.
        :rtype: Dict[int, int]

        :example:
            >>> permutation = Permutation(1)
            >>> permutation.map()
            {1: 1}
            >>> permutation = Permutation(3, 1, 2)
            >>> permutation.map()
            {1: 3, 2: 1, 3: 3}
        """
        return self._map

    def order(self) -> int:
        r"""
        Return the order of the permutation.

        Recall that the order of a permutation :math:`\sigma` is the smallest positive integer :math:`n \in \mathbb{N}`
        such that :math:`\sigma^n = id`, where :math:`id` is the identity permutation.

        :return: The order of the permutation.
        :rtype: int

        :example:
            >>> permutation = Permutation(3, 1, 2)
            >>> permutation.order()
            1
            >>> permutation = Permutation(3, 1, 2)
            >>> permutation.order()
            3
            >>> permutation = Permutation(1, 3, 4, 5, 2, 6)
            >>> permutation.order()
            4
        """
        return self.cycle_decomposition().order()

    def orbit(self, item: Union[int, Iterable, "Permutation"]) -> List[Union[int, Iterable, "Permutation"]]:
        """
        Calculates the orbit of the specified element under the permutation,
        which is the set of all elements obtained by repeatedly applying the permutation
        to the initial element until it returns to itself.

        :param item: The initial element or iterable to compute the orbit for.
        :type item: Union[int, Iterable, "Permutation"]

        :return: The orbit of the specified element under the permutation.
        :rtype: List[Union[int, Iterable, "Permutation"]]

        :example:
            >>> permutation = Permutation(3, 1, 2)
            >>> permutation.orbit(1)
            [1, 3, 2]
            >>> permutation.orbit([1, 2, 3])
            [[1, 2, 3], [2, 3, 1], [3, 1, 2]]
            >>> permutation.orbit("abc")
            ['abc', 'bca', 'cab']
            >>> permutation.orbit(Permutation(3, 1, 2))
            [Permutation(3, 1, 2), Permutation(2, 3, 1), Permutation(1, 2, 3)]
        """
        orbit = [item]
        next_element = self(item)
        while next_element != item:
            orbit.append(next_element)
            next_element = self(next_element)
        return orbit

    def cycle_decomposition(self) -> "CycleDecomposition":
        """
        Decomposes the permutation into its cycle decomposition.

        :return: The cycle decomposition of the permutation.
        :rtype: CycleDecomposition

        :example:
            >>> permutation = Permutation(1)
            >>> permutation.cycle_decomposition()
            (1)
            >>> permutation = Permutation(3, 1, 2)
            >>> permutation.cycle_decomposition()
            (1 3 2)
            >>> permutation = Permutation(1, 3, 4, 5, 2, 6)
            >>> permutation.cycle_decomposition()
            (1)(2 3 4 5)(6)
        """
        cycles, visited = [], set()
        for idx in self.domain:
            if idx not in visited:
                orbit = self.orbit(idx)
                cycles.append(symmetria.elements.cycles.Cycle(*orbit))
                visited.update(orbit)
        return symmetria.elements.cycles.CycleDecomposition(*cycles)

    def is_derangement(self) -> bool:
        r"""
        Check if the permutation is a derangement.

        Recall that a permutation :math:`\sigma` is called a derangement if it has no fixed points, i.e.,
        :math:`\sigma(x) \neq x` for every :math:`x` in the permutation domain.

        :return: True if the permutation is a derangement, False otherwise.
        :rtype: bool

        :example:
            >>> permutation = Permutation(1)
            >>> permutation.is_derangement()
            False
            >>> permutation = Permutation(3, 1, 2)
            >>> permutation.is_derangement()
            True
            >>> permutation = Permutation(1, 3, 4, 5, 2, 6)
            >>> permutation.is_derangement()
            False
        """
        for idx in self.domain:
            if self(idx) == idx:
                return False
        return True

    def support(self) -> Set[int]:
        """
        Returns a set containing the indices in the domain of the permutation
        whose images are different from their respective indices, i.e., the set of :math:`n` in the permutation
        domain which are not mapped to itself.

        :return: The support set of the permutation.
        :rtype: Set[int]

        :example:
            >>> permutation = Permutation(1)
            >>> permutation.support()
            set()
            >>> permutation = Permutation(3, 1, 2)
            >>> permutation.support()
            {1, 2, 3}
            >>> permutation = Permutation(1, 3, 4, 5, 2, 6)
            >>> permutation.support()
            {2, 3, 4, 5}
        """
        return {idx for idx in self.domain if self(idx) != idx}

    def one_line_notation(self) -> str:
        """
        Returns a string representation of the permutation in the one-line notation,

        :return: The one-line notation of the permutation.
        :rtype: str

        :example:
            >>> permutation = Permutation(1)
            >>> permutation.one_line_notation()
            '1'
            >>> permutation = Permutation(3, 1, 2)
            >>> permutation.one_line_notation()
            '123'
            >>> permutation = Permutation(1, 3, 4, 5, 2, 6)
            >>> permutation.one_line_notation()
            '134524'
        """
        return str(int(self))


if __name__ == '__main__':
    a = Permutation(1)
    b = Permutation(3, 1, 2)
    c = Permutation(1, 3, 4, 5, 2, 6)
    print(b.orbit(1), b.orbit([1, 2, 3]), b.orbit("abc"), b.orbit(b))
