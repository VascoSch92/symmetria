from dataclasses import dataclass


@dataclass(init=False, frozen=True, order=False, eq=False)
class _Element:
    """Base class for elements."""

    def rep(self) -> str:
        """Shortcut for `__repr__()`."""
        return self.__repr__()

    def typename(self) -> str:
        """Shortcut for the name of the class type."""
        return self.__class__.__name__
