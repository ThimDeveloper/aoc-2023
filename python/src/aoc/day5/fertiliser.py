import dataclasses
from pprint import pprint
from typing import List, Literal, Mapping
from aoc.shared.io import FileUtility
import regex as re


@dataclasses.dataclass
class GardenerMap:
    type: str
    mappings: Mapping[int, int] = dataclasses.field(default_factory=dict)

    def add_mapping(
        self, source_range_start: str, destination_range_start: str, range_length: str
    ) -> None:
        for i in range(int(range_length)):
            self.mappings[int(source_range_start) + i] = int(destination_range_start) + 1

    def get(self, number: int) -> int:
        return self.mappings.get(number, number)


class Fertiliser(FileUtility):
    def __init__(
        self,
        assets_directory: str = "assets",
        output_file_name: str = "output.txt",
    ) -> None:
        super().__init__(__file__, assets_directory, output_file_name)
        self.name_type_map = {"soil": "seed-to-soil", "fertilizer": "soil-to-fertilizer"}

    def _get_seeds(self, data: List[str]):
        return [int(seed) for seed in data[0].strip("seeds: ").split(" ")]

    def _get_map(
        self,
        type: Literal[
            "seed-to-soil",
            "soil-to-fertilizer",
            "fertilizer-to-water",
            "water-to-light",
            "light-to-temperature",
            "temperature-to-humidity",
            "humidity-to-location",
        ],
        data: List[str],
    ) -> GardenerMap:
        gardener_map = GardenerMap(type)
        for line in data:
            if type in line:
                mapping_lines = [val.split(" ") for val in line.strip(f"{type} map:\n").split("\n")]
                for mapping in mapping_lines:
                    self.soil_map.add_mapping(mapping[1], mapping[0], mapping[2])
                return gardener_map

    def _read_input(self, file_name: str):
        file_path = self._get_file_path(file_name)
        with open(file_path, "r") as fd:
            lines = fd.read()

        seeds_and_maps = [line.strip() for line in lines.split("\n\n")]
        seeds = self._get_seeds(seeds_and_maps)
        soil_map = self._get_map(seeds_and_maps)

    def parse_seed_mapping(self, file_name: str) -> int:
        self._read_input(file_name)
