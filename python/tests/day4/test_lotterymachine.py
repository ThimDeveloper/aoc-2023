import pytest

from aoc.day4.lotterymachine import LotteryMachine

@pytest.fixture
def lotterymachine() -> LotteryMachine:
    return LotteryMachine(output_file_name="test_output.txt")


def test_parse_line(lotterymachine) -> None:
    card = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
    print(lotterymachine._parse_card(card))