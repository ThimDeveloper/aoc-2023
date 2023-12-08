from pprint import pprint
import dataclasses
from typing import List, Tuple
from aoc.shared.io import FileUtility
import regex as re


@dataclasses.dataclass
class EngineNode:
    value: str
    adjecent: List["EngineNode"] = dataclasses.field(default_factory=[])


class EngineFixer(FileUtility):
    def __init__(
        self,
        assets_directory: str = "assets",
        output_file_name: str = "output.txt",
    ) -> None:
        super().__init__(__file__, assets_directory, output_file_name)
        self.pattern = re.compile(r"(\d+)|(\D){1}")
        self.symbol_pattern = re.compile(r"[\D^\.]")

    def _filter_regex_matches(self, value: Tuple[str, str]) -> str:
        return list(filter(None, value))[0]

    def _generate_matrix(self, lines: List[str]) -> List[List[str]]:
        return [
            [self._filter_regex_matches(matches) for matches in self.pattern.findall(row)]
            for row in lines
        ]

    def _generate_engine_nodes(self, matrix: List[List[str]]):
        adjecency_matrix = [[0, 0 + 1, 0 + 2], [0, 0 + 1, 0 + 2], [0, 0 + 1, 0 + 2]]
        print(matrix[adjecency_matrix])

        for i in range(len(matrix) - 3):
            adjecent_elements = []
            for j in range(len(matrix[i]) - 3):
                if i > 0 and j > 0:
                    adjecent_elements.extend([matrix[i-1][j], matrix[i][j+1]])

    def sum_of_parts(self, file_name: str) -> int:
        file_path = self._get_file_path(file_name)
        with open(file_path, "r") as fd:
            lines = [line.replace("\n", "") for line in fd.readlines()]
            matrix = self._generate_matrix(lines)
            return matrix
