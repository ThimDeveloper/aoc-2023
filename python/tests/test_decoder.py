import os
import pytest
from aoc.day_1.decoder import ElfCoordinateDecoder


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


def test_decoder(decoder) -> None:
    file_name = "test_puzzle.txt"
    assert decoder.decode(file_name) == 300
