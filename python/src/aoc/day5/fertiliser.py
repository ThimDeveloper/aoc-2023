from aoc.shared.io import FileUtility


class Fertiliser(FileUtility):
    def __init__(
        self,
        assets_directory: str = "assets",
        output_file_name: str = "output.txt",
    ) -> None:
        super().__init__(__file__, assets_directory, output_file_name)

    def _read_input(self):
        pass

    def parse_seed_mapping(self) -> int:
        pass
