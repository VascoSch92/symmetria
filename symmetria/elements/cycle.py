from typing import TYPE_CHECKING, Any, Set, Dict, List, Tuple, Union, Iterable, Iterator
from collections import OrderedDict

import symmetria.elements.permutation
import symmetria.elements.cycle_decomposition
from symmetria.elements._base import _Element
from symmetria.elements._utils import _pretty_print_table
from symmetria.elements._validators import _validate_cycle

if TYPE_CHECKING:
    from symmetria.elements.permutation import Permutation
    from symmetria.elements.cycle_decomposition import CycleDecomposition

__all__ = ["Cycle"]


class Cycle(_Element):
    r"""The ``Cycle`` class represents the cycle elements of a symmetric group.

    Recall that a cycle is a permutation that rearranges the elements of a finite set in a circular fashion, i.e.,
    moves each element to the position of the next element in a cycle manner, with the last element being moved to the
    position of the first element.

    To define a cycle, you need to provide its cycle notation.

    For example, to define the cycle :math:`\sigma \in S_3` given by :math:`\sigma(1)=3`, :math:`\sigma(2)=1` and
    :math:`\sigma(3)=2`, you should write ``Cycle(1, 3, 2)``

    .. note:: A cycle can have different representations. For example, the cycle ``Cycle(1, 3, 2)`` can be also
        written ``Cycle(2, 1, 3)``.

        By convention, a cycle start always with the smaller number. Don't panic, you can define a
        cycle in the way you like the most, but then it will be stored following the above convention.

    :param cycle: Set of integers representing the cycle notation of the cycle.
    :type cycle: int

    :raises ValueError: If there is an integer in the provided cycle which is not strictly positive.

    :example:
        >>> from symmetria import Cycle
        ...
        >>> cycle = Cycle(1, 3, 2)
        >>> cycle = Cycle(*[1, 3, 2])
        >>> cycle = Cycle(*(1, 3, 2))
    """

    __slots__ = ["_cycle", "_domain"]

    def __new__(cls, *cycle: int) -> "Cycle":
        _validate_cycle(cycle=cycle)
        return super().__new__(cls)

    def __init__(self, *cycle: int) -> None:
        self._cycle: Tuple[int, ...] = self._standardization(cycle=cycle)
        self._domain: Iterable[int] = range(1, max(self._cycle) + 1)

    @staticmethod
    def _standardization(cycle: Tuple[int, ...]) -> Tuple[int, ...]:
        """Private method to standardize a set of integers to form a cycle.

        The standard form for a cycle is the (unique) one where the first element is the smallest.
        """
        smallest_element_index = cycle.index(min(cycle))
        if smallest_element_index == 0:
            return tuple(cycle)
        return cycle[smallest_element_index:] + cycle[:smallest_element_index]

    def __bool__(self) -> bool:
        r"""Check if the cycle is different from the identity cycle.

        :return: True if the cycle is different from the identity cycle, False otherwise.
        :rtype: bool

        :example:
            >>> from symmetria import Cycle
            ...
            >>> bool(Cycle(1))
            False
            >>> bool(Cycle(2, 1, 3))
            True

        :note: Every cycle of the form ``Cycle(n)`` is considered empty for every :math:`n \in \mathbb{N}`, i.e.,
            ``bool(Cycle(n)) = False``.
        """
        return len(self.elements) != 1

    def __call__(self, item: Any) -> Any:
        """Call the cycle on the `item` object, i.e., mimic a cycle action on the element `item`.

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
            >>> from symmetria import Cycle, Permutation
            ...
            >>> cycle = Cycle(3, 1, 2)
            >>> cycle(2)
            3
            >>> cycle("abc")
            'cab'
            >>> cycle([1, 2, 3])
            [3, 1, 2]
            >>> cycle(Permutation(3, 1, 2))
            Permutation(1, 2, 3)
        """
        if isinstance(item, int):
            return self._call_on_integer(original=item)
        elif isinstance(item, (str, list, tuple)):
            if max(self.elements) > len(item):
                raise ValueError(f"Not enough object to permute {item} using the cycle {self}.")
            return self._call_on_str_list_tuple(original=item)
        elif isinstance(item, symmetria.elements.permutation.Permutation):
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
        elif isinstance(item, symmetria.elements.cycle_decomposition.CycleDecomposition):
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
        """Private method for calls on permutation."""
        cycles = [self]
        for idx in original.domain:
            if idx not in self:
                cycles.append(Cycle(idx))
        cycle_decomposition = symmetria.elements.cycle_decomposition.CycleDecomposition(*cycles)
        return symmetria.elements.permutation.Permutation.from_cycle_decomposition(cycle_decomposition) * original

    def _call_on_cycle_decomposition(self, original: "CycleDecomposition") -> "CycleDecomposition":
        """Private method for calls on cycle decomposition."""
        cycles = [self]
        for idx in original.domain:
            if idx not in self:
                cycles.append(Cycle(idx))
        cycle_decomposition = symmetria.elements.cycle_decomposition.CycleDecomposition(*cycles)
        return cycle_decomposition * original

    def __contains__(self, item: Any) -> bool:
        """Membership check, i.e., if an element is contained in the cycle.

        :param item: The object to check membership for.
        :type item: Any

        :return: True if the given element is in the cycle. Otherwise, False.
        :rtype: bool

        :example:
            >>> from symmetria import Cycle
            ...
            >>> 1 in Cycle(1, 2, 3)
            True
            >>> 7 in Cycle(1, 2, 3)
            False
        """
        return item in self._cycle

    def __eq__(self, other: Any) -> bool:
        """Check if the cycle is equal to another object.

        :param other: The object to compare with.
        :type other: Any

        :return: True if the cycle is equal to `other`, i.e., they define the same map. Otherwise, False.
        :rtype: bool

        :example:
            >>> from symmetria import Cycle
            ...
            >>> Cycle(1, 2, 3) == Cycle(3, 1, 2)
            True
            >>> Cycle(1, 3, 2) == Cycle(1, 2, 3)
            False
            >>> Cycle(1, 2, 3) == 13
            False
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
        """Return the value of the cycle at the given index `item`.

        The index corresponds to the position in the cycle in its standardize form, starting from 0.

        :param item: The index of the cycle.
        :type item: int

        :return: The value of the cycle at the specified index.
        :rtype: int

        :raises IndexError: If the index is out of range.

        :example:
            >>> from symmetria import Cycle
            ...
            >>> cycle = Cycle(1, 3, 2)
            >>> for idx in range(len(cycle)):
            ...    cycle[idx]
            1
            3
            2
        """
        return self._cycle[item]

    def __int__(self) -> int:
        """Convert the cycle to its integer representation.

        In other words, return a numeric one line notation of the cycle.

        :return: The integer representation of the cycle.
        :rtype: int

        :example:
            >>> from symmetria import Cycle
            ...
            >>> int(Cycle(1))
            1
            >>> int(Cycle(13))
            13
            >>> int(Cycle(3, 1, 2))
            123
            >>> int(Cycle(1, 3, 4, 5, 2, 6))
            134526
        """
        return sum([element * 10 ** (len(self) - idx) for idx, element in enumerate(self.elements, 1)])

    def __iter__(self) -> Iterator[int]:
        """Return an iterator over the cycles in the cycle decomposition.

        :return: An iterator over the Cycle objects contained.
        :rtype: Iterator[Cycle]

        :example:
            >>> from symmetria import Cycle
            >>> cycle = Cycle(1, 2, 3, 4)
            >>> for element in cycle:
            ...     print(element)
            1
            2
            3
            4
        """
        return iter(self._cycle)

    def __len__(self) -> int:
        """Return the length of the cycle, which is the number of elements in its domain.

        :return: The length of the cycle.
        :rtype: int

        :example:
            >>> from symmetria import Cycle
            ...
            >>> len(Cycle(3, 1, 2))
            3
            >>> len(Cycle(1, 3, 4, 5, 2, 6))
            6
        """
        return len(self._cycle)

    def __mul__(self, other: "Cycle") -> "Cycle":
        """
        :raise NotImplementedError: Multiplication between cycles is not supported. However, composition is supported.
            Try to call your cycle on the cycle you would like to compose.
        """
        raise NotImplementedError(
            "Multiplication between cycles is not supported. However, composition is supported. \n"
            "Try to call your cycle on the cycle you would like to compose."
        )

    def __repr__(self) -> str:
        r"""Return a string representation of the cycle in the format `Cycle(x, y, z, ...)`,
        where :math:`x, y, z, ... \in \mathbb{N}` are the elements of the cycle.

        :return: A string representation of the cycle.
        :rtype: str

        :example:
            >>> from symmetria import Cycle
            ...
            >>> Cycle(3, 1, 2).__repr__()
            'Cycle(1, 2, 3)'
            >>> Cycle(1, 3, 4, 5, 2, 6).__repr__()
            'Cycle(1, 3, 4, 5, 2, 6)'
        """
        return f"Cycle({', '.join(str(element) for element in self.elements)})"

    def __str__(self) -> str:
        r"""Return a string representation of the cycle in the form of cycle notation.

        Recall that for a cycle :math:`\sigma` of order n, its cycle notation is given by

        .. math:: (\sigma(x)\quad\sigma^2(x)\quad...\quad\sigma^n(x)),

        where x is an element in the support of the cycle, and :math:`n \in \mathbb{N}` is the cycle order.

        :return: A string representation of the cycle.
        :rtype: str

        :example:
            >>> from symmetria import Cycle
            ...
            >>> print(Cycle(3, 1, 2))
            (1 2 3)
            >>> print(Cycle(1, 3, 4, 5, 2, 6))
            (1 3 4 5 2 6)
        """
        return "(" + " ".join([str(element) for element in self.elements]) + ")"

    def cycle_decomposition(self) -> "CycleDecomposition":
        """Convert the cycle into its cycle decomposition, representing it as a product of disjoint cycles.

        In the specific case of a cycle, it converts it from the class ``Cycle`` to the class ``CycleDecomposition``.

        :return: The cycle decomposition of the permutation.
        :rtype: CycleDecomposition

        :example:
            >>> from symmetria import Cycle
            ...
            >>> Cycle(1).cycle_decomposition()
            CycleDecomposition(Cycle(1))
            >>> Cycle(3).cycle_decomposition()
            CycleDecomposition(Cycle(1), Cycle(2), Cycle(3))
            >>> Cycle(3, 1, 2).cycle_decomposition()
            CycleDecomposition(Cycle(1, 2, 3))
        """
        return symmetria.elements.cycle_decomposition.CycleDecomposition(
            *([Cycle(idx) for idx in self.domain if idx not in self] + [self])
        )

    def cycle_notation(self) -> str:
        r"""Return a string representing the cycle notation of the cycle.

        Recall that for a cycle :math:`\sigma` of order n, its cycle notation is given by

        .. math:: (\sigma(x)\quad\sigma^2(x)\quad...\quad\sigma^n(x)),

        where x is an element in the support of the cycle, and :math:`n \in \mathbb{N}` is the cycle order.

        :return: The cycle notation of the cycle.
        :rtype: str

        :example:
            >>> from symmetria import Cycle
            ...
            >>> Cycle(1).cycle_notation()
            '(1)'
            >>> Cycle(3, 1, 2).cycle_notation()
            '(1 2 3)'
            >>> Cycle(3, 1, 2, 4, 5, 6).cycle_notation()
            '(1 2 4 5 6 3)'
        """
        return str(self)

    def degree(self) -> int:
        """Return the degree of the cycle.

        Recall that the degree of a cycle is the number of elements on which it acts.

        :return: The degree of the cycle.
        :rtype: int

        :example:
            >>> from symmetria import Cycle
            ...
            >>> Cycle(1).degree()
            1
            >>> Cycle(1, 3, 2).degree()
            3
            >>> Cycle(1, 4, 3, 2).degree()
            4
        """
        return len(self)

    def describe(self) -> str:
        """Return a table describing the cycle.

        :return: A table describing the cycle.
        :rtype: str

        :example:
            >>> from symmetria import Cycle
            ...
            >>> c = Cycle(3, 5, 6, 7).describe()
            >>> print(c)
            +----------------------------------------------------+
            |                 Cycle(3, 5, 6, 7)                  |
            +----------------------------------------------------+
            | order                    |            4            |
            +--------------------------+-------------------------+
            | degree                   |            4            |
            +--------------------------+-------------------------+
            | is derangement           |          True           |
            +--------------------------+-------------------------+
            | inverse                  |        (3 7 6 5)        |
            +--------------------------+-------------------------+
            | parity                   |        -1 (odd)         |
            +--------------------------+-------------------------+
            | cycle notation           |        (3 5 6 7)        |
            +--------------------------+-------------------------+
            | inversions               |           []            |
            +--------------------------+-------------------------+
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
                    "inversions": str(self.inversions()),
                }
            ),
        )

    @property
    def domain(self) -> Iterable[int]:
        """Return an iterable containing the elements of the domain of the cycle.

        Here, the domain of a cycle is the set of indices for which the cycle is defined.

        :return: The domain of the cycle.
        :rtype: Iterable[int]

        :example:
            >>> from symmetria import Cycle
            ...
            >>> Cycle(1).domain
            range(1, 2)
            >>> Cycle(13).domain
            range(1, 14)
            >>> Cycle(3, 1, 2).domain
            range(1, 4)
            >>> Cycle(1, 3, 4, 5, 2, 6).domain
            range(1, 7)
        """
        return self._domain

    @property
    def elements(self) -> Tuple[int, ...]:
        """Return a tuple containing the elements of the cycle in its standard form.

        :return: The elements of the cycle.
        :rtype: Tuple[int]

        :example:
            >>> from symmetria import Cycle
            ...
            >>> Cycle(1).elements
            (1,)
            >>> Cycle(3, 1, 2).elements
            (1, 2, 3)
            >>> Cycle(3, 4, 7, 1, 2).elements
            (1, 2, 3, 4, 7)
        """
        return self._cycle

    def equivalent(self, other: Any) -> bool:
        """Check if the cycle is equivalent to the `other` object.

        In `symmetria`, a permutation of the symmetric group can have different representations. For example,
        it can be a `Permutation`, or a `Cycle`, or also a `CycleDecomposition`. The method checks if the (self)
        cycle is representing the same permutation of the `other` object.

        :param other:
        :type other: Any

        :return: True if the cycle is equivalent to the `other` object.
        :rtype bool:

        :example:
            >>> from symmetria import Cycle, Permutation, CycleDecomposition
            ...
            >>> Cycle(1, 2, 3).equivalent(Permutation(2, 3, 1))
            True
            >>> Cycle(1, 2, 3).equivalent(CycleDecomposition(Cycle(1, 2, 3)))
            True
            >>> Cycle(1, 2, 3).equivalent(CycleDecomposition(Cycle(1, 2, 3), Cycle(4)))
            True
        """
        if isinstance(other, Cycle):
            return self == other
        if isinstance(other, symmetria.elements.cycle_decomposition.CycleDecomposition):
            # case where both are the identity
            if bool(self) is False and bool(other) is False:
                return max(self.elements) == max([max(cycle.elements) for cycle in iter(other)])
            # cases where is the identity but the other no
            elif (bool(self) is False and bool(other) is True) or (bool(self) is True and bool(other) is False):
                return False
            # both not the identity
            else:
                for cycle in iter(other):
                    if len(cycle) > 1:
                        return self == cycle
        elif isinstance(other, symmetria.elements.permutation.Permutation):
            return symmetria.elements.permutation.Permutation.from_cycle(cycle=self) == other
        return False

    def inverse(self) -> "Cycle":
        r"""Return the inverse of the cycle.

        Recall that the inverse of a permutation :math:`\sigma \in S_n`, for some :math:`n \in \mathbb{N}`, is the
        the only permutation :math:`\tau \in S_n` such that :math:`\sigma * \tau = \tau * \sigma = id`,
        where :math:`id` is the identity permutation.

        Note that for a cycle, its inverse is just the backward cycle.

        :return: The inverse of the cycle.
        :rtype: Cycle

        :example:
            >>> from symmetria import Cycle
            ...
            >>> Cycle(1, 2, 3).inverse()
            Cycle(1, 3, 2)
            >>> Cycle(1, 3, 4, 2).inverse()
            Cycle(1, 2, 4, 3)
            >>> Cycle(2, 3, 1, 5, 4).inverse()
            Cycle(1, 3, 2, 4, 5)
        """
        return Cycle(*self.elements[::-1])

    def inversions(self) -> List[Tuple[int, int]]:
        r"""Return the inversions of the cycle.

        Recall that an inversion of a permutation :math:`\sigma \in S_n`, for :math:`n \in \mathbb{N}`, is a pair
        :math:`(i, j)` of positions (indexes), where the entries of the permutation are in the opposite order, i.e.,
        :math:`i<j` but :math:`\sigma(i)>\sigma(j)`.

        .. note:: The inversions of the cycle are computed after the cycle is standardized in its normal form, i.e.,
            :math:`c_1 < c_j` for every :math:`c_j \neq c_1` in the cycle :math:`c = (c_1, ..., c_n)`.

        :return: The inversions of the cycle.
        :rtype: List[Tuple[int, int]]

        :example:
            >>> from symmetria import Cycle
            ...
            >>> Cycle(1, 2, 3).inversions()
            []
            >>> Cycle(1, 3, 4, 2).inversions()
            [(2, 4), (3, 4)]
            >>> Cycle(1, 2, 5, 4, 3).inversions()
            [(3, 4), (3, 5), (4, 5)]
        """
        inversions, elements = [], list(self.elements)
        min_element = 1
        for i, p in enumerate(elements, 1):
            if p == min_element:
                min_element += 1
            else:
                for j, q in enumerate(elements[i:], 1):
                    if p > q:
                        inversions.append((i, i + j))
        return inversions

    def is_derangement(self) -> bool:
        r"""Check if the cycle is a derangement.

        Recall that a permutation :math:`\sigma` is called a derangement if it has no fixed points, i.e.,
        :math:`\sigma(x) \neq x` for every :math:`x` in the permutation domain.

        By definition, a cycle is a derangement if and only if it is not the identity cycle.

        :return: True if the cycle is a derangement, False otherwise.
        :rtype: bool

        :example:
            >>> from symmetria import Cycle
            ...
            >>> Cycle(1).is_derangement()
            False
            >>> Cycle(13).is_derangement()
            False
            >>> Cycle(1, 2, 3).is_derangement()
            True
        """
        return len(self) > 1

    def is_even(self) -> bool:
        """Check if the cycle is even.

        Recall that a cycle is said to be even if it can be expressed as the product of an even number of
        transpositions.

        :return: True if the cycle is even, False otherwise.
        :rtype: bool

        :example:
            >>> from symmetria import Cycle
            ...
            >>> Cycle(1).is_even()
            True
            >>> Cycle(1, 2).is_even()
            False
            >>> Cycle(1, 2, 3, 4, 5, 6).is_even()
            False
            >>> Cycle(1, 2, 3, 4, 5, 6, 7).is_even()
            True
        """
        return self.sgn() == 1

    def is_odd(self) -> bool:
        """Check if the cycle is odd.

        Recall that a cycle is said to be odd if it can be expressed as the product of an odd number of
        transpositions.

        :return: True if the cycle is odd, False otherwise.
        :rtype: bool

        :example:
            >>> from symmetria import Cycle
            ...
            >>> Cycle(1).is_odd()
            False
            >>> Cycle(1, 2).is_odd()
            True
            >>> Cycle(1, 2, 3, 4, 5, 6).is_odd()
            True
            >>> Cycle(1, 2, 3, 4, 5, 6, 7).is_odd()
            False
        """
        return self.sgn() == -1

    @property
    def map(self) -> Dict[int, int]:
        """Return a dictionary representing the mapping of the cycle,
        where keys are indices and values are the corresponding elements after the permutation.

        :return: The mapping of the cycle.
        :rtype: Dict[int, int]

        :example:
            >>> from symmetria import Cycle
            ...
            >>> Cycle(1).map
            {1: 1}
            >>> Cycle(3).map
            {3: 3}
            >>> Cycle(3, 1, 2).map
            {1: 2, 2: 3, 3: 1}
        """
        return {element: self[(idx + 1) % len(self)] for idx, element in enumerate(self.elements)}

    def orbit(self, item: Any) -> List[Any]:
        r"""Compute the orbit of `item` object under the action of the cycle.

        Recall that the orbit of the action of a cycle :math:`\sigma` on an element x is given by the set

        .. math:: \{ \sigma^n(x): n \in \mathbb{N}\}.

        :param item: The initial element or iterable to compute the orbit for.
        :type item: Any

        :return: The orbit of the specified element under the permutation.
        :rtype: List[Any]

        :example:
            >>> from symmetria import Cycle, CycleDecomposition, Permutation
            ...
            >>> Cycle(1, 3, 2).orbit(1)
            [1, 3, 2]
            >>> Cycle(1, 3, 2).orbit([1, 2, 3])
            [[1, 2, 3], [2, 3, 1], [3, 1, 2]]
            >>> Cycle(1, 3, 2).orbit("abc")
            ['abc', 'bca', 'cab']
            >>> Cycle(1, 3, 2).orbit(Permutation(3, 1, 2))
            [Permutation(3, 1, 2), Permutation(2, 3, 1), Permutation(1, 2, 3)]
        """
        if isinstance(item, Cycle):
            item = item.cycle_decomposition()
        orbit = [item]
        next_element = self(item)
        while next_element != item:
            orbit.append(next_element)
            next_element = self(next_element)
        return orbit

    def order(self) -> int:
        r"""Return the order of the cycle.

        Recall that the order of a permutation :math:`\sigma` is the smallest positive integer :math:`n \in \mathbb{N}`
        such that :math:`\sigma^n = id`, where :math:`id` is the identity permutation. Therefore, the order of a cycle
        is nothing but just its length.

        :return: The order of the cycle.
        :rtype: int

        :example:
            >>> from symmetria import Cycle
            ...
            >>> Cycle(1).order()
            1
            >>> Cycle(3, 1, 2).order()
            3
            >>> Cycle(1, 3, 4, 5, 2, 6).order()
            6
        """
        return len(self)

    def sgn(self) -> int:
        r"""Return the sign of the cycle.

        Recall that the sign, signature, or signum of a permutation :math:`\sigma` is defined as +1 if :math:`\sigma`
        is even, and -1 if :math:`\sigma` is odd.

        To compute the sign of a cycle, we use the fact that a cycle is odd if and only if it has even length.

        :return: 1 if the cycle is even, -1 if the cycle is odd.
        :rtype: int

        :example:
            >>> from symmetria import Cycle
            ...
            >>> Cycle(1).sgn()
            1
            >>> Cycle(1, 2).sgn()
            -1
            >>> Cycle(1, 2, 3, 4, 5, 6).sgn()
            -1
            >>> Cycle(1, 2, 3, 4, 5, 6, 7).sgn()
            1
        """
        return -1 if len(self) % 2 == 0 else 1

    def support(self) -> Set[int]:
        """Return a set containing the indices in the domain of the cycle whose images are different from their
        respective indices, i.e., the set of :math:`n` in the cycle domain which are not mapped to itself.

        The support of a cycle is elementwise equal to the domain of the cycle if and only if the cycle is not
        the identity cycle. Otherwise, it is empty.

        :return: The support set of the cycle.
        :rtype: Set[int]

        :example:
            >>> from symmetria import Cycle
            ...
            >>> Cycle(1).support()
            set()
            >>> Cycle(13).support()
            set()
            >>> Cycle(3, 1, 2).support()
            {1, 2, 3}
            >>> Cycle(1, 3, 4, 5, 2, 6).support()
            {1, 2, 3, 4, 5, 6}
        """
        return set(self._cycle) if len(self) > 1 else set()
