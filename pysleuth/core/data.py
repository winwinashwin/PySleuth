from pathlib import Path


class Data:
    __instance = None

    @staticmethod
    def getRootDir():
        return Data.__get().__getRootDirImpl()

    @staticmethod
    def newLogFile(name):
        return Data.__get().__newLogFileImpl(name)

    def __getRootDirImpl(self):
        # TODO: take from env file maybe?
        return Path(".") / "data"

    def __newLogFileImpl(self, name):
        root = self.getRootDir()

        return root / name

    @staticmethod
    def __get():
        """ Static access method. """
        if Data.__instance == None:
            Data()

        return Data.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if Data.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Data.__instance = self
