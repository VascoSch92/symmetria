Command Line Interface
======================

Symmetria also provides a simple command line interface to find all what you need just with a line.

.. code-block:: text

    $ symmetria 132

    +------------------------------------------------------+
    |                 Permutation(1, 3, 2)                 |
    +------------------------------------------------------+
    | order                     |            2             |
    +---------------------------+--------------------------+
    | degree                    |            3             |
    +---------------------------+--------------------------+
    | is derangement            |          False           |
    +---------------------------+--------------------------+
    | inverse                   |        (1, 3, 2)         |
    +---------------------------+--------------------------+
    | parity                    |         -1 (odd)         |
    +---------------------------+--------------------------+
    | cycle notation            |         (1)(2 3)         |
    +---------------------------+--------------------------+
    | cycle type                |          (1, 2)          |
    +---------------------------+--------------------------+
    | inversions                |         [(2, 3)]         |
    +---------------------------+--------------------------+
    | ascents                   |           [1]            |
    +---------------------------+--------------------------+
    | descents                  |           [2]            |
    +---------------------------+--------------------------+
    | excedencees               |           [2]            |
    +---------------------------+--------------------------+
    | records                   |          [1, 2]          |
    +---------------------------+--------------------------+

Check it out.

.. code-block:: text

    $ symmetria --help

    Symmetria, an intuitive framework for working with the symmetric group and its elements.


    Usage: symmetria <ARGUMENT> [OPTIONS]

    Options:
     -h, --help        Print help
     -v, --version     Print version

    Argument (optional):
     permutation       A permutation you want to learn more about.
                       The permutation must be given in its one-line format, i.e.,
                       for the permutation Permutation(2, 3, 1), write 231.