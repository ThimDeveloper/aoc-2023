import os
import re
from typing import List


class ElfCoordinateDecoder:
    def __init__(
        self, assets_directory: str = "assets", output_file_name: str = "output.txt"
    ) -> None:
        self.assets_path = os.path.join(
            os.path.abspath(os.path.dirname(__file__)), assets_directory
        )
        self.lettered_digit_pattern = re.compile(r"(\w)+")
        self.output = self._get_file_path(output_file_name)
        self.digit_pattern = re.compile(r"(\d){1}")

    def _get_file_path(self, file_name: str) -> str:
        return os.path.join(self.assets_path, file_name)

    def _parse_int(self, digit_str: str) -> int:
        return int(digit_str)

    def _decode_line(self, line: str) -> int:
        digits: List[str] = self.digit_pattern.findall(line)
        line_digit_str = digits[0] + digits[-1]
        line_digit = self._parse_int(line_digit_str)

        with open(self.output, "+a") as fd:
            fd.write(f"{line}:{digits}:{line_digit}\n")
        return line_digit

    def decode(self, file_name: str) -> int:
        if os.path.exists(self.output):
            os.remove(self.output)
        file_path = self._get_file_path(file_name)

        with open(file_path, "r") as fd:
            return sum([self._decode_line(line.strip("\n")) for line in fd.readlines()])
