from typing import Any, Set, Dict, List, Tuple, Union, Iterable

import symmetria.elements.cycle
import symmetria.elements.cycle_decomposition
from symmetria._interfaces import _Element

__all__ = ["Permutation"]


class Permutation(_Element):
    r"""The ``Permutation`` class represents an element of the symmetric group as a map, i.e., a bijective function
    from a finite set of integer :math:`\{1, ..., n\}`, for some :math:`n \in \mathbb{N}_{>0}`, to itself.

    To define a permutation, it is needed to provide a sequence of integers defining the image of the permutation.

    For example, to define the permutation :math:`\sigma \in S_3` given by :math:`\sigma(1)=3, \sigma(2)=1`, and
    :math:`\sigma (3)=2`, you should write ``Permutation(3, 1, 2)``.

    :param image: Set of integers defining the image of the permutation.
    :type image: int

    :raises ValueError: If there is an integer in the provided image which is not strictly positive.
    :raises ValueError: If there is an integer which is strictly greater than the total number of integers.
    :raises ValueError: If there are repeated integers.

    :example:
        >>> permutation = Permutation(3, 1, 2)
        >>> permutation = Permutation(*[3, 1, 2])
        >>> permutation = Permutation(*(3, 1, 2))
    """

    __slots__ = ["_map", "_domain"]

    def __init__(self, *image: int) -> None:
        self._map: Dict[int, int] = self._validate_image(image)
        self._domain: Iterable[int] = range(1, len(self._map) + 1)

    @staticmethod
    def _validate_image(image: Tuple[int, ...]) -> Dict[int, int]:
        """Private method to check if a set of integers is eligible as image for a permutation.

        Recall that, a tuple of integers represent the image of a permutation if the following conditions hold:
            - all the integers are strictly positive;
            - all the integers are bounded by the total number of integers;
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
        """Check if the permutation is different from the identity permutation.

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

    def __call__(self, item: Any) -> Any:
        """Call the permutation on the `item` object, i.e., mimic a permutation action on the element `item`.

        - If `item` is an integer, it applies the permutation to the integer.
        - If `item` is a string, a list or a tuple, it applies the permutation permuting the values using the indeces.
        - If `item` is a permutation, it returns the multiplication of the two permutations, i.e., the compositions.
        - If `item` is a cycle or a cycle decomposition, it returns the composition in cycle decomposition.

        :param item: The object on which the permutation acts.
        :type item: Any

        :return: The permuted object.
        :rtype: Any

        :raises AssertionError: If the length of the permutation is greater than the length of `item`, i.e.,
            the permutation cannot permute the `item`.
        :raises ValueError: If the permutation and the object `item` don't belong to the same Symmetric group.
        :raises TypeError: If the `item` is not of a supported type. See list above for supported types.

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
            if len(self) > len(item):
                raise ValueError(f"Not enough object to permute {item} using the permutation {self}.")
            return self._call_on_str_list_tuple(original=item)
        elif isinstance(item, Permutation):
            return self * item
        elif isinstance(item, symmetria.elements.cycle.Cycle):
            if set(item.domain).issubset(set(self.domain)) is False:
                raise ValueError(
                    f"Cannot compose permutation {self} with cycle {item},"
                    " because they don't live in the same Symmetric group."
                )
            return self._call_on_cycle(cycle=item)
        elif isinstance(item, symmetria.elements.cycle_decomposition.CycleDecomposition):
            if self.domain != item.domain:
                raise ValueError(
                    f"Cannot compose permutation {self} with cycle decomposition {item},"
                    " because they don't live in the same Symmetric group."
                )
            return self._call_on_cycle_decomposition(item)
        raise TypeError(f"Calling a permutation on {type(item)} is not supported.")

    def _call_on_integer(self, idx: int) -> int:
        """Private method for calls on integer."""
        return self[idx] if 1 <= idx <= len(self) else idx

    def _call_on_str_list_tuple(self, original: Union[str, Tuple, List]) -> Union[str, Tuple, List]:
        """Private method for calls on strings, tuples and lists."""
        permuted = list(_ for _ in original)
        for idx, w in enumerate(original, 1):
            permuted[self._call_on_integer(idx=idx) - 1] = w
        if isinstance(original, str):
            return "".join(permuted)
        elif isinstance(original, Tuple):
            return tuple(p for p in permuted)
        else:
            return permuted

    def _call_on_cycle(self, cycle: "Cycle") -> "CycleDecomposition":
        """Private method for calls on cycles."""
        permutation = []
        for element in self.domain:
            if element in cycle:
                idx = cycle.elements.index(element)
                permutation.append(self[cycle[(idx + 1) % len(cycle)]])
            else:
                permutation.append(self[element])
        return Permutation(*permutation).cycle_decomposition()

    def _call_on_cycle_decomposition(self, cycle_decomposition: "CycleDecomposition") -> "CycleDecomposition":
        """Private method for calls on cycle decomposition."""
        return Permutation.from_dict(
            p={idx: self._map[cycle_decomposition.map[idx]] for idx in self.domain}
        ).cycle_decomposition()

    def __eq__(self, other: Any) -> bool:
        """Check if the permutation is equal to `another` object.

        :param other: The object to compare with.
        :type other: Any

        :return: True if the permutation is equal to `other`, i.e., they define the same map. Otherwise, False.
        :rtype: bool
        """
        if isinstance(other, Permutation):
            return self.map == other.map
        return False

    def __getitem__(self, item: int) -> int:
        """Return the value of the permutation at the given index `item`.

        In other words, it returns the image of the permutation at point `item`.
        The index corresponds to the position in the permutation, starting from 0.

        :param item: The index of the permutation.
        :type item: int

        :return: The value of the permutation at the specified index.
        :rtype: int

        :raises IndexError: If the index is out of range.
        """
        return self.map[item]

    def __int__(self) -> int:
        """Convert the permutation to its integer representation.

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
        """Return the length of the permutation, which is the number of elements in its domain.

        :return: The length of the permutation.
        :rtype: int

        :example:
            >>> permutation = Permutation(1)
            >>> len(permutation)
            1
            >>> permutation = Permutation(3, 1, 2)
            >>> len(permutation)
            3
            >>> permutation = Permutation(1, 3, 4, 5, 2, 6)
            >>> len(permutation)
            6
        """
        return len(list(self.domain))

    def __mul__(self, other: "Permutation") -> "Permutation":
        """Multiply the permutation with another permutation, resulting in a new permutation
        that represents the composition of the two permutations.

        :param other: The other permutation to multiply with.
        :type other: Permutation

        :return: The composition of the two permutations.
        :rtype: Permutation

        :raises ValueError: If the permutations don't live in the same Symmetric group.
        :raises TypeError: If the other object is not a Permutation.

        :example:
            >>> Permutation(1, 2, 3) * Permutation(3, 2, 1)
            Permutation(3, 2, 1)
            >>> Permutation(1) * Permutation(1)
            Permutation(1)
            >>> Permutation(3, 4, 5, 1, 2) * Permutation(3, 5, 1, 2, 4)
            Permutation(5, 2, 3, 4, 1)
        """
        if isinstance(other, Permutation):
            if self.domain != other.domain:
                raise ValueError(
                    f"Cannot compose permutation {self} with permutation {other},"
                    " because they don't live in the same Symmetric group."
                )
            return Permutation.from_dict(p={idx: self._map[other._map[idx]] for idx in self.domain})
        raise TypeError(f"Product between types `Permutation` and {type(other)} is not implemented.")

    def __repr__(self) -> str:
        r"""Return a string representation of the permutation in the format "Permutation(x, y, z, ...)",
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
        """Return a string representation of the permutation in the form of tuples.

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
        """Create a permutation object from a dictionary where keys represent indices and values represent the
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
        """Return a permutation from a cycle.

        In other word, it converts a cycle into a permutation.

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
        """Return a permutation from a cycle decomposition.

        In other word, it converts a cycle decomposition into a permutation.

        :param cycle_decomposition: A cycle decomposition.
        :type cycle_decomposition: CycleDecomposition

        :return: A permutation equivalent to the given cycle.
        :rtype: Permutation

        :example:
            >>> cd = CycleDecomposition(Cycle(1))
            >>> Permutation.from_cycle_decomposition(cd)
            (1)
            >>> cd = CycleDecomposition(Cycle(4, 3), Cycle(1, 2)))
            >>> Permutation.from_cycle_decomposition(cd)
            (2, 1, 4, 3)
        """
        return Permutation.from_dict(p=cycle_decomposition.map)

    @property
    def domain(self) -> Iterable[int]:
        """Return an iterable containing the elements of the domain of the permutation.

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
        """Return a dictionary representing the mapping of the permutation.

        The keys of the dictionary are indices, while the values are the corresponding elements after permutation.

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

    def equivalent(self, other: Any) -> bool:
        """Check if the permutation is equivalent to another object.

        This method is introduced because we can have different representation of the same permutation, e.g., as a
        cycle, or as cycle decomposition.

        :param other: The object to compare with.
        :type other: Any

        :return: True if the permutation is equivalent to the other object, False otherwise.
        :rtype: bool

        :example:
            >>> permutation_a = Permutation(1, 2, 3)
            >>> permutation_b = Permutation(1, 2, 3)
            >>> permutation_a.equivalent(permutation_b)
            True
            >>> permutation = Permutation(3, 1, 2)
            >>> cycle = Cycle(1, 3, 2)
            >>> cycle.equivalent(cycle)
            True
            >>> permutation = Permutation(2, 1, 4, 3)
            >>> cycle_decomposition = CycleDecomposition(Cycle(1, 2), Cycle(3, 4))
            >>> permutation.equivalent(cycle_decomposition)
            True
        """
        if isinstance(other, Permutation):
            return self == other
        elif isinstance(other, symmetria.elements.cycle.Cycle):
            return self == Permutation.from_cycle(other)
        elif isinstance(other, symmetria.elements.cycle_decomposition.CycleDecomposition):
            return self == Permutation.from_cycle_decomposition(other)
        return False

    def orbit(self, item: Any) -> List[Any]:
        r"""Compute the orbit of `item` object under the action of the cycle.

        Recall that the orbit of the action of a permutation :math:`\sigma` on an element x is given by the set
        :math:`\{ \sigma^n(x): n \in \mathbb{N}\}`.

        :param item: The initial element or iterable to compute the orbit for.
        :type item: Any

        :return: The orbit of the specified element under the permutation.
        :rtype: List[Any]

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
            >>> permutation.orbit(Cycle(1, 2, 3))
            [
                CycleDecomposition(Cycle(1, 2, 3)),
                CycleDecomposition(Cycle(1), Cycle(2), Cycle(3)),
                CycleDecomposition(Cycle(1, 3, 2)),
            ]
        """
        if isinstance(item, symmetria.elements.cycle.Cycle):
            item = item.cycle_decomposition()
        orbit = [item]
        next_element = self(item)
        while next_element != item:
            orbit.append(next_element)
            next_element = self(next_element)
        return orbit

    def order(self) -> int:
        r"""Return the order of the permutation.

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

    def cycle_decomposition(self) -> "CycleDecomposition":
        """Decompose the permutation into its cycle decomposition.

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
                cycles.append(symmetria.elements.cycle.Cycle(*orbit))
                visited.update(orbit)
        return symmetria.elements.cycle_decomposition.CycleDecomposition(*cycles)

    def cycle_notation(self) -> str:
        """Return a string representing the cycle notation of the permutation.

        :return: The cycle notation of the permutation.
        :rtype: str

        :example:
            >>> Permutation(1).cycle_notation()
            '(1)'
            >>> Permutation(3, 1, 2).cycle_notation()
            '(1 3 2)'
            >>> Permutation(3, 1, 2, 4, 5, 6).cycle_notation()
            '(1 3 2)(4)(5)(6)'
        """
        return self.cycle_decomposition().cycle_notation()

    def is_derangement(self) -> bool:
        r"""Check if the permutation is a derangement.

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
        """Return a set containing the indices in the domain of the permutation whose images are different from their
        respective indices, i.e., the set of :math:`n` in the permutation domain which are not mapped to itself.

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
        r"""Return a string representation of the permutation in the one-line notation, i.e., in the form
        :math:`\sigma(x_1)\sigma(x_2)...\sigma(x_n)`, where :math:`\sigma` is a permutation and :math:`x_1, ..., x_n`
        are the elements permuted by :math:`\sigma`.

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
