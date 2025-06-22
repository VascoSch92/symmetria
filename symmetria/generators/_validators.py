from typing import List


def _check_algorithm_parameter(value: str, supported: List[str]) -> None:
    """Private method to check the value provided for the parameter `algorithm`.

    Recall that the parameter `algorithm` must be a string present in the list `supported`.
    """
    if isinstance(value, str) is False:
        raise TypeError(f"The parameter `algorithm` must be of type string, but {type(value)} was provided.")
    if value not in supported:
        raise ValueError(
            f"The given algorithm ({value}) is not supported.\n"
            f"Here, a list of supported algorithm for generations of permutations {supported}."
        )


def _check_degree_parameter(value: int) -> None:
    """Private method to check the value provided for the parameter `degree`.

    Recall that the parameter `degree` must be a non-negative integer different from zero.
    """
    if isinstance(value, int) is False:
        raise TypeError(f"The parameter `degree` must be of type int, but {type(value)} was provided.")
    if value < 1:
        raise ValueError(f"The parameter `degree` must be a non-zero positive integer, but {value} was provided.")
