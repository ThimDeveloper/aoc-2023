from aoc.day1.decoder import ElfCoordinateDecoder
from aoc.day2.gamemachine import GameMachine
from aoc.day4.lotterymachine import LotteryMachine


if __name__ == "__main__":
    # Day 1
    decoder = ElfCoordinateDecoder()
    file_name = "puzzle.txt"
    print(ElfCoordinateDecoder.__name__)
    print(decoder.decode(file_name))

    # Day 3

    # Day 2
    # gamemachine = GameMachine()
    # file_name = "games.txt"
    # print(gamemachine.evaluate_games(file_name, operation="power"))

    # Day 4.1
    # lotterymachine = LotteryMachine()
    # file_name = "cards.txt"
    # print(lotterymachine.read_cards(file_name, operation="points"))

    # Day 4.2
    lotterymachine = LotteryMachine()
    file_name = "cards.txt"
    print(lotterymachine.read_cards(file_name, operation="cards"))
