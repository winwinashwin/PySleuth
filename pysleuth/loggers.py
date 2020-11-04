from pathlib import Path
import os

from .core.base.logger import BaseLogger
from .core.data import Data


class Loggers:
    __instance = None
    loggers = dict()

    @staticmethod
    def getNewLogger(name: str):
        return Loggers.__get().__getNewLoggerImpl(name)

    def __getNewLoggerImpl(self, name: str):
        assert name not in self.loggers

        self.loggers[name] = BaseLogger()
        return self.loggers[name].new(name, Data.newLogFile(name))

    @staticmethod
    def __get():
        """ Static access method. """
        if Loggers.__instance == None:
            Loggers()

        return Loggers.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if Loggers.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            if not os.path.exists(Data.getRootDir()):
                os.mkdir(Data.getRootDir())

            Loggers.__instance = self
