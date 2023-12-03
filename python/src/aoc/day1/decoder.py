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
        self.spelled_digit_pattern = re.compile(
            r"(one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine)"
        )
        self.digit_pattern = re.compile(
            r"(\d){1}|(one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine)"
        )
        self.digit_mapping = {
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9",
        }

    def _is_spelled_out_digit(self, digit: str) -> bool:
        return bool(self.spelled_digit_pattern.match(digit))

    def _get_file_path(self, file_name: str) -> str:
        return os.path.join(self.assets_path, file_name)

    def _parse_int(self, digit_str: str) -> int:
        return int(digit_str)

    def _conditionally_transform_digit(self, digit: str) -> str:
        if self._is_spelled_out_digit(digit):
            return self.digit_mapping[digit]
        return digit

    def _parse_line(self, line: str) -> List[str]:
        digits: List[str] = [
            self._conditionally_transform_digit(digit)
            for digit in [
                list(filter(None, match))[0] for match in self.digit_pattern.findall(line)
            ]
        ]
        return digits

    def _calculate_line_sum(self, digits: List[str]) -> int:
        line_digit_str = digits[0] + digits[-1]
        line_digit = self._parse_int(line_digit_str)
        return line_digit

    def _decode_line(self, line: str) -> int:
        digits = self._parse_line(line)
        line_digit = self._calculate_line_sum(digits)
        with open(self.output, "+a") as fd:
            fd.write(f"{line} - {digits} - {line_digit}\n")
        return line_digit

    def decode(self, file_name: str) -> int:
        if os.path.exists(self.output):
            os.remove(self.output)
        file_path = self._get_file_path(file_name)

        with open(file_path, "r") as fd:
            return sum([self._decode_line(line.strip("\n")) for line in fd.readlines()])
