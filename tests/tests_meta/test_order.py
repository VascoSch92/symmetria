import ast
from typing import List
from pathlib import Path

import pytest


class OrderTestSuite:
    """Base class to test the order of methods in the script `SCRIPT_PATH`.

    The order of the methods must match the following:
        1. The __init__ method.
        2. All magic methods in alphabetically order.
        3. All class methods in alphabetically order.
        4. All properties in alphabetically order.
        5. ALl other methods in alphabetically order.
    """

    SCRIPT_PATH: str

    @pytest.fixture
    def script_methods(self) -> List:
        """Retrieve all the method in the given script. It assumes that there is just one class in the script."""
        target = Path(self.SCRIPT_PATH).read_text()
        module = ast.parse(target)

        for leaf in module.body:
            if isinstance(leaf, ast.ClassDef):
                return [item for item in leaf.body if isinstance(item, ast.FunctionDef)]

    @pytest.fixture
    def magic_methods(self, script_methods) -> List[str]:
        """Return list of magic methods present in the class. The method __init__ is not included."""
        return [item.name for item in script_methods if item.name.startswith("__") and item.name != "__init__"]

    @pytest.fixture
    def properties(self, script_methods) -> List[str]:
        """Return list of properties in the class."""
        return [item.name for item in script_methods if "property" in item.decorator_list]

    @pytest.fixture
    def generic_methods(self, script_methods) -> List[str]:
        """Return list of generic methods, i.e., without decorators and not starting with `_`, in the class."""
        undecorated_methods = [item for item in script_methods if not item.decorator_list]
        return [item.name for item in undecorated_methods if item.name.startswith("_") is False]

    def test_order_magic_methods(self, magic_methods) -> None:
        """Test order magic methods."""
        assert sorted(magic_methods) == magic_methods

    def test_order_properties(self, properties) -> None:
        """Test order properties."""
        assert sorted(properties) == properties

    def test_order_generic_methods(self, generic_methods) -> None:
        """Test order generic methods."""
        assert sorted(generic_methods) == generic_methods


class TestOrderMethodsElementClass(OrderTestSuite):
    SCRIPT_PATH = "symmetria/elements/_interface.py"


class TestOrderMethodsPermutationClass(OrderTestSuite):
    SCRIPT_PATH = "symmetria/elements/permutation.py"


class TestOrderMethodsCycleClass(OrderTestSuite):
    SCRIPT_PATH = "symmetria/elements/cycle.py"


class TestOrderMethodsCycleDecompositionClass(OrderTestSuite):
    SCRIPT_PATH = "symmetria/elements/cycle_decomposition.py"
