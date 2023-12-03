import pytest
from aoc.day2.gamemachine import Condition, CubeSet, Game, GameMachine


@pytest.fixture
def gamemachine() -> GameMachine:
    return GameMachine(output_file_name="test_output.txt")


def test_parse_game(gamemachine) -> None:
    game_string = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    game = gamemachine._parse_game(game_string)
    assert game.id == 1
    assert len(game.sets) == 3
    assert game.sets[0].blue == 3
    assert game.sets[0].red == 4

    assert game.sets[1].red == 1
    assert game.sets[1].green == 2
    assert game.sets[1].blue == 6

    assert game.sets[2].green == 2


def test_valid_game() -> None:
    condition = Condition(
        **{
            "red": 12,
            "blue": 14,
            "green": 13,
        }
    )
    game = Game("1", [CubeSet(red=10, blue=10, green=10), CubeSet(red=1, blue=3, green=1)])
    assert game.is_game_possible(condition) is True


def test_invalid_game() -> None:
    condition = Condition(
        **{
            "red": 12,
            "blue": 14,
            "green": 13,
        }
    )
    game = Game("1", [CubeSet(red=10, blue=10, green=14), CubeSet(red=13, blue=3, green=1)])
    assert game.is_game_possible(condition) is False


def test_evaluate_games(gamemachine) -> None:
    file_name = "test_games.txt"
    possible_games = gamemachine.evaluate_games(file_name)
    assert possible_games == 8
