# Contribute

If you would like to contribute to the project, please take a moment to read the following points.

1. Checks if there is an [issue](https://github.com/VascoSch92/symmetria/issues) where the contribution
   you had in mind is already discussed.
   If it is not the case, open a new [issue](https://github.com/VascoSch92/symmetria/issues).
   you would like to contribute but are unsure what to work on, take a look at the
   [issue](https://github.com/VascoSch92/symmetria/issues) section.
   There are plenty of ideas we would like to implement here.

1. Time to code. Once you have finished coding your implementation, open a pull-request (PR) to the `main` branch.
   Note that the PR title should start with one of the following (included parentheses):

   - \[API_CHANGE\]: If there is a change to the project's API.
   - \[DEPRECATED\]: If the PR deprecate some functionalities.
   - \[DOC\]: If the PR improves the documentation.
   - \[ENHANCEMENT\]: if the PR improve and existing functionality.
   - \[FEATURE\]: if the PR add a new feature.
   - \[FIX\]: If the PR solve issues, bugs, or unexpected behavior.
   - \[MAINTENANCE\]: If the PR has to do with CI/CD or setup.
   - \[RELEASE\]: If the PR is a preparation for a release.

   An example is

   ```text
   [FEATURE] Add method AAA to class BBB
   ```

1. However, before opening a PR, it is a good practice to have pre-commit installed.
   To use the pre-commit hook, you first need to install `pre-commit` using the command:

   ```bash
   pip install pre-commit
   pre-commit --version
   ```

   and then install it into your git hooks using:

   ```bash
   pre-commit install
   ```

   You can also run the pre-commit locally by running the following command
   from the project's working directory:

   ```bash
   pre-commit run --all-files
   ```

1. Now your PR is ready for review!

Thanks for your contribution ❤️
