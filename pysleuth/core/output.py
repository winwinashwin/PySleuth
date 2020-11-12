import pathlib
import logging
import os

from .._base import Singleton
from .. import config


def _setupLogger(name: str, file: str, formatter: str, level: int):
    """ Generate multiple loggers as required """
    handler = logging.FileHandler(file, mode="w")
    handler.setFormatter(logging.Formatter(formatter))

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger


class Loggers:
    @staticmethod
    def getMaster(name: str):
        logFmt = "[ %(asctime)s : %(levelname)s\t: %(name)s\t] %(message)s"
        logFile = Path().getRootDir() / "master.log"
        logLevel = logging.INFO

        return _setupLogger(name, logFile, logFmt, logLevel)

    @staticmethod
    def getComponent(name: str, file: str, level: int = logging.DEBUG):
        logFmt = "[ %(asctime)s ]: %(message)s"

        return _setupLogger(name, file, logFmt, level)


class Path(metaclass=Singleton):
    def __init__(self):
        subDirs = set()
        subDirs.add(self.getRootDir() / "mouse" / "shots")
        subDirs.add(self.getRootDir() / "screen")

        for subDir in subDirs:
            if os.path.exists(subDir):
                continue
            os.makedirs(subDir)

    def getRootDir(self):
        root = config.get().general.saveDataTo
        return pathlib.Path(os.path.join(root, "data"))
