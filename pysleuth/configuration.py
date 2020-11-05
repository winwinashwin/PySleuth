import yaml

from .base import singleton


class StructDB(object):
    def __init__(self, data):
        for name, value in data.items():
            setattr(self, name.replace("-", "_"), self._wrap(value))

    def _wrap(self, value):
        if isinstance(value, (tuple, list, set, frozenset)):
            return type(value)([self._wrap(v) for v in value])
        else:
            return StructDB(value) if isinstance(value, dict) else value


@singleton
class ConfigHandler:
    def __init__(self):
        self._fileRoot = dict()

        self._processed = None

    def loadFrom(self, file: str) -> None:
        with open(file, "r") as fp:
            self._fileRoot = yaml.safe_load(fp)
            self._processed = StructDB(self._fileRoot)

    def getSettingsGeneral(self):
        assert self._processed is not None

        return self._processed.PySleuth.General

    def getActiveComponents(self):
        assert self._processed is not None

        return self._processed.PySleuth.Components.Active

    def getComponentSettings(self, compName: str):
        assert self._processed is not None

        return getattr(self._processed.PySleuth.Components, compName)


def loadConfig(configurationFile: str):
    c = ConfigHandler()
    c.loadFrom(configurationFile)
