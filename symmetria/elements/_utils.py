from typing import Dict, List
from dataclasses import field, dataclass

from typing_extensions import Self


@dataclass
class Table:
    title: str
    _rows: Dict[str, str] = field(default_factory=dict)

    _max_length_row: int = 0

    def add(self, attribute: str, value: str) -> Self:
        self._max_length_row = max(self._max_length_row, len(attribute) + len(value))
        self._rows[attribute] = value
        return self

    def build(self) -> str:
        length_table = len(self.title) + self._max_length_row + 20 + (len(self.title) + self._max_length_row) % 2

        table: List[str] = []
        table.append(self._get_header(length_table=length_table))

        for key, value in self._rows.items():
            table.append(self._get_row(length_table // 2, a=key, b=value))
            table.append(self._get_separation_for_rows(length_table=length_table))

        return "\n".join(table)

    def _get_header(self, length_table: int) -> str:
        """Return the header of the table."""
        return "\n".join(
            [
                "+" + "-" * length_table + "+",
                f"|{self.title:^{length_table}}|",
                "+" + "-" * length_table + "+",
            ]
        )

    def _get_row(self, length: int, a: str, b: str) -> str:
        """Return a row of the table."""
        return (
            "|" + "{:<{length}}".format(" " + a, length=length) + "|" + "{:^{length}}".format(b, length=length - 1) + "|"
        )

    def _get_separation_for_rows(self, length_table: int) -> str:
        """Return a separation line for two rows."""
        return "+" + "-" * (length_table // 2) + "+" + "-" * (length_table // 2 - 1) + "+"
