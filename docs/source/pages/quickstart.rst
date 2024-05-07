Quickstart
==========

placeholder

.. tab-set::

    .. tab-item:: Permutation

        .. code-block:: python

            permutation = Permutation(2, 3, 1)
            print(permutation)
            # (2, 3, 1)

    .. tab-item:: Cycle

        .. code-block:: python

            cycle = Cycle(2, 3, 1)
            print(cycle)
            # (2 3 1)

    .. tab-item:: CycleDecomposition

        .. code-block:: python

            cycle_decomposition = CycleDecomposition(Cycle(2, 3, 1), Cycle(4, 5))
            print(cycle_decomposition)
            # (2 3 1)(4 5)

placeholder

.. tab-set::

    .. tab-item:: Permutation

        .. code-block:: python

            permutation = Permutation(1, 3, 4, 5, 2, 6)
            permutation.order()
            # 4

    .. tab-item:: Cycle

        .. code-block:: python

            cycle = Cycle(1, 3, 4, 5, 2, 6)
            cycle.order()
            # 4

    .. tab-item:: CycleDecomposition

        .. code-block:: python

            cycle_decomposition = CycleDecomposition(Cycle(1, 3, 2), Cycle(4, 5))
            cycle_decomposition.order()
            # 6
