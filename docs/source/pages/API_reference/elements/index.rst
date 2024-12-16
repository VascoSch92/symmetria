Elements
========

The symmetric group boasts a multitude of elements, precisely :math:`n!`, where :math:`n` is
the number of elements on which the group operates.
These elements can be represented in various forms, such as permutations, cycles, or cycle decompositions.

Symmetria furnishes three distinct classes – ``Permutation``, ``Cycle``, and ``CycleDecomposition`` –
to represent an element within the symmetric group in different way. Up to you to pick the representation which
fit at best your needs.

.. note::
    The class ``Permutation`` is, in some sense, the basic class to represent a permutation. It is raccomanded to work
    with it if you don't have specific needs to have cycles or cycles decomposition of permutations.

The following table summarize the functionalities provided by each class.
Here, **P** denotes the class ``Permutation``, **C** the class ``Cycle``, and **CD** the class ``CycleDecomposition``.

.. list-table:: overview
   :widths: 35 35 10 10 10
   :header-rows: 1

   * - Feature
     - Description
     - **P**
     - **C**
     - **CD**
   * - ``__call__``
     - Call the permutation on an object
     - ✅
     - ✅
     - ✅
   * - ``__mul__``
     - Multiplication (composition) between permutations
     - ✅
     - ❌
     - ✅
   * - ``__pow__``
     - Power of a permutation
     - ✅
     - ❌
     - ✅
   * - ``ascents``
     - Return the positions of the permutation ascents
     - ✅
     - ❌
     - ✅
   * - ``cycle_decomposition``
     - Cycle decomposition of the permutation
     - ✅
     - ✅
     - ✅
   * - ``cycle_type``
     - Return the cycle type of the permutation
     - ✅
     - ❌
     - ✅
   * - ``cycle_notation``
     - Return the cycle notation of the permutation
     - ✅
     - ✅
     - ✅
   * - ``degree``
     - Return the degree of the permutation
     - ✅
     - ✅
     - ✅
   * - ``descents``
     - Return the positions of the permutation descents
     - ✅
     - ❌
     - ✅
   * - ``describe``
     - Return a table describing the permutation
     - ✅
     - ✅
     - ✅
   * - ``exceedances``
     - Return the positions of the permutation exceedances
     - ✅
     - ❌
     - ✅
   * - ``inverse``
     - Compute the inverse of the permutation
     - ✅
     - ✅
     - ✅
   * - ``inversions``
     - Return the inversions of the permutation
     - ✅
     - ✅
     - ✅
   * - ``is_conjugate``
     - Check if two permutations are conjugate
     - ✅
     - ❌
     - ✅
   * - ``is_derangement``
     - Check if the permutation is a derangement
     - ✅
     - ✅
     - ✅
   * - ``is_even``
     - Check if the permutation is even
     - ✅
     - ✅
     - ✅
   * - ``is_odd``
     - Check if the permutation is odd
     - ✅
     - ✅
     - ✅
   * - ``is_regular``
     - Check if the permutation is regular
     - ✅
     - ❌
     - ✅
   * - ``lehmer_code``
     - Return the Lehmer code of the permutation
     - ✅
     - ❌
     - ✅
   * - ``lexicographic_rank``
     - Return the lexicographic rank of the permutation
     - ✅
     - ❌
     - ✅
   * - ``map``
     - Return the map defining the permutation
     - ✅
     - ✅
     - ✅
   * - ``one_line_notation``
     - Return the one line notation of the permutation
     - ✅
     - ❌
     - ❌
   * - ``orbit``
     - Compute image of a given element under the permutation
     - ✅
     - ✅
     - ✅
   * - ``order``
     - Return the order of the permutation
     - ✅
     - ✅
     - ✅
   * - ``records``
     - Return the positions of the permutation records
     - ✅
     - ❌
     - ✅
   * - ``sgn``
     - Return the sign of the permutation
     - ✅
     - ✅
     - ✅
   * - ``support``
     - Return the support of the permutation
     - ✅
     - ✅
     - ✅




.. toctree::
    :maxdepth: 1
    :hidden:

    permutation
    cycle
    cycle_decomposition
