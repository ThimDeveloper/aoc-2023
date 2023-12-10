from pprint import pprint
import pytest
from aoc.day3.enginefixer import EngineFixer


@pytest.fixture
def enginefixer() -> EngineFixer:
    return EngineFixer(output_file_name="test_output.txt")


def test_sum_of_parts(enginefixer) -> None:
    file_name = "test_schematics.txt"
    nodes = enginefixer.sum_of_parts(file_name)
    # pprint(nodes[0:3])
