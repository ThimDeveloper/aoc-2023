from pprint import pprint
from aoc.shared.io import FileUtility
import regex as re


class EngineFixer(FileUtility):
    def __init__(
        self,
        assets_directory: str = "assets",
        output_file_name: str = "output.txt",
    ) -> None:
        super().__init__(__file__, assets_directory, output_file_name)
        self.symbol_pattern = re.compile(r"(\d+)|(\D+)")

    def sum_of_parts(self, file_name: str) -> int:
        file_path = self._get_file_path(file_name)
        with open(file_path, "r") as fd:
            lines = [line.replace("\n", "") for line in fd.readlines()]
            symbol_matrix = [self.symbol_pattern.findall(line) for line in lines]
            print("\n")
            pprint(symbol_matrix)
            return symbol_matrix
