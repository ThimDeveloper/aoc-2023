from aoc.day1.decoder import ElfCoordinateDecoder
from aoc.day2.gamemachine import GameMachine


if __name__ == "__main__":
    # Day 1
    # decoder = ElfCoordinateDecoder()
    # file_name = "puzzle.txt"
    # print(decoder.decode(file_name))

    # Day 2
    gamemachine = GameMachine()
    file_name = "games.txt"
    print(gamemachine.evaluate_games(file_name))
