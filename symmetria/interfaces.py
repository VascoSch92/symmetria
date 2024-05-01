from abc import ABC, abstractmethod
from typing import Dict, Set, Iterable


class _Element(ABC):
    """Abstract class which exposes methods to implement in class representing permutations"""

    @abstractmethod
    def __bool__(self) -> bool:
        # TODO: add description
        raise NotImplementedError

    @abstractmethod
    def __eq__(self, other) -> bool:
        raise NotImplementedError

    @abstractmethod
    def __int__(self) -> int:
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
