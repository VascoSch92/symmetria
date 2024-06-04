Quickstart
==========

Symmetria offers three classes for representing permutations: ``Permutation``, ``Cycle``, and ``CycleDecomposition``.
Each of these classes has its own set of advantages and disadvantages depending on the specific goal you want to
achieve.

Below is a brief example showcasing the capabilities of every of the aforementioned classes.

Let's start by defining a permutation and exploring how we can represent it in various formats.

.. tab-set::

    .. tab-item:: Permutation
        :sync: permutation

        .. code-block:: python

            from symmetria import Permutation

            permutation = Permutation(1, 3, 4, 5, 2, 6)

            permutation                         # Permutation(1, 3, 4, 5, 2, 6)
            str(permutation)                    # (1, 3, 4, 5, 2, 6)
            permutation.cycle_notation()        # (1)(2 3 4 5)(6)
            permutation.one_line_notation()     # 134526

    .. tab-item:: Cycle
        :sync: cycle

        .. code-block:: python

            from symmetria import Cycle

            cycle = Cycle(1, 3, 4, 5, 2, 6)

            cycle                       # Cycle(1, 3, 4, 5, 2, 6)
            cycle.cycle_notation()      # (1 3 4 5 2 6)
            str(cycle)                  # (1 3 4 5 2 6)
            int(cycle)                  # 134526

    .. tab-item:: CycleDecomposition
        :sync: cycledecomposition

        .. code-block:: python

            from symmetria import Cycle, CycleDecomposition

            cd = CycleDecomposition(Cycle(1, 2), Cycle(3, 4))

            cd                     # CycleDecomposition(Cycle(1, 2), Cycle(3, 4))
            cd.cycle_notation()    # (1 2)(3 4)
            str(cd)                # (1 2)(3 4)
            cd[0], cd[1]           # Cycle(1, 2), Cycle(3, 4)


Permutation objects are easy to manipulate. They implement nearly every standard functionality of basic Python objects.
As a rule of thumb, if something seems intuitively possible, you can probably do it.

.. tab-set::

    .. tab-item:: Permutation
        :sync: permutation

        .. code-block:: python

            from symmetria import Permutation

            idx = Permutation(1, 2, 3)
            permutation = Permutation(1, 3, 2)

            if permutation:
                print(f"The permutation {permutation} is not the identity.")
            if idx == Permutation(1, 2, 3):
                print(f"The permutation {idx} is the identity permutation.")
            if  permutation != idx:
                print(f"The permutations {permutation} and {idx} are different.")

            # The permutation (1, 3, 2) is not the identity.
            # The permutation (1, 2, 3) is the identity permutation.
            # The permutations (1, 3, 2) and (1, 2, 3) are different.

    .. tab-item:: Cycle
        :sync: cycle

        .. code-block:: python

            from symmetria import Cycle

            idx = Cycle(1)
            cycle = Cycle(1, 3, 2)

            if cycle:
                print(f"The cycle {cycle} is not the identity.")
            if idx == Cycle(1):
                print(f"The cycle {idx} is the identity cycle.")
            if  cycle != idx:
                print(f"The cycles {cycle} and {idx} are different.")

            # The cycle (1 3 2) is not the identity.
            # The cycle (1 2 3) is the identity permutation.
            # The cycles (1 3 2) and (1 2 3) are different.

    .. tab-item:: CycleDecomposition
        :sync: cycledecomposition

        .. code-block:: python

            from symmetria import Cycle, CycleDecomposition

            idx = CycleDecomposition(Cycle(1), Cycle(2), Cycle(3))
            cd = CycleDecomposition(Cycle(1, 2), Cycle(3))

            if cd:
                print(f"The cycle decomposition {cd} is not the identity.")
            if idx == CycleDecomposition(Cycle(1), Cycle(2), Cycle(3)):
                print(f"The cycle decomposition {cd} is the identity.")
            if  cd != idx:
                print(f"The cycle decompositions {cd} and {idx} are different.")

            # The cycle decomposition (1 2)(3) is not the identity.
            # The cycle decomposition (1)(2)(3) is the identity.
            # The cycle decompositions (1 2)(3) and (1)(2)(3) are different.


Basic arithmetic operations are implemented.

.. tab-set::

    .. tab-item:: Permutation
        :sync: permutation

        .. code-block:: python

            from symmetria import Permutation

            permutation = Permutation(3, 1, 4, 2)

            multiplication = permutation * permutation   # Permutation(4, 3, 2, 1)
            power = permutation ** 2                     # Permutation(4, 3, 2, 1)
            inverse = permutation ** -1                  # Permutation(2, 4, 1, 3)
            identity = permutation * inverse             # Permutation(1, 2, 3, 4)

    .. tab-item:: CycleDecomposition
        :sync: cycledecomposition

        .. code-block:: python

            from symmetria import Cycle, CycleDecomposition

            cd = CycleDecomposition(Cycle(1, 4, 2), Cycle(3))

            multiplication = cd * cd # CycleDecomposition(Cycle(1, 2, 4), Cycle(3))
            power = cd ** 2          # CycleDecomposition(Cycle(1, 2, 4), Cycle(3))
            inverse = cd ** -1       # CycleDecomposition(Cycle(2, 4, 1), Cycle(3))
            identity = cd * inverse  # CycleDecomposition(Cycle(1), Cycle(2), Cycle(3), Cycle(4))

Actions on different objects are also implemented.

.. tab-set::

    .. tab-item:: Permutation
        :sync: permutation

        .. code-block:: python

            from symmetria import Permutation

            permutation = Permutation(3, 2, 4, 1)

            permutation(3)                                # 4
            permutation("abcd")                           # 'dbac'
            permutation(["I", "love", "Python", "!"])     # ['!', 'love', 'I', 'Python']

    .. tab-item:: Cycle
        :sync: cycle

        .. code-block:: python

            from symmetria import Cycle

            cycle = Cycle(1, 3, 4, 2)

            cycle(3)                                # 4
            cycle("abcd")                           # 'bdac'
            cycle(["I", "love", "Python", "!"])     # ['love', '!', 'I', 'Python']

    .. tab-item:: CycleDecomposition
        :sync: cycledecomposition

        .. code-block:: python

            from symmetria import Cycle, CycleDecomposition

            cd = CycleDecomposition(Cycle(1, 3), Cycle(2, 4))

            cd(3)                               # 1
            cd("abcd")                          # 'cdab'
            cd(["I", "love", "Python", "!"])    # ['Python', '!', 'I', 'love']

Moreover, many methods are already implemented. If what you are looking for is not available,
let us know as soon as possible.

.. tab-set::

    .. tab-item:: Permutation
        :sync: permutation

        .. code-block:: python

            from symmetria import Permutation

            permutation = Permutation(3, 2, 4, 1)

            permutation.order()                 # 3
            permutation.support()               # {1, 3, 4}
            permutation.sgn()                   # 1
            permutation.cycle_decomposition()   # CycleDecomposition(Cycle(1, 3, 4), Cycle(2))
            permutation.cycle_type()            # (1, 3)
            permutation.is_derangement()        # False
            permutation.is_regular()            # False
            permutation.inversions()            # [(1, 2), (1, 4), (2, 4), (3, 4)]
            permutation.ascents()               # [2]
            permutation.descents()              # [1, 3]

    .. tab-item:: Cycle
        :sync: cycle

        .. code-block:: python

            from symmetria import Cycle

            cycle = Cycle(2, 3, 5, 7, 6)

            cycle.order()                   # 5
            cycle.support()                 # {2, 3, 5, 7, 6}
            cycle.sgn()                     # 1
            cycle.cycle_decomposition()     # CycleDecomposition(Cycle(1), Cycle(2, 3, 5, 7, 6), Cycle(4))
            cycle.is_derangement()          # True
            cycle.inversions()              # [(4, 5)]

    .. tab-item:: CycleDecomposition
        :sync: cycledecomposition

        .. code-block:: python

            from symmetria import Cycle, CycleDecomposition

            cd = CycleDecomposition(Cycle(1, 3), Cycle(2, 4))

            cd.order()                 # 2
            cd.support()               # {1, 2, 3, 4}
            cd.sgn()                   # 1
            cd.is_even()               # True
            cd.cycle_type()            # (2, 2)
            cd.is_derangement()        # True
            cd.is_regular()            # True
            cd.inversions()            # [(1, 3), (1, 4), (2, 3), (2, 4)]
            cd.ascents()               # [1, 3]
            cd.descents()              # [2]

Click [here](https://symmetria.readthedocs.io/en/latest/pages/API_reference/elements/index.html) for an overview of
all the functionalities implemented in `symmetria`.
