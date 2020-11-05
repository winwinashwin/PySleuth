from pathlib import Path

from ..base import singleton
from ..config_handler import ConfigHandler


@singleton
class Data:
    def __init__(self):
        pass

    def getRootDir(self):

        return Path(".") / "data"

    def newLogFile(self, name):
        root = self.getRootDir()

        return root / name
