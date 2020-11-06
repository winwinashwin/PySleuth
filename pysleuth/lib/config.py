import configparser
import os

from .base import singleton


def settings(section: str):
    def inner(fn):
        def wrapped(self, component: str = ""):
            if component:
                sec = f"{section} - {component}"
            else:
                sec = section
            assert sec in self.root.sections()
            return self.root[sec]
        return wrapped
    return inner


@singleton
class ConfigHandler:
    def __init__(self):
        self._fileRoot = configparser.RawConfigParser()

    def loadFrom(self, file: str) -> None:
        assert os.path.exists(file)

        self._fileRoot.read(file)

    @property
    def root(self):
        return self._fileRoot

    @settings("CONTROL")
    def getCfgControl(self):
        pass

    @settings("OUTPUT")
    def getCfgOutput(self):
        pass

    @settings("RUN")
    def getCfgRun(self):
        pass

    @settings("COMPONENT")
    def getCfgComponent(self, component):
        pass


def loadConfig(configurationFile: str):
    c = ConfigHandler()
    c.loadFrom(configurationFile)
