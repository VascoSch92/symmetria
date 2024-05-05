from abc import ABC, abstractmethod
from typing import Dict, Set, Iterable, Any, List


class _Element(ABC):
    """Abstract class which exposes methods to implement in class representing permutations"""

    def name(self) -> str:
        """Shortcut for the class name. Used for the tests."""
        return self.__class__.__name__

    def rep(self) -> str:
        """Shortcut for `__repr__()`. Used for tests."""
        return self.__repr__()

    @abstractmethod
    def __bool__(self) -> bool:
        # TODO: add description
        raise NotImplementedError

    @abstractmethod
    def __eq__(self, other) -> bool:
        # TODO: add description
        raise NotImplementedError

    @abstractmethod
    def __int__(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def __mul__(self, other):
        raise NotImplementedError

    @abstractmethod
    def __repr__(self) -> str:
        # TODO: add description
        raise NotImplementedError

    @abstractmethod
    def __str__(self) -> str:
        # TODO: add description
        raise NotImplementedError

    @property
    @abstractmethod
    def domain(self) -> Iterable[int]:
        # TODO: add description
        raise NotImplementedError

    @property
    @abstractmethod
    def map(self) -> Dict[int, int]:
        # TODO: add description
        raise NotImplementedError

    """@staticmethod
    @abstractmethod
    def from_dict(permutation: Dict) -> "Element":
        raise NotImplementedError
    """

    @abstractmethod
    def cycle_notation(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def equivalent(self, other: Any) -> bool:
        raise NotImplementedError

    @abstractmethod
    def orbit(self, item: Any) -> List[Any]:
        raise NotImplementedError

    @abstractmethod
    def order(self) -> int:
        # TODO: add description
        raise NotImplementedError

    @abstractmethod
    def is_derangement(self) -> bool:
        # TODO: add description
        raise NotImplementedError

    @abstractmethod
    def support(self) -> Set[int]:
        # TODO: add description
        raise NotImplementedError
