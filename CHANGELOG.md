# Changelog

## Legend

- API_CHANGE: Any changes to the project's API
- DEPRECATED: Indication of features that will be removed in future releases
- ENHANCEMENT: Improvements to existing features that do not introduce new functionality
- FEATURE: New features added to enhance functionality
- FIX: Resolved issues, bugs, or unexpected behavior
- REMOVED: Features or functionalities removed from the project

## Version Policy

The version is represented by three digits: a.b.c.

- Bump the first digit (a) for an API_CHANGE.
- Bump the second digit (b) for a FEATURE or a critical FIX.
- Bump the third digit (c) for an ENHANCEMENT or a small FIX.
- Once a digit is bumped, set all the digits to its right to zero.

## Unreleased


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
