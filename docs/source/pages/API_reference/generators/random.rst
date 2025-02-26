Random Generation
=================

`Symmetria` provides a way to generate random permutation.

You can use the random generation of permutations in the following way

.. code-block:: python

    import symmetria

    permutations = symmetria.random_generator(algorithm="lexicographic", degree=3)

If you don't want to have a generator and you want to just have a singular random permutation
you can use write

.. code-block:: python

    import symmetria

    permutation = symmetria.random(algorithm="lexicographic", degree=3)


A list of implemented algorithms to generate permutations:

.. list-table:: overview
   :widths: 35 50 15
   :header-rows: 1

   * - Algorithm
     - Description
     - Reference
   * - ``random``
     - A permutation is generated by choosing the integer uniformly.
     -
   * - ``fisher-yates``
     - The permutations are generate following the **Steinhaus-Johnson-Trotter algorithm**.
     - `[1]`_

.. _[1]: https://en.wikipedia.org/wiki/Lexicographic_order

====

The API of the method is given as following:

.. automodule:: symmetria.generators.random.api
   :members: random_generator
   :exclude-members: random