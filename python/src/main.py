from pprint import pprint
from aoc.day1.decoder import ElfCoordinateDecoder
from aoc.day2.gamemachine import GameMachine
from aoc.day3.enginefixer import EngineFixer
from aoc.day4.lotterymachine import LotteryMachine
from aoc.day5.fertiliser import Fertiliser


if __name__ == "__main__":
    # Day 1
    # decoder = ElfCoordinateDecoder()
    # file_name = "puzzle.txt"
    # print(ElfCoordinateDecoder.__name__)
    # print(decoder.decode(file_name))

    # Day 3.1
    # enginefixer = EngineFixer()
    # file_name = "schematics.txt"
    # pprint(enginefixer.sum_of_parts(file_name, "parts"))

    # Day 3.2
    # enginefixer = EngineFixer()
    # file_name = "schematics.txt"
    # pprint(enginefixer.sum_of_parts(file_name, "gears"))

    # Day 2
    # gamemachine = GameMachine()
    # file_name = "games.txt"
    # print(gamemachine.evaluate_games(file_name, operation="power"))

    # Day 4.1
    # lotterymachine = LotteryMachine()
    # file_name = "cards.txt"
    # print(lotterymachine.read_cards(file_name, operation="points"))

    # Day 4.2
    # lotterymachine = LotteryMachine()
    # file_name = "cards.txt"
    # print(lotterymachine.read_cards(file_name, operation="cards"))

    # Day 5.1
    fertiliser = Fertiliser()
    fertiliser.parse_seed_mapping("test_seedmap.txt")