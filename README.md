# Welcome to symmetria

______________________________________________________________________

Symmetria provides an intuitive, thorough, and comprehensive framework for interacting
with the symmetric group and its elements.

- 📦 - installable via pip
- 🐍 - compatible with Python **3.9**, **3.10**, **3.11** and **3.12**
- 👍 - intuitive API
- 🔢 - mathematically corrected
- ✅ - 100% of test coverage

You can give a look at how to work with symmetria in the section [quickstart](#quickstart),
or you can check (almost) all the functionality implemented
[here](#list-of-implemented-functionality).

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
print(permutation.one_line_notation()   # 134526
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
permuttation.cycle_decomposition()
# returns CycleDecomposition(Cycle(1), Cycle(2, 3, 4, 5), Cycle(6))
permutation.order()  # 4
permutation.support()  # {2, 3, 4, 5}
permutation.is_derangement()  # True
```

## List of implemented functionality

A list of (some) of the functionality implemented for the various classes representing permutation.
Here, `P` is for `Permutation`, `C`for `Cycle`, and `CD` for `CycleDecomposition`.

| Feature               | Description                                            | P   | C   | CD  |
| --------------------- |--------------------------------------------------------| --- | --- | --- |
| `__call__`            | Call a permutation on an object                        | ✅   | ✅   | ✅   |
| `__mul__`             | Multiplication (composition) between permutations      | ✅   | ❌   | ✅   |
| `cycle_decomposition` | Cycle decomposition of the permutation                 | ✅   | ✅   | ✅   |
| `cycle_notation`      | Return the cycle notation of the permutation           | ✅   | ✅   | ✅   |
| `is_derangement`      | Check if the permutation is a derangement              | ✅   | ✅   | ✅   |
| `map`                 | Return the map defining the permutation                | ✅   | ✅   | ✅   |
| `one_line_notation`   | Return the one line notation of the permutation        | ✅   | ❌   | ❌   |
| `support`             | Return the support of the permutation                  | ✅   | ✅   | ✅   |
| `orbit`               | Compute image of a given element under the permutation | ✅   | ✅   | ✅   |
| `order`               | Return the order of the permutation                    | ✅   | ✅   | ✅   |
