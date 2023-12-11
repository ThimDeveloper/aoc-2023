from pprint import pprint
import dataclasses
from typing import List, Tuple
from aoc.shared.io import FileUtility
import regex as re
import uuid
import math


@dataclasses.dataclass
class Coordinates:
    x: int
    y: int

    def __eq__(self, __value: "Coordinates") -> bool:
        return (self.x == __value.x) and (self.y == __value.y)


@dataclasses.dataclass
class EngineNode:
    id: uuid.UUID
    value: str
    coordinates: List[Coordinates]
    neighbour_values: List[str] = dataclasses.field(default_factory=[])

    def is_digit(self) -> bool:
        return self.value.isdigit()

    def is_star(self) -> bool:
        return self.value == "*"

    def should_count_number(self) -> bool:
        if self.is_digit() and list(filter(lambda x: not x.isdigit(), self.neighbour_values)) > 0:
            return True
        return False

    @staticmethod
    def calculate_eucludian_distance(own_coordinates: Coordinates, coordinates: Coordinates) -> int:
        x = math.pow(own_coordinates.x - coordinates.x, 2)
        y = math.pow(own_coordinates.y - coordinates.y, 2)
        return math.sqrt(x + y)

    def is_neighbour(self, node: "EngineNode") -> bool:
        for own_coordinates in self.coordinates:
            for node_coordinates in node.coordinates:
                if int(self.calculate_eucludian_distance(own_coordinates, node_coordinates)) == 1:
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
        self.single_symbol_pattern = re.compile(r"(\d){1}|(\D){1}")
        self.nodes: List[EngineNode] = []

    def _filter_regex_matches(self, value: Tuple[str, str]) -> str:
        return list(filter(None, value))[0]

    def _generate_nodes(self, lines: List[str]) -> List[List[str]]:
        # y = 0
        # x = 0
        for y, row in enumerate(lines):
            for x, symbol in enumerate(
                self._filter_regex_matches(matches) for matches in self.pattern.findall(row)
            ):
                if symbol != ".":
                    range_of_symbol = len(symbol)
                    coordinates = [Coordinates(x + i, y) for i in range(range_of_symbol)]
                    id = uuid.uuid4()
                    self.nodes.append(EngineNode(id, symbol, coordinates, []))
                    if range_of_symbol > 1:
                        x += range_of_symbol
                    
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
