import dataclasses
import os
from typing import List
import regex as re
from aoc.shared.io import FileUtility


@dataclasses.dataclass
class Card:
    winning_numbers: List[str]
    card_numbers: List[str]

    def points(self) -> int:
        count_of_winning_numbers = len(
            list(filter(lambda number: number in self.winning_numbers, self.card_numbers))
        )
        return pow(2, (count_of_winning_numbers - 1))


class LotteryMachine(FileUtility):
    def __init__(
        self,
        assets_directory: str = "assets",
        output_file_name: str = "output.txt",
    ) -> None:
        super().__init__(__file__, assets_directory, output_file_name)
        self.card_pattern = re.compile(r"(?:Card \d\: )(.+)")
        self.winning_pattern = re.compile(r"(\d+)")

    def _parse_card(self, line: str) -> Card:
        numbers = (
            str(self.card_pattern.findall(line)).replace("  ", ",").replace(" ", ",").split("|")
        )
        winning_numbers = numbers[0].split(",")
        card_numbers = numbers[1].split(",")
        card = Card(winning_numbers, card_numbers)
        return card

    def count_points(self, file_name: str) -> int:
        if os.path.exists(self.output):
            os.remove(self.output)

        file_path = os.path.join(self.assets_path, file_name)
        with open(file_path, "r") as fd:
            cards = [self._parse_card(line) for line in fd.readlines()]
