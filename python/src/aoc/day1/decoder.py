import os
import regex as re
from typing import List
from aoc.shared.io import FileUtility


class ElfCoordinateDecoder(FileUtility):
    def __init__(
        self, assets_directory: str = "assets", output_file_name: str = "output.txt"
    ) -> None:
        super().__init__(__file__, assets_directory, output_file_name)
        self.lettered_digit_pattern = re.compile(r"(\w)+")
        self.only_digit_pattern = re.compile(r"(\d){1}")

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

    def _parse_int(self, digit_str: str) -> int:
        return int(digit_str)

    def _conditionally_transform_digit(self, digit: str) -> str:
        if self._is_spelled_out_digit(digit):
            return self.digit_mapping[digit]
        return digit

    def _parse_line_digit(self, line: str) -> List[str]:
        digits: List[str] = self.only_digit_pattern.findall(line, overlapped=True)
        return digits

    def _parse_line_spelled_and_digit(self, line: str) -> List[str]:
        digits: List[str] = [
            self._conditionally_transform_digit(digit)
            for digit in [
                list(filter(None, match))[0]
                for match in self.digit_pattern.findall(line, overlapped=True)
            ]
        ]
        return digits

    def _calculate_line_sum(self, digits: List[str]) -> int:
        line_digit_str = digits[0] + digits[-1]
        line_digit = self._parse_int(line_digit_str)
        return line_digit

    def _decode_line(self, line: str) -> int:
        digits = self._parse_line_spelled_and_digit(line)
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
