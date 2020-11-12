from datetime import datetime

from ....core.components.mouse import MouseMonitor
from ....core.components.screen import saveScreenShot
from ..._base import BaseController
from .... import config
from ....core import output


class MouseMntrController(BaseController):
    def __init__(self):
        super(MouseMntrController, self).__init__()

        self.worker = MouseMonitor()
        logFile = output.Path().getRootDir() / "mouse/clicks.log"
        self.worker.initLogger("mouse/clicks.log", logFile)

        self.connectSlots()

    def startWorker(self):
        self.worker.start()

    def connectSlots(self):
        self.worker.SIG_clicked.connect(self, "onMouseClick")

    def onMouseClick(self, x: int, y: int, button: str, pressed: bool):
        msg = f"{'Pressed' if pressed else 'Released'} {button} at ({x}, {y})"
        self.worker.log(msg)

        cfg = config.get().mouseMntr

        if cfg.captureOnActivity:
            self.grabScreen()

    def grabScreen(self):
        dt_string = datetime.now().strftime("%d-%m-%y %H-%M-%S")
        filePath = output.Path().getRootDir() / "mouse" / \
            "shots" / f"{dt_string}.jpg"
        saveScreenShot(filePath)
