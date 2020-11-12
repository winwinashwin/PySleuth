from datetime import datetime

from ....core.components.screen import ScreenMonitor, saveScreenShot
from .... core import output
from ..._base import BaseController
from .... import config

logger = output.Loggers.getMaster(__name__)


class ScreenMntrController(BaseController):
    def __init__(self):
        super(ScreenMntrController, self).__init__()

        self.worker = ScreenMonitor()

        cfg = config.get().screenMntr
        self.setWorkerPause(cfg.logEvery)

        self.connectSlots()

    def startWorker(self):
        self.worker.start()
        logger.info("Screen monitoring active")
        self.isWorkerActive = True

    def connectSlots(self):
        self.worker.SIG_grab.connect(self, "onGrabScreen")

    def onGrabScreen(self):
        dt_string = datetime.now().strftime("%d-%m-%y %H-%M-%S")
        filePath = output.Path().getRootDir() / "screen" / f"{dt_string}.jpg"
        saveScreenShot(filePath)
        logger.debug("Screen grabbed")

    def setWorkerPause(self, pause: int):
        try:
            assert isinstance(pause, int) and pause > 0 and pause != None
        except AssertionError:
            logger.warn(
                f"Expected unsigned int, got: {pause}, setting to 5 second", exc_info=True)
            pause = 5

        self.worker.setPause(pause)
