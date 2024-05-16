Quickstart
==========

Symmetria offers three classes for representing permutations: ``Permutation``, ``Cycle``, and ``CycleDecomposition``.
Each of these classes has its own set of advantages and disadvantages depending on the specific goal you want to
achieve.

Below is a brief example showcasing the capabilities of one of the aforementioned classes.

To begin, import your selected class with:

.. tab-set::

    .. tab-item:: Permutation
        :sync: permutation

        .. code-block:: python

            from symmetria import Permutation

    .. tab-item:: Cycle
        :sync: cycle

        .. code-block:: python

            from symmetria import Cycle

    .. tab-item:: CycleDecomposition
        :sync: cycledecomposition

        .. code-block:: python

            from symmetria import CycleDecomposition

you can now instantiate a permutation

.. tab-set::

    .. tab-item:: Permutation
        :sync: permutation

        .. code-block:: python

            permutation = Permutation(1, 3, 4, 5, 2, 6)
            print(permutation)
            # (1, 3, 4, 5, 2, 6)

    .. tab-item:: Cycle
        :sync: cycle

        .. code-block:: python

            cycle = Cycle(1, 3, 4, 5, 2, 6)
            print(cycle)
            # (1 3 4 5 2 6)

    .. tab-item:: CycleDecomposition
        :sync: cycledecomposition

        .. code-block:: python

            cycle_decomposition = CycleDecomposition(Cycle(1, 3, 4,), Cycle( 5, 2, 6))
            print(cycle_decomposition)
            # (1 3 4)(5 2 6)

You can employ standard syntax to manipulate these objects, designed for utmost intuitiveness.
Here are a few illustrative examples:

.. tab-set::

    .. tab-item:: Permutation
        :sync: permutation

        .. code-block:: python

            if permutation:
                print("The permutation is different from the identity permutation.")
            if permutation == Permutation(1, 2, 3, 4, 5, 6):
                print("The permutation is equal to the identity.")
            if len(permutation) == 6:
                print("The permutation has 6 elements, i.e., it acts on 6 elements.")
            # The permutation is different from the identity.
            # The permutation has 6 elements, i.e., it acts on 6 elements

    .. tab-item:: Cycle
        :sync: cycle

        .. code-block:: python

            if cycle:
                print("The cycle is different from the identity cycle.")
            if permutation == Cycle(1):
                print("The cycle is equal to the identity cycle.")
            if len(cycle) == 6:
                print("The cycle has length 6, i.e., it is a 6-cycle.")
            # The cycle is different from the identity cycle.
            # The cycle has length 6, i.e., it is a 6-cycle.

    .. tab-item:: CycleDecomposition
        :sync: cycledecomposition

        .. code-block:: python

            if cycle_decomposition:
                print("The cycle decomposition is different from the identity permutation.")
            if len(cycle_decomposition) == 6:
                print("The cycle decomposition has length 6, i.e., it is composed by 6 cycles.")
            # The cycle is different from the identity cycle.
            # The cycle decomposition has length 6, i.e., it is composed by 6 cycles.

Many methods for retrieving the properties of the permutation you wish to work with are already available.

.. tab-set::

    .. tab-item:: Permutation
        :sync: permutation

        .. code-block:: python

            permutation.order()  # 4
            permutation.support()  # {2, 3, 4, 5}
            permutation.is_derangement()  # True

    .. tab-item:: Cycle
        :sync: cycle

        .. code-block:: python

            cycle.order() # 6
            cycle.support() # {1, 3, 4, 5, 2, 6}
            cycle.is_derangemenet() # True

    .. tab-item:: CycleDecomposition
        :sync: cycledecomposition

        .. code-block:: python

            cycle_decomposition.order() # 3
            cycle_decomposition.support() # {1, 2, 3, 4, 5, 6}
            cycle_decomposition.is_derangement() # True

You can find more in the API reference section.
