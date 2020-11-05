from pathlib import Path
import logging
import os

from .data import Data
from ..base import singleton


class _Logger(object):
    def __init__(self):
        self.formatter = logging.Formatter('%(asctime)s: %(message)s')

    def new(self, name, file, level=logging.DEBUG):
        handler = logging.FileHandler(file)
        handler.setFormatter(self.formatter)

        logger = logging.getLogger(name)
        logger.setLevel(level)
        logger.addHandler(handler)

        return logger


@singleton
class Loggers:
    def __init__(self):
        self.loggers = dict()
        if not os.path.exists(Data().getRootDir()):
            os.mkdir(Data().getRootDir())

    def getNewLogger(self, name: str):
        assert name not in self.loggers

        self.loggers[name] = _Logger()
        return self.loggers[name].new(name, Data().newLogFile(name))
