import dataclasses
import os
from typing import List, Literal
import regex as re
from aoc.shared.io import FileUtility


@dataclasses.dataclass
class Card:
    id_string: str
    winning_numbers: List[str]
    card_numbers: List[str]

    def points(self) -> int:
        count_of_winning_numbers = len(
            list(filter(lambda number: number in self.winning_numbers, self.card_numbers))
        )
        if count_of_winning_numbers == 0:
            return 0
        return pow(2, (count_of_winning_numbers - 1))
    
    def total_cards(self, cards: List["Card"]) -> int:
        pass

    def __post_init__(self) -> None:
        self.id = str(self.id_string)


class LotteryMachine(FileUtility):
    def __init__(
        self,
        assets_directory: str = "assets",
        output_file_name: str = "output.txt",
    ) -> None:
        super().__init__(__file__, assets_directory, output_file_name)
        self.card_pattern = re.compile(r"(?:Card\s+\d+\: )(.+)")
        self.card_id_patterN = re.compile(r"(?:Card\s+)(\d+)(?:\:)")
        self.number_pattern = re.compile(r"(\S)+")

    def _parse_card(self, line: str) -> Card:
        numbers = str(self.card_pattern.findall(line)[0])
        line_break_reached = False
        winning_numbers = []
        card_numbers = []
        for m in self.number_pattern.finditer(numbers):
            symbol = m.group()
            if symbol == "|":
                line_break_reached = True
                continue
            if not line_break_reached:
                winning_numbers.append(symbol)
            else:
                card_numbers.append(symbol)
        card = Card(winning_numbers, card_numbers)
        return card

    def _count_points(self, cards: List[Card]) -> int:
        return sum([card.points() for card in cards])

    def _count_cards_total(self, cards: List[Card]) -> int:
        pass

    def read_cards(self, file_name: str, operation: Literal["points", "cards"]) -> int:
        if os.path.exists(self.output):
            os.remove(self.output)

        file_path = os.path.join(self.assets_path, file_name)
        with open(file_path, "r") as fd:
            cards = [self._parse_card(line) for line in fd.readlines()]

        if operation == "points":
            return self._count_points(cards)
        if operation == "cards":
            return self._count_cards_total(cards)
        return ValueError(f"No opeartion of type {operation}")
