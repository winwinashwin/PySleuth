from datetime import datetime

from ..core.components import ScreenMonitor, saveScreenShot
from ..core.data import Data
from .base import BaseController
from ..configuration import ConfigHandler


class ScreenMntrController(BaseController):
    def __init__(self):
        super(ScreenMntrController, self).__init__()

        self.worker = ScreenMonitor()

        cfg = ConfigHandler().getComponentSettings("Screen_Monitor")
        self.worker.setPause(cfg.log_every)

        self.connectSlots()

    def startWorker(self):
        self.worker.start()

    def connectSlots(self):
        self.worker.SIG_grab.connect(self, "onGrabScreen")

    def onGrabScreen(self):
        dt_string = datetime.now().strftime("%d-%m-%y %H-%M-%S")
        filePath = Data().getRootDir() / "screen" / f"{dt_string}.jpg"
        saveScreenShot(filePath)
