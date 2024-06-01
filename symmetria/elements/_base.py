class _Element:
    """Base class for elements."""

    @staticmethod
    def name() -> str:
        """Shortcut for the class name."""
        return __class__.__name__

    def rep(self) -> str:
        """Shortcut for `__repr__()`."""
        return self.__repr__()
