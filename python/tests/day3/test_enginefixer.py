from pprint import pprint
import pytest
from aoc.day3.enginefixer import EngineFixer


@pytest.fixture
def enginefixer() -> EngineFixer:
    return EngineFixer(output_file_name="test_output.txt")


def test_sum_of_parts(enginefixer) -> None:
    file_name = "test_schematics.txt"
    result = enginefixer.sum_of_parts(file_name, "parts")
    print(result)


def test_sum_of_parts(enginefixer) -> None:
    file_name = "test_schematics.txt"
    result = enginefixer.sum_of_parts(file_name, "parts")
    assert result == 4361


def test_gear_ratio(enginefixer) -> None:
    file_name = "test_schematics.txt"
    result = enginefixer.sum_of_parts(file_name, "gears")
    assert result == 467835
