from pynput import keyboard

from .base import BaseComponent
from ..signal import Signal


class KeyLogger(BaseComponent):
    SIG_KeyPressed = Signal(str)

    def __init__(self):
        super(KeyLogger, self).__init__()

    def run(self):
        listener = keyboard.Listener(
            on_press=lambda key: self.SIG_KeyPressed.emit(str(key))
        )
        listener.start()
