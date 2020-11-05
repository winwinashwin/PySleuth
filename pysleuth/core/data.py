from pathlib import Path
import os

from ..base import singleton
from ..config_handler import ConfigHandler


@singleton
class Data:
    def __init__(self):
        os.makedirs(os.path.join(self.getRootDir(), "mouse"))

    def getRootDir(self):

        return Path(".") / "data"

    def newLogFile(self, name):
        root = self.getRootDir()

        return root / name
