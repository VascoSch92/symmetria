from math import lcm, prod
from typing import TYPE_CHECKING, Any, Set, Dict, List, Tuple, Union, Iterable
from collections import OrderedDict

import symmetria.elements.cycle
import symmetria.elements.permutation
from symmetria.elements._base import _Element
from symmetria.elements._utils import _pretty_print_table
from symmetria.elements._validators import _validate_cycle_decomposition

if TYPE_CHECKING:
    from symmetria.elements.cycle import Cycle
    from symmetria.elements.permutation import Permutation

__all__ = ["CycleDecomposition"]


class CycleDecomposition(_Element):
    r"""The ``CycleDecomposition`` class represents the cycle decomposition of a permutation of the symmetric group.

    Recall that every permutation of the symmetric group can be represented uniquely as the composition of a finite
    number of cycles thanks to the `Cycle Decomposition Theorem for Permutations`.

    To define a permutation as a cycle decomposition, you need to provide its cycles.

    For example, to define the permutation given by the cycles: ``Cycle(2, 1)`` and ``Cycle(4, 3)``, you should write
    ``CycleDecomposition(Cycle(2, 1), Cycle(4, 3))``.

    .. note::
        By convention, a cycle decomposition starts always with the
        smaller cycle, i.e., the cycle with the smallest element, and is increasing.

        This is because a cycle decomposition can have different representations. Don't panic, you can write the
        cycle decomposition in the way you like the most, but then it will be stored following the above convention.

    :param cycle: Cycle factors of the permutation.
    :type cycle: Cycle

    :raises ValueError: If there are two or more cycles with non-disjoint support.
    :raises ValueError: If there are missing cycles in the decomposition.

    :example:
        >>> from symmetria import Cycle, CycleDecomposition
        ...
        >>> cycle = CycleDecomposition(Cycle(2, 1), Cycle(4, 3))
        >>> cycle = CycleDecomposition(*[Cycle(2, 1), Cycle(4, 3)])
        >>> cycle = CycleDecomposition(*(Cycle(2, 1), Cycle(4, 3)))
    """

    __slots__ = ["_cycles", "_domain"]

    def __new__(cls, *cycles: "Cycle") -> "CycleDecomposition":
        _validate_cycle_decomposition(cycles=cycles)
        return super().__new__(cls)

    def __init__(self, *cycles: "Cycle") -> None:
        self._cycles: Tuple["Cycle", ...] = self._standardization(cycles=cycles)
        self._domain: Iterable[int] = range(
            1,
            max(max(cycle.elements) for cycle in self._cycles) + 1,
        )

    @staticmethod
    def _standardization(cycles: Tuple["Cycle", ...]) -> Tuple["Cycle", ...]:
        """Private method to standardize a tuple of cycles to become a cycle decomposition.

        A cycle decomposition is standardized if the cycles are ordered by increasingly the first element of each cycle.
        """
        return tuple(sorted(cycles, key=lambda cycle: cycle[0]))

    def __bool__(self) -> bool:
        r"""Check if the cycle decomposition is non-empty, i.e., it is different from the identity
        cycle decomposition.

        :return: True if the cycle decomposition is different from the identity cycle decomposition, False otherwise.
        :rtype: bool

        :example:
            >>> from symmetria import Cycle, CycleDecomposition
            ...
            >>> bool(CycleDecomposition(Cycle(1)))
            False
            >>> bool(CycleDecomposition(Cycle(1), Cycle(2)))
            False
            >>> bool(CycleDecomposition(Cycle(2, 1, 3)))
            True

        :note: Every cycle of the form ``CycleDecomposition(Cycle(n))`` is considered empty for every
            :math:`n \in \mathbb{N}`, i.e., ``bool(CycleDecomposition(Cycle(n))) = False``. Same for cycle decomposition
            of identity cycle, e.g., ``CycleDecomposition(Cycle(1), Cycle(2), Cycle(3)).``
        """
        return any(bool(cycle) for cycle in iter(self))

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
        elif isinstance(item, (str, list, tuple)):
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
        elif isinstance(original, tuple):
            return tuple(p for p in permuted)
        else:
            return permuted

    def _call_on_permutation(self, original: "Permutation") -> "Permutation":
        return symmetria.elements.permutation.Permutation.from_cycle_decomposition(self) * original

    def __eq__(self, other: Any) -> bool:
        """Check if the cycle decomposition is equal to the `other` object.

        :param other: The object to compare with.
        :type other: Any

        :return: True if the cycle decomposition is equal to `other`, i.e., they define the same map. Otherwise, False.
        :rtype: bool

        :example:
            >>> from symmetria import Cycle, CycleDecomposition
            ...
            >>> CycleDecomposition(Cycle(1, 2)) == CycleDecomposition(Cycle(1, 2))
            True
            >>> CycleDecomposition(Cycle(1), Cycle(2)) == CycleDecomposition(Cycle(1), Cycle(2))
            True
            >>> CycleDecomposition(Cycle(1), Cycle(2, 3)) == CycleDecomposition(Cycle(1))
            False
        """
        if isinstance(other, CycleDecomposition):
            if len(self) != len(other):
                return False
            for cycle_a, cycle_b in zip(iter(self), iter(other)):
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
            >>> from symmetria import Cycle, CycleDecomposition
            ...
            >>> CycleDecomposition(Cycle(1, 2), Cycle(3, 4))[0]
            Cycle(1, 2)
        """
        return self._cycles[idx]

    def __iter__(self) -> Iterable["Cycle"]:
        """Return an iterator over the cycles in the cycle decomposition.

        :return: An iterator over the cycles in the cycle decomposition.
        :rtype: Iterable[Cycle]

        :example:
            >>> from symmetria import Cycle, CycleDecomposition
            ...
            >>> for cycle in CycleDecomposition(Cycle(1, 2), Cycle(3, 4)):
            ...     print(cycle)
            (1 2)
            (3 4)
        """
        return iter(self._cycles)

    def __len__(self) -> int:
        """Return the length of the cycle decomposition, which is the number of cycles present in the decomposition.

        :return: The length of the cycle decomposition.
        :rtype: int

        :example:
            >>> from symmetria import Cycle, CycleDecomposition
            ...
            >>> len(CycleDecomposition(Cycle(1)))
            1
            >>> len(CycleDecomposition(Cycle(1, 3), Cycle(2)))
            2
            >>> len(CycleDecomposition(Cycle(1, 3), Cycle(4, 5), Cycle(2, 6)))
            3
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

    def __pow__(self, power: int) -> "CycleDecomposition":
        """Return the permutation object to the chosen power.

        :param power: the exponent for the power operation.
        :type power: int

        :return: the power of the cycle decomposition.
        :rtype: Permutation

        :raises TypeError: If `power` is not an integer.

        :example:
            >>> from symmetria import Cycle, CycleDecomposition
            ...
            >>> CycleDecomposition(Cycle(3), Cycle(1), Cycle(2)) ** 0
            CycleDecomposition(Cycle(1), Cycle(2), Cycle(3))
            >>> CycleDecomposition(Cycle(1, 2), Cycle(3)) ** 1
            CycleDecomposition(Cycle(1, 2), Cycle(3))
            >>> CycleDecomposition(Cycle(1, 2), Cycle(3)) ** -1
            CycleDecomposition(Cycle(1, 2), Cycle(3))
            >>> CycleDecomposition(Cycle(1, 3), Cycle(2, 4))**2
            CycleDecomposition(Cycle(1), Cycle(2), Cycle(3), Cycle(4))
        """
        if isinstance(power, int) is False:
            raise TypeError(f"Power operation for type {type(power)} not supported.")
        elif self is False or power == 0:
            return CycleDecomposition(*[symmetria.elements.cycle.Cycle(i) for i in self.domain])
        elif power == 1:
            return self
        elif power <= -1:
            return self.inverse() ** abs(power)
        else:
            return self * (self ** (power - 1))

    def __repr__(self) -> str:
        r"""Return a string representation of the cycle decomposition.

         The string representation is in the following format:

        .. math:: 'CycleDecomposition(Cycle(x, ...), Cycle(y, ...), ...)',

        where :math:`x, y, ... \in \mathbb{N}` are the elements of the cycles.

        :return: A string representation of the cycle decomposition.
        :rtype: str

        :example:
            >>> from symmetria import Cycle, CycleDecomposition
            ...
            >>> CycleDecomposition(Cycle(1)).__repr__()
            'CycleDecomposition(Cycle(1))'
            >>> CycleDecomposition(Cycle(1, 3), Cycle(2)).__repr__()
            'CycleDecomposition(Cycle(1, 3), Cycle(2))'
            >>> CycleDecomposition(Cycle(1, 3), Cycle(4, 5, 2, 6)).__repr__()
            'CycleDecomposition(Cycle(1, 3), Cycle(2, 6, 4, 5))'
        """
        return f"CycleDecomposition({', '.join([cycle.__repr__() for cycle in iter(self)])})"

    def __str__(self) -> str:
        """Return a string representation of the cycle decomposition in the cycle notation.

        :return: A string representation of the cycle decomposition.
        :rtype: str

        :example:
            >>> from symmetria import Cycle, CycleDecomposition
            ...
            >>> str(CycleDecomposition(Cycle(1)))
            '(1)'
            >>> str(CycleDecomposition(Cycle(1, 3), Cycle(2)))
            '(1 3)(2)'
            >>> str(CycleDecomposition(Cycle(1, 3), Cycle(4, 5, 2, 6)))
            '(1 3)(2 6 4 5)'
        """
        return "".join([str(c) for c in iter(self)])

    def ascents(self) -> List[int]:
        r"""Return the ascents of the cycle decomposition.

        Recall that an ascent of a permutation :math:`\sigma \in S_n`, where :math:`n \in \mathbb{N}`, is any position
        :math:`i<n` such that :math:`\sigma(i) < \sigma(i+1)`.

        :return: The ascents of the cycle decomposition.
        :rtype: List[int]

        :example:
            >>> from symmetria import Cycle, CycleDecomposition
            ...
            >>> CycleDecomposition(Cycle(1, 2, 3)).ascents()
            [1]
            >>> CycleDecomposition(Cycle(1), Cycle(2), Cycle(3)).ascents()
            [1, 2]
            >>> CycleDecomposition(Cycle(2, 3), Cycle(4, 5, 1)).ascents()
            [3]
        """
        permutation = symmetria.Permutation.from_cycle_decomposition(self)
        return permutation.ascents()

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
            >>> from symmetria import Cycle, CycleDecomposition
            ...
            >>> CycleDecomposition(Cycle(1)).cycle_notation()
            '(1)'
            >>> CycleDecomposition(Cycle(1, 3, 2)).cycle_notation()
            '(1 3 2)'
            >>> CycleDecomposition(Cycle(1, 3, 2), Cycle(4)).cycle_notation()
            '(1 3 2)(4)'
        """
        return str(self)

    def cycle_type(self) -> Tuple[int, ...]:
        r"""Return the cycle type of the cycle decomposition.

        Recall that the cycle type of the permutation :math:`\sigma` is a sequence of integer, where
        There is a 1 for every fixed point of :math:`\sigma`, a 2 for every transposition, and so on.

        .. note:: Note that the resulting tuple is sorted in ascending order.

        :return: The cycle type of the cycle decomposition.
        :rtype: Tuple[int]

        :example:
            >>> from symmetria import Cycle, CycleDecomposition
            ...
            >>> CycleDecomposition(Cycle(1)).cycle_type()
            (1,)
            >>> CycleDecomposition(Cycle(3, 1, 2)).cycle_type()
            (3,)
            >>> CycleDecomposition(Cycle(1, 3, 2), Cycle(4)).cycle_type()
            (1, 3)
            >>> CycleDecomposition(Cycle(1, 2), Cycle(3, 4)).cycle_type()
            (2, 2)
        """
        return tuple(sorted(len(cycle) for cycle in iter(self)))

    def degree(self) -> int:
        """Return the degree of the cycle decomposition.

        Recall that the degree of a cycle decomposition is the number of elements on which it acts.

        :return: The degree of the cycle decomposition.
        :rtype: int

        :example:
            >>> from symmetria import Cycle, CycleDecomposition
            ...
            >>> CycleDecomposition(Cycle(1)).degree()
            1
            >>> CycleDecomposition(Cycle(1), Cycle(3, 2)).degree()
            3
            >>> CycleDecomposition(Cycle(1, 4), Cycle(3, 2)).degree()
            4
        """
        return max(max(cycle.elements) for cycle in self._cycles)

    def descents(self) -> List[int]:
        r"""Return the descents of the cycle decomposition.

        Recall that a descent of a permutation :math:`\sigma \in S_n`, where :math:`n \in \mathbb{N}`, is any position
        :math:`i<n` such that :math:`\sigma(i) > \sigma(i+1)`.

        :return: The descents of the cycle decomposition.
        :rtype: List[int]

        :example:
            >>> from symmetria import Cycle, CycleDecomposition
            ...
            >>> CycleDecomposition(Cycle(1, 2, 3)).descents()
            [2]
            >>> CycleDecomposition(Cycle(1), Cycle(2), Cycle(3)).descents()
            []
            >>> CycleDecomposition(Cycle(2, 3), Cycle(4, 5, 1)).descents()
            [1, 2, 4]
        """
        permutation = symmetria.Permutation.from_cycle_decomposition(self)
        return permutation.descents()

    def describe(self) -> str:
        """Return a table describing the cycle decomposition.

        :return: A table describing the cycle decomposition.
        :rtype: str

        :example:
            >>> from symmetria import Cycle, CycleDecomposition
            ...
            >>> cycle_decomposition = CycleDecomposition(Cycle(1, 3), Cycle(2)).describe()
            >>> print(cycle_decomposition)
            +--------------------------------------------------------------------------------------+
            |                      CycleDecomposition(Cycle(1, 3), Cycle(2))                       |
            +--------------------------------------------------------------------------------------+
            | order                                     |                    2                     |
            +-------------------------------------------+------------------------------------------+
            | degree                                    |                    2                     |
            +-------------------------------------------+------------------------------------------+
            | is derangement                            |                  False                   |
            +-------------------------------------------+------------------------------------------+
            | inverse                                   |                 (1 3)(2)                 |
            +-------------------------------------------+------------------------------------------+
            | parity                                    |                 -1 (odd)                 |
            +-------------------------------------------+------------------------------------------+
            | cycle notation                            |                 (1 3)(2)                 |
            +-------------------------------------------+------------------------------------------+
            | cycle type                                |                  (1, 2)                  |
            +-------------------------------------------+------------------------------------------+
            | inversions                                |         [(1, 2), (1, 3), (2, 3)]         |
            +-------------------------------------------+------------------------------------------+
            | ascents                                   |                    []                    |
            +-------------------------------------------+------------------------------------------+
            | descents                                  |                  [1, 2]                  |
            +-------------------------------------------+------------------------------------------+
            | excedencees                               |                   [1]                    |
            +-------------------------------------------+------------------------------------------+
            | records                                   |                   [1]                    |
            +-------------------------------------------+------------------------------------------+
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
        """Return an iterable containing the elements of the domain of the cycle decomposition.

        The domain of a cycle decomposition is the set of indices for which the cycle decomposition is defined.

        :return: The domain of the cycle decomposition.
        :rtype: Iterable[int]

        :example:
            >>> from symmetria import Cycle, CycleDecomposition
            ...
            >>> CycleDecomposition(Cycle(1)).domain
            range(1, 2)
            >>> CycleDecomposition(Cycle(3, 1, 2)).domain
            range(1, 4)
            >>> CycleDecomposition(Cycle(1), Cycle(3, 4, 5, 2, 6)).domain
            range(1, 7)
        """
        return self._domain

    def equivalent(self, other: Any) -> bool:
        """Check if the cycle decomposition is equivalent to another object.

        This method is introduced because we can have different representation of the same cycle decomposition, e.g.,
        as a cycle, or as permutation.

        :param other: The object to compare with.
        :type other: Any

        :return: True if the cycle decomposition is equivalent to the other object, False otherwise.
        :rtype: bool

        :example:
            >>> from symmetria import Cycle, CycleDecomposition, Permutation
            ...
            >>> cycle_decomposition = CycleDecomposition(Cycle(1, 2, 3))
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
                for cycle in iter(self):
                    if len(cycle) > 1 and cycle != other:
                        return False
            return True
        elif isinstance(other, symmetria.elements.permutation.Permutation):
            return symmetria.elements.permutation.Permutation.from_cycle_decomposition(self) == other
        return False

    def exceedances(self, weakly: bool = False) -> List[int]:
        r"""Return the exceedances of the cycle decomposition.

        Recall that an exceedance of a permutation :math:`\sigma \in S_n`, where :math:`n \in \mathbb{N}`, is any
        position :math:`i \in \{ 1, ..., n\}` where :math:`\sigma(i) > i`. An exceedance is called weakly if
        :math:`\sigma(i) \geq i`.

        :param weakly: `True` to return the weakly exceedances of the cycle decomposition. Default `False`.
        :type weakly: bool

        :return: The exceedances of the cycle decomposition.
        :rtype: List[int]

        :example:
            >>> from symmetria import Cycle, CycleDecomposition
            ...
            >>> CycleDecomposition(Cycle(1, 2), Cycle(3)).exceedances()
            [1]
            >>> CycleDecomposition(Cycle(1, 2), Cycle(3)).exceedances(weakly=True)
            [1, 3]
            >>> CycleDecomposition(Cycle(2, 3), Cycle(4, 5, 1)).exceedances()
            [1, 2, 4]
            >>> CycleDecomposition(Cycle(1), Cycle(2), Cycle(3)).exceedances()
            []
            >>> CycleDecomposition(Cycle(1), Cycle(2), Cycle(3)).exceedances(weakly=True)
            [1, 2, 3]
        """
        return symmetria.Permutation.from_cycle_decomposition(self).exceedances(weakly=weakly)

    def inverse(self) -> "CycleDecomposition":
        r"""Return the inverse of the cycle decomposition.

        Recall that the inverse of a permutation :math:`\sigma \in S_n`, for some :math:`n \in \mathbb{N}`, is the
        the only permutation :math:`\tau \in S_n` such that :math:`\sigma * \tau = \tau * \sigma = id`,
        where :math:`id` is the identity permutation.

        :return: The inverse of the cycle decomposition.
        :rtype: CycleDecomposition

        :example:
            >>> from symmetria import Cycle, CycleDecomposition
            ...
            >>> CycleDecomposition(Cycle(1, 2, 3)).inverse()
            CycleDecomposition(Cycle(1, 3, 2))
            >>> CycleDecomposition(Cycle(1, 2), Cycle(3, 4)).inverse()
            CycleDecomposition(Cycle(1, 2), Cycle(3, 4))
        """
        return CycleDecomposition(*[cycle.inverse() for cycle in iter(self)])

    def inversions(self) -> List[Tuple[int, int]]:
        r"""Return the inversions of the cycle decomposition.

        Recall that an inversion of a permutation :math:`\sigma \in S_n`, for :math:`n \in \mathbb{N}`, is a pair
        :math:`(i, j)` of positions (indexes), where the entries of the permutation are in the opposite order, i.e.,
        :math:`i<j` but :math:`\sigma(i)>\sigma(j)`.

        :return: The inversions of the ycle decomposition.
        :rtype: List[Tuple[int, int]]

        :example:
            >>> from symmetria import Cycle, CycleDecomposition
            ...
            >>> CycleDecomposition(Cycle(1), Cycle(2), Cycle(3)).inversions()
            []
            >>> CycleDecomposition(Cycle(1, 2, 3)).inversions()
            [(1, 3), (2, 3)]
        """
        return symmetria.elements.permutation.Permutation.from_cycle_decomposition(self).inversions()

    def is_conjugate(self, other: "CycleDecomposition") -> bool:
        r"""Check if two cycle decompositions are conjugated.

        Recall that two permutations :math:`\sigma, \quad \tau \in S_n`, for some :math:`n \in \mathbb{N}`, are said to
        be conjugated if there is :math:`\gamma \in S_n` such that :math:`\gamma\sigma\gamma^{-1} = \tau`.

        :param other: a cycle decomposition
        :type other: CycleDecomposition

        :return: True if self and other are conjugated, False otherwise.
        :rtype: bool

        :example:
            >>> from symmetria import Cycle, CycleDecomposition
            ...
            >>> cycle_dec = CycleDecomposition(Cycle(1, 2, 3))
            >>> cycle_dec.is_conjugate(cycle_dec)
            True
            >>> cycle_dec_a = CycleDecomposition(Cycle(1, 3, 2, 5, 4))
            >>> cycle_dec_b = CycleDecomposition(Cycle(1, 4, 3, 5, 2))
            >>> cycle_dec_a.is_conjugate(cycle_dec_b)
            True
            >>> cycle_dec_a = CycleDecomposition(Cycle(1, 2), Cycle(3, 4))
            >>> cycle_dec_b = CycleDecomposition(Cycle(1), Cycle(3, 2, 4))
            >>> cycle_dec_a.is_conjugate(cycle_dec_b)
            False
        """
        if isinstance(other, CycleDecomposition) is False:
            raise TypeError(f"Method `is_conjugate` not implemented for type {type}.")
        return self.cycle_type() == other.cycle_type()

    def is_derangement(self) -> bool:
        r"""Check if the cycle decomposition is a derangement.

        Recall that a permutation :math:`\sigma` is called a derangement if it has no fixed points, i.e.,
        :math:`\sigma(x) \neq x` for every :math:`x` in the permutation domain.

        :return: True if the permutation is a derangement, False otherwise.
        :rtype: bool

        :example:
            >>> from symmetria import Cycle, CycleDecomposition
            ...
            >>> CycleDecomposition(Cycle(1)).is_derangement()
            False
            >>> CycleDecomposition(Cycle(1, 2, 3)).is_derangement()
            True
            >>> CycleDecomposition(Cycle(1), Cycle(2, 3)).is_derangement()
            False
        """
        for cycle in iter(self):
            if len(cycle) == 1:
                return False
        return True

    def is_even(self) -> bool:
        """Check if the cycle decomposition is even.

        Recall that a permutation is said to be even if it can be expressed as the product of an even number of
        transpositions.

        :return: True if the cycle decomposition is even, False otherwise.
        :rtype: bool

        :example:
            >>> from symmetria import Cycle, CycleDecomposition
            ...
            >>> CycleDecomposition(Cycle(1)).is_even()
            True
            >>> CycleDecomposition(Cycle(1, 2), Cycle(3)).is_even()
            False
            >>> CycleDecomposition(Cycle(1), Cycle(2, 4, 7, 6), Cycle(3, 5)).is_even()
            True
        """
        return self.sgn() == 1

    def is_odd(self) -> bool:
        """Check if the cycle decomposition is odd.

        Recall that a permutation is said to be odd if it can be expressed as the product of an odd number of
        transpositions.

        :return: True if the cycle decomposition is odd, False otherwise.
        :rtype: bool

        :example:
            >>> from symmetria import Cycle, CycleDecomposition
            ...
            >>> CycleDecomposition(Cycle(1)).is_odd()
            False
            >>> CycleDecomposition(Cycle(1, 2), Cycle(3)).is_odd()
            True
            >>> CycleDecomposition(Cycle(1), Cycle(2, 4, 7, 6), Cycle(3, 5)).is_odd()
            False
        """
        return self.sgn() == -1

    def is_regular(self) -> bool:
        """Check if the cycle decomposition is regular.

        Recall that a permutation is said regular if all cycles in its cycle decomposition have the same length.

        :return: True if the cycle decomposition is regular, False otherwise.
        :rtype: bool

        :example:
            >>> from symmetria import Cycle, CycleDecomposition
            ...
            >>> CycleDecomposition(Cycle(1)).is_regular()
            True
            >>> CycleDecomposition(Cycle(2, 1)).is_regular()
            True
            >>> CycleDecomposition(Cycle(2, 1), Cycle(3)).is_regular()
            False
        """
        return all(len(cycle) == len(self[0]) for cycle in iter(self))

    def lehmer_code(self) -> List[int]:
        """Return the Lehmer code of the cycle decomposition.

        Recall that the Lehmer code of a permutation is a sequence that encodes the permutation as a series of integers.
        Each integer represents the number of smaller elements to the right of a given element in the permutation.

        :return: the Lehmer code of the cycle decomposition.
        :rtype: List[int]

        :example:
            >>> from symmetria import CycleDecomposition, Cycle
            ...
            >>> CycleDecomposition(Cycle(1)).lehmer_code()
            [0]
            >>> CycleDecomposition(Cycle(1, 2), Cycle(3)).lehmer_code()
            [1, 0, 0]
            >>> CycleDecomposition(Cycle(1, 4), Cycle(2, 3)).lehmer_code()
            [3, 2, 1, 0]
        """
        return symmetria.Permutation.from_cycle_decomposition(self).lehmer_code()

    def lexicographic_rank(self) -> int:
        """Return the lexicographic rank of the cycle decomposition.

        Recall that the lexicographic rank of a permutation refers to its position in the list of all
        permutations of the same degree sorted in lexicographic order.

        :return: the lexocographic rank of the cycle decomposition.
        :rtype: int

        :example:
            >>> from symmetria import Cycle, CycleDecomposition
            ...
            >>> CycleDecomposition(Cycle(1)).lexicographic_rank()
            1
            >>> CycleDecomposition(Cycle(1, 3, 2)).lexicographic_rank()
            5
            >>> CycleDecomposition(Cycle(1, 3, 2), Cycle(4, 5)).lexicographic_rank()
            50
        """
        return symmetria.elements.permutation.Permutation.from_cycle_decomposition(self).lexicographic_rank()

    @property
    def map(self) -> Dict[int, int]:
        """Return a dictionary representing the mapping of the cycle decomposition,
        where keys are indices and values are the corresponding elements after permutation.

        :return: The mapping of the cycle decompostiion.
        :rtype: Dict[int, int]

        :example:
            >>> from symmetria import Cycle, CycleDecomposition
            ...
            >>> CycleDecomposition(Cycle(1)).map
            {1: 1}
            >>> CycleDecomposition(Cycle(1, 2), Cycle(3, 4)).map
            {1: 2, 2: 1, 3: 4, 4: 3}
        """
        _map = {}
        for cycle in iter(self):
            _map.update(cycle.map)
        return _map

    def orbit(self, item: Any) -> List[Any]:
        r"""Compute the orbit of `item` object under the action of the cycle decomposition.

        Recall that the orbit of the action of a cycle decomposition :math:`\sigma` on an element x is given by the set

        ..math:: \{ \sigma^n(x): n \in \mathbb{N}\}.

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

    def order(self) -> int:
        r"""Return the order of the cycle permutation.

        Recall that the order of a cycle decompostion is the least common multiple of lengths (order) of its cycles.

        :return: The order of the cycle permutation.
        :rtype: int

        :example:
            >>> from symmetria import Cycle, CycleDecomposition
            ...
            >>> CycleDecomposition(Cycle(1)).order()
            1
            >>> CycleDecomposition(Cycle(1, 3, 2)).order()
            3
            >>> CycleDecomposition(Cycle(1, 3, 2), Cycle(4, 5)).order()
            6
        """
        return lcm(*[len(cycle) for cycle in iter(self)])

    def records(self) -> List[int]:
        r"""Return the records of the cycle decomposition.

        Recall that a record of a permutation :math:`\sigma \in S_n`, where :math:`n \in \mathbb{N}`, is a position
        :math:`i \in \{1, ..., n\}` such that is either :math:`i=1` or :math:`\sigma(j) < \sigma(i)`
        for all :math:`j<i`.

        .. note:: There are definitions of records in the literature where the first index is not considered as a
            record.

        :return: The records of the cycle decomposition.
        :rtype: List[int]

        :example:
            >>> from symmetria import Cycle, CycleDecomposition
            ...
            >>> CycleDecomposition(Cycle(1)).records()
            [1]
            >>> CycleDecomposition(Cycle(1, 2), Cycle(3)).records()
            [1, 3]
            >>> CycleDecomposition(Cycle(1), Cycle(2, 4, 7, 6), Cycle(3, 5)).records()
            [1, 2, 3, 4]
        """
        return symmetria.Permutation.from_cycle_decomposition(self).records()

    def sgn(self) -> int:
        r"""Return the sign of the cycle decomposition.

        Recall that the sign, signature, or signum of a permutation :math:`\sigma` is defined as +1 if :math:`\sigma`
        is even, and -1 if :math:`\sigma` is odd.

        To compute the sign of a cycle decomposition, we use the fact that the sign is a homomorphism of groups, i.e.,
        the sign of the cycle decomposition is just the product of the signs of the cycle componing it.

        :return: 1 if the cycle decomposition is even, -1 if the cycle decomposition is odd.
        :rtype: int

        :example:
            >>> from symmetria import Cycle, CycleDecomposition
            ...
            >>> CycleDecomposition(Cycle(1)).sgn()
            1
            >>> CycleDecomposition(Cycle(1, 2), Cycle(3)).sgn()
            -1
            >>> CycleDecomposition(Cycle(1), Cycle(2, 4, 7, 6), Cycle(3, 5)).sgn()
            1
        """
        return prod([cycle.sgn() for cycle in iter(self)])

    def support(self) -> Set[int]:
        r"""Return a set containing the indices in the domain of the permutation whose images are different from
        their respective indices, i.e., the set of :math:`n \in \mathbb{N}` in the permutation domain which are
        not mapped to itself.

        :return: The support set of the cycle decomposition.
        :rtype: Set[int]

        :example:
            >>> from symmetria import Cycle, CycleDecomposition
            ...
            >>> CycleDecomposition(Cycle(1)).support()
            set()
            >>> CycleDecomposition(Cycle(1), Cycle(2, 3)).support()
            {2, 3}
            >>> CycleDecomposition(Cycle(3, 4, 5, 6), Cycle(2, 1)).support()
            {1, 2, 3, 4, 5, 6}
        """
        return {element for cycle in iter(self) if len(cycle) != 1 for element in iter(cycle.elements)}
