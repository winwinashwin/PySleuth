from datetime import datetime

from ....core.components.screen import ScreenMonitor, saveScreenShot
from .... core import output
from ..._base import BaseController
from .... import config


class ScreenMntrController(BaseController):
    def __init__(self):
        super(ScreenMntrController, self).__init__()

        self.worker = ScreenMonitor()

        cfg = config.get().screenMntr
        self.worker.setPause(cfg.logEvery)

        self.connectSlots()

    def startWorker(self):
        self.worker.start()

    def connectSlots(self):
        self.worker.SIG_grab.connect(self, "onGrabScreen")

    def onGrabScreen(self):
        dt_string = datetime.now().strftime("%d-%m-%y %H-%M-%S")
        filePath = output.Path().getRootDir() / "screen" / f"{dt_string}.jpg"
        saveScreenShot(filePath)
