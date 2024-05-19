from abc import ABC, abstractmethod
from typing import Any, Set, Dict, List, Iterable


class _Element(ABC):
    """Abstract class which exposes methods to implement in class representing permutations."""

    def name(self) -> str:
        """Shortcut for the class name. Used for the tests."""
        return self.__class__.__name__

    def rep(self) -> str:
        """Shortcut for `__repr__()`. Used for tests."""
        return self.__repr__()

    @abstractmethod
    def __bool__(self) -> bool:
        """Implement method `bool( )`."""
        raise NotImplementedError

    @abstractmethod
    def __call__(self, item: Any) -> Any:
        """Implement method `self( )`."""
        raise NotImplementedError

    @abstractmethod
    def __eq__(self, other) -> bool:
        """Implement equality between two objects."""
        raise NotImplementedError

    @abstractmethod
    def __int__(self) -> int:
        """Implement method `int( )`."""
        raise NotImplementedError

    @abstractmethod
    def __mul__(self, other):
        """Implement multiplication between two object."""
        raise NotImplementedError

    @abstractmethod
    def __repr__(self) -> str:
        """Implement method `__repr__( )`."""
        raise NotImplementedError

    @abstractmethod
    def __str__(self) -> str:
        """Implement method `__str__( )`."""
        raise NotImplementedError

    @property
    @abstractmethod
    def domain(self) -> Iterable[int]:
        """Return the domain on which the element is defined."""
        raise NotImplementedError

    @property
    @abstractmethod
    def map(self) -> Dict[int, int]:
        """Return a dictionary representing the map defining the element."""
        raise NotImplementedError

    # TODO: decide if we want to implement this method also for the classes Cycle and CycleDecomposition
    # @staticmethod
    # @abstractmethod
    # def from_dict(permutation: Dict) -> "Element":
    #     raise NotImplementedError

    @abstractmethod
    def cycle_decomposition(self) -> "CycleDecomposition":
        """Return the cycle decomposition of the element."""
        raise NotImplementedError

    @abstractmethod
    def cycle_notation(self) -> str:
        """Return the cycle notation of the object."""
        raise NotImplementedError

    @abstractmethod
    def equivalent(self, other: Any) -> bool:
        """Check if two object coming from two different classes represent the same permutation."""
        raise NotImplementedError

    @abstractmethod
    def is_derangement(self) -> bool:
        """Return if the element is a derangement or not."""
        raise NotImplementedError

    @abstractmethod
    def orbit(self, item: Any) -> List[Any]:
        """Return the orbit created from the action of the element on the item."""
        raise NotImplementedError

    @abstractmethod
    def order(self) -> int:
        """Return the order of the element."""
        raise NotImplementedError

    @abstractmethod
    def support(self) -> Set[int]:
        """Return the support of the element."""
        raise NotImplementedError
