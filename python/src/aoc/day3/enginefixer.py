from pprint import pprint
import dataclasses
from typing import List, Tuple
from aoc.shared.io import FileUtility
import regex as re
import uuid


@dataclasses.dataclass
class Coordinates:
    xstart: int
    xend: int
    ystart: int
    yend: int

    def __eq__(self, __value: "Coordinates") -> bool:
        return (self.x == __value.x) and (self.y == __value.y)


@dataclasses.dataclass
class EngineNode:
    id: uuid.UUID
    value: str
    coordinates: Coordinates
    neighbour_values: List[str] = dataclasses.field(default_factory=[])

    def is_digit(self) -> bool:
        return self.value.isdigit()

    def is_star(self) -> bool:
        return self.value == "*"

    def should_count_number(self) -> bool:
        if self.is_digit() and list(filter(lambda x: not x.isdigit(), self.neighbour_values)) > 0:
            return True
        return False

    def is_neighbour(self, node: "EngineNode") -> bool:
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                valid_neigbour_coordinates = Coordinates(
                    self.coordinates.x + x, self.coordinates.y + y
                )

                if valid_neigbour_coordinates == node.coordinates:
                    return True
        return False

    def find_neighbours(self, nodes: List["EngineNode"]) -> List[str]:
        for node in nodes:
            if node.id != self.id and self.is_neighbour(node):
                self.neighbour_values.append(node.value)
        return self.neighbour_values


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

    def _generate_nodes(self, lines: List[str]) -> List[List[str]]:
        for y, row in enumerate(lines):
            for x, symbol in enumerate(
                self._filter_regex_matches(matches) for matches in self.pattern.findall(row)
            ):
                if symbol != ".":
                    xend = x + len(symbol) - 1
                    coordinates = Coordinates(x, xend, y)
                    id = uuid.uuid4()
                    self.nodes.append(EngineNode(id, symbol, coordinates, []))
        return self.nodes

    def _generate_adjency_lists(self):
        for node in self.nodes[0:1]:
            node_neighbour_values = node.find_neighbours(self.nodes)
            node.neighbour_values = node_neighbour_values
            pprint(node)
            pprint("neighbours")
            pprint(node_neighbour_values)

    def sum_of_parts(self, file_name: str) -> List[EngineNode]:
        file_path = self._get_file_path(file_name)
        with open(file_path, "r") as fd:
            lines = [line.replace("\n", "") for line in fd.readlines()]
            nodes = self._generate_nodes(lines)
            self._generate_adjency_lists()
            return nodes
