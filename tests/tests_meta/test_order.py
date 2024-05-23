import ast
from typing import List
from pathlib import Path

import pytest


class OrderTestSuite:
    """Base class to test the order of methods in the script `SCRIPT_PATH`.

    The order of the methods must match the following:
        1. The __init__ method.
        2. All magic methods in alphabetically order.
        3. ALl other methods in alphabetically order.
    """

    SCRIPT_PATH: str

    @pytest.fixture
    def script_methods(self) -> List:
        """Retrieve all the method in the given script. It assumes that there is just one class in the script."""
        target = Path(self.SCRIPT_PATH).read_text()
        module = ast.parse(target)

        for leaf in module.body:
            if isinstance(leaf, ast.ClassDef):
                return [item.name for item in leaf.body if isinstance(item, ast.FunctionDef)]

    @staticmethod
    def test_init_first_method(script_methods) -> None:
        if "__init__" in script_methods:
            assert script_methods.index("__init__") == 0, "The `__init__` method is not in first position."

    @staticmethod
    def test_order(script_methods) -> None:
        script_methods = [
            method
            for method in script_methods
            if method != "__init__"  # exclude __init__
            and not (method.startswith("_") and not method.startswith("__"))  # exclude private method but not magic
        ]
        assert sorted(script_methods) == script_methods


class TestOrderMethodsElementClass(OrderTestSuite):
    """Test methods order for class `_Element`."""

    SCRIPT_PATH = "symmetria/elements/_interface.py"


class TestOrderMethodsPermutationClass(OrderTestSuite):
    """Test methods order for class `Permutation`."""

    SCRIPT_PATH = "symmetria/elements/permutation.py"


class TestOrderMethodsCycleClass(OrderTestSuite):
    """Test methods order for class `Cycle`."""

    SCRIPT_PATH = "symmetria/elements/cycle.py"


class TestOrderMethodsCycleDecompositionClass(OrderTestSuite):
    """Test methods order for class `CycleDecomposition`."""

    SCRIPT_PATH = "symmetria/elements/cycle_decomposition.py"
