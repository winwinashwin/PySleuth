from pathlib import Path
import os

from ..base import singleton
from ..config_handler import ConfigHandler


@singleton
class Data:
    def __init__(self):

        subDirs = set()
        subDirs.add(self.getRootDir() / "mouse" / "shots")
        subDirs.add(self.getRootDir() / "screen")

        for subDir in subDirs:
            if os.path.exists(subDir):
                continue
            os.makedirs(subDir)

    def getRootDir(self):
        return Path(".") / "data"

    def newLogFile(self, name: str):
        return self.getRootDir() / name
