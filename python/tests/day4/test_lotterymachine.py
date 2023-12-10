from pprint import pprint
import pytest

from aoc.day4.lotterymachine import LotteryMachine


@pytest.fixture
def lotterymachine() -> LotteryMachine:
    return LotteryMachine(output_file_name="test_output.txt")


def test_parse_line(lotterymachine) -> None:
    card_line = "Card 113: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
    card = lotterymachine._parse_card(card_line)
    assert card.winning_numbers == ["41", "48", "83", "86", "17"]
    assert card.card_numbers == ["83", "86", "6", "31", "17", "9", "48", "53"]


def test_count_points(lotterymachine) -> None:
    points = lotterymachine.read_cards("test_cards.txt", operation="points")
    assert points == 13


def test_count_cards_total(lotterymachine) -> None:
    total_cards = lotterymachine.read_cards("test_cards.txt", operation="cards")
    assert total_cards == 30
