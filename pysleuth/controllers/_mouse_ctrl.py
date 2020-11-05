from ..core.components import MouseMonitor
from .base import BaseController


class MouseMntrController(BaseController):
    def __init__(self):
        super(MouseMntrController, self).__init__()

        self.worker = MouseMonitor()
        self.worker.initLogger("mouse/clicks")

        self.connectSlots()

    def startWorker(self):
        self.worker.start()

    def connectSlots(self):
        self.worker.SIG_clicked.connect(self, "onMouseClick")

    def onMouseClick(self, x: int, y: int, button: str, pressed: bool):
        self.worker.log(f"{'Pressed' if pressed else 'Released'} {button} at ({x}, {y})")