from pprint import pprint
from typing import List
from aoc.shared.io import FileUtility
import regex as re


class EngineFixer(FileUtility):
    def __init__(
        self,
        assets_directory: str = "assets",
        output_file_name: str = "output.txt",
    ) -> None:
        super().__init__(__file__, assets_directory, output_file_name)
        self.symbol_pattern = re.compile(r"(\d+)|(\D){1}")

    def sum_of_parts(self, file_name: str) -> int:
        file_path = self._get_file_path(file_name)
        with open(file_path, "r") as fd:
            lines = [line.replace("\n", "") for line in fd.readlines()]
            symbol_matrix = []
            for idx_row, row in enumerate(lines):
                symbol_matrix.append([])
                for column_value in self.symbol_pattern.findall(row):
                    filtered_column_value = list(filter(None, column_value))[0]
                    symbol_matrix[idx_row].append(filtered_column_value)
            # [x for y in collection for x in y] # [A for B in C for D in E]
            pprint(symbol_matrix)
            return symbol_matrix
