from math import factorial
from typing import TYPE_CHECKING, Any, Set, Dict, List, Tuple, Union, Iterable
from collections import OrderedDict

import symmetria.elements.cycle
import symmetria.elements.cycle_decomposition
from symmetria.elements._base import _Element
from symmetria.elements._utils import _pretty_print_table
from symmetria.elements._validators import _validate_permutation

if TYPE_CHECKING:
    from symmetria.elements.cycle import Cycle
    from symmetria.elements.cycle_decomposition import CycleDecomposition

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
        >>> from symmetria import Permutation
        ...
        >>> permutation = Permutation(3, 1, 2)
        >>> permutation = Permutation(*[3, 1, 2])
        >>> permutation = Permutation(*(3, 1, 2))
    """

    __slots__ = ["_map", "_domain", "_image"]

    def __new__(cls, *image: int) -> "Permutation":
        _validate_permutation(image=image)
        return super().__new__(cls)

    def __init__(self, *image: int) -> None:
        self._map: Dict[int, int] = dict(enumerate(image, 1))
        self._domain: Iterable[int] = range(1, len(self._map) + 1)
        self._image: Tuple[int, ...] = tuple(image)

    def __bool__(self) -> bool:
        """Check if the permutation is different from the identity permutation.

        :return: True if the permutation is different from the identity, False otherwise.
        :rtype: bool

        :example:
            >>> from symmetria import Permutation
            ...
            >>> bool(Permutation(1))
            False
            >>> bool(Permutation(2, 1, 3))
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
            >>> from symmetria import Permutation
            ...
            >>> permutation = Permutation(3, 1, 2)
            >>> permutation(2)
            1
            >>> permutation("abc")
            'bca'
            >>> permutation([1, 2, 3])
            [2, 3, 1]
            >>> permutation(Permutation(3, 1, 2))
            Permutation(2, 3, 1)
        """
        if isinstance(item, int):
            return self._call_on_integer(idx=item)
        elif isinstance(item, (str, list, tuple)):
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
        elif isinstance(original, tuple):
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

        :example:
            >>> from symmetria import Permutation
            ...
            >>> Permutation(1, 2, 3) == Permutation(1, 2, 3)
            True
            >>> Permutation(1, 2, 3) == Permutation(3, 2, 1)
            False
            >>> Permutation(1, 2, 3) == 12
            False
        """
        if isinstance(other, Permutation):
            return self.map == other.map
        return False

    def __getitem__(self, item: int) -> int:
        """Return the value of the permutation at the given index `item`.

        In other words, it returns the image of the permutation at point `item`.

        .. note:: The index corresponds to the element in the domain of the permutation, i.e.,
            the index is a number between 1 and the length of the permutation.

        :param item: The index of the permutation.
        :type item: int

        :return: The value of the permutation at the specified index.
        :rtype: int

        :raises IndexError: If the index is out of range.

        :example:
            >>> from symmetria import Permutation
            ...
            >>> permutation = Permutation(2, 3, 1)
            >>> for idx in range(1, len(permutation)+1):
            ...     permutation[idx]
            2
            3
            1
        """
        return self.map[item]

    def __int__(self) -> int:
        """Convert the permutation to its integer representation.

        :return: The integer representation of the permutation.
        :rtype: int

        :example:
            >>> from symmetria import Permutation
            ...
            >>> int(Permutation(3, 1, 2))
            312
            >>> int(Permutation(1, 3, 4, 5, 2, 6))
            134526
        """
        return sum([self[element] * 10 ** (len(self) - element) for element in self.domain])

    def __len__(self) -> int:
        """Return the length of the permutation, which is the number of elements in its domain.

        :return: The length of the permutation.
        :rtype: int

        :example:
            >>> from symmetria import Permutation
            ...
            >>> len(Permutation(1))
            1
            >>> len(Permutation(3, 1, 2))
            3
            >>> len(Permutation(1, 3, 4, 5, 2, 6))
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
            >>> from symmetria import Permutation
            ...
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

    def __pow__(self, power: int) -> "Permutation":
        """Return the permutation object to the chosen power.

        :param power: the exponent for the power operation.
        :type power: int

        :return: the power of the permutation.
        :rtype: Permutation

        :raises TypeError: If `power` is not an integer.

        :example:
            >>> from symmetria import Permutation
            ...
            >>> Permutation(3, 1, 2)**0
            Permutation(1, 2, 3)
            >>> Permutation(3, 1, 2)**1
            Permutation(3, 1, 2)
            >>> Permutation(3, 1, 2)**-1
            Permutation(2, 3, 1)
            >>> Permutation(3, 1, 2)**2
            Permutation(2, 3, 1)
        """
        if isinstance(power, int) is False:
            raise TypeError(f"Power operation for type {type(power)} not supported.")
        elif self is False or power == 0:
            return Permutation(*list(self.domain))
        elif power == 1:
            return self
        elif power <= -1:
            return self.inverse() ** abs(power)
        else:
            return self * (self ** (power - 1))

    def __repr__(self) -> str:
        r"""Return a string representation of the permutation in the format `Permutation(x, y, z, ...)`,
        where :math:`x, y, z, ... \in \mathbb{N}` are the elements of the permutation.

        :return: A string representation of the permutation.
        :rtype: str

        :example:
            >>> from symmetria import Permutation
            ...
            >>> Permutation(3, 1, 2).__repr__()
            'Permutation(3, 1, 2)'
            >>> Permutation(1, 3, 4, 5, 2, 6).__repr__()
            'Permutation(1, 3, 4, 5, 2, 6)'
        """
        return f"Permutation({', '.join([str(self._map[idx]) for idx in self.domain])})"

    def __str__(self) -> str:
        """Return a string representation of the permutation in the form of a tuple.

        The string representation represents the image of the permutation.

        :return: A string representation of the permutation.
        :rtype: str

        :example:
            >>> from symmetria import Permutation
            ...
            >>> print(Permutation(3, 1, 2))
            (3, 1, 2)
            >>> print(Permutation(1, 3, 4, 5, 2, 6))
            (1, 3, 4, 5, 2, 6)
        """
        return str(self.image) if len(self.image) > 1 else f"({self.image[0]})"

    def ascents(self) -> List[int]:
        r"""Return the ascents of the permutation.

        Recall that an ascent of a permutation :math:`\sigma \in S_n`, where :math:`n \in \mathbb{N}`, is any position
        :math:`i<n` such that :math:`\sigma(i) < \sigma(i+1)`.

        :return: The ascents of the permutation.
        :rtype: List[int]

        :example:
            >>> from symmetria import Permutation
            ...
            >>> Permutation(1, 2, 3).ascents()
            [1, 2]
            >>> Permutation(3, 4, 5, 2, 1, 6, 7).ascents()
            [1, 2, 5, 6]
            >>> Permutation(4, 3, 2, 1).ascents()
            []
        """
        return [idx + 1 for idx in range(len(self) - 1) if self.image[idx] < self.image[idx + 1]]

    def cycle_decomposition(self) -> "CycleDecomposition":
        """Decompose the permutation into its cycle decomposition.

        :return: The cycle decomposition of the permutation.
        :rtype: CycleDecomposition

        :example:
            >>> from symmetria import Cycle, CycleDecomposition, Permutation
            ...
            >>> Permutation(1).cycle_decomposition()
            CycleDecomposition(Cycle(1))
            >>> Permutation(3, 1, 2).cycle_decomposition()
            CycleDecomposition(Cycle(1, 3, 2))
            >>> Permutation(1, 3, 4, 5, 2, 6).cycle_decomposition()
            CycleDecomposition(Cycle(1), Cycle(2, 3, 4, 5), Cycle(6))
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
            >>> from symmetria import Permutation
            ...
            >>> Permutation(1).cycle_notation()
            '(1)'
            >>> Permutation(3, 1, 2).cycle_notation()
            '(1 3 2)'
            >>> Permutation(3, 1, 2, 4, 5, 6).cycle_notation()
            '(1 3 2)(4)(5)(6)'
        """
        return self.cycle_decomposition().cycle_notation()

    def cycle_type(self) -> Tuple[int, ...]:
        r"""Return the cycle type of the permutation.

        Recall that the cycle type of the permutation :math:`\sigma` is a sequence of integer, where
        There is a 1 for every fixed point of :math:`\sigma`, a 2 for every transposition, and so on.

        .. note:: The resulting tuple is sorted in ascending order.

        :return: The cycle type of the permutation.
        :rtype: Tuple[int]

        :example:
            >>> from symmetria import Permutation
            ...
            >>> Permutation(1).cycle_type()
            (1,)
            >>> Permutation(3, 1, 2).cycle_type()
            (3,)
            >>> Permutation(3, 1, 2, 4, 5, 6).cycle_type()
            (1, 1, 1, 3)
            >>> Permutation(1, 4, 5, 7, 3, 2, 6).cycle_type()
            (1, 2, 4)
        """
        return tuple(sorted(len(cycle) for cycle in iter(self.cycle_decomposition())))

    def degree(self) -> int:
        """Return the degree of the permutation.

        Recall that the degree of a permutation is the number of elements on which it acts.

        :return: The degree of the permutation.
        :rtype: int

        :example:
            >>> from symmetria import Permutation
            ...
            >>> Permutation(1).degree()
            1
            >>> Permutation(1, 3, 2).degree()
            3
            >>> Permutation(1, 4, 3, 2).degree()
            4
        """
        return len(self)

    def descents(self) -> List[int]:
        r"""Return the descents of the permutation.

        Recall that a descent of a permutation :math:`\sigma \in S_n`, where :math:`n \in \mathbb{N}`, is any position
        :math:`i<n` such that :math:`\sigma(i) > \sigma(i+1)`.

        :return: The descents of the permutation.
        :rtype: List[int]

        :example:
            >>> from symmetria import Permutation
            ...
            >>> Permutation(1, 2, 3).descents()
            []
            >>> Permutation(3, 4, 5, 2, 1, 6, 7).descents()
            [3, 4]
            >>> Permutation(4, 3, 2, 1).descents()
            [1, 2, 3]
        """
        return [idx + 1 for idx in range(len(self) - 1) if self.image[idx] > self.image[idx + 1]]

    def describe(self) -> str:
        """Return a table describing the permutation.

        :return: A table describing the permutation.
        :rtype: str

        :example:
            >>> from symmetria import Permutation
            ...
            >>> p = Permutation(2, 4, 1, 3, 5).describe()
            >>> print(p)
            +----------------------------------------------------------------------+
            |                      Permutation(2, 4, 1, 3, 5)                      |
            +----------------------------------------------------------------------+
            | order                             |                4                 |
            +-----------------------------------+----------------------------------+
            | degree                            |                5                 |
            +-----------------------------------+----------------------------------+
            | is derangement                    |              False               |
            +-----------------------------------+----------------------------------+
            | inverse                           |         (3, 1, 4, 2, 5)          |
            +-----------------------------------+----------------------------------+
            | parity                            |             -1 (odd)             |
            +-----------------------------------+----------------------------------+
            | cycle notation                    |           (1 2 4 3)(5)           |
            +-----------------------------------+----------------------------------+
            | cycle type                        |              (1, 4)              |
            +-----------------------------------+----------------------------------+
            | inversions                        |     [(1, 3), (2, 3), (2, 4)]     |
            +-----------------------------------+----------------------------------+
            | ascents                           |            [1, 3, 4]             |
            +-----------------------------------+----------------------------------+
            | descents                          |               [2]                |
            +-----------------------------------+----------------------------------+
            | excedencees                       |              [1, 2]              |
            +-----------------------------------+----------------------------------+
            | records                           |            [1, 2, 5]             |
            +-----------------------------------+----------------------------------+
        """
        return _pretty_print_table(
            title=self.rep(),
            body=OrderedDict(
                {
                    "order": str(self.order()),
                    "degree": str(len(self)),
                    "is derangement": str(self.is_derangement()),
                    "inverse": str(self.inverse()),
                    "parity": "+1 (even)" if self.sgn() > 0 else "-1 (odd)",
                    "cycle notation": self.cycle_notation(),
                    "cycle type": str(self.cycle_type()),
                    "inversions": str(self.inversions()),
                    "ascents": str(self.ascents()),
                    "descents": str(self.descents()),
                    "excedencees": str(self.exceedances()),
                    "records": str(self.records()),
                }
            ),
        )

    @property
    def domain(self) -> Iterable[int]:
        """Return an iterable containing the elements of the domain of the permutation.

        The domain of a permutation is the set of indices for which the permutation is defined.

        :return: The domain of the permutation.
        :rtype: Iterable[int]

        :example:
            >>> from symmetria import Permutation
            ...
            >>> Permutation(1).domain
            range(1, 2)
            >>> Permutation(3, 1, 2).domain
            range(1, 4)
            >>> Permutation(1, 3, 4, 5, 2, 6).domain
            range(1, 7)
        """
        return self._domain

    def equivalent(self, other: Any) -> bool:
        """Check if the permutation is equivalent to another object.

        This method is introduced because we can have different representation of the same permutation, e.g., as a
        cycle, or as cycle decomposition.

        :param other: The object to compare with.
        :type other: Any

        :return: True if the permutation is equivalent to the other object, False otherwise.
        :rtype: bool

        :example:
            >>> from symmetria import Cycle, CycleDecomposition, Permutation
            ...
            >>> Permutation(1, 2, 3).equivalent(Permutation(1, 2, 3))
            True
            >>> Permutation(3, 1, 2).equivalent(Cycle(1, 3, 2))
            True
            >>> cycle_decomp = CycleDecomposition(Cycle(1, 2), Cycle(3, 4))
            >>> Permutation(2, 1, 4, 3).equivalent(cycle_decomp)
            True
        """
        if isinstance(other, Permutation):
            return self == other
        elif isinstance(other, symmetria.elements.cycle.Cycle):
            return self == Permutation.from_cycle(other)
        elif isinstance(other, symmetria.elements.cycle_decomposition.CycleDecomposition):
            return self == Permutation.from_cycle_decomposition(other)
        return False

    def exceedances(self, weakly: bool = False) -> List[int]:
        r"""Return the exceedances of the permutation.

        Recall that an exceedance of a permutation :math:`\sigma \in S_n`, where :math:`n \in \mathbb{N}`, is any
        position :math:`i \in \{ 1, ..., n\}` where :math:`\sigma(i) > i`. An exceedance is called weakly if
        :math:`\sigma(i) \geq i`.

        :param weakly: `True` to return the weakly exceedances of the permutation. Default `False`.
        :type weakly: bool

        :return: The exceedances of the permutation.
        :rtype: List[int]

        :example:
            >>> from symmetria import Permutation
            ...
            >>> Permutation(1, 2, 3).exceedances()
            []
            >>> Permutation(1, 2, 3).exceedances(weakly=True)
            [1, 2, 3]
            >>> Permutation(4, 3, 2, 1).exceedances()
            [1, 2]
            >>> Permutation(3, 4, 5, 2, 1, 6, 7).exceedances()
            [1, 2, 3]
            >>> Permutation(3, 4, 5, 2, 1, 6, 7).exceedances(weakly=True)
            [1, 2, 3, 6, 7]
        """
        if weakly:
            return [i for i, p in enumerate(self.image, 1) if p >= i]
        return [i for i, p in enumerate(self.image, 1) if p > i]

    @classmethod
    def from_cycle(cls, cycle: "Cycle") -> "Permutation":
        """Return a permutation from a cycle.

        In other word, it converts a cycle into a permutation.

        :param cycle: A cycle.
        :type cycle: Cycle

        :return: A permutation equivalent to the given cycle.
        :rtype: Permutation

        :example:
            >>> from symmetria import Cycle, Permutation
            ...
            >>> Permutation.from_cycle(Cycle(1))
            Permutation(1)
            >>> Permutation.from_cycle(Cycle(1, 2, 3))
            Permutation(2, 3, 1)
            >>> Permutation.from_cycle(Cycle(3))
            Permutation(1, 2, 3)
        """
        image = []
        cycle_length = len(cycle)
        for element in range(1, max(cycle.domain) + 1):
            if element in cycle:
                idx = cycle.elements.index(element)
                image.append(cycle[(idx + 1) % cycle_length])
            else:
                image.append(element)
        return cls(*image)

    @classmethod
    def from_cycle_decomposition(cls, cycle_decomposition: "CycleDecomposition") -> "Permutation":
        """Return a permutation from a cycle decomposition.

        In other word, it converts a cycle decomposition into a permutation.

        :param cycle_decomposition: A cycle decomposition.
        :type cycle_decomposition: CycleDecomposition

        :return: A permutation equivalent to the given cycle.
        :rtype: Permutation

        :example:
            >>> from symmetria import Cycle, CycleDecomposition, Permutation
            ...
            >>> Permutation.from_cycle_decomposition(CycleDecomposition(Cycle(1)))
            Permutation(1)
            >>> Permutation.from_cycle_decomposition(CycleDecomposition(Cycle(4, 3), Cycle(1, 2)))
            Permutation(2, 1, 4, 3)
        """
        return cls.from_dict(p=cycle_decomposition.map)

    @classmethod
    def from_dict(cls, p: Dict[int, int]) -> "Permutation":
        """Create a permutation object from a dictionary where keys represent indices and values represent the
        images of the indeces.

        :param p: A dictionary representing the permutation.
        :type p: Dict[int, int]

        :return: A permutation created from the dictionary.
        :rtype: Permutation

        :example:
            >>> from symmetria import Permutation
            ...
            >>> Permutation.from_dict({1: 3, 2: 1, 3: 2})
            Permutation(3, 1, 2)
            >>> Permutation.from_dict({1: 5, 2: 3, 3: 1, 4: 2, 5:4})
            Permutation(5, 3, 1, 2, 4)
        """
        return cls(*[p[idx] for idx in range(1, len(p) + 1)])

    @property
    def image(self) -> Tuple[int, ...]:
        r"""Return the image of the permutation.

        For example, consider the permutation :math:`\sigma \in S_3` given by :math:`\sigma(1)=3, \sigma(2)=1`, and
        :math:`\sigma (3)=2`, then the image of :math:`\sigma` is :math:`(3, 1, 2)` .

        :return: The image of the permutation.
        :rtype: Tuple[int]

        :example:
            >>> from symmetria import Permutation
            ...
            >>> Permutation(1, 2, 3).image
            (1, 2, 3)
            >>> Permutation(1, 3, 4, 2).image
            (1, 3, 4, 2)
            >>> Permutation(2, 3, 1, 5, 4).image
            (2, 3, 1, 5, 4)
        """
        return self._image

    def inverse(self) -> "Permutation":
        r"""Return the inverse of the permutation.

        Recall that the inverse of a permutation :math:`\sigma \in S_n`, for some :math:`n \in \mathbb{N}`, is the
        the only permutation :math:`\tau \in S_n` such that :math:`\sigma * \tau = \tau * \sigma = id`,
        where :math:`id` is the identity permutation.

        :return: The inverse of the permutation.
        :rtype: Permutation

        :example:
            >>> from symmetria import Permutation
            ...
            >>> Permutation(1, 2, 3).inverse()
            Permutation(1, 2, 3)
            >>> Permutation(1, 3, 4, 2).inverse()
            Permutation(1, 4, 2, 3)
            >>> Permutation(2, 3, 1, 5, 4).inverse()
            Permutation(3, 1, 2, 5, 4)
        """
        return Permutation.from_dict({item: key for key, item in self.map.items()})

    def inversions(self) -> List[Tuple[int, int]]:
        r"""Return the inversions of the permutation.

        Recall that an inversion of a permutation :math:`\sigma \in S_n`, for :math:`n \in \mathbb{N}`, is a pair
        :math:`(i, j)` of positions (indexes), where the entries of the permutation are in the opposite order, i.e.,
        :math:`i<j` but :math:`\sigma(i)>\sigma(j)`.

        :return: The inversions of the permutation
        :rtype: List[Tuple[int, int]]

        :example:
            >>> from symmetria import Permutation
            ...
            >>> Permutation(1, 2, 3).inversions()
            []
            >>> Permutation(1, 3, 4, 2).inversions()
            [(2, 4), (3, 4)]
            >>> Permutation(3, 1, 2, 5, 4).inversions()
            [(1, 2), (1, 3), (4, 5)]
        """
        inversions, image = [], list(self.image)
        min_element = 1
        for i, p in enumerate(image, 1):
            if p == min_element:
                min_element += 1
            else:
                for j, q in enumerate(image[i:], 1):
                    if p > q:
                        inversions.append((i, i + j))
        return inversions

    def is_conjugate(self, other: "Permutation") -> bool:
        r"""Check if two permutations are conjugated.

        Recall that two permutations :math:`\sigma, \quad \tau \in S_n`, for some :math:`n \in \mathbb{N}`, are said to
        be conjugated if there is :math:`\gamma \in S_n` such that :math:`\gamma\sigma\gamma^{-1} = \tau`.

        :param other: a permutation
        :type other: Permutation

        :return: True if self and other are conjugated, False otherwise.
        :rtype: bool

        :raises TypeError: If `other` is not a permutation.

        :example:
            >>> from symmetria import Permutation
            ...
            >>> Permutation(1, 2, 3).is_conjugate(Permutation(1, 2, 3))
            True
            >>> Permutation(1, 2, 3).is_conjugate(Permutation(3, 2, 1))
            False
            >>> Permutation(3, 2, 5, 4, 1).is_conjugate(Permutation(5, 2, 1, 4, 3))
            True
        """
        if isinstance(other, Permutation) is False:
            raise TypeError(f"Method `is_conjugate` not implemented for type {type}.")
        return self.cycle_type() == other.cycle_type()

    def is_derangement(self) -> bool:
        r"""Check if the permutation is a derangement.

        Recall that a permutation :math:`\sigma` is called a derangement if it has no fixed points, i.e.,
        :math:`\sigma(x) \neq x` for every :math:`x` in the permutation domain.

        :return: True if the permutation is a derangement, False otherwise.
        :rtype: bool

        :example:
            >>> from symmetria import Permutation
            ...
            >>> Permutation(1).is_derangement()
            False
            >>> Permutation(3, 1, 2).is_derangement()
            True
            >>> Permutation(1, 3, 4, 5, 2, 6).is_derangement()
            False
        """
        for idx in self.domain:
            if self(idx) == idx:
                return False
        return True

    def is_even(self) -> bool:
        """Check if the permutation is even.

        Recall that a permutation is said to be even if it can be expressed as the product of an even number of
        transpositions.

        :return: True if the permutation is even, False otherwise.
        :rtype: bool

        :example:
            >>> from symmetria import Permutation
            ...
            >>> Permutation(1).is_even()
            True
            >>> Permutation(2, 1).is_even()
            False
            >>> Permutation(2, 1, 3).is_even()
            False
            >>> Permutation(2, 3, 4, 5, 6, 1).is_even()
            False
        """
        return self.sgn() == 1

    def is_odd(self) -> bool:
        """Check if the permutation is odd.

        Recall that a permutation is said to be odd if it can be expressed as the product of an odd number of
        transpositions.

        :return: True if the permutation is odd, False otherwise.
        :rtype: bool

        :example:
            >>> from symmetria import Permutation
            ...
            >>> Permutation(1).is_odd()
            False
            >>> Permutation(2, 1).is_odd()
            True
            >>> Permutation(2, 1, 3).is_odd()
            True
            >>> Permutation(2, 3, 4, 5, 6, 1).is_odd()
            True
        """
        return self.sgn() == -1

    def is_regular(self) -> bool:
        """Check if the permutation is regular.

        Recall that a permutation is said regular if all cycles in its cycle decomposition have the same length.

        :return: True if the permutation is regular, False otherwise.
        :rtype: bool

        :example:
            >>> from symmetria import Permutation
            ...
            >>> Permutation(1, 2, 3).is_regular()
            True
            >>> Permutation(2, 1).is_regular()
            True
            >>> Permutation(2, 1, 3).is_regular()
            False
        """
        cycle_decomposition = self.cycle_decomposition()
        return all(len(cycle) == len(cycle_decomposition[0]) for cycle in iter(cycle_decomposition))

    def lehmer_code(self) -> List[int]:
        """Return the Lehmer code of the permutation.

        Recall that the Lehmer code of a permutation is a sequence that encodes the permutation as a series of integers.
        Each integer represents the number of smaller elements to the right of a given element in the permutation.

        :return: the Lehmer code of the permutation.
        :rtype: List[int]

        :example:
            >>> from symmetria import Permutation
            ...
            >>> Permutation(1).lehmer_code()
            [0]
            >>> Permutation(2, 1, 3).lehmer_code()
            [1, 0, 0]
            >>> Permutation(4, 3, 2, 1).lehmer_code()
            [3, 2, 1, 0]
            >>> Permutation(4, 1, 3, 2, 7, 6, 5, 8).lehmer_code()
            [3, 0, 1, 0, 2, 1, 0, 0]
        """
        n = len(self)
        lehmer_code = [0] * n
        stack: List[Tuple[int, int]] = []  # (value, count)

        for i in range(n, 0, -1):
            count = 0
            while stack and stack[-1][0] < self[i]:
                _, old_count = stack.pop()
                count += 1 + old_count
            lehmer_code[i - 1] = count
            stack.append((self[i], count))

        return lehmer_code

    def lexicographic_rank(self) -> int:
        """Return the lexicographic rank of the permutation.

        Recall that the lexicographic rank of a permutation refers to its position in the list of all
        permutations of the same degree sorted in lexicographic order.

        :return: the lexocographic rank of the permutation.
        :rtype: int

        :example:
            >>> from symmetria import Permutation
            ...
            >>> Permutation(1).lexicographic_rank()
            1
            >>> Permutation(1, 2, 3).lexicographic_rank()
            1
            >>> Permutation(1, 3, 2).lexicographic_rank()
            2
            >>> Permutation(3, 2, 1, 4).lexicographic_rank()
            15
        """
        n = self.__len__()
        rank = 1

        for i in range(n):
            right_smaller = 0
            for j in range(i + 1, n):
                if self[i + 1] > self[j + 1]:
                    right_smaller += 1
            rank += right_smaller * factorial(n - i - 1)

        return rank

    @property
    def map(self) -> Dict[int, int]:
        """Return a dictionary representing the mapping of the permutation.

        The keys of the dictionary are indices, while the values are the corresponding elements after permutation.

        :return: The mapping of the permutation.
        :rtype: Dict[int, int]

        :example:
            >>> from symmetria import Permutation
            ...
            >>> Permutation(1).map
            {1: 1}
            >>> Permutation(3, 1, 2).map
            {1: 3, 2: 1, 3: 2}
        """
        return self._map

    def one_line_notation(self) -> str:
        r"""Return a string representation of the permutation in the one-line notation, i.e., in the form
        :math:`\sigma(x_1)\sigma(x_2)...\sigma(x_n)`, where :math:`\sigma` is a permutation and :math:`x_1, ..., x_n`
        are the elements permuted by :math:`\sigma`.

        :return: The one-line notation of the permutation.
        :rtype: str

        :example:
            >>> from symmetria import Permutation
            ...
            >>> Permutation(1).one_line_notation()
            '1'
            >>> Permutation(3, 1, 2).one_line_notation()
            '312'
            >>> Permutation(1, 3, 4, 5, 2, 6).one_line_notation()
            '134526'
        """
        return str(int(self))

    def orbit(self, item: Any) -> List[Any]:
        r"""Compute the orbit of `item` object under the action of the cycle.

        Recall that the orbit of the action of a permutation :math:`\sigma` on an element x is given by the set

        .. math:: \{ \sigma^n(x): n \in \mathbb{N}\}

        :param item: The initial element or iterable to compute the orbit for.
        :type item: Any

        :return: The orbit of the specified element under the permutation.
        :rtype: List[Any]

        :example:
            >>> from symmetria import Cycle, CycleDecomposition, Permutation
            ...
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
            >>> from symmetria import Permutation
            ...
            >>> Permutation(1, 2, 3).order()
            1
            >>> Permutation(3, 1, 2).order()
            3
            >>> Permutation(1, 3, 4, 5, 2, 6).order()
            4
        """
        return self.cycle_decomposition().order()

    def records(self) -> List[int]:
        r"""Return the records of the permutation.

        Recall that a record of a permutation :math:`\sigma \in S_n`, where :math:`n \in \mathbb{N}`, is a position
        :math:`i \in \{1, ..., n\}` such that is either :math:`i=1` or :math:`\sigma(j) < \sigma(i)`
        for all :math:`j<i`.

        .. note:: There are definitions of records in the literature where the first index is not considered as a
            record.

        :return: The records of the permutation.
        :rtype: List[int]

        :example:
            >>> from symmetria import Permutation
            ...
            >>> Permutation(1, 2, 3).records()
            [1, 2, 3]
            >>> Permutation(3, 1, 2).records()
            [1]
            >>> Permutation(1, 3, 4, 5, 2, 6).records()
            [1, 2, 3, 4, 6]
        """
        records = [1]
        tmp_max = self[1]
        for i in self.domain:
            if self[i] > tmp_max:
                records.append(i)
                tmp_max = self[i]
        return records

    def sgn(self) -> int:
        r"""Return the sign of the permutation.

        Recall that the sign, signature, or signum of a permutation :math:`\sigma` is defined as +1 if :math:`\sigma`
        is even, i.e., :math:`\sigma` has an even number of inversions, and -1 if :math:`\sigma` is odd, i.e.,
        :math:`\sigma` has an odd number of inversions.

        :return: 1 if the permutation is even, -1 if the permutation is odd.
        :rtype: int

        :example:
            >>> from symmetria import Permutation
            ...
            >>> Permutation(1).sgn()
            1
            >>> Permutation(2, 1).sgn()
            -1
            >>> Permutation(2, 3, 4, 5, 6, 1).sgn()
            -1
        """
        return -1 if len(self.inversions()) % 2 else 1

    def support(self) -> Set[int]:
        r"""Return a set containing the indices in the domain of the permutation whose images are different from their
        respective indices, i.e., the set of :math:`n` in the permutation domain which are not mapped to itself.

        :return: The support set of the permutation.
        :rtype: Set[int]

        :example:
            >>> from symmetria import Permutation
            ...
            >>> Permutation(1).support()
            set()
            >>> Permutation(3, 1, 2).support()
            {1, 2, 3}
            >>> Permutation(1, 3, 4, 5, 2, 6).support()
            {2, 3, 4, 5}
        """
        return {idx for idx in self.domain if self(idx) != idx}
