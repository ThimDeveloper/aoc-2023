from pprint import pprint
import dataclasses
from typing import List, Tuple
from aoc.shared.io import FileUtility
import regex as re


@dataclasses.dataclass
class EngineNode:
    value: str
    x: int
    y: int
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
        self.nodes: List[EngineNode] = []

    def _filter_regex_matches(self, value: Tuple[str, str]) -> str:
        return list(filter(None, value))[0]

    def _generate_matrix(self, lines: List[str]) -> List[List[str]]:
        for y, row in enumerate(lines):
            for x, symbol in enumerate(
                self._filter_regex_matches(matches) for matches in self.pattern.findall(row)
            ):
                if symbol != ".":
                    self.nodes.append(EngineNode(symbol, x, y, []))
        return self.nodes

    def _generate_adjency_list(self, matrix: List[List[str]]):
        pass

    def sum_of_parts(self, file_name: str) -> int:
        file_path = self._get_file_path(file_name)
        with open(file_path, "r") as fd:
            lines = [line.replace("\n", "") for line in fd.readlines()]
            matrix = self._generate_matrix(lines)
            return matrix
