from typing import Any


def error_message(expected: Any, got: Any) -> str:
    """
    Return an error message in the format "Expected: <expected>. Got <got>" comparing the expected value with
    the actual value.

    :param expected: The expected value.
    :type expected: Any
    :param got: The actual value.
    :type got: Any

    :return: A string containing the error message.
    :rtype: str
    """
    return f"Expected {expected}, but got {got}."
