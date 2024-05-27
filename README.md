<a href="https://symmetria.readthedocs.io/en/latest/"><img src="./docs/source/_static/symmetria.png" width="200" align="right" /></a>

<span style="font-size:4em;">**Welcome to symmetria**</span>

Symmetria provides an intuitive, thorough, and comprehensive framework for interacting
with the symmetric group and its elements.

- 📦 - installable via pip
- 🐍 - compatible with Python **3.9**, **3.10**, **3.11** and **3.12**
- 👍 - intuitive **API**
- 🧮 - a lot of functionalities already implemented
- ✅ - 100% of test coverage

You can give a look at how to work with symmetria in the section [quickstart](#quickstart),
or you can directly visit the [docs](https://symmetria.readthedocs.io/en/latest/).

An interesting list of all the functionalities implemented by symmetria can be found
[here](https://symmetria.readthedocs.io/en/latest/pages/API_reference/elements/index.html).

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change, and give a look to the
[contribution guidelines](https://github.com/VascoSch92/symmetria/blob/main/CONTRIBUTING.md).

## Installation

Symmetria can be comfortably installed from PyPI using the command

```bash
pip install symmetria
```

or directly from the source GitHub code with

```bash
pip install git+https://github.com/VascoSch92/symmetria@xxx
```

where `xxx` is the name of the branch or the tag you would like to install.

You can check that `symmetria` was successfully installed by typing the command

```bash
symmetria --version
```

## Quickstart

Let's get started with symmetria. First and foremost, we can import the `Permutation`
class from `symmetria`. The Permutation class serves as the fundamental class for
working with elements of the symmetric group, representing permutations as
bijective maps. Additionally, you can utilize the `Cycle` class and `CycleDecomposition`
class to work with cycle permutations and permutations represented as cycle
decompositions, respectively.

```python
from symmetria import Permutation

permutation = Permutation(1, 3, 4, 5, 2, 6)
```

You can now represent your permutation in various formats:

```python
print(permutation)                      # (1, 3, 4, 5, 2, 6)
print(permutation.cycle_notation())     # (1)(2 3 4 5)(6)
print(permutation.one_line_notation())  # 134526
```

Permutations can be compared between them and are easy to manipulate.

```python
if permutation:
    print("The permutation is different from the identity.")
if permutation == Permutation(1, 2, 3, 4, 5, 6):
    print("The permutation is equal to the identity.")
if len(permutation) == 6:
    print("The permutation acts on 6 elements.")
print(permutation * permutation)
```

Furthermore, we can decompose a permutation into its cycle decomposition
(`CycleDecomposition`) and compute its order and support.

```python
permutation.cycle_decomposition()
# returns CycleDecomposition(Cycle(1), Cycle(2, 3, 4, 5), Cycle(6))
permutation.order()  # 4
permutation.support()  # {2, 3, 4, 5}
permutation.is_derangement()  # True
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
