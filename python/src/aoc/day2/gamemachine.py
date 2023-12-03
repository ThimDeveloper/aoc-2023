import os
from typing import List, Optional
from aoc.shared.io import FileUtility
import dataclasses
import regex as re


@dataclasses.dataclass
class Condition:
    red: int
    green: int
    blue: int


@dataclasses.dataclass
class CubeSet:
    red: Optional[int] = 0
    green: Optional[int] = 0
    blue: Optional[int] = 0


@dataclasses.dataclass
class Game:
    id_str: str
    sets: List[CubeSet]

    def _is_set_possible(self, set: CubeSet, condition: Condition) -> bool:
        return all(
            [set.red <= condition.red, set.green <= condition.green, set.blue <= condition.blue]
        )

    def is_game_possible(self, condition: Condition) -> bool:
        return all([self._is_set_possible(set, condition) for set in self.sets])

    def __post_init__(self) -> None:
        self.id = int(self.id_str)


class GameMachine(FileUtility):
    def __init__(
        self,
        assets_directory: str = "assets",
        output_file_name: str = "output.txt",
        condition: Condition = Condition(**{"red": 12, "green": 13, "blue": 14}),
    ) -> None:
        super().__init__(__file__, assets_directory, output_file_name)
        # 12 red cubes, 13 green cubes, and 14 blue cubes
        self.condition = condition
        self.game_pattern = re.compile(r"(?:Game )(\d+)(?:\: )(.+)")
        self.red_pattern = re.compile(r"(\d+)(?:red)")
        self.blue_pattern = re.compile(r"(\d+)(?:blue)")
        self.green_pattern = re.compile(r"(\d+)(?:green)")

    def _convert_match_to_int(self, match: List[str]) -> int:
        if len(match) != 0:
            return int(match[0])
        return 0

    def _parse_game(self, line: str) -> Game:
        game_line = self.game_pattern.findall(line)
        id = game_line[0][0]
        sets_in_line = f"{game_line[0][1]}".replace(" ", "").split(";")
        sets: List[CubeSet] = []
        for set in sets_in_line:
            red = self._convert_match_to_int(self.red_pattern.findall(set))
            blue = self._convert_match_to_int(self.blue_pattern.findall(set))
            green = self._convert_match_to_int(self.green_pattern.findall(set))
            sets.append(CubeSet(red, green, blue))

        game = Game(id, sets)
        with open(self.output, "a+") as fd:
            fd.write(f"{game_line} - {game.id} - {sets}\n")
        return game

    def sum_of_valid_games(self, games: List[Game]) -> int:
        return sum([game.id for game in games if game.is_game_possible(self.condition)])

    def evaluate_games(self, file_name: str) -> int:
        if os.path.exists(self.output):
            os.remove(self.output)

        file_path = os.path.join(self.assets_path, file_name)
        with open(file_path, "r") as fd:
            games = [self._parse_game(line) for line in fd.readlines()]
            return self.sum_of_valid_games(games)
