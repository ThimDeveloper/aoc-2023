import os
import pytest
from aoc.day1.decoder import ElfCoordinateDecoder


@pytest.fixture
def decoder() -> ElfCoordinateDecoder:
    return ElfCoordinateDecoder(output_file_name="test_output.txt")


def test_asset_path_is_valid(decoder) -> None:
    assert os.path.exists(decoder.assets_path)
    assert os.path.isdir(decoder.assets_path)


def test_decode_line_multi_digits(decoder) -> None:
    line = "1abc2"
    assert decoder._decode_line(line) == 12


def test_decode_line_single_digit(decoder) -> None:
    line = "treb7uchet"
    assert decoder._decode_line(line) == 77


def test_spelled_out_digit(decoder) -> None:
    spelled_digit = "two"
    string_digit = "2"
    assert decoder._is_spelled_out_digit(spelled_digit) is True
    assert decoder._is_spelled_out_digit(string_digit) is False


# def test_decode_line_spelled_out(decoder) -> None:
#     line = "z234oneight"
#     assert decoder._decode_line(line) == 28


def test_pars_line_spelled_out(decoder) -> None:
    import re

    input_string = "z234oneight"
    result = [int(digit) for digit in re.findall(r"\d+|\d", input_string)]

    print(result)


def test_decoder(decoder) -> None:
    file_name = "test_puzzle.txt"
    assert decoder.decode(file_name) == 142


def test_decoder_spelled(decoder) -> None:
    file_name = "test_puzzle_spelled.txt"
    assert decoder.decode(file_name) == 281
