.. symmetria documentation master file, created by
   sphinx-quickstart on Tue Apr 30 19:40:58 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to symmetria's documentation!
=====================================

`Symmetria` provides an intuitive, thorough, and comprehensive framework for interacting
with the symmetric group and its elements.

- 📦 - installable via **pip**
- 🐍 - compatible with Python **3.9**, **3.10**, **3.11** and **3.12**
- 👍 - intuitive API
- 🧮 - a lot of functionalities already implemented
- ✅ - 100% tested


.. grid:: 1 2 1 2
    :margin: 5 5 0 0
    :padding: 0 0 0 0
    :gutter: 4

    .. grid-item-card:: :octicon:`info` Getting started
        :text-align: center
        :class-title: sd-fs-5
        :class-card: sd-p-3

        First time working with `symmetria`?

        .. button-ref:: pages/getting_started/installation
            :ref-type: doc
            :click-parent:
            :color: primary
            :outline:
            :expand:

            Start here

    .. grid-item-card:: :octicon:`light-bulb` Want to contribute?
        :text-align: center
        :class-title: sd-fs-5
        :class-card: sd-p-3

        Pull requests are welcome.

        .. button-link:: https://github.com/VascoSch92/symmetria/issues
            :click-parent:
            :color: primary
            :outline:
            :expand:

            Join the conversation :octicon:`link-external`

    .. grid-item-card:: :octicon:`sync` Elements
        :text-align: center
        :class-title: sd-fs-5
        :class-card: sd-p-3

        All about elements of the symmetric group

        .. button-ref:: pages/API_reference/elements/index
            :ref-type: doc
            :color: primary
            :outline:
            :click-parent:
            :expand:

            API Reference

    .. grid-item-card:: :octicon:`package` Groups
        :text-align: center
        :class-title: sd-fs-5
        :class-card: sd-p-3

        All about permutation groups

        .. button-ref:: pages/API_reference/groups/index
            :ref-type: doc
            :color: primary
            :outline:
            :click-parent:
            :expand:

            API reference



.. warning:: The documentations is still a working in progress.
   If you find an error or you think something could have be made better,
   feel free to open a PR to correct it.


.. toctree::
   :maxdepth: 1
   :caption: Getting started
   :hidden:

   pages/getting_started/installation
   pages/getting_started/quickstart


.. toctree::
   :maxdepth: 2
   :caption: API references
   :hidden:

   pages/API_reference/elements/index
   pages/API_reference/groups/index
   pages/API_reference/generators/index

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: Community

   pages/community/contributing.md
   pages/community/changelog.md
   pages/community/license
   pages/community/code_of_conduct.md

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: Links

   Symmetria on GitHub <https://github.com/VascoSch92/symmetria>
   Symmetria on PyPI <https://pypi.org/project/symmetria/>
   Symmetria on PePy <https://www.pepy.tech/projects/symmetria>

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
