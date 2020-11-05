from pynput import keyboard

from ..base import BaseFeature
from ..signal import Signal


class KeyLogger(BaseFeature):
    KEY_PRESSED = Signal(str)

    def __init__(self):
        super(KeyLogger, self).__init__()

    def run(self):
        listener = keyboard.Listener(on_press=self._emitSignal)
        listener.start()

    def _emitSignal(self, key):
        self.KEY_PRESSED.emit(str(key))