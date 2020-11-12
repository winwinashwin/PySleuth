import yaml
from dacite import from_dict

from ._config import Configuration
from ._convert import converter
from ._validate import validateInput

from .._base import Singleton


class _ConfigurationHandler(metaclass=Singleton):
    def __init__(self):
        self._config: Configuration

    @property
    def config(self):
        return self._config

    def load(self, file: str):
        with open(file, "r") as fp:
            rawConfig = yaml.safe_load(fp)

        converted = converter(rawConfig)
        validateInput(rawConfig)

        self._config = from_dict(data_class=Configuration, data=converted)


def loadConfig(fromFile: str):
    _ConfigurationHandler().load(fromFile)


def get():
    """ return configuration """
    return _ConfigurationHandler().config
