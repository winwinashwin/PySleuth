from pathlib import Path

from ..base import singleton


@singleton
class Data:
    def __init__(self):
        pass

    def getRootDir(self):
        # TODO: take from env file maybe?
        return Path(".") / "data"

    def newLogFile(self, name):
        root = self.getRootDir()

        return root / name
