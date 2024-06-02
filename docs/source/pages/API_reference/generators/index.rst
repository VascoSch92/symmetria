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
     - here
   * - ``heap``
     - The permutations are generate following the **Heap's algorithm**.
     - here


.. toctree::
    :maxdepth: 1
    :hidden:

    generate
