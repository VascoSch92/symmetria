from collections import OrderedDict


def _pretty_print_table(title: str, body: OrderedDict[str, str]) -> str:
    """Private method to print an ordered dictionary in a table format."""
    max_length_keys = max([len(key) for key in body.keys()])
    max_length_values = max([len(value) for value in body.values()])
    max_length_body = max(max_length_values, max_length_keys)

    if (len(title) + max_length_body) % 2 == 0:
        length_table = len(title) + max_length_body + 20
    else:
        length_table = len(title) + max_length_body + 21

    table = "+" + "-" * length_table + "+"
    table += "\n"
    table += "|" + "{:^{length}}".format(title, length=length_table) + "|"
    table += "\n"
    table += "+" + "-" * length_table + "+"
    table += "\n"

    for name, value in body.items():
        table += _get_row(length_table // 2, a=name, b=value)
        table += "\n"
        table += "+" + "-" * (length_table // 2) + "+" + "-" * (length_table // 2 - 1) + "+"
        table += "\n"

    # the -1 is to delete the lase "\n" from the table
    return table[:-1]


def _get_row(length: int, a: str, b: str) -> str:
    """Return a row of the table."""
    return "|" + "{:<{length}}".format(" " + a, length=length) + "|" + "{:^{length}}".format(b, length=length - 1) + "|"
