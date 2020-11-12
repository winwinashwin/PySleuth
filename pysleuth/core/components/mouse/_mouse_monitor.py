from pynput import mouse

from .._base import BaseComponent
from ..signal import Signal


class MouseMonitor(BaseComponent):
    SIG_clicked = Signal(int, int, str, bool)

    def __init__(self):
        super(MouseMonitor, self).__init__()

    def run(self):
        listener = mouse.Listener(on_click=self._emitSignal)
        listener.start()

    def _emitSignal(self, x, y, button, pressed):
        self.SIG_clicked.emit(x, y, str(button), pressed)
