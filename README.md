<a href="https://symmetria.readthedocs.io/en/latest/"><img src="./docs/source/_static/symmetria.png" width="200" align="right" /></a>

## **Welcome to symmetria**

Symmetria provides an intuitive, thorough, and comprehensive framework for interacting
with the symmetric group and its elements.

- 📦 - installable via pip
- 🐍 - compatible with Python **3.9**, **3.10**, **3.11** and **3.12**
- 👍 - intuitive **API**
- 🧮 - a lot of functionalities already implemented
- ✅ - 100% of test coverage

You can give a look at how to work with symmetria in the section [quickstart](#quickstart),
or you can directly visit the [docs](https://symmetria.readthedocs.io/en/latest/).

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change, and give a look to the
[contribution guidelines](https://github.com/VascoSch92/symmetria/blob/main/CONTRIBUTING.md).

---

- [Installation](#installation)
- [Quickstart](#quickstart)
- [Command Line Interface](#command-line-interface)
- [Overview](#overview)

---
## Installation

Symmetria can be comfortably installed from PyPI using the command

```text
$ pip install symmetria
```

or directly from the source GitHub code with

```text
$ pip install git+https://github.com/VascoSch92/symmetria@xxx
```

where `xxx` is the name of the branch or the tag you would like to install.

You can check that `symmetria` was successfully installed by typing the command

```text
$ symmetria --version
```

## Quickstart

Let's get started with symmetria. First and foremost, we can import the `Permutation`
class from `symmetria`. The Permutation class serves as the fundamental class for
working with elements of the symmetric group, representing permutations as
bijective maps. Otherwise, you can utilize the `Cycle` class and `CycleDecomposition`
class to work with cycle permutations and permutations represented as cycle
decompositions, respectively.

Let's start by defining a permutation and exploring how we can represent it in various formats.

```python
from symmetria import Permutation

permutation = Permutation(1, 3, 4, 5, 2, 6)

permutation                         # Permutation(1, 3, 4, 5, 2, 6)
str(permutation)                    # (1, 3, 4, 5, 2, 6)
permutation.cycle_notation()        # (1)(2 3 4 5)(6)
permutation.one_line_notation()     # 134526
```

Permutation objects are easy to manipulate. They implement nearly every standard functionality of basic Python objects. 
As a rule of thumb, if something seems intuitively possible, you can probably do it.

```python
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
```

Basic arithmetic operations are implemented.

```python
from symmetria import Permutation

permutation = Permutation(3, 1, 4, 2)

multiplication = permutation * permutation      # Permutation(4, 3, 2, 1)
power = permutation ** 2                        # Permutation(4, 3, 2, 1)
inverse = permutation ** -1                     # Permutation(2, 4, 1, 3)
identity = permutation * inverse                # Permutation(1, 2, 3, 4)
```

Actions on different objects are also implemented.

```python
from symmetria import Permutation

permutation = Permutation(3, 2, 4, 1)

permutation(3)                                # 4
permutation("abcd")                           # 'dbac'
permutation(["I", "love", "Python", "!"])     # ['!', 'love', 'I', 'Python']
```

Moreover, many methods are already implemented. If what you are looking for is not available, 
let us know as soon as possible.

```python
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
```

If you can't decide what you want, just print everything

```python
from symmetria import Permutation

print(Permutation(3, 2, 4, 1).describe())
```

in a nice formatted table:

```text
+----------------------------------------------------------------------------+
|                          Permutation(3, 2, 4, 1)                           |
+----------------------------------------------------------------------------+
| order                                |                  3                  |
+--------------------------------------+-------------------------------------+
| degree                               |                  4                  |
+--------------------------------------+-------------------------------------+
| is derangement                       |                False                |
+--------------------------------------+-------------------------------------+
| inverse                              |            (4, 2, 1, 3)             |
+--------------------------------------+-------------------------------------+
| parity                               |              +1 (even)              |
+--------------------------------------+-------------------------------------+
| cycle notation                       |             (1 3 4)(2)              |
+--------------------------------------+-------------------------------------+
| cycle type                           |               (1, 3)                |
+--------------------------------------+-------------------------------------+
| inversions                           |  [(1, 2), (1, 4), (2, 4), (3, 4)]   |
+--------------------------------------+-------------------------------------+
| ascents                              |                 [2]                 |
+--------------------------------------+-------------------------------------+
| descents                             |               [1, 3]                |
+--------------------------------------+-------------------------------------+
| excedencees                          |               [1, 3]                |
+--------------------------------------+-------------------------------------+
| records                              |               [1, 3]                |
+--------------------------------------+-------------------------------------+
```

Click [here](https://symmetria.readthedocs.io/en/latest/pages/API_reference/elements/index.html) for an overview of 
all the functionalities implemented in `symmetria`.


## Command Line Interface
Symmetria also provides a simple command line interface to find all what you need just with a line.

```text
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
```

Check it out.

```text
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
```


## Overview

| **Statistics**    | ![Static Badge](https://img.shields.io/badge/symmetria-blue?style=for-the-badge)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Repository**    | ![GitHub Repo stars](https://img.shields.io/github/stars/VascoSch92/symmetria)  ![GitHub forks](https://img.shields.io/github/forks/VascoSch92/symmetria) ![GitHub watchers](https://img.shields.io/github/watchers/VascoSch92/symmetria)                                                                                                                                                                                                                                                                                                                                                                                                     |
| **Size**          | ![GitHub repo file or directory count](https://img.shields.io/github/directory-file-count/VascoSch92/symmetria) ![GitHub repo size](https://img.shields.io/github/repo-size/VascoSch92/symmetria)                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **Issues**        | ![GitHub Issues or Pull Requests](https://img.shields.io/github/issues/VascoSch92/symmetria?logo=GitHub&color=yellow) ![GitHub Issues or Pull Requests](https://img.shields.io/github/issues-closed/VascoSch92/symmetria?logo=GitHub&color=green)                                                                                                                                                                                                                                                                                                                                                                                             |
| **Pull Requests** | ![GitHub Issues or Pull Requests](https://img.shields.io/github/issues-pr/VascoSch92/symmetria?logo=GitHub&color=yellow) ![GitHub Issues or Pull Requests](https://img.shields.io/github/issues-pr-closed/VascoSch92/symmetria?logo=GitHub&color=green)                                                                                                                                                                                                                                                                                                                                                                                       |                                           
| **Open Source**   | [![MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/VascSch92/symmetria/blob/main/LICENSE) [![MIT](https://img.shields.io/badge/Contributing-😃-blue.svg)](https://github.com/VascSch92/symmetria/blob/main/CONTRIBUTING.md) [![MIT](https://img.shields.io/badge/Code_of_conduct-⚖️-blue.svg)](https://github.com/VascSch92/symmetria/blob/main/CODE_OF_CONDUCT.md)                                                                                                                                                                                                                                               |
| **DOCS**          | ![Read the Docs](https://img.shields.io/readthedocs/symmetria?logo=readthedocs)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                                                                                                                                    
| **CI/CD**         | ![tests](https://github.com/VascoSch92/symmetria/actions/workflows/tests.yml/badge.svg) ![tests](https://github.com/VascoSch92/symmetria/actions/workflows/code-style.yml/badge.svg) ![tests](https://github.com/VascoSch92/symmetria/actions/workflows/release.yml/badge.svg)                                                                                                                                                                                                                                                                                                                                                                |
| **Code**          | [![!pypi](https://img.shields.io/pypi/v/symmetria?color=orange)](https://pypi.org/project/symmetria/) [![!python-versions](https://img.shields.io/pypi/pyversions/symmetria)](https://www.python.org/) [![!black](https://img.shields.io/badge/code%20style-ruff-8A2BE2.svg)](https://github.com/astral-sh/ruff)                                                                                                                                                                                                                                                                                                                              |
| **Downloads**     | [![Downloads](https://static.pepy.tech/personalized-badge/symmetria?period=week&units=international_system&left_color=grey&right_color=blue&left_text=weekly%20(pypi))](https://pepy.tech/project/symmetria) [![Downloads](https://static.pepy.tech/personalized-badge/symmetria?period=month&units=international_system&left_color=grey&right_color=blue&left_text=monthly%20(pypi))](https://pepy.tech/project/symmetria) [![Downloads](https://static.pepy.tech/personalized-badge/symmetria?period=total&units=international_system&left_color=grey&right_color=blue&left_text=cumulative%20(pypi))](https://pepy.tech/project/symmetria) |
