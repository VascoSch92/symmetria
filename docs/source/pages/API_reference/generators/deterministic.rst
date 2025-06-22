Deterministic Generation
========================

`Symmetria` provides a way to generate all the permutations of a given degree. The generation follows different
algorithms which can be specified.

You can use the generator of permutations in the following way

.. code-block:: python

    import symmetria

    permutations = symmetria.generate(algorithm="lexicographic", degree=3)

A list of implemented algorithms to generate permutations:

.. list-table:: overview
   :widths: 35 50 15
   :header-rows: 1

   * - Algorithm
     - Description
     - Reference
   * - ``lexicographic``
     - The permutations are generate following the **lexicographic order**.
     - `[1]`_
   * - ``heap``
     - The permutations are generate following the **Heap's algorithm**.
     - `[2]`_
   * - ``steinhaus-johnson-trotter``
     - The permutations are generate following the **Steinhaus-Johnson-Trotter algorithm**.
     - `[3]`_
   * - ``zaks``
     - The permutations are generate following the **Zaks algorithm**.
     - `[4]`_

.. _[1]: https://en.wikipedia.org/wiki/Lexicographic_order
.. _[2]: https://academic.oup.com/comjnl/article/6/3/293/360213
.. _[3]: https://en.wikipedia.org/wiki/Steinhaus–Johnson–Trotter_algorithm
.. _[4]: https://www.academia.edu/95743174/A_new_algorithm_for_generation_of_permutations

====

The API of the method is given as following:

.. automodule:: symmetria.generators.algorithm.api
   :members: generate
   :exclude-members: random, random_generator
