class _Element:
    """Base class for elements."""

    def __repr__(self) -> str:
        return "_Element()"

    def rep(self) -> str:
        """Shortcut for `__repr__()`."""
        return self.__repr__()

    def typename(self) -> str:
        """Shortcut for the name of the class type.

        :return: The name of the class type.
        :rtype: str

        :example:
            >>> from symmetria import Cycle, CycleDecomposition, Permutation
            ...
            >>> Permutation(1, 2, 3).typename()
            'Permutation'
            >>> Cycle(1, 2).typename()
            'Cycle'
            >>> CycleDecomposition(Cycle(1, 3, 2)).typename()
            'CycleDecomposition'
        """
        return self.__class__.__name__
