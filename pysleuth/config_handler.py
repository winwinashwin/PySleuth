import yaml

from .base import singleton


@singleton
class ConfigHandler:
    def __init__(self):
        self._fileRoot = dict()

    def loadFrom(self, file: str) -> None:
        with open(file, "r") as fp:
            self._fileRoot = yaml.safe_load(fp)

    def getSettingsGeneral(self):
        pass


def loadConfig(configurationFile: str):
    c = ConfigHandler()
    c.loadFrom(configurationFile)
