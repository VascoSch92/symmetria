# Changelog

## Legend

- API_CHANGE: Any changes to the project's API.
- DEPRECATED: Indication of features that will be removed in future releases.
- DOCUMENTATION: Something to do with the documentation.
- ENHANCEMENT: Improvements to existing features that do not introduce new functionality.
- FEATURE: New features added to enhance functionality.
- FIX: Resolved issues, bugs, or unexpected behavior.
- MAINTENANCE: Something which has to do with CI/CD or setup.
- REMOVED: Features or functionalities removed from the project.

## Version Policy

The version is represented by three digits: a.b.c.

- Bump the first digit (a) for an API_CHANGE.
- Bump the second digit (b) for a big new FEATURE or a critical FIX.
- Bump the third digit (c) for a small new FEATURE, an ENHANCEMENT or a small FIX.
- Once a digit is bumped, set all the digits to its right to zero.

## Unreleased

## \[0.3.3\] - 2025-06-22

FEATURE:
- `generators`: add `zaks` generator

MAINTENANCE:
- `.pre-commit-config.yaml`: add `mypy`
- `symmetria.generators`: change API private methods

## \[0.3.2\] - 2025-02-08

MAINTENANCE:
- deprecated symmetria.generator: This function will be deprecated in a future version. Use `permutation_generator` instead
- deprecated symmetria.generators.random.api.random: This function will be deprecated in a future version. Use `random_permutation` instead
- `Makefile`: added `ruff` command.

## \[0.3.1\] - 2024-12-16

FEATURE:
- `symmetria.Permutation`: add `lexicographic_rank` method
- `symmetria.CycleDecomposition`: add `lexicographic_rank` method
- `symmetria.Permutation`: add `lehmer_code` method
- `symmetria.CycleDecomposition`: add `lehmer_code` method

FIX:
- `symmetria.Permutation`: fix small typos in class methods

## \[0.3.0\] - 2024-07-15

FEATURE:
- `symmetria.Permutation`: add `degree` method
- `symmetria.CyclePermutation`: add `degree` method
- `symmetria.Cycle`: add `degree` method
- `symmetria.random`: add random module to create random permutations

ENHANCEMENT:
- `symmetria.Permutation`: change how the sign is computed
- `symmetria.Permutation`: add `__new__` method to the class
- `symmetria.CyclePermutation`: add `__new__` method to the class
- `symmetria.Cycle`: add `__new__` method to the class

## \[0.2.0\] - 2024-06-12

FEATURE:
- `cli`: add (minimal) command line interface

DOCUMENTATION:
- add documentation for command line interface

## \[0.1.1\] - 2024-06-10

FEATURE:
- `symmetria.Permutation`: add `describe` method
- `symmetria.CyclePermutation`: add `describe` method
- `symmetria.Cycle`: add `describe` method


## \[0.1.0\] - 2024-06-05

DEPRECATED:
- `symmetria.Cycle`: delete method `__pow__` as was not consistent
- `symmetria.Cycle`: delete `NotImplementedError` for `is_regular` and `is_conjugate`
- `symmetria.CycleDecomposition`: delete `NotImplementedError` for `__int__`  

DOCUMENTATION:
- `README.md`: improve section quickstart
- `quickstart.rst`: improve examples

FEATURE:
- `generators`: add structure to generate permutations
- `generators`: add `lexicographic` generator
- `generators`: add generator following `Heap`'s algorithm
- `generators`: add generator following `Steinhaus-Johnson-Trotter`'s algorithm


## \[0.0.5\] - 2024-06-01

FEATURE:
- `symmetria.Permutation`: add `ascents` method
- `symmetria.CyclePermutation`: add `ascents` method
- `symmetria.Permutation`: add `descents` method
- `symmetria.CyclePermutation`: add `descents` method
- `symmetria.Permutation`: add `exceedances` method
- `symmetria.CyclePermutation`: add `exceedances` method
- `symmetria.Permutation`: add `records` method
- `symmetria.CyclePermutation`: add `records` method

MAINTENANCE:
- `tests`: Refactor. Now the code is more concise, and it is easier to add a new test.
- `symmetria.elements._base.py`: Simplify the base class for elements object.

## \[0.0.4\] - 2024-05-28

FEATURE:

- `symmetria.Permutation`: add `is_regular` method
- `symmetria.Cycle`: add `is_regular` method
- `symmetria.CyclePermutation`: add `is_regular` method
- `symmetria.Permutation`: add `inversions` method
- `symmetria.Cycle`: add `inversions` method
- `symmetria.CyclePermutation`: add `inversions` method
- `symmetria.Permutation`: add `image` property
- `symmetria.Permutation`: add `__pow__` method
- `symmetria.Cycle`: add `__pow__` method
- `symmetria.CyclePermutation`: add `__pow__` method


## \[0.0.3\] - 2024-05-25

FEATURE:

- `symmetria.Permutation`: add `is_conjugate` method
- `symmetria.Cycle`: add `is_conjugate` method
- `symmetria.CyclePermutation`: add `is_conjugate` method


## \[0.0.2\] - 2024-05-24

FEATURE:

- `symmetria.Permutation`: add `sgn` method
- `symmetria.Cycle`: add `sgn` method
- `symmetria.CyclePermutation`: add `sgn` method
- `symmetria.Permutation`: add `inverse` method
- `symmetria.Cycle`: add `inverse` method
- `symmetria.CyclePermutation`: add `inverse` method
- `symmetria.Permutation`: add `is_even` and `is_odd` methods
- `symmetria.Cycle`: add `is_even` and `is_odd` methods
- `symmetria.CyclePermutation`: add `is_even` and `is_odd` methods
- `symmetria.Permutation`: add `cycle_type` method
- `symmetria.Cycle`: add `cycle_type` method
- `symmetria.CyclePermutation`: add `cycle_type` method

MAINTENANCE:

- `tests.tests_meta.test_order.py`: add test suite for order of methods
- `docs._static.symmetria.png`: logo for symmetria
- `.github.workflows.tests`: add doctest


## \[0.0.1\] - 2024-05-16

MAINTENANCE:

- `.github`: add workflows `tests.yml`, `code-style.yml`, `release.yml` and `check-pr-title.yml`
- `.github.pull_request_template.md`: add pull request template
- `.github.ISSUE_TEMPLATE`: add templates for issues
- `tests`: in module tests we import as in the API
- `.pre-commit-config.yml`: add `check-toml` and `name-tests-test`
- `docs`: first version of the docs implemented

## \[0.0.0\] - 2024-05-01

🎉🚀 First version of `symmetria` 🚀🎉
