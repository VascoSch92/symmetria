Generate
=====================

To use the generator of permutation, import it as

.. code-block:: python

    import symmetria
    ...
    permutations = symmetria.generate(algorithm="lexicographic", degree=3)


The API of the method is given as following:

.. automodule:: symmetria
   :members: generate
   :exclude-members: Cycle, CycleDecomposition, Permutation