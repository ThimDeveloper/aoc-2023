from abc import ABC
import os


class FileUtility(ABC):
    def __init__(
        self,
        subclass_location: str,
        assets_directory: str = "assets",
        output_file_name: str = "output.txt",
    ) -> None:
        self.assets_path = os.path.join(
            os.path.abspath(os.path.dirname(subclass_location)), assets_directory
        )
        self.output = self._get_file_path(output_file_name)

    def _get_file_path(self, file_name: str) -> str:
        return os.path.join(self.assets_path, file_name)
