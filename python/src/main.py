from aoc.day1.decoder import ElfCoordinateDecoder


if __name__ == "__main__":
    decoder = ElfCoordinateDecoder()
    file_name = "puzzle.txt"
    print(decoder.decode(file_name))
