Generators
==========

`Symmetria` provides a way to generate all the permutations of a given degree. The generation follows different
algorithms which can be specified.

.. note:: The permutation are generated following a well-defined pattern, i.e., they are not random.

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

.. _[1]: https://en.wikipedia.org/wiki/Lexicographic_order
.. _[2]: https://academic.oup.com/comjnl/article/6/3/293/360213
.. _[3]: https://en.wikipedia.org/wiki/Steinhaus–Johnson–Trotter_algorithm

.. toctree::
    :maxdepth: 1
    :hidden:

    generate
